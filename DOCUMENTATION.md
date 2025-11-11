# FDOT D5 Analysis - Complete Documentation

## Data Processing Pipeline

### 1. Data Source
- **File:** Age Projections - Florida (1).xlsx
- **Format:** Excel spreadsheet
- **Coverage:** All 67 Florida counties
- **Time Period:** 2025-2050
- **Source:** BEBR (University of Florida)

### 2. Data Structure

**Input Format (Excel):**
```
County | Age/Sex | 2025 | 2030 | 2035 | 2040 | 2045 | 2050
-------|---------|------|------|------|------|------|------
...    | ...     | ...  | ...  | ...  | ...  | ...  | ...
```

**Age Categories Processed:**
- 0-4 years
- 5-17 years
- 18-24 years
- 25-54 years
- 55-64 years
- 65-79 years
- 80+ years
- Total (aggregate)

### 3. Processing Steps

**Step 1: Data Extraction**
- Parse Excel file
- Convert age range formats (e.g., "00-00" → "0-4")
- Standardize numeric columns
- Handle missing values

**Step 2: Regional Aggregation**
- Create FDOT D5 aggregate (sum of 9 counties)
- Create Florida aggregate (sum of all 67 counties)
- Maintain statewide comparison

**Step 3: Growth Calculation**
```
Growth % = ((Population_2050 - Population_2025) / Population_2025) × 100
```

**Step 4: Statistical Analysis**
- Ordinary Least Squares (OLS) regression
- Welch t-test for group comparisons
- Calculate interaction effects

### 4. Output Data Structure

**JSON Format (analysis_results.json):**

```json
{
  "summary": {
    "analysis_period": "2025-2050",
    "d5_counties": ["BREVARD", "FLAGLER", ...],
    "age_groups": ["0-4", "5-17", ...],
    "aging_groups": ["65-79", "80+"],
    "working_groups": ["0-4", "5-17", "18-24", "25-54"]
  },
  "growth_data": [
    {
      "Region": "FDOT D5 Aggregate",
      "AgeGroup": "0-4",
      "Pop_2025": 261423,
      "Pop_2050": 303198,
      "GrowthPct": 15.98,
      "IsD5": true
    },
    ...
  ],
  "county_time_series": [
    {
      "County": "ORANGE",
      "AgeGroup": "0-4",
      "Year": 2025,
      "Population": 85000,
      "Is_D5": true
    },
    ...
  ],
  "regression_by_age": {
    "0-4": {
      "r_squared": 0.9997,
      "interaction_pvalue": 0.002574,
      "is_significant": true
    },
    ...
  }
}
```

## Statistical Methods

### Regression Analysis

**Model:** 
```
Population ~ Year_Centered + Region_D5 + (Year_Centered × Region_D5)
```

**Variables:**
- `Year_Centered`: Years since 2025 (0, 5, 10, 15, 20, 25)
- `Region_D5`: Binary indicator (1 = D5, 0 = Florida)
- Interaction term captures D5-specific growth advantage

**Results by Age Group:**

| Age Group | R² | Interaction p-value | Significant |
|-----------|:--:|:-------------------:|:-----------:|
| 0-4 | 0.9997 | 0.0026 | ✓ YES |
| 5-17 | 0.9993 | 0.0033 | ✓ YES |
| 18-24 | 0.9997 | 0.0004 | ✓ YES |
| 25-54 | 0.9991 | 0.0021 | ✓ YES |
| 55-64 | 0.9923 | 0.1778 | ✗ NO |
| 65-79 | 0.9938 | 0.4518 | ✗ NO |
| 80+ | 0.9982 | <0.0001 | ✓ YES |
| **Total** | **0.9997** | **<0.0001** | **✓ YES** |

**Interpretation:**
- R² > 0.99: Excellent fit - model explains >99% of variance
- Significant interaction terms indicate D5 grows faster than Florida
- Non-significant 55-64 and 65-79: Florida growth comparable to D5 in these cohorts

### Hypothesis Test: Aging vs. Working-Age

**Groups:**
- Aging cohorts: 65-79, 80+ (D5)
- Working-age: 0-4, 5-17, 18-24, 25-54 (D5)

**Method:** Welch Two-Sample t-test
- Assumes unequal variances
- Appropriate for small samples

**Results:**
- t-statistic: 1.686
- p-value: 0.167
- Result: Not significant at α = 0.05

**Interpretation:** Aging and working-age cohorts show different growth rates, but difference is not statistically significant. Aging cohorts show higher absolute growth (120.63% for 80+, 21.24% for 65-79).

## Key Metrics Explained

### Growth Rate
Percentage change in population from 2025 to 2050:
```
Growth % = ((Pop_2050 - Pop_2025) / Pop_2025) × 100
```

### D5 Advantage
Ratio of D5 growth to Florida growth:
```
Advantage = D5_Growth_Rate / Florida_Growth_Rate
```

Example: 80+ age group
- D5: 120.63%
- Florida: 39.61%
- Advantage: 120.63 / 39.61 = 3.05x

### Population Density
Not calculated in this analysis but can be computed using area data.

## Data Quality & Limitations

### Strengths
- ✓ Official BEBR projections
- ✓ 100% coverage of Florida counties
- ✓ Rigorous cohort-component methodology
- ✓ R² = 0.9997 indicates excellent model fit
- ✓ 3,216 data points for validation

### Limitations
- ⚠ Projections assume demographic trends continue
- ⚠ Actual results may differ due to:
  - Unexpected migration patterns
  - Economic shifts
  - Policy changes
  - Pandemics or disasters
- ⚠ County-level data has some variability
- ⚠ Does not include spatial/geographic analysis

### Recommendations
- Use as planning baseline, not absolute prediction
- Consider multiple scenarios
- Update projections periodically
- Combine with other data sources
- Factor in local knowledge and trends

## Data Access & Formats

### JSON (analysis_results.json)
- **Best for:** Data analysis, programming
- **Size:** ~500 KB
- **Tools:** Python, R, JavaScript, Excel (import as Web Data)
- **Structure:** Hierarchical with arrays

### Excel (FDOT_D5_Summary_Tables.xlsx)
- **Best for:** Business users, presentations
- **Format:** Multi-sheet workbook
- **Sheets:** 6 professional tables
- **Size:** ~100 KB

### CSV (can be exported)
- **Best for:** Import into analysis software
- **Format:** Text file with comma-separated values
- **Tools:** All spreadsheet software, R, Python

## Using This Data

### Python Example
```python
import json

with open('analysis_results.json') as f:
    data = json.load(f)

# Get D5 growth data
d5_growth = [r for r in data['growth_data'] if r['IsD5']]
print(d5_growth)

# Get county time series
orange = [r for r in data['county_time_series'] 
          if r['County'] == 'ORANGE']
print(orange)
```

### Excel Import
1. File → Open → analysis_results.json
2. Excel opens JSON Navigator
3. Select desired tables
4. Import to spreadsheet

### R Example
```r
library(jsonlite)
data <- fromJSON('analysis_results.json')
growth_df <- data.frame(data$growth_data)
```

## For More Information

- **BEBR Official Site:** https://www.bebr.ufl.edu/
- **FDOT:** https://www.fdot.gov/
- **Florida Population:** https://www.bebr.ufl.edu/
- **Census Data:** https://www.census.gov/

## Version History

### Version 1.0.0 (November 10, 2025)
- Initial release
- Complete 2025-2050 projections
- 67 Florida counties
- 8 age demographic groups
- Interactive dashboard
- Download functionality
