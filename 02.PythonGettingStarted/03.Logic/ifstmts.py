number: int = 5

if number == 5 :
    print("number is 5")
else:
    print("number already not 5")


if number:
    print("number is defined and is truthy")

empty_string = ""

if not empty_string:
    print("empty string is falsy")
else:
    print("empty string is truthy")