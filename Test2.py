import os
import pandas as pd
path = r"D:\shekar\Engineering Test Risk Analytics\Engineering Test Files"
print('Your folder path is"',path,'"')
before = dict ([(f, None) for f in os.listdir (path)])
print(before)
while True:
        after = dict ([(f, None) for f in os.listdir (path)])
        added = [f for f in after if not f in before]
        if added:
                print("Added: ", ", ".join (added))
                new_data = pd.read_csv(path+r"\\"+added[0])
                before[added[0]] = None
                unique_secure = new_data['Source IP'].unique()
                print(unique_secure)
               
               
        else:
             before = after