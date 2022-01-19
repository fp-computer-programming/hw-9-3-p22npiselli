# Nolan Piselli

def temp_convert():
    temp = int(input('Input a temperature. '))
    scale = input('Input your scale ("C" or "F"). ')

    if scale.lower() == "c":
        final_temp = (temp * (9/5)) + 32
        print(final_temp)
    elif scale.lower() == "f":
        final_temp = (temp - 32) * (5/9)
        print(final_temp)
    else:
        print('Please input either "C" or "F" and try again.')

temp_convert()
