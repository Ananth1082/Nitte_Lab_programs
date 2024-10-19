def crc(data, gen_pol):
    check_val = data[:len(gen_pol)]  
    for i in range(len(gen_pol), len(data)):
        if check_val[0] == '1':
            check_val = bin(int(check_val, 2) ^ int(gen_pol, 2))[2:].zfill(len(gen_pol))
        check_val = check_val[1:] + data[i]
    # Perform the final XOR operation for the last segment
    if check_val[0] == '1':
        check_val = bin(int(check_val, 2) ^ int(gen_pol, 2))[2:].zfill(len(gen_pol))
    return check_val[1:]  # Remove the leading bit

# Transmitting data
data = input("Enter the data to be transmitted: ")
gen_pol = input("Enter the generating polynomial: ")
data += "0" * (len(gen_pol) - 1)
check_val = crc(data, gen_pol)
print("Check value (CRC):", check_val)
transmitted_data = data[:-(len(gen_pol) - 1)] + check_val
print("Data sent will be:", transmitted_data)

# Receiving data
received_data = input("Enter the received data: ")
gen_pol = input("Enter the generating polynomial: ")
print("\n-----------------------------")
print("Data received:", received_data)
check_val = crc(received_data, gen_pol)
if '1' in check_val:
    print("\nError detected\n")
else:
    print("\nNo error detected\n")