from PyInquirer import prompt
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New name: ",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    name = prompt(user_questions)
    print(name)
    import csv
    with open('users.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([name['name']])
    return