def fizzbuzz(numbers): 
    strings = []
    for number in numbers:
        if number % 15 == 0:
            strings.append("fizzbuzz")
        elif number % 3 == 0:
            strings.append("fizz")
        elif number % 5 == 0:
            strings.append("buzz")
        else:
            strings.append(str(number))
    return strings