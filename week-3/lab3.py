import json

default_config = {
    "app_name": "Student Management System",
    "version": "1.0",
    "settings": {
        "theme": "light",
        "language": "English",
        "notifications": True
    }
}

try:
    with open("config.json", "r") as file:
        config = json.load(file)

except FileNotFoundError:
    config = default_config

    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)

print("Application:", config["app_name"])
print("Version:", config["version"])
print("Theme:", config["settings"]["theme"])
print("Language:", config["settings"]["language"])
print("Notifications:", config["settings"]["notifications"])

config["settings"]["theme"] = "dark"

with open("config.json", "w") as file:
    json.dump(config, file, indent=4)

print("\nConfiguration updated successfully!")