from pprint import pprint
import json

with open("file.json", mode="r", encoding="utf-8") as read_file:
    data = json.load(read_file)

def get_projects_info(data):
    projects = data.get("projects", [])
    return projects




def get_projects_name(projects_info):
    for project in projects_info:
        if project["name"]:
            print(project["name"])
   
   
   
def get_teams_info(projects_info):
    teams= []
    for project in projects_info:
        if project["team"]:
            teams.extend(project["team"])
    return teams
                         
def get_team_members(teams_info):
    for team in teams_info:
        members = []
        for member in team:
            if "name" in member:
                members.append(member["name"])
        print(members)
    return members
    
def get_tasks_info(teams_info):
    tasks = []
    for team in teams_info:
        if "tasks" in team:
            tasks.extend(task)
    print("task info", tasks)
    return tasks

def get_tasks_description(tasks_info): 
    tasks_desc = []
    for task in tasks_info:
        if "description" in task:
            tasks_desc.append(task["description"])
    print(tasks_desc)
    return tasks_desc
    
    
projects_info = get_projects_info(data)
get_projects_name(projects_info)
teams_info = get_teams_info(projects_info)

get_team_members(teams_info)
tasks_info = get_tasks_info(teams_info)
get_tasks_description(tasks_info)


