import os
import json

class User:
    def __init__(self,f_name, l_name, email, password, mobile):
        self.user_no = User.get_max_user_no() + 1
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        self.password = password
        self.mobile = mobile
    
    @staticmethod
    def get_users():
        if os.stat("data/users.json").st_size != 0 :
            handler = open("data/users.json", "r")
            users = json.load(handler)
            handler.close()
            return users #returns a list of dictionaries contains users data
        return []
    
    def get_max_user_no():
        user_nums = [ user["user_no"] for user in User.get_users() ]
        return max(user_nums) if user_nums else 0

    def save(self):
        users = User.get_users()
        try:
            handler = open("data/users.json", "w")
        except:
            return False
        users.append(self.__dict__)
        handler.write(json.dumps(users))        
        handler.close()
        return True
    
    @classmethod
    def login(cls, email, password):
        users = cls.get_users()
        for user in users:
            if user["email"] == email and user["password"] == password:
                return user
        return False

    
    def user_projects(self):
        #instance from project
        #use get all projects
        #then select only
        pass
