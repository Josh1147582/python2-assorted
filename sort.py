import math

# sort.py sorts numbers given in sort.txt and displays information about them.
# I made this for a stats homework assignment with several of these
# calculations.

f = open('sort.txt', 'r')
s = f.read()
s = s.replace('\n', ' ')
arr = s.split(' ')
print('Sorted: '+str(sorted(arr)))
total = 0
for i in arr:
    total += float(i)
print('Mean: ' + str(total/len(arr)))
mean = total/len(arr)
arr1 = arr[0:int(math.ceil(len(arr)/2))]
total=0
for i in arr1:
    total += float(i)
print('Lower fourth: '+ str(total/len(arr1)))
lf= total/len(arr1)
arr2 = arr[int(math.ceil(len(arr)/2)):]
total=0
for i in arr2:
    total += float(i)
print('Upper fourth: '+ str(total/len(arr2)))
uf = total/len(arr2)
fs = uf-lf
lt = lf-(1.5*fs)
ut = (1.5*fs)+uf
print("Lower threshhold: "+str(lt))
print("Upper threshhold: "+str(ut))
print("Outliers:")
for i in arr:
    if (float(i)< lf-(1.5*fs)) or (float(i) > (1.5*fs)+uf):
        print(i)
print("Extreme Outliers")
for i in arr:
    if (float(i)< lf-(3*fs)) or (float(i) > (3*fs)+uf):
        print(i)

