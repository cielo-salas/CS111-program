def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"

    binary_result = ""
    integer_part = abs(int(decimal_num))
    fractional_part = abs(decimal_num) - integer_part

    # Convert integer part to binary
    while integer_part > 0:
        binary_result = str(integer_part % 2) + binary_result
        integer_part //= 2

    if fractional_part > 0:
        binary_result += "."

    # Convert fractional part to binary (up to any digits you want sir)
        for _ in range(32):
            fractional_part *= 2
            binary_result += str(int(fractional_part))
            fractional_part -= int(fractional_part)

        return binary_result


decimal_number = 12.14
binary_representation = decimal_to_binary(decimal_number)
print(binary_representation)
