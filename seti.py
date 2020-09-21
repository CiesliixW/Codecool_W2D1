def decimal_to_binary(decimal_number):
    """Returns the array of digits in binary representation of a decimal number"""
    second_number = decimal_number // 2 
    list1 = []
    
    while second_number > 0: 
        first_number = decimal_number % 2
        second_number = decimal_number // 2
        decimal_number = second_number
        list1.append(first_number)

    print(list1)
    


        


binary_digits = [1,0,1,1,1]
def binary_to_decimal(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    potega = len(binary_digits)
    while potega > 0:
        potega = len(binary_digits) -1
        for i in binary_digits:  
            decimal = i * 2 ** potega

    print(decimal)

binary_to_decimal(binary_digits)



def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    pass


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    pass


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass
