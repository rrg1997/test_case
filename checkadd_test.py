# This is sample file
import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql import SQLContext

spark = SparkSession.builder.appName("test-case").getOrCreate()

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

def test_multiplication():
    assert 2 * 3 == 6

def test_division():
    assert 6 / 3 == 2
