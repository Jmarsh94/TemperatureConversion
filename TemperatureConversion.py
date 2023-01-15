def to_celsius(fahrenheit):                 # Justin Marsh Week 2 lab2 Temperature Conversion
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# the main function is used to test the other functions


if __name__ == "__main__":
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(to_celsius(temp), 2), "Celsius")

    for temp in range(0, 101, 20):
        print(temp, "Celsius =", round(to_fahrenheit(temp), 2),
              "Fahrenheit")
