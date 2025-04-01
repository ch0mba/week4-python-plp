with open('input_file.txt', 'r') as file:
        content = file.read()
        print(content)
 

modified_content = content.replace(' Uses CSS Grid to structure the sidebar and content.', ' Use tailwind CSS to structure the sidebar and content.')
with open('output_file.txt', 'w') as file:
        file.write(modified_content)
        print(modified_content)

# Convert text to upper case
upper_case = modified_content.upper()

# Write the processed text to output_file.txt
with open('output_file.txt', 'a') as file:
        file.write(upper_case)
        print(upper_case)
# Count the number of words