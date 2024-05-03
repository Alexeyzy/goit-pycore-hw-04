from pathlib import Path
from pprint import pprint

def get_cats_info(path)-> dict:
    if path.exists():    
        list_cats = []
        with open(path,"r", encoding="UTF-8") as file:
            while True:	 
                keys = ["id","name","age"]
                dict_cats = dict.fromkeys(keys)
                line = file.readline().strip()   
                if not line: break               
                dict_cats["id"], dict_cats["name"] , dict_cats["age"] = line.split(",")
                list_cats.append(dict_cats)
        return list_cats 
    else:
        print("Не знайдено файл")

FILE = Path(__file__).parent/"cats.txt"
pprint((get_cats_info(FILE)))