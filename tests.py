#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 13:41:05 2023

@author: udaniweerasinghe
"""
import pytest
from functions import *
from pytest import approx


def test_numberofvalues():
    assert numberofvalues([100,200,300,400,500])==5
    
def test_calc_total():
    assert calc_total([100,200,300,400,500])==1500
    
    
def test_calc_mean():
    assert calc_mean([100,200,300,400,500])==300
    
    
def test_calc_median():
    assert calc_median([500,200,400,300,100])==300
    
def test_calc_mode():
    assert calc_mode([100,200,300,100,500])==100
    
def test_calc_max():
    assert calc_max([100,200,300,400,500])==500
    
def test_calc_min():
    assert calc_min([100,200,300,400,500])==100
    
def test_calc_range():
    assert calc_range([100,200,300,400,500])==400
    
def test_calc_interquartile_range():
    assert calc_interquartile_range([100,200,300,400,500])==300
    
def test_calc_mode_skewness():
    assert approx(calc_mode_skewness([100,200,300,400,500]),0.001)==1.264
    
def test_calc_median_skewness():
    assert approx(calc_median_skewness([100,200,300,400,500]),0.001)==0
    
def test_calc_standard_deviation():
    assert approx(calc_standard_deviation([10,20,30,40,50]),0.001)==15.811
    
def test_calc_correlation():
    x=[1,2,3,4,5]
    y=[1,2,3,4,5]
    assert approx(calc_correlation(x,y),0.001)==0.999
    
def test_num_of_continenets():
    assert num_of_continenets({
    "name": "Shashi",
    "age": 25,
    "is_student": True,
    "grades": [85, 92, 78, 90],
    "address": {
        "street": "123 Main St",
        "city": "Athlone"}})==5

def test_max_count():
    assert(max_count({"value1": 10,"value2": 25,"value3": 42,"value4": 17,"value5": 56}))==("value5",56)

    
def test_min_count():
    assert(min_count({"value1": 10,"value2": 25,"value3": 42,"value4": 17,"value5": 56}))==("value1",10)

def test_max_value():
    assert(max_value({"value1": [10,20,30],"value2": [25],"value3": [42,34,45,56,78],"value4": [17,34,12,23,35,21],"value5": [56]}))==("value3",255)
    

def test_min_value():
    assert(min_value({"value1": [10,20,30],"value2": [25],"value3": [42,34,45,56,78],"value4": [17,34,12,23,35,21],"value5": [56]}))==("value2",25)
    

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
    