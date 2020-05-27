import json

with open("logs.json", "r", encoding="utf-16") as f:
    source = f.read()

data = json.loads(source)

for items in range (0, len(data["AssociatedArtifacts"])):
    try:
        print(data["AssociatedArtifacts"][items]["Owner"])

    except KeyError:
        print("This key does not have a name!")
        continue