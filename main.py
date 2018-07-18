import os

project = os.getenv('PROJECT_NAME')
domain = os.getenv('DOMAIN')
username = os.getenv('ADMIN_USERNAME')
password = os.getenv('ADMIN_PASSWORD')

def auth(domain, username, password):
    pass

def listUsers(domain, session):
    pass

def viewUser(domain, session, user):
    pass

def editUser(domain, session, user):
    pass

