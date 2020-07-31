my_list = [12, 45, 'pepe', 'miguel', 6]

numbers = []

for num in "10":
    print(num)

for num in range(5):
    print(num)

user_1 = {
    "username": "pepe valor",
    "id": 22,
}
user_2 = {
    "username": "fulano sinvalor",
    "id": 33,
    "email": "email@email.com",
}

mis_users = [user_1, user_2]

for user in mis_users:
    print(user['username'])

for user in mis_users:
    if 'email' in user:
        print(user['email'])

selected_user = {}
my_user_lookup = 33

for user in mis_users:
    if 'id' in user:
        if user['id'] == my_user_lookup:
            selected_user = user
print(selected_user)