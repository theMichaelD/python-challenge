import json
from anytree import Node, RenderTree

# Read the input file
json_file = 'input-file.json'
with open(json_file) as json_data:
    data = json.load(json_data)

print(json.dumps(data, indent=2))

# Print out the employee tree in ASCII format
# If the manager is null then they are the top of the hierarchy
# If the manager is 1, add them to the heirachy
# Repeat until all employees are added
# Then pretty print the result in ASCII format with indent = 2
for user in data:
    if user['manager'] is None:
        print('%s\n' % user['first_name'])
        print('Employees of: %s' % user['first_name'])

for user in data:
    if user['manager'] is not None:
        

# Print out total salary requirement
salary_total=0
for user in data:
    salary_total += int(user['salary'])
print('Total salary: %d\n' % salary_total)