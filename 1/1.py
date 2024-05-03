from pathlib import Path

def total_salary(path) -> list:
   
    if path.exists():
        res = 0
        total_lines = 0
        res_list = []

        with open(path,"r", encoding="UTF-8") as file:
            while True:	 
                line = file.readline().strip()   
                if not line: break
                point = line.find(",")
                if point:
                    res += int(line[point+1:])
                    total_lines += 1 
            
            res_list.append(res)
            res_list.append(int(res/total_lines))      
            return res_list
    else:
        print("Не знайдено файл")

FILE = Path(__file__).parent/"salary.txt"
try:    
    total, average = total_salary(FILE)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except:
    pass