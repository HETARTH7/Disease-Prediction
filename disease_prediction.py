import numpy as np
import pandas as pd
# import seaborn as sns

training=pd.read_csv('Data/Training.csv').values
testing=pd.read_csv('Data/Testing.csv').values

print(training)
print(testing)