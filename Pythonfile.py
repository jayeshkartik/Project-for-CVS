import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Specify the relative file path
file_path = 'Dataset.csv'

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Now you can work with the DataFrame 'df'
    print(df.head())  # Print the first few rows of the DataFrame
except FileNotFoundError:
    print("File not found. Please check the file path.")

#Loading the dataset
data=pd.read_csv("Dataset.csv")
print("The Dataset used for the project:",data)


#Exploratory Data Analysis

#Display the top 5 rows of the dataset
head_data=data.head(5)
print("The top 5 rows of the dataset is:",head_data)

#Display the number of rows and columns of a dataset-
shape_data=data.shape
print("The number of rows and columns in the dataframe is:",shape_data)

#Display the name of each column of the dataframe-
columns_data=data.columns.tolist()
print("Columns present in the dataset:",columns_data)


#2.Data Cleaning
#Count the number of missing values in dataset
null_counts=data.isnull().sum()
print("The total number of null values in each column:",null_counts)

# Drop rows with any NA/null values in specific columns
columns_to_check = data.columns
columns_to_remove = ['Year', 'Month', 'Footnote']
main_data= data.drop(columns=columns_to_remove)
print("The dataframe after removing the unnecessary columns:")
print(main_data)

# Display the resulting DataFrame
main_df=main_data.dropna()
print("The Dataframe after removing null values is")
print(main_df)

#Dropping the duplicates
main_df=main_df.drop_duplicates()

#Statistical Analysis of the dataframe
data_desc=main_df.describe()
print("Description of the Dataset")
print(data_desc)
#Information about the dataframe
print("Information of the Dataset")
data_info=main_df.info()
print(data_info)


# Rename columns
main_df = main_df.rename(columns={'Pneumonia and COVID-19 Deaths': 'P&C Deaths','Pneumonia, Influenza, or COVID-19 Deaths': 'P/I/C Deaths'})
numeric_col=main_df[['COVID-19 Deaths', 'Pneumonia Deaths','P&C Deaths', 'Influenza Deaths', 'P/I/C Deaths']]


#Skewness of the dataframe
numeric_col_skew=numeric_col.skew()
print("Skewness of the Dataframe:")
print(numeric_col_skew)
plot1=plt.plot(numeric_col_skew)
plt.savefig('plot1.png')
print(plot1)



#Mean of the Dataframe
numeric_col_mean=numeric_col.mean()
print("Mean of the Dataframe:")
print(numeric_col_mean)


#Median of the Dataframe
numeric_col_median=numeric_col.median()
print("Median of the Dataframe:")
print(numeric_col_median)
plot3=plt.plot(numeric_col_median)
plt.savefig('plot3.png')
print(plot3)



# Grouping the data by Age Group and summing up the number of deaths for each type
# Dropping rows where 'Age Group' is 'All Ages'
main_df = main_df[main_df['Age Group'] != 'All Ages']
deaths_by_age = main_df.groupby('Age Group').agg({
    'COVID-19 Deaths': 'sum',
    'Pneumonia Deaths': 'sum',
    'P&C Deaths': 'sum',
    'Influenza Deaths': 'sum',
    'P/I/C Deaths': 'sum'
}).reset_index()

# Plotting the number of different types of deaths in different age group using a bar plot
plt.figure(figsize=(12, 8))
x = deaths_by_age['Age Group']
y = deaths_by_age.drop(columns='Age Group').sum(axis=1)
plt.bar(x, y)
# Adding labels and title
plt.xlabel('Age Group')
plt.ylabel('Number of Deaths')
plt.title('Number of Different Types of Deaths in Different Age Group')
# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
# Show plot
plt.tight_layout()
plt.savefig('plot4.png')
plot4=plt.show()



# Grouping the data by Sex and summing up the number of deaths for each type
main_df = main_df[main_df['Sex'] != 'All Sexes']
deaths_by_gender = main_df.groupby('Sex').agg({
    'COVID-19 Deaths': 'count',
    'Pneumonia Deaths': 'count',
    'P&C Deaths': 'count',
    'Influenza Deaths': 'count',
    'P/I/C Deaths': 'count'
}).reset_index()

# Plotting the number of different types of deaths in different gender using a bar plot
plt.figure(figsize=(12, 8))
x = deaths_by_gender['Sex']
y = deaths_by_gender.drop(columns='Sex').sum(axis=1)
plt.bar(x, y)

# Adding labels and title
plt.xlabel('Sex')
plt.ylabel('Number of Deaths')
plt.title('Number of Different Types of Deaths in Different Gender')
# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
# Show plot
plt.tight_layout()
plt.savefig('plot5.png')
plot5=plt.show()
# Grouping the data by State and summing up the number of deaths for each type
main_df = main_df[main_df['State'] != 'United States']
deaths_by_state = main_df.groupby('State').agg({
    'COVID-19 Deaths': 'mean',
    'Pneumonia Deaths': 'mean',
    'P&C Deaths': 'mean',
    'Influenza Deaths': 'mean',
    'P/I/C Deaths': 'mean'
}).reset_index()

