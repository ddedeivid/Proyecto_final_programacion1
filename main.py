from models.user import User
from models.project import Project
from models.task import Task
from models.subtask import SubTask
from models.client import Client
from models.email_notification import EmailNotification
from models.sms_notification import SmsNotification

users = []
clients = []
projects = []
tasks = []
sub_tasks = []
notifications = []


def find_client(clients_list: list, client_contact_email, client_phone):
    for client in clients_list:
        if client.get_contact_email() == client_contact_email or client.get_phone_number() == client_phone:
            return client
    return None


def find_user(users_list: list, first_name, last_name, email):
    for user in users_list:
        if ((user.get_first_name() == first_name and user.get_last_name() == last_name)
                or user.get_email() == email):
            return user
    return None


def find_project(projects_list: list, project_name):
    for project in projects_list:
        if project.get_title() == project_name:
            return project
    return None


def find_task(tasks_list: list, task_id):
    for task in tasks_list:
        if task.get_id() == task_id:
            return task
    return None


def determine_task_id(tasks_list: list):
    if not tasks_list:
        return "001"
    task_size = len(tasks_list)
    if task_size < 10:
        return "00" + str(task_size + 1)
    elif task_size < 100:
        return "0" + str(task_size + 1)
    else:
        return str(task_size + 1)


def get_task_by_project_name(tasks_list: list, project_name: str):
    tasks_by_project = []
    for task in tasks_list:
        if task.get_project() is not None:
            if task.get_project().get_title() == project_name:
                tasks_by_project.append(task)
    return tasks_by_project


def show_menu():
    print("\n--- Task Management System ---")
    print("1. Register an user")
    print("2. Register a client")
    print("3. Create Project")
    print("4. Create Task")
    print("5. Create Sub-task")
    print("6. View Tasks and Details")
    print("7. View Subtask and Details")
    print("8. Send Notifications")
    print("9. List users")
    print("10. List clients")
    print("11. List projects")
    print("12. View tasks of a project")
    print("X. Exit")
    return input("Select an option: ")

def main():
    while True:
        option = show_menu()

        if option == "1":
            print("\n-- Register an User --")
            name = input("Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            birth_date = input("Birthday (YYYY-MM-DD): ")
            position = input("Position: ")
            new_user = User(name, last_name, birth_date, email, position)
            users.append(new_user)
            print("User registered successfully.")

        elif option == "2":
            print("\n-- Register a Client --")
            company_name = input("Company Name: ")
            contact_name = input("Contact Name: ")
            contact_email = input("Contact Email: ")
            phone_number = input("Contact Phone: ")
            business_sector = input("Business Sector: ")
            new_client = Client(company_name, contact_name, contact_email, phone_number, business_sector)
            clients.append(new_client)
            print("Client registered successfully.")

        elif option == "3":
            print("\n -- Creating Project --")
            title = input("Title: ")
            description = input("Description: ")
            start_date = input("Start Date (YYYY-MM-DD): ")
            end_date = input("End Date (YYYY-MM-DD): ")

            # Adding the client searching for it in the clients list
            client_email = input("Client contact email: ")
            client_phone = input("Client contact phone number: ")
            client = find_client(clients, client_email, client_phone)
            if client is None:
                print("Client not found. Please register the client first.")
                continue

            # Adding the user searching for it in the user list
            user_first_name = input("User first name: ")
            user_last_name = input("User last name: ")
            user_email = input("User email: ")
            user = find_user(users, user_first_name, user_last_name, user_email)
            if user is None:
                print("User not found. Please register the user first.")
                continue

            new_project = Project(title, description, start_date, end_date, client, user)
            projects.append(new_project)
            print("\nProject created successfully!")

        elif option == "4":
            print("\n -- Creating Task --")
            task_id = determine_task_id(tasks)
            title = input("Title: ")
            description = input("Description: ")

            # Adding the user searching for it in the user list
            user_first_name = input("User first name: ")
            user_last_name = input("User last name: ")
            user_email = input("User email: ")
            responsible_user = find_user(users, user_first_name, user_last_name, user_email)
            if responsible_user is None:
                print("Responsible user not found. Task creation aborted.")
                continue

            # Adding the project searching for it in the project list
            project_name = input("Project title: ")
            project = find_project(projects, project_name)
            if project is None:
                print("Project not found. Task creation aborted.")
                continue

            category = input("Category: ")
            priority = input("Priority: ")
            status = input("Status: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            task = Task(task_id, title, description, responsible_user, project, category, priority, status, due_date)
            tasks.append(task)
            print("\nTask created successfully!")

        elif option == "5":
            print("\n -- Creating Sub-task --")
            task_id = determine_task_id(sub_tasks)
            title = input("Title: ")
            description = input("Description: ")

            # Adding the user searching for it in the user list
            user_first_name = input("User first name: ")
            user_last_name = input("User last name: ")
            user_email = input("User email: ")
            responsible_user = find_user(users, user_first_name, user_last_name, user_email)
            if responsible_user is None:
                print("Responsible user not found. Task creation aborted.")
                continue

            # Adding the project searching for it in the project list
            project_name = input("Project name: ")
            project = find_project(projects, project_name)
            if project is None:
                print("Project not found. Task creation aborted.")
                continue

            category = input("Category: ")
            priority = input("Priority: ")
            status = input("Status: ")
            due_date = input("Due Date (YYYY-MM-DD): ")

            # Adding the parent task
            parent_task_id = input("Parent Task ID: ")
            parent_task = find_task(tasks, parent_task_id)
            if parent_task is None:
                print("Parent task not found. Sub-task creation aborted.")
                continue

            subtask = SubTask(task_id, title, description, responsible_user, project, category, priority, status,
                              due_date, parent_task)
            sub_tasks.append(subtask)
            print("\nSub-task created successfully!")

        elif option == "6":
            if len(tasks) == 0:
                print("There is no task created!")
                continue
            print("\n-- List of Tasks --")
            for t in tasks:
                print(t.show_info())

        elif option == "7":
            if len(sub_tasks) == 0:
                print("\n--There is no subtask created!--")
                continue
            print("\n-- List of Subtasks --")
            for t in sub_tasks:
                print(t.show_info())

        elif option == "8":
            print("\n-- Sending Pending Notifications --")
            # Polymorphism:
            notifications.append(
                EmailNotification("Task Assigned", "You have a new task", "ID: 101", "2024-05-16", "test@mail.com"))
            notifications.append(SmsNotification("Urgent", "Deadline exceeded", "ID: 101", "2024-05-16", "3004445566"))

            for notif in notifications:
                notif.send()  # Calls the corresponding method based on the object type
            notifications.clear()

        elif option == "9":
            if len(users) == 0:
                print("There is no user listed!")
                continue
            else:
                print("\n-- List of Users --")
                for u in users:
                    u.show_info()

        elif option == "10":
            print("\n-- Client list --")
            if len(clients) == 0:
                print("There is no client listed!")
                continue
            else:
                print("\n-- List of Clients --")
                for c in clients:
                    c.show_info()

        elif option == "11":
            print("\n-- Project list --")
            if len(projects) == 0:
                print("There is no project listed!")
                continue
            else:
                print("\n-- List of Projects --")
                for p in projects:
                    p.show_info()

        elif option == "12":
            project_name = input("Project title: ")
            if project_name:
                tasks_by_project = get_task_by_project_name(tasks, project_name)
                if len(tasks_by_project) > 0:
                    print("\n-- Task by project --")
                    for t in tasks_by_project:
                        t.show_info()

        elif option == "X" or option == "x":
            print("Exiting the system...")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()