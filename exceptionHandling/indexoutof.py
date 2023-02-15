a = ["Python", "Exceptions", "try and except"]
try:

     for i in range( 0,2):
        print( "The index and element from the array is", i, a[i] )

except:
    print ("Index out of range")
else:
    print("operation Done Successfully")