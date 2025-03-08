

try:
    a = int(input("Enter a Number divided for:\n"))
    b = int(input("Enter a Number divided by:\n"))
    print(a/b)
except ValueError as e:
    print("Given Input is wrong,",e)
except ZeroDivisionError as e:
    print(" Divided by 0 is not possible",e)
except Exception as e:
    print("Some went wrong:", e)
finally:
    print("Thank You!!!")