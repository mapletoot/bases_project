def from_base_ten_converter(number_to_convert, base):
    if type(base) != int or base <= 0:
        return "Base must be a positive integer"
    
    magnitude_index = 0
    magnitude_checker = number_to_convert
    while magnitude_checker > 10:
        magnitude_index += 1
        magnitude_checker /= 10
    
    print(magnitude_index)

  
    

print(from_base_ten_converter(23, 2))
