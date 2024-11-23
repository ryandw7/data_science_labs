import os
import json

def read_all_scores():
    os.system("clear")
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
    blocker = input("")
                    

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
        return best

def write_score(topic, subtopic, score):
    current_best = read_score(topic, subtopic)
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
    

def read_score_wrapper(read_function, *args, **kwargs):
    with open('./lab_data/user_scores.json', 'r') as f:
        data = json.load(f)
        read_function(data)
        f.close()
        
def write_score_wrapper(write_function, *args, **kwargs):
    with open('./lab_data/user_scores.json', 'w') as f:
        write_function(f, *args, **kwargs)
        f.close()

def mark_completed(topic, subtopic):
    data = ""
    with open('./lab_data/user_scores.json', 'r') as f:
        data = json.load(f)
        
        for i in range(len(data[f"{topic}"])):
            if data[f"{topic}"][i]["topic"] == subtopic:
                data[f"{topic}"][i]["status"] = "Completed"
                f.close()
                with open('./lab_data/user_scores.json', 'w') as f:
                    json.dump(data, f, indent=4)


def grab_score_by_id(id):
    did = id.split("_")
    
    with open('./lab_data/user_scores.json', 'r') as f:
        data = json.load(f)['labs']
        for id_seg in range(len(did)):
            for i in data:
                new_seg = "_".join(did[0: id_seg + 1])
                print(new_seg)
                if i['id'] == new_seg:
                    data = i["children"]
                    break
            
    print(data)    
    return(data)

grab_score_by_id("3_1_1")