# Plotting the number of different types of deaths in different state using a bar plot
plt.figure(figsize=(12, 8))
x = deaths_by_state['State']
y = deaths_by_state.drop(columns='State').sum(axis=1)
plt.bar(x, y)

# Adding labels and title
plt.xlabel('State')
plt.ylabel('Number of Deaths')
plt.title('Number of Different Types of Deaths in Different State')
# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
# Show plot
plt.tight_layout()
plt.savefig('plot6.png')
plot6=plt.show()


# Pivot the deaths_by_state DataFrame for better visualization
heatmap_data = deaths_by_state.drop(columns='State').set_index(deaths_by_state['State'])

# Plotting the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True)

# Adding labels and title
plt.xlabel('Types of Deaths')
plt.ylabel('State')
plt.title('Number of Different Types of Deaths in Different States')

# Show plot
plt.tight_layout()
plt.savefig('plot7.png')
plot7=plt.show()



# Compute correlation matrix
correlation_matrix = numeric_col.corr()
print("Correlation Matrix:")
print(correlation_matrix)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.savefig('plot8.png')
plot8=plt.show()


# Handling Outliers
# Identify outliers using boxplots
plt.figure(figsize=(10, 6))
sns.boxplot(data=numeric_col)
plt.title("Boxplot of numerical features")
plt.xticks(rotation=45)
plt.savefig('plot9.png')
plot9=plt.show()


# Grouping the data by 'State' and summing up the number of deaths for each type
deaths_by_state = main_df.groupby('State').agg({
    'COVID-19 Deaths': 'sum',
    'Pneumonia Deaths': 'sum',
    'P&C Deaths': 'sum',
    'Influenza Deaths': 'sum',
    'P/I/C Deaths': 'sum'
}).reset_index()

# Calculate the total number of deaths for each type across all states
total_deaths = deaths_by_state.drop(columns='State').sum()

# Plotting a pie chart for the different types of deaths contributing to total deaths
plt.figure(figsize=(8, 8))

# Define labels for each category (types of deaths)
labels = total_deaths.index

# Get total number of deaths for each category
sizes = total_deaths.values

# Plotting the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# Adding title
plt.title('Percentage of Different Types of Deaths Contributing to Total Deaths')

# Show plot
plt.axis('equal')
plt.savefig('plot10.png')
plot10=plt.show()

# Define the directory path
directory = "C:/Users/jayes/OneDrive/Desktop/CVS Individual Project/Results/"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the file path
file_path = "analysis_results.txt"

# Save results to a text file
with open(file_path, "w") as text_file:
    text_file.write("Introduction to report:,\n")
    text_file.write("**Title: Understanding COVID-19 Deaths by Gender and Age**")
    text_file.write("Introduction")
    text_file.write("As we continue to fight COVID-19, it's crucial to understand who it affects most. The CDC has been gathering data on COVID-19 deaths based on gender and age. This report looks into that data to see how the virus impacts different groups. By studying these patterns, we can figure out where to focus our efforts to save lives and protect public health. This report aims to help policymakers, doctors, researchers, and everyone else understand who's most at risk from COVID-19.")
    text_file.write("The top 5 rows of the dataset is:,\n")
    text_file.write(str(head_data) + "\n\n")
    text_file.write("The number of rows and columns in the dataframe is:,\n")
    text_file.write(str(shape_data) + "\n\n")
    text_file.write("Columns present in the dataset:,\n")
    text_file.write(str("columns_data") + "\n\n")
    text_file.write("The total number of null values in each column:,\n")
    text_file.write(str("null_counts") + "\n\n")
    text_file.write("Description of the Dataset:\n")
    text_file.write(str(data_desc) + "\n\n")
    text_file.write("Information of the Dataset:\n")
    text_file.write(str(data_info) + "\n\n")
    text_file.write("Skewness of the Dataframe:\n")
    text_file.write(str(numeric_col_skew) + "\n\n")
    text_file.write("Mean of the Dataframe:\n")
    text_file.write(str(numeric_col_mean) + "\n\n")
    text_file.write("Median of the Dataframe:\n")
    text_file.write(str(numeric_col_median) + "\n\n")
    text_file.write("Correlation Matrix:\n")
    text_file.write(str(correlation_matrix) + "\n\n")

print("Results saved to:", file_path)

# Save main_df as a CSV file
csv_file_path="main_dataframe.csv"
main_df.to_csv(csv_file_path, index=False)

print("main_df saved as CSV file:", csv_file_path)
