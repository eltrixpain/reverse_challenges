def reverse_file_bytes(input_file: str, output_file: str):
    with open(input_file, "rb") as f:
        data = f.read()
    
    reversed_data = data[::-1]  # Reverse the bytes
    
    with open(output_file, "wb") as f:
        f.write(reversed_data)

input_file = "Reverseme.png"  # Change this to your input file
output_file = "chall"  # Change this to your desired output file
reverse_file_bytes(input_file, output_file)

