# Nolan Piselli

try:
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)

except ValueError:
    print("Please enter a number.")
    print("Thank you for using my program.")

except ZeroDivisionError:
    print('Do not input "0" as your prior period.')
    print("Thank you for using my program.")
except:
    print("Thank you for using my program.")