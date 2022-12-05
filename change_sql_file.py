import json
from os import walk

"""
reads the config file and inserts the Dataset ID and Project ID into the .sql files
"""

f = open('config.json')
data = json.load(f)
project_id = data['Bigquery']['Project_ID']['ID']
dataset_id = data['Bigquery']['Dataset_ID']['ID']
print(project_id)
print(dataset_id)
with open('data-model.sql', 'r') as file:
    data = file.read().rstrip()
    final=data.replace('formel_Uzi',dataset_id)
    final=final.replace('my-project-1535534415901',project_id)
    f = open("data-model.sql", "w")
    f.write(final)
    f.close()
    #print(final)
f = []
for (dirpath, dirnames, filenames) in walk('Data_Transformations/Queries'):
    f.extend(filenames)
    break
for name in f:
    with open('Data_Transformations/Queries/'+name, 'r') as file:
        print(name)
        data = file.read().rstrip()
        final=data.replace('formel_uzi',dataset_id)
        final=final.replace('my-project-blabla',project_id)
        f = open('Data_Transformations/Queries/'+name, "w")
        f.write(final)
        f.close()
        #print(final)
with open('Data_Extraction/upload_to_bigquery.py', 'r') as file:
        data = file.read().rstrip()
        final=data.replace('formel_Uzi',dataset_id)
        final=final.replace('my-project-1535534415901',project_id)
        f = open('Data_Extraction/upload_to_bigquery.py/'+name, "w")
        f.write(final)
        f.close()
        #print(final)