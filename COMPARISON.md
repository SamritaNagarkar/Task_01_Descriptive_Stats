
## Phase 1 vs Phase 2: Comparison and Reflections

### Do the results agree?

For the most part, the results from the pure Python implementation and the Pandas-based analysis are consistent. Key statistics such as count, mean, median, minimum, and maximum values match closely across both approaches.

One noticeable difference appears in the standard deviation values. This is expected because Pandas calculates the sample standard deviation (using n-1 in the denominator), while the pure Python implementation uses the population standard deviation (using n). This leads to small numerical differences but does not indicate an error.

Overall, the outputs align well and validate the correctness of the manual implementation.

### Where did the pure Python approach require explicit decisions?

The pure Python implementation required making several decisions that Pandas handles automatically:

* **Missing value handling:**
  I had to explicitly define what counts as a missing value (e.g., empty strings, "NA", "N/A") and ensure those values were excluded from calculations.

* **Type inference:**
  Determining whether a column is numeric or categorical required checking each value and deciding how to handle mixed data types. For example, some columns appeared numeric at first glance but actually contained structured string data.

* **Data interpretation challenges:**
  Certain columns such as *spend*, *impressions*, and *estimated_audience_size* contained values formatted as dictionary-like strings (e.g., `{'lower_bound': '200', 'upper_bound': '299'}`), rather than plain numbers. This required careful handling, as these values could not be directly used in numeric computations.

* **Edge cases:**
  I had to explicitly account for scenarios such as:

  * Columns with all missing values
  * Columns with only one unique value
  * Columns with zero variance
  * Columns that appear numeric but are actually structured or categorical in nature

In contrast, Pandas abstracts all of these decisions and applies its own internal logic, which is efficient but less transparent.

### What did I learn from the pure Python implementation?

Writing the analysis from scratch provided a much deeper understanding of the dataset and the challenges involved in real-world data processing.

Some key takeaways:

* **Data is not always what it seems:**
  Columns that initially appear numeric may actually contain structured or encoded information, which changes how they should be analyzed.

* **Type inference is non-trivial:**
  Determining whether a column is numeric or categorical is not always straightforward and depends heavily on how the data is represented.

* **Statistical calculations involve assumptions:**
  Implementing metrics like standard deviation highlighted how different formulas (population vs sample) can lead to slightly different results.

* **Tools like Pandas hide complexity:**
  While Pandas makes analysis much faster and more convenient, it abstracts away important decisions about data interpretation, missing values, and type handling.

Overall, the pure Python phase helped build a strong conceptual foundation, while the Pandas phase demonstrated how powerful libraries can streamline the same work once those concepts are understood.
