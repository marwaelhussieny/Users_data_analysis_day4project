# Users_data_analysis_day4project
# 👥 Users Data Analysis

A Python data analysis project for ITI Data analysis final course that fetches real user data from a public API, explores it with Pandas, and visualizes key insights using Seaborn .

## 📋 Requirements

```
pandas
matplotlib
seaborn
requests
```

---

## 📊 What This Project Does

### Data Loading
- Fetches data from the API using `requests` + `pd.json_normalize()`

### Data Exploration
- Shape of the DataFrame (rows, columns)
- List of all column names
- Data types per column
- Missing values per column
- Duplicate row count
- Summary statistics for numeric columns
- Value counts for: gender, bloodGroup, eyeColor, role, address.country

### Data Cleaning
- Extracts `country` from nested `address` column if missing
- Handles missing values in `age`, `height`, `weight` (fill with mean/median or drop)

### Analysis Questions Answered
1. What is the average age of users?
2. Average age by gender?
3. Number of users per gender?
4. Top 10 cities with the most users?
5. Average height and weight overall?
6. Is there any obvious relationship between age and height/weight?

### Visualizations (Seaborn)
At least 5 plots including:
- Distribution of ages
- Average age by gender
- User count by gender
- Top 10 cities by user count
- Height vs. Weight scatter (colored by gender)
- Age vs. Height / Age vs. Weight correlation plots

---

## 📁 Project Structure

```
users-data-analysis/
│
├── analysis.py        # Main analysis script
├── requirements.txt   # Project dependencies
├── README.md          # Project documentation
└── plots/             # Saved plot images (auto-generated)
```

---

## 🛠 Tools Used

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data loading & manipulation |
| Seaborn | Statistical visualizations |
| Matplotlib | Plot rendering |
| Requests | API data fetching |


- All plots use Seaborn's `whitegrid` style for consistency
- Plots are saved to the `/plots` directory automatically
