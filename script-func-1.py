from pprint import pprint
import json



def main():
    with open("file.json", mode="r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    for project in data["projects"]:
        print(project["name"])
        team_member_count = 0
        task_count = 0
        
        for team_member in project["team"]:
            team_member_count += 1 
            for task in team_member["tasks"]:
                    task_count += 1 
        print("Member Count", team_member_count)
        print("Task Count", task_count)

if __name__ == "__main__":     
    main()
    
