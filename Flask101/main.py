class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
        
    def login(self):
        self.is_logged_in = True
        print(f"{self.name} logged in.")
    def logout(self):
        self.is_logged_in = False
        print(f"{self.name} logged out.")

def is_authenticated_decorator(function):
    def wrapper(user):
        if user.is_logged_in:
            function(user)
        else:
            print("User is not authenticated.")
    return wrapper

@is_authenticated_decorator
def create_post(user):
    print(f"{user.name} created a post.")
    
new_user = User("John")
new_user.login()
create_post(new_user)
new_user.logout()
create_post(new_user)
