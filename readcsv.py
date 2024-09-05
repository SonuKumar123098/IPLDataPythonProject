'''import csv

f = open("/home/sonu/Downloads/IplProjectData/matches.csv", 'r')
f1 = open("/home/sonu/Downloads/IplProjectData/deliveries.csv", 'r')

ro = csv.reader(f, delimiter=',')
ro1 = csv.reader(f1, delimiter=',')
ld = list(ro)
ld1 = list(ro1)
print(ld)
print(ld1)'''
import csv
with open("/home/sonu/Downloads/IplProjectData/matches.csv", 'r') as f, \
     open("/home/sonu/Downloads/IplProjectData/deliveries.csv", 'r') as f1:
    ro = csv.reader(f, delimiter=',')
    ro1 = csv.reader(f1, delimiter=',')
    ld = list(ro)
    ld1 = list(ro1)
    # print(ld)
    # print(ld1)
