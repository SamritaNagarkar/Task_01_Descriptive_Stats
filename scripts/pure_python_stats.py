import csv
import os
import math
from collections import Counter

# Setting up paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "fb_ads_president_scored_anon.csv")
results_dir = os.path.join(script_dir, "..", "results")
os.makedirs(results_dir, exist_ok=True)
results_file = os.path.join(results_dir, "summary_statistics.txt")

# creating helper functions for numeric detection and stats computation
def clean_value(value):
    """Standard cleaning for numeric detection"""
    return value.replace(",", "").replace("$", "").strip()


def is_number(value):
    """Check if value is numeric after cleaning"""
    try:
        float(clean_value(value))
        return True
    except:
        return False


def compute_numeric_stats(values):
    """Compute numeric statistics safely"""

    if len(values) == 0:
        return None

    values_sorted = sorted(values)
    n = len(values)

    mean_val = sum(values) / n

    # Calculating median
    if n % 2 == 0:
        median_val = (values_sorted[n // 2 - 1] + values_sorted[n // 2]) / 2
    else:
        median_val = values_sorted[n // 2]

    # Calculating std deviation
    variance = sum((x - mean_val) ** 2 for x in values) / n
    std_dev_val = math.sqrt(variance)

    return {
        "count": n,
        "mean": mean_val,
        "min": min(values),
        "max": max(values),
        "median": median_val,
        "std_dev": std_dev_val
    }

def compute_categorical_stats(values):
    """Compute categorical statistics"""

    if len(values) == 0:
        return None

    counter = Counter(values)
    mode_value, mode_freq = counter.most_common(1)[0]

    return {
        "count": len(values),
        "unique": len(counter),
        "mode": mode_value,
        "mode_freq": mode_freq,
        "top_5": counter.most_common(5)
    }

# Loading Data
rows = []
with open(data_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    columns = reader.fieldnames

    for row in reader:
        rows.append(row)

total_rows = len(rows)
total_columns = len(columns)

# Missing value counts
missing_counts = {}
for col in columns:
    missing_counts[col] = sum(
        1 for row in rows if row[col] == "" or row[col] is None
    )

# Type inference
column_types = {}
for col in columns:
    numeric_count = 0
    total_checked = 0

    for row in rows:
        val = row[col]
        if val == "" or val is None:
            continue

        total_checked += 1

        if is_number(val):
            numeric_count += 1

    if total_checked == 0:
        column_types[col] = "empty"
    elif numeric_count / total_checked >= 0.9:
        column_types[col] = "numeric"
    else:
        column_types[col] = "categorical"

# Column statistics
numeric_results = {}
categorical_results = {}
for col in columns:
    values = [
        row[col] for row in rows
        if row[col] != "" and row[col] is not None
    ]

    if column_types[col] == "numeric":
        cleaned_values = []
        for v in values:
            try:
                cleaned_values.append(float(clean_value(v)))
            except:
                continue

        numeric_results[col] = compute_numeric_stats(cleaned_values)

    elif column_types[col] == "categorical":
        categorical_results[col] = compute_categorical_stats(values)


# Outputting results to text file
with open(results_file, "w", encoding="utf-8") as f:

    f.write("Overview of the Dataset:\n")
    f.write(f"Total rows: {total_rows}\n")
    f.write(f"Total columns: {total_columns}\n\n")

    f.write("Type of all columns-\n")
    for col, dtype in column_types.items():
        f.write(f"{col}: {dtype}\n")

    f.write("\nMissing Values-\n")
    for col, count in missing_counts.items():
        f.write(f"{col}: {count}\n")

    f.write("\nStats of numerical columns-\n")
    for col, stats in numeric_results.items():
        f.write(f"\n{col}\n")
        if stats is None:
            f.write("No valid numeric data\n")
            continue

        for key, value in stats.items():
            f.write(f"{key}: {value}\n")

    f.write("\nStats of categorical columns-\n")
    for col, stats in categorical_results.items():
        f.write(f"\n{col}\n")
        if stats is None:
            f.write("No valid categorical data\n")
            continue

        f.write(f"count: {stats['count']}\n")
        f.write(f"unique: {stats['unique']}\n")
        f.write(f"mode: {stats['mode']} ({stats['mode_freq']})\n")

        f.write("top 5 values:\n")
        for val, cnt in stats["top_5"]:
            f.write(f"  {val}: {cnt}\n")


print("Phase 1 complete.")
print(f"Results saved to: {results_file}")