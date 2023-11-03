import json

def writecsv(name, data):
    """
    Writes a DataFrame to a csv-file with the given name
    - name (str): the name of the resulted file
    - data (DataFrame): the data which to be transformed into csv-format

    Results:
    - FILE (csv)
    """
    try:
        data.to_csv(f"{name}.csv", index=False)
    except AttributeError as ae:
        print(f'\x1b[31mAttributeError: {ae}\x1b[0m')

def writejson(name, data):
    """
    Writes a DataFrame to a json-file with the given name
    - name (str): the name of the resulted file
    - data (DataFrame): the data which to be transformed into json-format

    Results:
    - FILE (json)
    """
    #TODO: schrijf functie zodanig dat volledige data wordt ingeladen
    with open(f"{name}.json", "w") as json_file:
        json.dump(list(data), json_file, indent=4)
