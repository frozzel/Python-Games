class User: 
    def __init__(self, first_name, last_name, age):
        print("New user being created...", first_name, last_name, age)
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.followers = 0  
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
    
    def __repr__(self):
        return f"User {self.first_name} {self.last_name}, age: {self.age}"
    
    
    

user1 = User("Dave", "Bowman", 30)
user_2 = User("Jane", "Doe", 25)

user1.follow(user_2)
print(user_2.followers)
print(user_2.following)

