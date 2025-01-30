class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001yg", "Murimi Shem")
user_2 = User("002oz", "Shem Murimi")

user_1.follow(user_2)

print(user_1.username, end='')
print(" following : ",user_1.following)
print(user_1.username, end='')
print(" followers : ",user_1.followers)

print(user_2.username, end='')
print(" followers: ", user_2.followers)
print(user_2.username, end='')
print(" following : ",user_2.following)

str = "heaven"
print(str[0])
