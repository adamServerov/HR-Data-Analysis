#  write your code here
import pandas as pd
import os
import math
file_path = os.path.join('data','dataset', 'input.txt')
df_rock = pd.read_csv(file_path)
df_rock.set_index('labels', inplace = True)
R = df_rock.loc['R'].null_deg.median()
M = df_rock.loc['M'].null_deg.median()

print(f"M = {round(M,3)} R = {round(R, 3)}")
