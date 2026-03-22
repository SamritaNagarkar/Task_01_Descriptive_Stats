import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "fb_ads_president_scored_anon.csv")
visuals_dir = os.path.join(script_dir, "..", "visuals")
os.makedirs(visuals_dir, exist_ok=True)

# Loading data
df = pd.read_csv(data_path)

# Spend Distribution Visualization
plt.figure()
df["spend"].value_counts().head(10).plot(kind="bar")

plt.title("Top Spend Ranges")
plt.xlabel("Spend Range")
plt.ylabel("Frequency")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(os.path.join(visuals_dir, "spend_distribution.png"))
plt.close()


# Top Advertisers Visualization
top_pages = df["page_name"].value_counts().head(10)

plt.figure()
top_pages.plot(kind="bar")

plt.title("Top Advertisers by Number of Ads")
plt.xlabel("Page Name")
plt.ylabel("Ad Count")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(os.path.join(visuals_dir, "top_advertisers.png"))
plt.close()


# Mentions Visualization
mentions = df["illuminating_mentions"].value_counts().head(10)

plt.figure()
mentions.plot(kind="bar")

plt.title("Top Mentions in Ads")
plt.xlabel("Mentions")
plt.ylabel("Count")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(os.path.join(visuals_dir, "mentions.png"))
plt.close()


# Topics Visualization
topic_cols = [col for col in df.columns if "illuminating_topic" in col]
topic_counts = df[topic_cols].sum().sort_values(ascending=False).head(10)

plt.figure()
topic_counts.plot(kind="bar")

plt.title("Most Common Topics in Ads")
plt.xlabel("Topic")
plt.ylabel("Frequency")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(os.path.join(visuals_dir, "topics.png"))
plt.close()


# Ads over time visualization
df["ad_delivery_start_time"] = pd.to_datetime(df["ad_delivery_start_time"])

ads_per_day = df.groupby(df["ad_delivery_start_time"].dt.date).size()

plt.figure()
ads_per_day.plot(kind="line")

plt.title("Ad Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Ads")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(os.path.join(visuals_dir, "ads_over_time.png"))
plt.close()