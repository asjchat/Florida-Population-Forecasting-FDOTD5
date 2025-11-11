# FDOT District 5 vs Florida - 65+ Population Growth Analysis

**Professional interactive visualization comparing population projections for FDOT District 5 against the State of Florida (2025-2050)**

🔗 **[View Live Visualization](#)** *(Add your GitHub Pages URL here after setup)*

---

## 📊 Overview

This comprehensive analysis dashboard provides:

- **Interactive Growth Comparisons**: Bar charts comparing 65+ demographic growth
- **Time Series Analysis**: Percentage growth trends from 2025 baseline
- **Top 10 Rankings**: Fastest growing counties with filters by age demographic
- **Statistical County Comparison**: OLS regression analysis between any two counties
- **Multi-County Growth Comparison**: Compare multiple counties simultaneously
- **Statistical Significance Testing**: Rigorous OLS regression with interaction terms

---

## 🎯 Key Features

### 1. Top 10 Fastest Growing Counties
Filter by:
- All Ages
- 65+ Aggregate
- 65-79 age group
- 80+ age group

FDOT District 5 counties highlighted when present in rankings.

### 2. Statistical County Comparison
- Select any FDOT District 5 county
- Compare against any Florida county
- Choose demographic category
- Get statistical significance results (p-values, growth rates)

### 3. Multi-County Growth Comparison
- Select multiple counties with checkboxes
- View growth rate (%) or actual population
- Toggle between visualization modes
- D5 counties clearly marked

### 4. Regression Analysis
- Full OLS regression results
- R-squared metrics
- Coefficient interpretations
- Statistical significance determination

---

## 🏛️ Design

**Visual Style**: McKinsey & Company corporate aesthetic
- Professional typography (Source Sans 3)
- Clean grid-based layout
- McKinsey color palette (Deep Navy #001A33, Blue #0066CC)
- Subtle animations and transitions
- Responsive design

---

## 🗂️ FDOT District 5 Counties

The analysis focuses on these 9 Central Florida counties:
1. Brevard
2. Flagler
3. Lake
4. Marion
5. Orange
6. Osceola
7. Seminole
8. Sumter
9. Volusia

---

## 📈 Data Source

Population projections based on Florida demographic forecasts covering:
- All 67 Florida counties
- Years: 2025, 2030, 2035, 2040, 2045, 2050
- Age groups: All Ages, 65-79, 80+, 65+ Aggregate

---

## 🚀 Viewing the Visualization

### Online (Recommended)
Visit the GitHub Pages URL: `[Your URL Here]`

### Local Setup
1. Download both files:
   - `comprehensive_analysis_visualization.html`
   - `analysis_results.json`
2. Place in the same directory
3. Start a local server:
   ```bash
   python -m http.server 8000
   ```
4. Open: `http://localhost:8000/comprehensive_analysis_visualization.html`

---

## 🛠️ Technical Stack

- **Visualization**: Plotly.js 2.27.0
- **Statistical Analysis**: Python (Pandas, Statsmodels)
- **Methodology**: OLS Regression with interaction terms
- **Design**: Pure HTML5, CSS3, JavaScript (ES6+)

---

## 📊 Statistical Methodology

### Regression Model
```
Population ~ Year_Centered * Region_D5
```

Where:
- `Year_Centered` = Year - 2025 (centered at baseline)
- `Region_D5` = Binary indicator (1 for D5, 0 for Florida)
- Interaction term tests if growth rates differ significantly

### Hypothesis Test
- **Null Hypothesis (H₀)**: Growth rates are equal (β₃ = 0)
- **Alternative (H₁)**: Growth rates differ (β₃ ≠ 0)
- **Significance Level**: α = 0.05

---

## 📄 License

This visualization is provided for analytical and educational purposes.

---

## 👤 Author

Ananda Chatterjee

---

## 📅 Last Updated

November 2025

---

**Questions or feedback?** Open an issue on this repository!
