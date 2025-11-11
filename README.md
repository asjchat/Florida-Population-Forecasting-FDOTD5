# FDOT District 5 Demographic Analysis (2025-2050)

##  Overview

This repository contains comprehensive population projections and demographic analysis for **FDOT District 5** (9 Central Florida counties) compared to statewide Florida for the period **2025-2050**.

### Key Findings

- **D5 grows 27.07%** vs **Florida 20.49%** (1.32x faster)
- **80+ population nearly TRIPLES** in D5 (+120.63% vs +39.61%)
- **D5 outpaces Florida in every age demographic** (1.37x to 3.05x advantage)
- **Aging shift significant:** 65+ population grows from 22.4% to 25.9% of D5 total

## 📁 Project Structure

```
FDOT_D5_Public_Release/
├── index.html                          (Interactive dashboard - START HERE)
├── analysis_results.json               (Complete dataset - 3,216 records)
├── metadata.json                       (Project metadata)
├── FDOT_D5_Summary_Tables.xlsx        (Professional summary tables)
├── README.md                          (This file)
├── DOCUMENTATION.md                   (Detailed methodology)
└── LICENSE                            (CC0 Public Domain)
```

##  Quick Start

### Option 1: View Online (No Installation Needed)
1. Open `index.html` in your browser
2. Use interactive controls to explore data
3. Click download buttons to get datasets

### Option 2: Analyze the Data
1. Open `analysis_results.json` in any text editor or JSON viewer
2. Import into Excel, Python, R, or other analysis tools
3. See `DOCUMENTATION.md` for data structure details

### Option 3: Use Summary Tables
1. Open `FDOT_D5_Summary_Tables.xlsx` in Excel
2. Six pre-formatted sheets with all key tables
3. Ready to use in presentations and reports

##  Download Functionality

The interactive dashboard includes download buttons for:

- **Dataset (JSON):** `analysis_results.json` - Complete county-level time series
- **Metadata (JSON):** `metadata.json` - Project information and specifications
- **Summary Tables (Excel):** `FDOT_D5_Summary_Tables.xlsx` - Professional tables

##  Data Summary

### Coverage
- **67 Florida counties** (all included)
- **9 FDOT D5 counties** (focus region)
- **8 age demographic groups**
- **6 projection years:** 2025, 2030, 2035, 2040, 2045, 2050
- **3,216 data records** total

### D5 Population Projections
| Year | Population | 5-Year Change |
|------|-----------|---------------|
| 2025 | 4,926,687 | — |
| 2030 | 5,235,048 | +6.2% |
| 2035 | 5,544,150 | +5.9% |
| 2040 | 5,833,689 | +5.2% |
| 2045 | 6,041,971 | +3.6% |
| 2050 | 6,260,326 | +3.6% |

**25-Year Growth: +27.07% (+1.33M people)**

##  Data Source

**BEBR Population Projections**
- Organization: Bureau of Economic and Business Research
- Institution: University of Florida
- Methodology: Cohort-component method with fertility, mortality, and migration assumptions
- Website: https://www.bebr.ufl.edu/

**Citation Format:**
> Bureau of Economic and Business Research, University of Florida. (2025). Age Projections - Florida. Retrieved from https://www.bebr.ufl.edu/

##  Age Group Comparison (D5 vs. Florida)

| Age Group | D5 Growth | FL Growth | D5 Advantage |
|-----------|----------|----------|--------------|
| 0-4 | 15.98% | 10.10% | 1.58x |
| 5-17 | 19.40% | 13.78% | 1.41x |
| 18-24 | 19.87% | 13.85% | 1.43x |
| 25-54 | 22.82% | 16.59% | 1.37x |
| 55-64 | 22.42% | 11.80% | **1.90x** |
| 65-79 | 21.24% | 14.02% | 1.51x |
| 80+ | 120.63% | 39.61% | **3.05x** ⭐ |
| **Total** | **27.07%** | **20.49%** | **1.32x** |

## FDOT District 5 Counties

1. **BREVARD** - Florida's Space Coast
2. **FLAGLER** - Historic coastal region
3. **LAKE** - Central ridge area
4. **MARION** - Ocala area
5. **ORANGE** - Orlando metro (largest D5 county)
6. **OSCEOLA** - Kissimmee area
7. **SEMINOLE** - Sanford/Altamonte Springs area
8. **SUMTER** - Summerfield/Villages area
9. **VOLUSIA** - Daytona Beach area

## Statistical Validation

- **Regression Model:** OLS with interaction terms
- **Model Fit:** R² = 0.9997 (99.97% variance explained)
- **Hypothesis Test:** Welch t-test (aging vs. working-age cohorts)
- **Data Quality:** 100% coverage of Florida counties

## Data Formats

### JSON (analysis_results.json)
```json
{
  "summary": {
    "analysis_period": "2025-2050",
    "d5_counties": [...],
    "age_groups": [...]
  },
  "growth_data": [...],
  "county_time_series": [...]
}
```

### Excel (FDOT_D5_Summary_Tables.xlsx)
- Sheet 1: Summary Overview
- Sheet 2: D5 Time Series
- Sheet 3: Florida Time Series
- Sheet 4: D5 vs Florida Comparison
- Sheet 5: D5 Counties Detail
- Sheet 6: Data Source Information

## How to Use This Data

### For Research
1. Download `analysis_results.json`
2. Import into Python, R, or Excel
3. Perform custom analysis
4. Reference BEBR as data source

### For Planning
1. Review `FDOT_D5_Summary_Tables.xlsx`
2. Use tables in presentations
3. Reference key metrics for decision-making
4. Share with stakeholders

### For Policy
1. Analyze aging population trends (65+ growing fastest)
2. Plan infrastructure for working-age growth
3. Consider migration and economic impacts
4. Reference official BEBR projections

## 📋 Features

### Interactive Dashboard (index.html)
- ✓ County selection with checkboxes
- ✓ Demographic group comparison
- ✓ Toggle between growth rate and absolute population
- ✓ Download dataset and metadata buttons
- ✓ Professional interface
- ✓ Responsive design (desktop & mobile)
- ✓ Offline capable after first load

### Data Downloads
- ✓ Complete JSON dataset
- ✓ Project metadata
- ✓ Summary tables (Excel)
- ✓ Documentation

#

