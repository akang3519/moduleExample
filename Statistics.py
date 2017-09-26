import statistics

numArray = [1,2,3,4,4,5]
print("Example data:", numArray)

print("The mean value of the data is", statistics.mean(numArray))
print("The medium of the data is", statistics.median(numArray))
print("The mode of the data", statistics.mode(numArray))
print("The standard deviation is", statistics.stdev(numArray))