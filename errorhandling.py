filename = input("Enter the filename: ")
# Check if the file exists
try: 
    # Open the file in read mode
    file = open(filename, 'r')
        # Read the content of the file
    data = file.read()
    print(data)

except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
finally:
    print("Thank you for using the file reader program.")