import json

def writecsv(name, data):
    data.to_csv(f"{name}.csv", index=False)

def writejson(name, data):
    #TODO: schrijf functie zodanig dat volledige data wordt ingeladen
    with open(f"{name}.json", "w") as json_file:
        json.dump(list(data), json_file, indent=4)

def writexcel(name, data):
    #TODO: deze functie schrijven
    pass