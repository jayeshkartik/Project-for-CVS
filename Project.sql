#Top 5 Age group with maximum number of deaths due to any any of the three reasons-
SELECT Age_Group,
       SUM(COVID_19_Deaths) AS Covid_Deaths, 
       SUM(Pneumonia_Deaths) AS Pneumonia_Deaths, 
       SUM(P_C_Deaths) AS Pneumonia_and_corona_deaths,
       SUM(P_I_C_Deaths) AS pneumonia_or_influenza_or_Corona_Deaths 
FROM `practice-project-419014.projectdataset.corona` 
GROUP BY Age_Group
ORDER BY Covid_Deaths + Pneumonia_Deaths + Pneumonia_and_corona_deaths + pneumonia_or_influenza_or_Corona_Deaths  DESC
LIMIT 5;


#Top 10 states with maximum deaths
SELECT State,COUNT(Total_Deaths) AS Total_Deaths
FROM `practice-project-419014.projectdataset.corona`
GROUP BY State
ORDER BY Total_Deaths DESC
LIMIT 10;

#Top 5 States with maximum deaths due to any of three diseases
SELECT State,
       SUM(COVID_19_Deaths) AS Covid_Deaths, 
       SUM(Pneumonia_Deaths) AS Pneumonia_Deaths, 
       SUM(P_C_Deaths) AS Pneumonia_and_corona_deaths,
       SUM(P_I_C_Deaths) AS pneumonia_or_influenza_or_Corona_Deaths 
FROM `projectdataset.corona`
GROUP BY State
ORDER BY Covid_Deaths + Pneumonia_Deaths + Pneumonia_and_corona_deaths + pneumonia_or_influenza_or_Corona_Deaths  DESC
LIMIT 5;

#Total number of Deaths every year
SELECT EXTRACT(YEAR FROM Start_Date) AS Year,
       SUM(Total_Deaths) AS Total_Deaths
FROM `projectdataset.corona`
GROUP BY Year
ORDER BY Year;

#Total number of Deaths every month
SELECT EXTRACT(YEAR FROM Start_Date) AS Year,EXTRACT(MONTH FROM Start_Date) AS Month,
       SUM(Total_Deaths) AS Total_Deaths
FROM `projectdataset.corona`
GROUP BY Month,Year
ORDER BY Month,Year;

#Top 10 states with maximum Average Deaths per Day
SELECT AVG(Total_Deaths) AS Average_Deaths_Per_Day,State
FROM `projectdataset.corona`
GROUP BY State
ORDER BY Average_Deaths_Per_Day
LIMIT 10;

#Maximum Number of Deaths in a single day
SELECT MAX(Total_Deaths) AS Max_Deaths_In_A_Single_Day,Start_Date,End_Date
FROM `projectdataset.corona`
GROUP BY Start_Date,End_Date
ORDER BY Max_Deaths_In_A_Single_Day;

#Total Deaths by Gender
SELECT Sex,SUM(Total_Deaths) AS Total_Deaths_By_Gender
FROM `projectdataset.corona`
GROUP BY Sex;


