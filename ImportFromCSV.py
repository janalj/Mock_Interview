import csv
def csvQuestion(fname):
    data = list(csv.reader(open(fname)))
    return data[1:]


