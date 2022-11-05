def creditEncrypter(number):
    length = len(number)
    # print(length)
    # print(number[length-1])
    print("*" * (length-4) + number[length-4:length])


creditEncrypter("9871955895")
