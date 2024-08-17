from pprint import pprint


data = {
    "projects": [
        {
            "project_id": 1,
            "name": "Project Alpha",
            "team": [
                {
                    "member_id": 101,
                    "name": "Alice",
                    "role": "Developer",
                    "tasks": [
                        {
                            "task_id": 1001,
                            "description": "Develop login module",
                            "status": "completed",
                            "hours_logged": 10
                        },
                        {
                            "task_id": 1002,
                            "description": "Implement OAuth",
                            "status": "in_progress",
                            "hours_logged": 5
                        }
                    ]
                },
                {
                    "member_id": 102,
                    "name": "Bob",
                    "role": "Tester",
                    "tasks": [
                        {
                            "task_id": 1003,
                            "description": "Test login module",
                            "status": "completed",
                            "hours_logged": 4
                        },
                        {
                            "task_id": 1004,
                            "description": "Prepare test cases for OAuth",
                            "status": "in_progress",
                            "hours_logged": 2
                        }
                    ]
                }
            ]
        },
        {
            "project_id": 2,
            "name": "Project Beta",
            "team": [
                {
                    "member_id": 103,
                    "name": "Charlie",
                    "role": "Developer",
                    "tasks": [
                        {
                            "task_id": 1005,
                            "description": "Design database schema",
                            "status": "completed",
                            "hours_logged": 8
                        },
                        {
                            "task_id": 1006,
                            "description": "Develop API endpoints",
                            "status": "in_progress",
                            "hours_logged": 7
                        }
                    ]
                },
                {
                    "member_id": 104,
                    "name": "Dave",
                    "role": "Project Manager",
                    "tasks": []
                }
            ]
        }
    ]
}



        
# list of all projects with members and tasks
for key, value in data.items():
    if key == "projects":
        for project in value:
            project_name = project["name"]
            project_id = project["project_id"]
            project_team = project["team"]
            print(f"Project Name: {project_name}")
            members_name = []
            for team_member in project_team:
                member_name = team_member["name"]
                tasks = team_member["tasks"]
                print(f"Member Name: {member_name}")

                if tasks:
                    tasks_name = []
                    for task in tasks:
                        task_name = task["description"]
                        tasks_name.append(task_name)
                    print(f"Member Tasks: {tasks_name}")
                else:
                    print(f"No tasks assigend to {member_name}")
                    # --> displays:
                    # Project Name: Project Alpha
                    # Member Name: Alice
                    # Member Tasks: ['Develop login module', 'Implement OAuth']
                    # Member Name: Bob
                    # Member Tasks: ['Test login module', 'Prepare test cases for OAuth']
                    # Project Name: Project Beta
                    # Member Name: Charlie
                    # Member Tasks: ['Design database schema', 'Develop API endpoints']
                    # Member Name: Dave
                    # No tasks assigend to Dave
print("****************************************************************")

# sum of working times for each team in each project & each member in a project/team
for project in data["projects"]:
    project_name = project["name"]
    total_team_hours = 0  # resetting the total team hours for each team
    # print(project["name"])
    for team_info in project["team"]:
        member_name = team_info["name"]
        # print(member_name)
        total_member_hours = sum(task["hours_logged"]
                                 for task in team_info["tasks"])
        total_team_hours += total_member_hours
        print(f"{member_name}'s total hours on {
              project_name}: {total_member_hours}")
    print(f"Total Team Hours for {project_name}: {total_team_hours}")
    # displays:
    # Alice's total hours on Project Alpha: 15
    # Bob's total hours on Project Alpha: 6
    # Total Team Hours for Project Alpha: 21
    # Charlie's total hours on Project Beta: 15
    # Dave's total hours on Project Beta: 0
    # Total Team Hours for Project Beta: 15
print("****************************************************************")

# list of all in-progress tasks with team member name and project name
in_progress_tasks = []
for project in data["projects"]:
    project_name = project["name"]
    for team_info in project["team"]:
        member_name = team_info["name"]
        for task in team_info["tasks"]:
            if task["status"] == "in_progress":
                task_name = task["description"]
                in_progress_tasks.append([f"Task Description: {task_name}, Project Name: {
                                         project_name}, Member Name: {member_name}"])
print("In Progress Tasks:", in_progress_tasks)
    # displays:
    # In Progress Tasks: [
    # [
    # 'Task Description: Implement OAuth,
    # Project Name: Project Alpha,
    # Member Name: Alice'
    # ],
    # [
    # 'Task Description: Prepare test cases for OAuth,
    # Project Name: Project Alpha,
    # Member Name: Bob'
    # ],
    # [
    # 'Task Description: Develop API endpoints,
    # Project Name: Project Beta,
    # Member Name: Charlie'
    # ]
    # ]
print("****************************************************************")

#summery of all projects with completed and in progress tasks divided by 100
# how many tasks out of 6 are completed? 3 out of 6
# how many tasks out of 6 are in progress? 3 out of 6
# all these out of 100


def get_percentage(part, whole): #gets the percentage of part out of whole
    if whole > 0:
        return (part / whole) * 100
    return 0
        


for project in data["projects"]:
    project_name = project["name"]
    total_tasks = 0
    completed_tasks = 0
    in_progress_tasks= 0 #resetting for the second project
    for team in project["team"]:
        total_tasks += len(team["tasks"])
# print(total_tasks) #prints the total number of the tasks ==> 6
        for task in team["tasks"]:
            if task["status"] == "completed":
                completed_tasks += 1
# print(f"Completed: {completed_tasks}") 
        for task in team["tasks"]:
            if task["status"] == "in_progress":
                in_progress_tasks += 1
# print(f"In Progress: {in_progress_tasks}")
    completed_percentage = get_percentage(completed_tasks, total_tasks)
    in_progress_percentage = get_percentage(in_progress_tasks, total_tasks)
    print(f"Project: {project_name}, Total Tasks: {total_tasks}, Compeleted: {completed_percentage}, In Progress: {in_progress_percentage}")