import os
import json
from datetime import datetime 
class Project:
    # user["user_no"] ,title, details, total_target, start_date, end_date
    def __init__(self, user_no, title, details, total_target, start_date, end_date, project_no = ""):
        self.user_no = user_no
        self.project_no = project_no or (Project.get_max_project_no() + 1)
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def get_all_projects():
        if os.stat("data/projects.json").st_size != 0:
            handler = open("data/projects.json", "r")
            projects = json.load(handler)
            handler.close()
            return projects
        else:
            return []
    
    @classmethod
    def get_max_project_no(cls):
        projects_nums = [ project["project_no"] for project in cls.get_all_projects() ]
        return max(projects_nums) if projects_nums else 0

    @classmethod
    def get_user_projects(cls,user_no):
        projects = cls.get_all_projects()
        return [project for project in projects if project["user_no"] == int(user_no)]
        
    def save(self):
        projects = self.get_all_projects()
        try:
            handler = open("data/projects.json", "w")
        except:
            return False
        projects.append(self.__dict__)
        handler.write(json.dumps(projects))        
        handler.close()
        return True

    def update(self):
        projects = self.get_all_projects()
        for project in projects:
            if project["project_no"] == self.project_no and project["user_no"] == self.user_no:
                project["title"] = self.title if  self.title else project["title"]
                project["details"] = self.details if  self.details else project["details"]
                project["total_target"] = self.total_target if self.total_target else project["total_target"]
                project["start_date"] = self.start_date if self.start_date else project["start_date"]
                project["end_date"] = self.end_date if self.end_date else project["end_date"]
                try:
                    handler = open("data/projects.json", "w")
                except:
                    return False
                handler.write(json.dumps(projects))
                handler.close()
                return True
        return False

    @classmethod
    def delete(cls, project_no, user_no):
        projects = cls.get_all_projects()
        for i, project in enumerate(projects):
            if project["project_no"] == project_no and project["user_no"] == user_no:
                projects.pop(i)
                try:
                    handler = open("data/projects.json", "w")
                except:
                    return False
                handler.write(json.dumps(projects))
                handler.close()
                return True
        return False
        



    @classmethod    
    def get_project(cls, user_no, project_no):
        projects = cls.get_all_projects()
        for project in projects:
            if project["project_no"] == project_no and project["user_no"] == user_no:
                return project
        return False

    @staticmethod
    def show(project_dict):
        print(f"Project Number: {project_dict['project_no']}")
        print(f"Project Name: {project_dict['title']}")
        print(f"Project details: {project_dict['details']}")
        print(f"Project total target: {project_dict['total_target']}")
        print(f"Project start date: {project_dict['start_date']}")
        print(f"Project end date: {project_dict['end_date']}")
        print("-------------------------------------------------")
    
    @classmethod
    def search_by_date(cls, date_str):
        projects = cls.get_all_projects()
        return  [ project for project in projects if datetime.strptime(date_str, "%d-%m-%Y") >= datetime.strptime(project["start_date"], "%d-%m-%Y") and datetime.strptime(date_str, "%d-%m-%Y") <= datetime.strptime(project["end_date"], "%d-%m-%Y") ]