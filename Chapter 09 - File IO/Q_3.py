# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 year old.

import os

# Get the directory path of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Create a folder for the multiplication tables
folder_name = "Multiplication Tables"
folder_path = os.path.join(current_directory, folder_name)
os.makedirs(folder_path, exist_ok=True)

# Generate multiplication tables from 2 to 20
for i in range(2, 21):
    table_content = ""
    for j in range(1, 11):
        result = i * j
        table_content += f"{i} x {j} = {result}\n"

    # Write the multiplication table to a file
    file_name = f"table_{i}.txt"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as file:
        file.write(table_content)

print("Multiplication tables generated and saved successfully!")









