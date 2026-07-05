# CFPB Consumer Complaints Dashboard

A Power BI dashboard analyzing over 1.28 million consumer complaints submitted to the 
Consumer Financial Protection Bureau (CFPB) between 2011 and 2019 — broken down by 
Product, State, and Year.
## Dashboard:

<img width="1372" height="791" alt="Screenshot 2026-07-05 222934" src="https://github.com/user-attachments/assets/e47e85de-a8b6-4f56-894b-1a18fb7b930a" />


## Project Goal

Explore consumer complaint patterns across financial products (mortgages, credit cards, 
debt collection, etc.), track complaint volume trends over time, and identify geographic 
concentration by state.

## Data Source

- **Dataset:** CFPB Consumer Complaint Database
- **Mirror used:** [Kaggle — Consumer Complaint Database](https://www.kaggle.com/datasets/selener/consumer-complaint-database)
- **Date range:** November 2011 – May 2019
- **Size:** ~702 MB raw, 18 columns

> **Note:** The raw and cleaned CSV files are not included in this repo due to GitHub's 
> file size limits. See [Reproducing This Project](#-reproducing-this-project) below.

## 🛠️ Data Cleaning Process

While loading the raw CSV into Power BI, the "Date received" column showed hundreds of 
thousands of conversion errors, along with garbage text (e.g. sentence fragments) 
appearing in date fields.

**Root cause:** The "Consumer complaint narrative" column contains free-text complaints 
where users pressed Enter multiple times while typing. These multi-line fields were 
correctly quoted per CSV standard, but Power BI's default Text/CSV importer doesn't 
handle quoted multi-line fields properly — it miscounted embedded line breaks as new 
rows, shifting columns out of alignment and inflating the apparent row count to 
1,970,829 (actually the number of physical text lines, not records).

**Fix:** Cleaned the data using Python (`pandas`, Python engine), which correctly parses 
quoted multi-line fields. This recovered the true record count of **1,282,355 rows** — 
verified against Kaggle's published date-range bucket totals — with zero data loss.


## Dashboard Visuals

1. **Card** — Total Complaints (1,282,355)
2. **Column Chart** — Complaints by Product (Mortgage, Debt collection, and Credit 
   reporting are the top three categories)
3. **Line Chart** — Complaints trend by year (2011–2019), showing steady growth peaking 
   around 2017–2018
4. **Filled Map** — Complaints by state, shaded by volume, with exact counts on hover

## Tech Stack

- **Python** (pandas) — data cleaning
- **Power BI Desktop** — dashboard and visualization

## Reproducing This Project

1. Download `rows.csv` from the 
   [Kaggle dataset](https://www.kaggle.com/datasets/selener/consumer-complaint-database)
2. Place it in the same folder as `clean_complaints.py`
3. Install pandas: `pip install pandas`
4. Run the cleaning script: python clean_complaints.py
5. 5. This generates `complaints_clean.csv`
6. Open `CFPB_Complaints_Dashboard.pbix` in Power BI Desktop and point the data source 
   to your local `complaints_clean.csv`
