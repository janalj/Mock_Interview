"""
run csv file 

"""

import csv

header = ['No.', 'Questions']

data = [[1,"tell me about yourself"],[2,"what is your biggest challenge"]

]

with open('Interview_Questions.csv','w',encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)