import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dataframe = pd.read_csv("Zomato data .csv")
print("dataframe")
pd.set_option('display.max_columns', None)
print(dataframe)
def extract_rating(rate):
    return float(rate.split('/')[0])


dataframe['rate'] = dataframe['rate'].apply(extract_rating)


dataframe.to_csv('Zomato data', index=False)

print(dataframe)

dataframe.info()
# What type of restaurants do the majority of customers oder from?
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("type of restaurants")
plt.show()

# The majority of customers order from dinning restaurants


# How many votes has each type of restaurants recived from customers?


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes':grouped_data})
plt.plot(result,c= "green",marker="o")
plt.xlabel("Type of restaurants",c="red",size=20)
plt.ylabel("Votes", c = "red",size=20)
plt.show()

# Dining has recived most ammount of votes



# What are the ratings that the mmajority of restaurants has recived?

plt.hist(dataframe['rate'],bins=5)
plt.title("ratings distributions")
plt.show()

# The majority restaruants recived ratoings from 3.5 to 4


# Zomato has observed that most couples order most of food online.What is the average spendings on each order?


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.show()

# The majority of couples prefer restauarants with an approximate cost of 300 rupees

# Which mode(online or offline )has recib=ved the maximum ratings?

plt.figure(figsize=(6,6))
sns.boxplot(x='online_order',y= 'rate',data= dataframe)
plt.show()

# offline orders recive less ratings compare to online orders


# Which type of restaurants recived more offline odres, so that zomato can produces customers with some good offers?

pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table,annot= True,cmap="YlGnBu",fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed in Type")
plt.show()

# Dinning restaurants primarily accepted offlim=ne orders, whereas cafes primarily recive online orders.This suggest that
# clients prefer orders in person at restaurants , but prefer online ordering in cafes