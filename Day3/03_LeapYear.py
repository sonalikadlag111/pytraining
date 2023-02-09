# 3. Check Leap Year

# Default function to implement conditions to check leap year
def CheckLeap(Year):

  # if((Year % 400 == 0) or
  #    (Year % 100 != 0) and
    if(Year % 4 == 0):
     print("Given Year is a leap Year")

    else:
     print(" Year is not a leap Year")

Year = int(input("Enter the year: "))

CheckLeap(Year)
