import json


def lambda_handler(event, context):
    print("input body: %s" % (event.get("body")))
    decimalNumber = int(event.get("body"))
    print("decimalNumber: %d" % (decimalNumber))


    decimalArray = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanSymbolArray = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''

    i = 0
    while  decimalNumber > 0:
        for _ in range(decimalNumber // decimalArray[i]):
            roman_num += romanSymbolArray[i]
            decimalNumber -= decimalArray[i]
        i += 1
    return roman_num
