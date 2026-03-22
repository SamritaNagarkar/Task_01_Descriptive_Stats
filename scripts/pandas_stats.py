import pandas as pd
import os

# Setting up paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "fb_ads_president_scored_anon.csv")
results_dir = os.path.join(script_dir, "..", "results")
os.makedirs(results_dir, exist_ok=True)
output_file = os.path.join(results_dir, "pandas_summary.txt")

# Loading the dataset
df = pd.read_csv(data_path)

# Finding basic info about the dataset and writing to output file
with open(output_file, "w", encoding="utf-8") as f:

    f.write("Structure of the dataset:\n")
    f.write(f"Shape: {df.shape}\n\n")

    f.write("Data Types-\n")
    f.write(f"{df.dtypes}\n\n")

    f.write("Dataset Info-\n")
    df.info(buf=f)

# sunmary statistics for numeric and categorical columns
with open(output_file, "a", encoding="utf-8") as f:

    f.write("\n\nStats of numerical columns -\n")
    f.write(f"{df.describe()}\n\n")

    f.write("Stats of categorical columns -\n")
    f.write(f"{df.describe(include='object')}\n\n")

# Finding missing values and writing to output file
missing_counts = df.isnull().sum()
missing_percent = (missing_counts / len(df)) * 100

with open(output_file, "a", encoding="utf-8") as f:

    f.write("Missing Values -\n")

    for col in df.columns:
        f.write(f"{col}: {missing_counts[col]} ({missing_percent[col]:.2f}%)\n")


# Analyzing each column and writing stats
with open(output_file, "a", encoding="utf-8") as f:

    for col in df.columns:

        f.write(f"\n\nColumn name: {col}\n")

        if pd.api.types.is_numeric_dtype(df[col]):

            f.write("Type: Numeric\n")
            f.write(f"Mean: {df[col].mean()}\n")
            f.write(f"Median: {df[col].median()}\n")
            f.write(f"Std Dev: {df[col].std()}\n")
            f.write(f"Min: {df[col].min()}\n")
            f.write(f"Max: {df[col].max()}\n")

        else:

            f.write("Type: Categorical\n")
            f.write(f"Unique values: {df[col].nunique()}\n")

            vc = df[col].value_counts()

            if len(vc) > 0:
                f.write(f"Mode: {vc.index[0]} ({vc.iloc[0]})\n")

            f.write("Top 5 values:\n")
            f.write(f"{vc.head(5)}\n")


print("Phase 2 complete.")
print(f"Results saved to: {output_file}")



# Additional exploratory analysis used for Phase 3 findings

print("\nTop organizations by spend:")
print(df.groupby("page_name")["spend"].value_counts().head(10))

print("\nSpend distribution:")
print(df["spend"].describe())

print("\nMentions of illuminating topics:")
print(df["illuminating_mentions"].value_counts().head(10))

print("\nDate overview:")
print(df["ad_delivery_start_time"].describe())

print("\nMissing values (top 10 columns):")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# Topic analysis
topic_cols = [col for col in df.columns if "illuminating_topic" in col]

print("\nTopic popularity (top 10):")
print(df[topic_cols].sum().sort_values(ascending=False).head(10))