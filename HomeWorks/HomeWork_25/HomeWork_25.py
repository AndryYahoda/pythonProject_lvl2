import re
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["task_database"]
collection = db["projects"]


def parse_line(line):
    """
    Parses a line containing project information and returns a dictionary with the project details.
    :param line: A string containing project information
    :return: A dictionary
    """
    pattern = r"(?P<type>КП|ВКР)\s+(?P<name>.+?)\s+(?P<language>Delphi\s+\d+\.\d+)\s+(?P<points>\d+)\+"
    match = re.match(pattern, line)
    if match:
        return {
            "Тип проекту": match.group("type"),
            "Назва проекту": match.group("name"),
            "Назва мови якою створено": match.group("language"),
            "Кількість поінтів": int(match.group("points")),
        }
    return None


file_path = "Task_25.txt"
parsed_data = []

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:
            project_data = parse_line(line)
            if project_data:
                parsed_data.append(project_data)

if parsed_data:
    collection.insert_many(parsed_data)

print(f"Кількість документів у колекції: {collection.count_documents({})}")
