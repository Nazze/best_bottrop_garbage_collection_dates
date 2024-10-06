import json

# Read the file
with open('input.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# Convert the JSON data to a Python object
data = json.loads(f'[{data}]')

# Create a new dictionary in the desired format
result = {item['name'] : item['id'] for item in data}

# Save the result to a new file
with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

print("Conversion completed!")
