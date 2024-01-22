#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 13:04:23 2023

@author: udaniweerasinghe
"""


from tests import *
from functions import *
import matplotlib.pyplot as plt

sales=[]
profit=[]
assets=[]
companycount_dict ={}
sales_dict={}
market_value_dict = {}
    
    
try:
    with open("company.csv","r" ) as datafile:
        datafile.readline()
        try:
            for line in datafile:
                company, sales_val, profits, cost, assets, marketvalue, country, continent, latitude, longitude = line.strip().split(",")
                try:
                    sales.append(float(sales_val))
                except ValueError:
                    print("Error in sales value: ",sales_val)
                try:
                    profit.append(float(profits))
                except ValueError:
                    print("Error in Profit value: ",profits)
                companycount_dict[continent]=companycount_dict.get(continent,0)+1
                if continent not in sales_dict:
                    sales_dict[continent] = []
                sales_dict[continent].append(float(sales_val))
                if continent not in market_value_dict:
                    market_value_dict[continent] = []
                market_value_dict[continent].append(float(marketvalue))
            
        except ValueError:
            print("exceptions value")
            
except FileNotFoundError:
    print("File Not Found")


while True:
    print("------------------------------------------")
    print("/Welcome to the top companies in the World analysis")
    print("1 - Statistics")
    print("2 - Visualization")
    print("q - Quit")
    choice = input("Please enter your selection.")
    
    if choice=="1":
        print ("1 - Overall Companies Analysis")
        print("2 - Categorized Analysis")
        print("3 - To move back to Main menu")
        choice2 = input("Enter your selection.") 
        if choice2=="1":
            
            print("***The sales and profits statistics analysis***")
            print("Number of identified top companies : " , numberofvalues(sales))  
            
            print(f"Total of Sales in top  {numberofvalues(sales)} companies : {calc_total(sales):.2f}")
            print(f"Average Sales in Top companies : {calc_mean(sales):.2f}")
            print(f"Median Sales Value :  {calc_median(sales)}")
            print("Common value of Sales : " , calc_mode(sales))
            print("The maximum sales value : " , calc_max(sales))
            print("The minimum sales value : " , calc_min(sales))
            print(f"The range in sales : {calc_range(sales)}")
            print(f"The interquartile range value : {calc_interquartile_range(sales):.2f}")
            print(f"Standard Deviation in Sales : {calc_standard_deviation(sales):.2f}")
            print(f"Median Skewness in Sales : {calc_median_skewness(sales):.2f}")
            print(f"Mode Skewness in Sales : {calc_mode_skewness(sales):.2f}")
            
            
            
            
            
            print("--------------------------------------------------")
             
            print("Total of Profits in top ", numberofvalues(profit),f" companies : {calc_total(profit):.2f}")
            print(f"Average Profits of companies : {calc_mean(profit):.2f}")
            print("Median of Profits",  calc_median(profit))
            print("Common value of Profits : " , calc_mode(profit))
            print("The Higest profits earned by a company : " , calc_max(profit))
            print("The Lowest profits earned by a company : " , calc_min(profit))
            print("The range in profits : " ,calc_range(profit))
            print(f"The interquartile range value : {calc_interquartile_range(profit):.2f}")
            print(f"Standard Deviation in Profits: {calc_standard_deviation(profit):.2f}")
            print(f"Median Skewness in Profits : {calc_median_skewness(profit):.2f}")
            print(f"Mode Skewness in Profits : {calc_mode_skewness(profit):.2f}")
            
            print(f"Correlation between Sales and Profits: {calc_correlation(sales, profit):.3f}")
            
        elif choice2=="2":
            print("Number of Continenets the companies in : ", num_of_continenets(market_value_dict))
            category, value = max_count(companycount_dict)
            print(f"Continenet with the higest number of top companies: {category} with a value {value}")
            category, value = min_count(companycount_dict)
            print(f"Continenet with the lowest number of top companies: {category} with a value {value}")
            category, value = max_value(market_value_dict)
            print(f"Continenet with the higest market value of top companies: {category} with a value of {value:.3f}")
            category, value = min_value(market_value_dict)
            print(f"Continenet with the lowest market value in top companies: {category} with a value {value:.3f}")
            
            
        
        
    elif choice=="2":
        print ("1 - Sales and Profits of top companies Visualization")
        print("2 -MarketValue of World continenet Visualization")
        print("3 - To move back to Main menu")
        choice2 = input("Enter your selection.")
        if choice2=="1":
            print("1 - View Histogram of  Sales and profits")
            print("2 - View Box Plots of  Sales and profits")
            print("3 - View Scatter Plot of  Sales and profits")
            print("4 - To move back to Main menu")
            choice3= input("Enter your selection.")
            if choice3=="1":
                print("1 - Sales Distribution")
                print("2 - Profits Distribution")
                choice4= input("Enter your selection.")
                if choice4=="1":
                    visu_histsales(sales)
                    plt.show()
                elif choice4=="2":
                    visu_histprofits(profit)
                    plt.show()
                else:
                    print("Invalid input. Please enter 1,2")
            elif choice3=="2":
                print("1 - Sales Distribution")
                print("2 - Profits Distribution")
                choice4= input("Enter your selection.")
                if choice4=="1":
                    visu_boxplots(sales, "Sales")
                    plt.show()
                elif choice4=="2":
                    visu_boxplots(profit,"Profits")
                    plt.show()
                else:
                    print("Invalid input. Please enter 1,2")
            elif choice3=="3":
                visu_scatter(sales, profit, "Sales", "Profits")
                plt.show()
            elif choice3=="4":
                break
            else:
                print("Invalid input. Please enter 1,2,3,4")
        elif choice2=="2":
            print("1 - Pie Chart - To view the percentage of companies in each continent")
            print("2 - Bar Chart - To view the market value of the companies in each continent")
            print("3 - Multibox Plot - To view the box plots for each of continenet market value distribution")
            choice4= input("Enter your selection.")
            if choice4=="1":
                visu_piechart(companycount_dict)
                plt.show()
            elif choice4=="2":
                visu_barchart(market_value_dict)
                plt.show()
            elif choice4=="3":
                visu_multiboxplot(market_value_dict)
                plt.show()
            else:
                print("Invalid input. Please enter 1,2,3")
            plt.show()
        elif choice2=="3":
            break
        else:
            print("Invalid input. Please enter 1,2,3") 
    else:
        print("end")
        break
        
    
    
    
        