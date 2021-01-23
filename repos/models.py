# """ GitHubApi : Custom Model Class for User """

# class GitHubUser:

#     def __init__(self , id , login , score):
#         self.id = id
#         self.login = login
#         self.score = score

#     def __str__(self):
#         return f"Hii i am {self.username} and this is my account"

#     def __repr__(self):
#         return f'GitHubUser{self.username}'

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(1000))