# Create a list from the specified start to end index of another list.


list = [10, 20, 30, 40, 50, 60,70,80,90]

start = int(input("enter Start value index :"))
end = int(input("enter the End value index :"))

if ( start < 0):
    print ("Invalid start index")

if( end > len(list)-1):
    print("Invalid end index")

list1 = list[start:end+1]
print ("list : ", list)
print ("list1: ", list1)