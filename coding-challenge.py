import json

class Employee:
    def __init__(self, id, first_name, salary, manager):
        self._id=id
        self._first_name = first_name
        self._salary = salary
        self._manager = manager
        self._list_of_direct_reports = []

    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._first_name

    @property
    def salary(self):
        return self._salary

    @property
    def manager(self):
        return self._manager

    @property
    def list_of_direct_reports(self):
        return self._list_of_direct_reports

    def add_direct_report(self, employee):
        self._list_of_direct_reports.append(employee)

# Print out the employee tree in ASCII format
# If the manager is null then they are the top of the hierarchy
# If the manager is 1, add them to the heirachy
# Repeat until all employees are added
# Then pretty print the result in ASCII format with indent = 2
# Build the tree from the top down
# Will have to iterate through the tree once for each layer of the tree
# Easiest to sort on a heap by manager id, then process? 
# Add node with (manager id, id) onto a heap, then remove from the heap and add to tree
# The input data starts with id 1 instead of 0 which is annoying
# Create a python dictionary (read: hash table) of employees to allow for looking up employees by id
def json_to_employee_converter(json_data_object):
    employee_dict = {}
    for user in json_data_object:
        employee = Employee(user['id'], user['first_name'], user['salary'], user['manager'])
        employee_dict[employee._id] = employee
    return employee_dict

# Print out total salary requirement
def print_total_salary(employee_dict):
    salary_total=0
    for employee in employee_dict.values():
        salary_total += int(employee.salary)
    print('Total salary: %d\n' % salary_total)

# Right now the employee tree is "bottom up", where the employee knows who the manager is, but the manager does not know who his employee is. 
# To more easily print the employee hierarchy, it makes sense to build a normal tree, where there is 1 root (the owner), and each node is aware of its connection to the nodes below it.
def build_employee_tree(employee_dict):
    tree_root = None
    for employee in employee_dict.values():
        # This code breaks if the manager is None/null
        if employee.manager is not None:
            manager = employee_dict[employee.manager]
            manager.add_direct_report(employee)
            #print('employee: %s, manager: %s' % (employee.first_name, manager.first_name))
        else:
            tree_root = employee
    return tree_root

# We've got the tree, which is contained within the object/class structure.
# We also need a pointer to the root of the tree. Now using the pointer to the root,
# we will iterate through the tree and print it
# NOTE: The ASCII output is indented slightly differently than in the prompt, but I think this way makes more sense.
# because the indentdation is applied consistently to the owner and all employees.
def print_employee_tree(tree_root, indentdation):
    #print('%s' % tree_root.first_name)
    if len(tree_root.list_of_direct_reports) > 0:
        print('%sEmployees of: %s' % ('   ' * indentdation, tree_root.first_name))
        for direct_report in tree_root.list_of_direct_reports:
                print('%s%s' % ('   ' * (indentdation + 1), direct_report.first_name))
        for direct_report in tree_root.list_of_direct_reports:
            print_employee_tree(direct_report, indentdation+1)
    



def main():  
    # Read the input file
    json_file = 'input-file.json'
    with open(json_file) as json_data:
        json_data_object = json.load(json_data)
    #print(json.dumps(data, indent=2))

    employee_dict = json_to_employee_converter(json_data_object)

    tree_root = build_employee_tree(employee_dict)

    print('%s' % tree_root.first_name)
    print_employee_tree(tree_root, 0)

    print_total_salary(employee_dict)

main()



