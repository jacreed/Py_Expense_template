from PyInquirer import prompt, Separator


def get_users(answers):
    users = []
    import csv
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            users.append(row[0])
    return users


def get_users_checkbox(answers):
    print(answers)
    users_involved = []
    import csv
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == answers['spender']:
                users_involved.append({'name': row[0], 'checked': True})
            else:
                users_involved.append({'name': row[0]})
    return users_involved


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_users
    },
    {
        "type":"checkbox",
        "name":"people_involved",
        "message":"New Expense - People involved: ",
        "choices": get_users_checkbox
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    print(infos)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    import csv
    with open('expense_report.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([infos['amount'], infos['label'], infos['spender'], infos['people_involved']])
    print("Expense Added !")
    return True

def get_status_report(*args):
    users = {}
    import csv
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            users[row[0]] = 0
    with open('expense_report.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            users[row[2]] -= int(row[0])
            nb_involved = len(row[3])
            expense_per_person = int(row[0])/nb_involved
            involved_person = row[3]
            for user in involved_person:
                users[user] += expense_per_person
    print(users)



