try:
    print(5/'a')

except ZeroDivisionError:
    print("you cannot divide by 0")
except TypeError:
    print("you cannot divide by string")
    
