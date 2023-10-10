import numpy as np
import pandas as pd
import json
import os
import time
start_time = time.time()


cricketer_filenames = []
for file in os.listdir('C:\Sophie Folder\Birkbeck\Project\Data\Cricketers_Wiki'):
    cricketer_filenames.append(os.path.join('C:\Sophie Folder\Birkbeck\Project\Data\Cricketers_Wiki',file))

cricketer_filenames[0:10]
len(cricketer_filenames)

dud_files = []

frames = []
counter = 0
for file in cricketer_filenames:
    try: 
        with open(file) as f:
            d=json.load(f)
            d=pd.json_normalize(d, max_level=1)
        frames.append(d)
        #df = pd.concat([df,d])
        counter+=1
    
    except:
        dud_files.append(file)
        counter+=1
    print(counter)
df = pd.concat(frames)

print(df.iloc[0])
print(len(dud_files))
full_csv = df.to_csv('full.csv')

wiki_df = df[['name','role']]
wiki_df.rename(columns={'fullname': 'Name', 'role': 'Playing role'}, inplace=True)
print(wiki_df.shape)
wiki_df = wiki_df.dropna()
print(wiki_df.shape)
print(wiki_df.head())
wiki_df.to_csv('wiki_cricketers.csv')

dud_df = pd.DataFrame(dud_files)
dud_csv = dud_df.to_csv('dud.csv')

end_time = time.time()

time_taken = end_time-start_time
print('Execution time:', time_taken, 'seconds')