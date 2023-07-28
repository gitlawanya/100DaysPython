class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("new user is being created")


    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Lawanya")
# user_1.id = "001"
# user_1.username = "Lawanya"
user_2 = User("002", "Raj")
# user_2.id = "002"
# user_2.username = "Raj"
# print(user_1.followers)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
