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
 ![image alt](https://github.com/amir-yousuf-01/data-craft-python/blob/ad53e6bdc777174ba934ac4a6af6e4ec9ee0f934/Zomato%20Project/1.png)

Insight:

Dining restaurants dominate Zomato listings (≈60% of all restaurants)

Cafes represent ≈25%, while Buffet and other types are less common
Business Implication:
Focus marketing efforts on dining establishments which have the highest market presence.

2. Customer Votes by Restaurant Type
 ![image alt](https://github.com/amir-yousuf-01/data-craft-python/blob/8807656790a26074929ce41dbb85ac2522c44376/Zomato%20Project/2.png)

Key Finding:

Dining restaurants receive 3× more votes than cafes

Buffet restaurants have surprisingly low engagement
Action Item:
Investigate why buffet restaurants underperform in customer engagement

3. Ratings Distribution
   ![image alt](https://github.com/amir-yousuf-01/data-craft-python/blob/0eb386413fcd513b889d6f42df1df3c6b1cd819d/Zomato%20Project/3.png)
   
Pattern Observed:

68% of ratings fall between 3.5-4.25 (normal distribution)

Few restaurants have extreme low (<2.5) or high (>4.5) ratings
Data Note:
Cleaned rating values show no "0" scores, confirming proper data preprocessing

4. Price Distribution for Two People
![image alt](https://github.com/amir-yousuf-01/data-craft-python/blob/cc66c4d36e336f5dae2641419fe0759d8b61b981/Zomato%20Project/4.png)

Customer Behavior:

Strong peak at ₹300 price point (mode value)

80% of orders fall between ₹250-500 range
Strategic Insight:
Price sensitivity observed - maintain offerings in ₹300-400 sweet spot

5. Online vs Offline Order Ratings
   ![image alt](https://github.com/amir-yousuf-01/data-craft-python/blob/12c3a66ab5f6472b8c2e3563e298c7635c003868/Zomato%20Project/5.png)
   
Notable Difference:

Online orders average 0.3 points higher (3.9 vs 3.6)

Offline orders show wider rating variance
Hypothesis:
Digital convenience may influence customer satisfaction positively

6. Order Type Heatmap
![image alt](https://github.com/amir-yousuf-01/data-craft-python/blob/28c30b97b236273e7cb20397080a0cd2dda5a0be/Zomato%20Project/6.png)

Key Observations:

Restaurant Type	Online Orders	Offline Orders
Dining	40%	60%
Cafes	80%	20%
Recommendation:
Develop cafe-specific online promotions and dining-focused in-person experiences
   
   

