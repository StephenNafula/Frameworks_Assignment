#  Frameworks_Assignment - CORD-19 Data Explorer

This project analyzes the [CORD-19 dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) (metadata.csv) and builds a simple **Streamlit app** to visualize COVID-19 research trends.

---

##  Project Structure
Frameworks_Assignment/
│
├── data/ # Place metadata.csv here
├── notebooks/ # Jupyter notebook with analysis
│ └── cord19_analysis.ipynb
├── app.py # Streamlit web application
├── requirements.txt # Python dependencies
└── README.md # Documentation

---

##  Installation
Clone the repo:
```bash
git clone https://github.com/YOUR-USERNAME/Frameworks_Assignment.git
cd Frameworks_Assignment
```

Install dependencies:
```bash
pip install -r requirements.txt
```
 Usage
Jupyter Notebook
```bash
jupyter notebook notebooks/cord19_analysis.ipynb
```

Streamlit App
```bash
streamlit run app.py
```

## Features

Data Cleaning & Exploration (titles, abstracts, journals, publication dates)

**Visualizations:**

Publications per year

Top journals

Word cloud of titles

Interactive filtering with Streamlit

## Reflection

This assignment helped me practice:

Loading and cleaning real-world data

Performing basic exploratory analysis

Creating clear visualizations

Building a simple web application

Biggest challenge: handling missing values and formatting dates.
Key learning: the data science workflow — Load → Clean → Analyze → Visualize → Present.
