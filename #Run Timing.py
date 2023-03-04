#Run Timing
from statistics import mean

print ("Enter 10 km run time:")

x = str(input())
total = str(x)
run = str(1)
while x!="":
    print ("Enter 10 km run time:")
    x= str(input())
    total = x+total
    run = run + str(1)

str(totalAverage = int(total) / int(run))

print("Average of " + totalAverage +", over" + run + " runs")

