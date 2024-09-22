import pandas as pd
import json

col = ["code", "classCode", "level", "levelNumber", "language", "title", "type", "abstract"]

def floor_to_hundred(num):
    return (int(num) // 100) * 100


def build_csv(json_file, output_nam):
    with open(json_file) as f: # f
        data = json.loads(f.read())

    df = pd.DataFrame(data["sectionList"][0]["items"])
    df["levelNumber"] = df["codeParts"].apply(lambda x: x["numeric1"])
    df["level"] = df["levelNumber"].apply(floor_to_hundred)
    df["classCode"] = df["codeParts"].apply(lambda x: x["alpha0"])

    df[col].to_csv(output_nam)

build_csv("favorites.json", "favorites.csv")
# build_csv("all.json", "all.csv")