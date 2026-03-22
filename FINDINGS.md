## Findings and Analysis

This analysis explores patterns in Facebook political advertising during the 2024 U.S. presidential election cycle. The goal is to understand how advertising activity is distributed across organizations, how messaging is structured, and whether meaningful temporal or thematic patterns emerge.

### 1. Structure of Ad Spend Data

A key observation is that the **spend column is not stored as a continuous numeric value**, but instead as **range-based values** (e.g., '0–99', '9000–9999').

This has important implications:

* Exact totals and averages cannot be directly computed
* The dataset reflects **spending brackets rather than precise amounts**

A large proportion of ads fall into the lowest spend range ('0–99'), which appears over 135,000 times. This indicates that **most ads operate on relatively small budgets**, while higher spending levels are less frequent.

---

### 2. Distribution of Advertising Activity

Although many organizations appear in the dataset, advertising activity is not evenly distributed.

A subset of organizations frequently appears in **higher spending brackets**, suggesting relatively higher advertising activity. Examples include:

* Jason Smith
* Restoration of America
* American Crossroads
* Future Coalition PAC

At the same time, a long tail of organizations operates within lower spending ranges. This creates a **skewed distribution**, where many small advertisers coexist with fewer high-activity entities.

---

### 3. Messaging and Candidate Mentions

The `illuminating_mentions` column provides insight into which political figures are referenced in ads.

Key observations:

* A large number of ads contain **no mentions at all (~73,000 entries)**
* The most frequently mentioned individuals include:

  * Donald Trump
  * Kamala Harris
  * Joe Biden

Some ads reference multiple individuals, indicating comparative or oppositional messaging.

Additionally, variations such as “Donald Trump” and “President Trump” appear separately, highlighting **inconsistent labeling** and suggesting that true mention frequencies may be fragmented across categories.

---

### 4. Temporal Patterns in Advertising

Advertising activity varies significantly over time:

* The dataset contains **558 unique dates**
* A major spike occurs on **October 28, 2024**, with over 10,000 ads

This suggests that ad activity is **event-driven rather than uniform**, with campaigns increasing output during key political moments.

---

### 5. Topic-Level Insights

The dataset includes binary indicators for various policy topics, allowing analysis of issue-level focus.

The most frequently occurring topics are:

* Economy
* Health
* Social and cultural issues
* Women’s issues

Less frequent topics include:

* Education
* Environment
* COVID

This pattern suggests that advertisers prioritize **broad, high-impact issues** that are likely to resonate with large audiences.

---

### 6. Data Quality and Preprocessing Challenges

Several challenges were encountered during analysis:

* Spend is stored as **range-based strings instead of numeric values**
* Candidate mentions contain **inconsistent labeling**
* Some columns contain missing values (e.g., ad stop time, bylines)

These issues required explicit handling and highlight an important reality:
**real-world datasets require significant preprocessing before analysis.**

---

### 7. Key Takeaways

* Most ads fall into **low spending ranges**, with fewer high-range campaigns
* Advertising activity is **unevenly distributed across organizations**
* Candidate mentions are **frequent but inconsistently labeled**
* Ad activity shows **clear temporal spikes**, suggesting event-driven behavior
* Messaging is dominated by **economy, healthcare, and social issues**
* Data cleaning and type handling are critical for accurate analysis

---

### Final Reflection

This analysis highlights the difference between automated summaries and hands-on data exploration. While Pandas provides quick statistical overviews, deeper understanding comes from engaging directly with the structure and limitations of the dataset.

Working through issues such as non-numeric spend values, inconsistent labels, and missing data provided insights that would not be immediately visible through automated tools alone.
