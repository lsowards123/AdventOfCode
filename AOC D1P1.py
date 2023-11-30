#Import the text file, store values to an array and read it out
import matplotlib.pyplot as plt
with open('AOCD1Input.txt', 'r') as f:
    list = [int(line) for line in f]   # save numbers to a list
#print (l)

#Iterate through the list
#print (range(len(list)))
counter = 0
for i in (range(len(list))):
    if list[i+1] > list[i]:
        counter = counter+1
print (counter)
#plt.plot(list, linewidth = 0.5)
#plt.show()