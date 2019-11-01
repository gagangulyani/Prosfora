from models.user import User

def is_active(self):
    # Here you should write whatever the code is
    # that checks the database if your user is active
    return self.active

@staticmethod
def is_authenticated():
    return True

@staticmethod
def is_anonymous():
    return False

def get_id(self):
    return self.userID