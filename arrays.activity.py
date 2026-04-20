import array as arr
a = arr.array('i',[1,2,3])
print("\nThe new array created is : ", end="")
for i in range (0,3):
    print(a[i], end = "")
print()

b = arr.array('d', [2.5,3.2,3.3])
print("\nThe new created array is : ",end="")
for i in range (0,3):
    print(b[i],end="")
a.insert(1,4)
print("\n array after intersection : ", end="")
for i in range (a):
    print (i,end="")
print()
b.append(4.4)
for i in range (b):
    print (i,end="")
print()
print("access elemnt is : ",a[2])
print("access elemnt is : ",b[0])