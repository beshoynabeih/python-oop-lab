import validate
from user import User
from project import Project
from datetime import datetime
# print(user.User.get_users())
# print(type(user.User.get_max_user_no()))
# print(project.Project.get_user_projects(2))
# print(project.Project.get_max_project_no())

print("*********************************************************************")
print("***************** Welcome to first python challenge *****************")
print("*********************************************************************")

while True:
    ans = input("Please, Enter '1' for login '2' for Registration '0' for exit: ").strip()
    if  ans == "1":
        email = input("please enter your email: ").strip()
        password = input("please enter your password: ").strip()           
        #check for credentials
        user = User.login(email, password)
        if user:
            # when credentials are correct
            print(f"Welcome {user['first_name']} {user['last_name']}")
            while True:
                ans = input("Please, Enter\n'1': For list all projects\n'2': For create new project\n'3': For edit a project\n'4': For delete a proejct\n'5': For search by date\n'6': For exit\n--> ")
                if not ans.isdigit() or not ans in ["1", "2", "3", "4", "5", "6"]:
                    print("invalid input")
                    continue
                elif ans == "6":
                    quit()
                elif ans == "1":                    
                    print("*********************************************")
                    print("***************** Projects *****************")
                    print("*********************************************")
                    for project_obj in Project.get_all_projects():
                        Project.show(project_obj)
                elif ans == "2":
                    #create a project
                    #index, title, details, total_target, start_date, end_date
                    while True:
                        title = input("please enter project title: ").strip()
                        if validate.validate_string(title) == True:
                            break
                        else:
                            print("invalid title, title only alphabet")
                    while True:
                        details = input("please enter project details: ").strip()
                        if validate.validate_string(details) == True:
                            break
                        else:
                            print("Invalid detials, details only alphabet")
                    while True:
                        total_target = input("please enter project total target: ").strip()
                        if total_target.isdigit():
                            break
                        else:
                            print("invalid total target")
                    while True:
                        start_date = input("please enter project start date (dd-mm-yyyy): ").strip()
                        if validate.validate_date(start_date):
                            break
                        else:
                            print("invalid date input")
                    while True:
                        end_date = input("please enter project end date (dd-mm-yyyy): ").strip()
                        if validate.validate_date(end_date):
                            if datetime.strptime(end_date, "%d-%m-%Y") > datetime.strptime(start_date, "%d-%m-%Y"):
                                break
                            else:
                                print("------> end date must be after start date <--------")
                                continue
                            break
                        else:
                            print("invalid date input")
                    
                    # if projects.project.create_project(user["user_no"] ,title, details, total_target, start_date, end_date):
                    #     print("Project created")
                    # else:
                    #     print("Error creating the project :)")
                    project_obj = Project(user["user_no"], title, details, total_target, start_date, end_date)
                    if project_obj.save():
                        print("Project created")
                    else:
                        print("an error occured")
                elif ans == "3":
                    #update a project
                    #user_projects_numbers = projects.project.user_projects(user["user_no"])
                    #print user project
                    user_projects = Project.get_user_projects(user["user_no"])
                    if user_projects:
                        print("*********************************************")
                        print(f"************* {user['first_name']} {user['last_name']} Projects **************")
                        print("*********************************************")
                        for pro_obj in user_projects:
                            Project.show(pro_obj)
                    else:
                        print("You have not any project")
                        continue
                    project_number = input("Please, insert a project number to update it: ").strip()
                    #find the project by number
                    if project_number.isdigit():
                        project_old = Project.get_project(user["user_no"], int(project_number))
                    else:
                        project_old = False
                    #if user input found and it is his own project
                    if project_old:
                        while True:
                            title = input("please enter project title: ").strip()
                            if not title or validate.validate_string(title):
                                break
                            else:
                                print("invalid title")
                        while True:
                            details = input("please enter project details: ").strip()
                            if not details or  validate.validate_string(details):
                                break
                            else:
                                print("Invalid detials")
                        while True:
                            total_target = input("please enter project total target: ").strip()
                            if not total_target or  total_target.isdigit():
                                break
                            else:
                                print("invalid total target")
                        while True:
                            start_date = input("please enter project start date (dd-mm-yyyy): ")
                            if not start_date:
                                break
                            elif validate.validate_date(start_date):
                                break
                            else:
                                print("invalid date input format")
                        while True:
                            end_date = input("please enter project end date (dd-mm-yyyy): ").strip()
                            if not end_date:
                                if start_date and datetime.strptime(project_old["end_date"], "%d-%m-%Y") <= datetime.strptime(start_date, "%d-%m-%Y"):
                                    print(f"old end date value {project_old['end_date']} can not be before {start_date}")
                                    continue
                                break
                            elif validate.validate_date(end_date):
                                if datetime.strptime(end_date, "%d-%m-%Y") > datetime.strptime(start_date or project_old["start_date"], "%d-%m-%Y"):
                                    break
                                else:
                                    print("------> end date must be after start date <--------")
                            else:
                                print("invalid date input format")
                        project = Project(user["user_no"], title, details, total_target, start_date, end_date, project_old["project_no"])
                        if project.update():
                            print("----------->Project Updated<-------------")
                        else:
                            print("----> Error updating the project :) <-----")

                    else:
                        print("----------->Invalid Project number<-------------")

                elif ans == "4":
                    #delete a project
                    user_projects = Project.get_user_projects(user["user_no"])
                    if user_projects:
                        print("*********************************************")
                        print(f"************* {user['first_name']} {user['last_name']} Projects **************")
                        print("*********************************************")
                        for pro_obj in user_projects:
                            Project.show(pro_obj)
                    else:
                        print("You have not any project")
                        continue
                    project_number = input("Please, insert a project number to delete it: ").strip()

                    if project_number.isdigit():
                        if Project.delete( int(project_number), user["user_no"] ):
                            print("----> project deleted <--------")
                        else:
                            print("----> project not found <----")
                    else:
                        print("-----> invalid input <------")

                elif ans == "5":
                    while True:                       
                        project_date_1 = input("Please, Enter a date (dd-mm-yyyy)").strip()
                        if validate.validate_date(project_date_1.strip()):
                            projects = Project.search_by_date(project_date_1)
                            if projects:
                                for project in projects:
                                    Project.show(project)
                            else:
                                print(f"---> no project in this date {project_date_1} <-----")
                            break
                        else:
                            print("--------------> Invalid date format <------------------")
                else:
                    print("--------------> Invalid input <------------------")
        else:
            print("----------> invaled credential <----------")
        

    elif ans == "2":
        #loop for user input till he enter valid
        while True:
            f_name = input("please enter your first name: ").strip()
            if validate.validate_f_name(f_name) == True:
                break
            else:
                print(validate.validate_f_name(f_name))
        while True:
            l_name = input("please enter your last name: ").strip()
            if validate.validate_l_name(l_name) == True:
                break
            else:
                print(validate.validate_l_name(l_name))
        while True:
            email = input("please enter your email: ").strip()
            if validate.validate_email(email) == True:
                break
            else:
                print("Invalid email address or email used before")
        while True:
            password = input("please enter your password: ").strip()
            if validate.validate_password(password) == True:
                break
            else:
                print(validate.validate_password(password))

        while True:
            conf_pass = input("please enter your confirmation password: ").strip()
            if validate.validate_conf_pass(conf_pass, password) == True:
                break
            else:
                print(validate.validate_conf_pass(conf_pass, password))
            
        while True:
            mobile = input("please enter your mobile number: ").strip()
            if validate.validate_mobile(mobile) == True:
                break
            else:
                print("Invalid mobile number or duplicated number")
        #create user object
        user = User(f_name,l_name,email,password,mobile)
        if user.save():
            print("Your account has been created")
    elif ans == "0":
        break
    else:
        print("Invalid input")