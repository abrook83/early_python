class User:
    def __init__(self, user_id, username):  # a function in a class is a 'method'.
        """Is a 'Constructor' method. 'init' is the method that initiatlises the instance of this class. 
        The parameters (in brackets) being passed into the instance are itself 'self', as well as any other 
        parameter we need to make the instance."""
        self.user_id = user_id
        """Set the instance's attributes by passing the input parameter to the new instance 'self'."""
        """Basically passing the input parameter 'username' into this instance of the class ('self.username')."""
        self.username = username
        self.followers = 0
        """Set an initial default value, which then means we don't need to initialise it in the 'init'."""
        self.following = 0

    def follow(self, user):   # functions must ALWAYS have a self parameter as the first parameter.
        user.followers +=1
        self.following += 1


user_1 = User("001", "abrook")      # we must pass the required parameters into the class as we create each instance.
user_2 = User("002", "davo")

# print(user_1.user_id)
# print(user_1.username)
# print(user_1.followers)

user_1.follow(user_2)       # runs the follow function on 'user_1' with the parameter 'user_2'.
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)