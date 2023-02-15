
marks = int(input("enter mark"))

try:

      a = marks / 100
      print(a)
except ZeroDivisionError:
    print("divide by 0 exception")
else:
  print("operation done perfectly")
