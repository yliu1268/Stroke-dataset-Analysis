#    a. Load libraries #
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#    b. Load dataset #
input_file = '/Users/youwen/Downloads/healthcare-dataset-stroke-data/train_2v.csv'
dataset = pd.read_csv(input_file)
print(dataset)

# [43400 rows x 12 columns] #
