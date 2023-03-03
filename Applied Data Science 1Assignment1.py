

#import libraries
import pandas as pd
import matplotlib.pyplot as plt


# reading my dataset

df = pd.read_csv('GDP_per_capita_table.csv', index_col=0)
print(df)
# Load the dataset into a Pandas dataframe


def plot_line(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    for country in df.columns:
        year = ['2017', '2018', '2019', '2020', '2021']
# Create a line plot for the countries
        ax.plot(year, df[country], label=country)
 # Add plot title and labels
    ax.set_xlabel('Year')
    ax.set_ylabel('GDP per capita (USD)')
    ax.set_title('GDP per capita in European countries (2017-2021)')
 # Show legend and plot
    ax.legend()
    plt.show()


plot_line(df)


# Bar plot

# Select the  data
def plot_bar(df, year):
    data = df.loc[year]
    fig, ax = plt.subplots(figsize=(8, 6))
# Create a barplot
    ax.bar(data.index, data.values)
# Add plot title and labels
    ax.set_xlabel('Countries')
    ax.set_ylabel('Gross Domestic Product per capita (USD)')
    ax.set_title('Gross Domestic Product per capita in European countries in 2021')
# Show plot
    plt.show()


plot_bar(df, 2021)


# Pie chart

# Select data for the year 2021
data_2021 = df.loc[2021]

# Create a pie chart
labels = data_2021.index
size = data_2021.values
plt.pie(size, labels=labels, autopct='%1.1f%%')
plt.axis('equal')

# Adding a title to my piechart
plt.title('Countries GDP_per_capita in 2021')

# Show the plot
plt.show()
