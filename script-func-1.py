from pprint import pprint
import json

def get_percentage(part, whole):
    if whole > 0:
        return (part / whole) * 100
    return 0

def get_in_progress_tasks(project):
    in_progress_tasks = []
    for team in project["team"]:
        for task in team["tasks"]:
            if task["status"] == "in_progress":
                in_progress_tasks.extend([f"Task Description: {task["description"]}, Member Name: {team["name"]}"])
    print(f"In Progress Tasks:\n   {in_progress_tasks}")


  
def get_logged_hours(project):
    total_team_hours = 0
    for team in project["team"]:
        total_member_hours = 0
        for task in team["tasks"]:
            total_member_hours += task["hours_logged"]
        total_team_hours += total_member_hours
        print(f"{team["name"]}'s total hours: {total_member_hours}")
    print(f"Total Team Hours: {total_team_hours}")


def get_summary(project):
    total_tasks = 0
    completed_tasks = 0
    in_progress_tasks = 0 
    for team in project["team"]:
        total_tasks += len(team["tasks"])
        for task in team["tasks"]:
            if task["status"] == "completed":
                completed_tasks += 1
            elif task["status"] == "in_progress":
                in_progress_tasks += 1
    completed_percentage = get_percentage(completed_tasks, total_tasks)
    in_progress_percentage = get_percentage(in_progress_tasks, total_tasks)
    print(f"Total Tasks: {total_tasks},\n   Compeleted: {completed_percentage}%,\n   In Progress: {in_progress_percentage}%")


def main():
    with open("file.json", mode="r", encoding="utf-8") as read_file:
        data = json.load(read_file)

    for project in data["projects"]:
        print(f"\n {project["name"]}")

        team_member_count = len(project["team"])
        task_count = 0
        for team_member in project["team"]:
            task_count += len(team_member["tasks"])
        print("Member Count", team_member_count)
        print("Task Count", task_count)

        get_logged_hours(project)
        get_in_progress_tasks(project)
        get_summary(project)
        
if __name__ == "__main__":
    main()
