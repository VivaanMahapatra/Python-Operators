import array as arr
array_num = arr.array('i',[1,3,5,7,9,3])
print("Original array :"+str(array_num))
print("Number of occurences of number 3 in said array is : "
+str(array_num.count(3)))
array_num.reverse()
print("The reverse order of the numbers in the array : ")
print(str(array_num))