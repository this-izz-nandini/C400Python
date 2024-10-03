import csv
import requests

CSV_URL = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'

with requests.get(CSV_URL, stream=True) as file:
    lines = (line.decode('utf-8') for line in file.iter_lines())
    data = [row for row in csv.reader(lines)]

# print(data)
total = len(data) - 1
print(f'total no. of records: {total}')

borough=[]
brooks=0

for row in data[1:]:
    if row[1] not in borough:
        borough.append(row[1])
    if row[1]=='Brooklyn':
        brooks +=1

borough.sort()
print(f'\n\nunique boroughs:\n {borough}')

print(f'\n\nBrooklyn boroughs: {brooks}')

# with open('/root/taxi_zone_output.txt', mode='w') as op:
#     op.write(f'total no. of records: {total}')
#     op.write(f'\n\nunique boroughs:\n {borough}')
#     op.write(f'\n\nBrooklyn boroughs: {brooks}')