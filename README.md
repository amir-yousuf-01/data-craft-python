# 🍽️ Zomato Data Analysis Project

This project focuses on cleaning, analyzing, and visualizing Zomato restaurant data to extract key business insights.  
It answers important questions about customer behavior, restaurant ratings, spending habits, and online ordering trends.

---

## 📚 Project Objectives
- Clean the messy Zomato dataset (handling ratings and missing values).
- Perform exploratory data analysis (EDA) to uncover patterns.
- Create visualizations to support insights.
- Provide business recommendations for customer engagement.

---

## 📊 Analyses Performed

| Analysis Question | Method | Key Result |
|:------------------|:-------|:-----------|
| What types of restaurants do customers prefer? | Count plot | Dining restaurants are most preferred. |
| Which restaurant types received the most votes? | Line plot | Dining receives maximum votes. |
| What is the typical rating range of restaurants? | Histogram | Most restaurants rated between 3.5 and 4.0. |
| How much do couples usually spend? | Count plot | Around ₹300 on average. |
| Online vs Offline orders: Which gets better ratings? | Boxplot | Online orders receive slightly higher ratings. |
| Which restaurant types favor online vs offline orders? | Heatmap | Cafes favor online orders; Dining favors offline. |

---

## 🛠️ Technologies Used
- Python 3
- Pandas (Data manipulation)
- Matplotlib (Data visualization)
- Seaborn (Advanced plots)

---

## 📂 Project Structure

```plaintext
Zomato Project/
├── zomato_analysis.py      # Main Python script (analysis code)
├── zomato_data.csv         # Input dataset
├── type_of_restaurants.png # Saved visualization images
├── ratings_distribution.png
├── online_vs_offline_ratings.png
├── couple_spendings.png
├── votes_by_restaurant_type.png
├── online_offline_heatmap.png
└── README.md               # Project overview (this file)
