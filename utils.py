import time
import json

def read_all_scores():
    with open('./lab_data/user_scores.json', 'r', encoding="latin-1") as f:
        data = json.load(f)
        for x in data:
            print(f"\n{x}")
            for y in data[f"{x}"]:
                for z in y:
                    key = z
                    value = y[f"{z}"]
                    if key == 'topic':
                        print(f"\n  {value}")
                    else:
                        print(f"    {key}: {value}")
                    

def read_score(topic, subtopic):
    with open('./lab_data/user_scores.json', 'r', encoding="latin-1") as f:
        data = json.load(f)
        best = 0
        if subtopic:
            for i in data[f"{topic}"]:
                if i["topic"] == subtopic:
                    best = i["best"]           
        else:
            return data['target']['best']
        print(best)
        return best

def write_score(topic, subtopic, score):
    current_best = read_score(topic, subtopic)
    print(score > current_best)
    data = ""
    
    with open("./lab_data/user_scores.json", "r") as f:
        data = json.load(f)
        parent = data[f"{topic}"]
        for i in range(len(parent)):
            if parent[i]["topic"] == subtopic:
                if parent[i]["best"] < score:
                    parent[i].update({"best":score})
                    f.close()
                    with open("./lab_data/user_scores.json", "w") as f:
                        json.dump(data, f, indent=4)
                        f.close()
                else:
                    f.close()
    
    

