from pprint import pprint
import json



def get_in_progress_tasks(project):
    in_progress_tasks = []
    for team_info in project["team"]:
        for task in team_info["tasks"]:
            if task["status"] == "in_progress":
                in_progress_tasks.append([f"Task Description: {task["description"]}, Member Name: {team_info["name"]}"])


    print("In Progress Tasks:", in_progress_tasks)
    
def get_logged_hours(project):
    total_team_hours = 0
    for team_info in project["team"]:
        total_member_hours = 0
        for task in team_info["tasks"]:
            total_member_hours += task["hours_logged"]
        total_team_hours += total_member_hours
        print(f"{team_info['name']}'s total hours: {total_member_hours}")
    print(f"Total Team Hours: {total_team_hours}")

    get_in_progress_tasks(project)

def main():
    with open("file.json", mode="r", encoding="utf-8") as read_file:
        data = json.load(read_file)

    for project in data["projects"]:
        print(project["name"])

        team_member_count = len(project["team"])
        task_count = 0
        for team_member in project["team"]:
            task_count += len(team_member["tasks"])
        print("Member Count", team_member_count)
        print("Task Count", task_count)

        get_logged_hours(project)

if __name__ == "__main__":
    main()
