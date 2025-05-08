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


📊 Visualization Analysis
1. Restaurant Type Distribution
2. ![image alt](https://github.com/amir-yousuf-01/data-craft-python/blob/ad53e6bdc777174ba934ac4a6af6e4ec9ee0f934/Zomato%20Project/1.png)
Insight:

Dining restaurants dominate Zomato listings (≈60% of all restaurants)

Cafes represent ≈25%, while Buffet and other types are less common
Business Implication:
Focus marketing efforts on dining establishments which have highest market presence

2. Customer Votes by Restaurant Type
Votes by Type
Key Finding:

Dining restaurants receive 3× more votes than cafes

Buffet restaurants have surprisingly low engagement
Action Item:
Investigate why buffet restaurants underperform in customer engagement

3. Ratings Distribution
Ratings Histogram
Pattern Observed:

68% of ratings fall between 3.5-4.25 (normal distribution)

Few restaurants have extreme low (<2.5) or high (>4.5) ratings
Data Note:
Cleaned rating values show no "0" scores, confirming proper data preprocessing

4. Price Distribution for Two People
Price Analysis
Customer Behavior:

Strong peak at ₹300 price point (mode value)

80% of orders fall between ₹250-500 range
Strategic Insight:
Price sensitivity observed - maintain offerings in ₹300-400 sweet spot

5. Online vs Offline Order Ratings
Order Ratings
Notable Difference:

Online orders average 0.3 points higher (3.9 vs 3.6)

Offline orders show wider rating variance
Hypothesis:
Digital convenience may influence customer satisfaction positively

6. Order Type Heatmap
Order Heatmap
Key Observations:

Restaurant Type	Online Orders	Offline Orders
Dining	40%	60%
Cafes	80%	20%
Recommendation:
Develop cafe-specific online promotions and dining-focused in-person experiences
   
   

