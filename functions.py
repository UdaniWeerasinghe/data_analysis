#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:25:35 2023

@author: udaniweerasinghe

"""
from math import sqrt
import matplotlib.pyplot as plt

def numberofvalues(numbers):
    """
    Calculation of Tnumber of values in a list
    Parameters
    ----------
    -numbers: list
    A list of numeric values
    Returns
    --------
    - number of values:int
    """
    return len(numbers)

def calc_total(numbers):
    """
    Calculation of Total for Numerical Columns
    Parameters
    ----------
    -numbers: list
    A list of numeric values
    Returns
    --------
    - sum :float
    """
    return sum(numbers)

def calc_mean(numbers):
    """
    Calculation of Mean for Numerical Columns
    Parameters
    ----------
    -numbers: list
    A list of numeric values
    
    Returns
    --------
    - mean :float
    """
    return sum(numbers)/len(numbers)


def calc_median(numbers):
    """
    Calculation of Median for Numerical Columns
    Parameters
    ----------
    -numbers: list
    A list of numeric values
    
    Returns
    --------
    - median :float
    """
    sorted_numbers=sorted(numbers)
    mid_index= int(len(numbers)/2)

    if len(sorted_numbers)%2==0:
        median =(sorted_numbers[mid_index-1]+sorted_numbers[mid_index])/2
    else:
        median =sorted_numbers[mid_index]
    return(median)    

def calc_mode(numbers):
    """
    Calculation of Mode for Numerical Columns
    Parameters
    ----------
    -numbers: list
    A list of numeric values
    
    Returns
    --------
    - mode :float
    """
    sorted_numbers = sorted(list(set(numbers)))
    frequencies = [numbers.count(value) for value in sorted_numbers]
    highest_num = frequencies.index(max(frequencies))
    mode = sorted_numbers[highest_num]
    return mode



def calc_max(numbers):
    """
    Calculation of Maximum for Numerical Columns
    Parameters
    ----------
    -numbers: list
    A list of numeric values
    Returns
    --------
    - maximum value :float
    """
    return max(numbers)

def calc_min(numbers):
    """
    Calculation of Minimum for Numerical Columns
    Parameters
    ----------
    -numbers: list
    A list of numeric values
    Returns
    --------
    - minimum :float
    """
    return min(numbers)

def calc_range(numbers):
    """
    Calculation of Range for Numerical Columns
    Parameters
    ----------
    -numbers: list
    A list of numeric values
    Returns
    --------
    - range :float
    """
    return calc_max(numbers)-calc_min(numbers)

def calc_interquartile_range(numbers):
    """
    Calculation of Interquartile range for Numerical Columns
    Parameters
    ----------
    -numbers: list
    A list of numeric values
    Returns
    --------
    - interquartile range :float
    """
    sorted_data = sorted(numbers)
    
    # Calculate the index for Q1 and Q3
    n = len(sorted_data)
    q1_index = int(0.25 * (n + 1))
    q3_index = int(0.75 * (n + 1))
    
    # Calculate Q1 and Q3
    q1 = sorted_data[q1_index - 1] if q1_index % 1 != 0 else (sorted_data[q1_index - 1] + sorted_data[q1_index]) / 2
    q3 = sorted_data[q3_index - 1] if q3_index % 1 != 0 else (sorted_data[q3_index - 1] + sorted_data[q3_index]) / 2
    
    # Calculate the interquartile range (IQR)
    iqr = q3 - q1
    return iqr

def calc_standard_deviation(numbers):
    
    """
    Calculation of Standard Diviation for Numerical Columns
    Parameters
    ----------
    -numbers: list
    A list of numeric values
    Returns
    --------
    - standard diviation :float
    """
    mean = calc_mean(numbers)
    squared_deviations = [(i - mean) ** 2 for i in numbers]
    sum_squared_deviation = sum(squared_deviations)
    standard_deviation = sqrt(sum_squared_deviation / (len(numbers) - 1))
    return standard_deviation

# calc_standard_deviation
def calc_mode_skewness(numbers):
    """
    Calculation of Mode Skewness for Numerical Column
    Parameters
    ----------
    -numbers: list
    A list of numeric values
    Returns
    --------
    - mode skewness :float
    """
    mode_skew = (calc_mean(numbers)-calc_mode(numbers))/calc_standard_deviation(numbers)
    return mode_skew

def calc_median_skewness(numbers):
    """
    Calculation of Median Skewnessfor Numerical Column
    Parameters
    ----------
    -numbers: list
    A list of numeric values
    Returns
    --------
    - median skewness :float
    """
    median_skew = (3*(calc_mean(numbers)-calc_median(numbers)))/calc_standard_deviation(numbers)
    return median_skew
    


def calc_correlation(x,y):
    """
    Calculation of Correlation for 2 Numerical Columns
    Parameters
    ----------
    -x: list
    -y: lisr
    2 lists of numeric values
    Returns
    --------
    - correlation :float
    """
    x_mean = sum(x)/len(x)
    y_mean = sum(y)/len(y)
    x_squared_dev = [(i - x_mean) ** 2 for i in x]
    y_squared_dev = [(j - y_mean) ** 2 for j in y]
    sum_x_squared_dev = sum(x_squared_dev)
    sum_y_squared_dev = sum(y_squared_dev)
    denominator= sqrt(sum_x_squared_dev)*sqrt(sum_y_squared_dev)
    numerator_without_sum = [(x[i] - x_mean)* (y[i] - y_mean)for i in range(len(x))]
    numerator = sum(numerator_without_sum)
    correlation = numerator/denominator
    return correlation
    
def num_of_continenets(dict1):
    """
    Calculation of categories in a dictionary
    Parameters
    ----------
    -dict1: 
    A dictionary of numeric values
    Returns
    --------
    - num of continenets :int
    """
    return len(dict1)

def max_count(dict1):
    """
    Calculation of maximum value in a dictionary
    Parameters
    ----------
    -dict1: 
    A dictionary of numeric values
    Returns
    --------
    -max_category: String
    - maximum value:float
    """
    max_category = max(dict1, key=dict1.get)
    max_value = dict1[max_category]
    return max_category,max_value
    
def min_count(dict1):
    """
    Calculation of minimum value in a dictionary
    Parameters
    ----------
    -dict1: 
    A dictionary of numeric values
    Returns
    --------
    -min_category: String
    - minimum value:float
    """
    min_category = min(dict1, key=dict1.get)
    min_value = dict1[min_category]
    return min_category,min_value

def max_value(dict1):
    """
    Calculation of total of maximum value in a dictionary
    Parameters
    ----------
    -dict1: 
    A dictionary of numeric values
    Returns
    --------
    -max_category: String
    - maximum value:float
    """
    max_sum=0
    max_category =None
    
    for category, values in dict1.items():
        current_sum = sum(values)
        if current_sum > max_sum:
            max_sum = current_sum
            max_category = category
    return max_category,max_sum
    
def min_value(dict1):
    """
    Calculation of total of minimum value in a dictionary
    Parameters
    ----------
    -dict1: 
    A dictionary of numeric values
    Returns
    --------
    -min_category: String
    - minimum value:float
    """
    min_sum = float('inf')  
    min_category =None
    
    for category, values in dict1.items():
        current_sum = sum(values)
        if current_sum < min_sum:
            min_sum = current_sum
            min_category = category
    return min_category,min_sum
    
def visu_multiboxplot(dict1):
    """
    Visualization of Boxplots for a values in a dictionary
    Parameters
    ----------
    -dict1: list
    A dictionary of numeric lists for each category
    Returns
    --------
    -  fig: matplotlib.figure.F
        - The figure object containing the boxplots
    - ax: AxesSubplot
        TheAxesSubplot object represting the Box plot axes
    """
    fig, ax = plt.subplots(1,1,figsize=(10,10)) 
    ax.set_title("Box Plot on market value of Companies in each Continenets")
    ax.set_ylabel("Continent")
    ax.set_xlabel("Market Value US $ billion")
    
    ax.boxplot(dict1.values(),showmeans=True, meanline=True, showfliers=False, vert=False, labels=dict1.keys())
    
    return fig,ax
    
    
    
def visu_piechart(dict1):
    """
    Visualization of Pie chart for a values in a dictionary
    Parameters
    ----------
    -dict1: dictionary 
    with numeric value for each category
    
    Returns
    --------
    -  fig: matplotlib.figure.F
        - The figure object containing the pie chart
    - ax: AxesSubplot
        TheAxesSubplot object represting the pie chart axes
    """
    
    
    fig, ax = plt.subplots(1,1,figsize=(10,10)) 
    
    
    ax.set_title("Pie Chart on number of companies in each continenet")
    ax.pie(dict1.values(), labels=dict1.keys(), autopct="%.0f%%")
    return fig,ax

def visu_barchart(dict1):
    """
    PVisualization of Pie chart for a values in a dictionary
    Parameters
    ----------
    -dict1: dictionary 
    A dictionary of numeric lists for each category
    
    Returns
    --------
    -  fig: matplotlib.figure.F
        - The figure object containing the bar chart
    - ax: AxesSubplot
        TheAxesSubplot object represting the bar chart axes
    """
    sums_dict = {category: sum(values) for category, values in dict1.items()}
    fig, ax = plt.subplots(1,1,figsize=(10,10)) 
    ax.set_xlabel("Continenets")
    ax.set_ylabel("Market Value of Companies in US $ Billion)")
    ax.set_title("Bar Chart on Market Value of top companies based on its Continent")
    
    ypos=(0,1,2,3,4,5)
    ax.set_xticks(ypos) # set the y ticks
    ax.set_xticklabels(sums_dict.keys()) #
    ax.bar(sums_dict.keys(),sums_dict.values())
    return fig,ax

def visu_histsales(list1):
    """
    Visualization of Histogram for a sales in a list
    Parameters
    ----------
    -list1: list 
    A list of numeric values
    
    Returns
    --------
    -  fig: matplotlib.figure.F
        - The figure object containing the histogram
    - ax: AxesSubplot
        TheAxesSubplot object represting the histogram axes
    """
    fig, ax = plt.subplots(1,1,figsize=(10,10)) 
    
    ax.set_title("Histogram of Sales of the Companies")
    ax.set_xlabel("Sales of the companies ($billion)")
    # set the label for the y-axis
    ax.set_ylabel("Number of Companies")
    # display horizontal gridlines
    ax.grid(axis="y")
    # set the bins (intervals)
    bins = range(0, int(max(list1))+50, 50)
    # set the x_ticks
    ax.set_xticks(bins)

    ax.hist(list1, bins, ec="black")
    return fig,ax
    
def visu_histprofits(list1):
    """
    Visualization of Histogram for a profits in a list
    Parameters
    ----------
    -list1: list 
    A list of numeric values
    
    Returns
    --------
    -  fig: matplotlib.figure.F
        - The figure object containing the histogram
    - ax: AxesSubplot
        TheAxesSubplot object represting the histogram axes

    """
    fig, ax = plt.subplots(1,1,figsize=(10,10)) 
    ax.set_title("Histogram of Profits")
    
    # set the label for the x-axis
    ax.set_xlabel("Profits of the companies ($billion)")
    # set the label for the y-axis
    ax.set_ylabel("Number of Companies")
    
    # display horizontal gridlines
    ax.grid(axis="y")
    
    # set the bins (intervals)
    bins = range(0, int(max(list1))+10, 10)
    
    
    # set the x_ticks
    ax.set_xticks(bins)
    # display the histogram using the list1
    ax.hist(list1, bins, ec="black")
    return fig,ax

def visu_boxplots(list1,label1):
    """
    Visualization of Box Plot for a list
    Parameters
    ----------
    -list1: list 
    A list of numeric values
    -label1 - String
    String mentionaing the what the list content
    
    Returns
    --------
    -  fig: matplotlib.figure.F
        - The figure object containing the BoxPlot
    - ax: AxesSubplot
        TheAxesSubplot object represting the BoxPlot axes
    """
    fig, ax = plt.subplots(1,1,figsize=(10,10)) 
    ax.set_title(f"Box Plot of {label1}")
    ax.set_ylabel(f"{label1} of the companies per year ($billion)")
    ax.boxplot(list1, showfliers=False)
    return fig,ax

def visu_scatter(list1,list2,label1,label2):
    """
    Visualization of Scatter for 2 list
    Parameters
    ----------
    -list1: list 
    A list of numeric values
    -list2: list 
    A list of numeric values
    -label1 - String
    String mentionaing the what the list1 content
    -label2 - String
    String mentionaing the what the list2 content
    
    Returns
    --------
    -  fig: matplotlib.figure.F
        - The figure object containing the Scatter
    - ax: AxesSubplot
        TheAxesSubplot object represting the Scatter axes
    """
    fig, ax = plt.subplots(1,1,figsize=(10,10)) 

    ax.set_title(f"Scatter Plot of {label1} and {label2} of the top companies")
    ax.set_xlabel(f"{label1} ($ billion) of the companies")
    ax.set_ylabel(f"{label2} ($ billion) of the companies")
    ax.grid(axis="both")

    # display the scatter plot using and ages_list
    ax.scatter(x=list1, y=list2, marker=".", s=2)  
    return fig,ax
