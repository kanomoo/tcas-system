from wcwidth import wcswidth
from .report_register import *
# คำนวณความกว้างของการแสดงผล

def pad_text(text, width = 0): # padding text เติมช่องว่าง ควรใช้เฉพาะภาษาไทย
    text = str(text)
    real_width = wcswidth(text)                         # คำนวณความกว้างจริงของข้อความในเทอมินอล (นับช่องว่างที่ข้อความใช้)
    if width == 0:
        return text 
    elif real_width < width:                            # ถ้าความกว้างจริงของข้อความน้อยกว่าความกว้างที่ต้องการ
        return text + " " * (width - real_width)        # เติมช่องว่างให้ครบตามความกว้างที่กำหนด เพื่อจัดข้อความให้อยู่ในตำแหน่ง len จริงๆ
    return text                                         # ถ้าความกว้างของข้อความมากกว่าหรือเท่ากับที่ต้องการ return เหมือนเดิม ใช้ format string จัดการต่อเอา

def data_course_info(): # เก็บข้อมูลจากไฟล์
    data = []
    with open(r"data_information/datas/data_course_info.txt","r",encoding="utf-8") as fout:
        for i in fout: 
            data.append(i.strip("\n").split("|"))
    return(sorted(data))

def data_dic_info():
    data = data_course_info()
    data_dic = {"university": {}}
    for course in data:
        university = course[0]
        faculty = course[1]
        program = course[2]

        catg_program = course[3]
        campus = course[4]
        expenses  = course[5]
        
        if university not in data_dic["university"]:
            data_dic["university"][university] = {}
        if faculty not in data_dic["university"][university]:
            data_dic["university"][university][faculty] = {}
        if program not in data_dic["university"][university][faculty]:
            data_dic["university"][university][faculty][program] = {}

        data_dic["university"][university][faculty][program] = {
            "Category of Program": catg_program,
            "Campus": campus,
            "Expenses": expenses,
        }

    return data_dic

def course_info(): # menu input course_info
    while True:
        print()
        head = f"|{"Course information":^40}|"
        line = f"+{"-" * (len(head) - 2)}+"
        choice = input(f"{line}\n{head}\n{line}\n|{"1. Setting Course Information":{len(head)-2}}|\n|{"2. Report All Course Information":{len(head)-2}}|\n|{"3. Report Course Total":{len(head)-2}}|\n|{"4. Go Back":{len(head)-2}}|\n{line}\nSelect option : ").strip()
        match choice:
            case "1":
                setting_university()
            case "2":
                all_course_info()
            case "3":
                report_course()
            case "4":
                break
            case _:
                print("Invalid input Please try again")
        
def setting_university():
    state = 0
    data = data_dic_info()
    while True:
        # ใช้ data ที่ เป็น dic
        print()
        result = ""
        head = f"|{'Search Course Information':^98}|"
        line = "-" * len(head)
        result += f"{line}\n{head}\n{line}\n"
        check_id = []
        # ค้นหาข้อมูลผ่าน data dic ต้องใช้ items ช่วย ที่ใช้คือ value
        for key,university in data.items():
            n = 0
            search_univ = {}
            for key_univ,faculty in university.items():
                n += 1
                # แปลงเป็น string เติม 0 ด้านหน้า id จะกรอกง่าย
                col_key_univ = pad_text(key_univ,len(head)-9)
                # ทำให้เป็นค่าความกว้างจริง
                search_univ[f"{n:0>2}"] = key_univ
                # สร้าง key id และ value ชื่อ
                result += (f"| {n:0>2} | {col_key_univ} |\n")
                check_id.append(f"{n:0>2}")
            result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
            result += line
        print(result)
        choice = input("Select data number or enter new data name (01 or มหาฯ) : ").strip()
        id = ""
        id += choice if choice != "00" and choice in check_id else ""
        if choice in search_univ and choice != "00": 
            # print(search_univ[choice])
            # return(search_univ[choice]) , data 
            setting_faculty(data, search_univ[choice])
        elif choice == "00": return True
        elif not choice.isdigit() : 
            if state == 0:
                print(f"New course information : {choice}")
                confirm = input("Confirm Information (y/n) : ").strip().lower()
                match confirm:
                    case "y":
                        if choice not in data["university"]:
                            data["university"][choice] = {}
                            state = 1
                    case "n":
                        pass
                    case _:
                        print("Invalid input Please try again")
                none_data = choice
            else: print(f"Please add data {none_data} to finishd")
        else: print("Invalid input Please try again")

  
def setting_faculty(n_data,univ):
    state = 0
    while True:
        try: 
            result = ""
            head = f"|{'Faculty':^98}|"
            line = "-" * len(head)
            result += f"{line}\n{head}\n{line}\n"
            check_id = []
        
            print()

            for key,university in n_data.items():
                n = 0
                search_fac = {}
                col_univ = pad_text(univ,68)
                result += (f"| {"University":25} | {col_univ} |\n{line}\n")

                for key_fac, faculty in university[univ].items():
                    n += 1
                    col_key_fac = pad_text(key_fac,len(head)-9)
                    search_fac[f"{n:0>2}"] = key_fac
                    # สร้าง key ตาม number format n_f จะเป็น key automatic
                    result += (f"| {n:0>2} | {col_key_fac} |\n")
                    check_id.append(f"{n:0>2}")
                result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
                result += line
    
            print(result)        
            choice = input("Select data number or enter new data name (01 or คณะ) : ").strip()
            if choice in search_fac and choice != "00": setting_program(n_data, univ, search_fac[choice])
            elif choice == "00": return True #add_university() #add_university()
            elif not choice.isdigit() : 
                if state == 0 :
                    print(f"New course information : {choice}")
                    confirm = input("Confirm Information (y/n) : ").strip().lower()
                    match confirm:
                        case "y":
                            if choice not in n_data["university"][univ]:
                                n_data["university"][univ][choice] = {}
                                state = 1
                        case "n":
                            pass
                        case _:
                            print("Invalid input Please try again")
                    none_data = choice
                else: print(f"Please add data {none_data} to finishd")
            else: print("Invalid input Please try again")
        except KeyError: return True

def setting_program(n_data,univ,fac):
    state = 0
    while True:
        try:
            result = ""
            head = f"|{'Couse Name':^98}|"
            line = "-" * len(head)
            result += f"{line}\n{head}\n{line}\n"
            check_id = []
        
            print()
            for key,university in n_data.items():
                n = 0
                col_univ = pad_text(univ,68)
                col_fac = pad_text(fac,68)

                result += (f"| {"University":25} | {col_univ} |\n")
                result += (f"| {"Faculty":25} | {col_fac} |\n{line}\n")

                search_program = {}
                for key_program, program in university[univ][fac].items():
                    n += 1
                    col_key_program = pad_text(key_program,len(head)-9)
                    search_program[f"{n:0>2}"] = key_program
                    # สร้าง key ตาม number format n_f จะเป็น key automatic
                    result += (f"| {n:0>2} | {col_key_program} |\n")
                    check_id.append(f"{n:0>2}")
                result += (f"| {0:0>2} | {"Back to Search Course Information":{len(head)-9}} |\n")
                result += line
       
            print(result)        
            choice = input("Select data number or enter new data name (01 or สาขา) : ").strip()
            if choice in search_program and choice != "00": setting_title(n_data, univ, fac, search_program[choice])
            elif choice == "00": return True #add_faculty(n_data,univ) #search_faculty(id,univ)
            elif not choice.isdigit() : 
                print(f"New course information : {choice}")
                confirm = input("Confirm Information (y/n) : ").strip().lower()
                match confirm:
                    case "y":
                        if state == 0:
                            if choice not in n_data["university"][univ][fac]:
                                n_data["university"][univ][fac][choice] = {}

                                n_data["university"][univ][fac][choice] = {
                                    "Category of Program": "Please add data",
                                    "Campus": "Please add data",
                                    "Expenses": "Please add data",
                                }
                                state = 1
                        else: print("Please add data to finishd")
                    case "n":
                        pass
                    case _:
                        print("Invalid input Please try again")
            else: print("Invalid input Please try again")
        except KeyError: return True

def setting_title(n_data ,univ ,fac ,program ):
    print()
    state = 0
    while True:
        try:
            result = ""
            head = f"|{'Couse Information':^98}|"
            line = "-" * len(head)
            result += f"{line}\n{head}\n{line}\n"
        
            for key,university in n_data.items():

                col_univ = pad_text(univ,68)
                col_fac = pad_text(fac,68)
                col_program = pad_text(program,68)

                result += (f"| {"University":25} | {col_univ} |\n")
                result += (f"| {"Faculty":25} | {col_fac} |\n")
                result += (f"| {"Program":25} | {col_program} |\n")

                data_title = []
                for key_title, title in university[univ][fac][program].items():
                    col_title = pad_text(title,68)
                    result += (f"| {key_title:25} | {col_title} |\n")
                    data_title.append(col_title)        
        except: 
            return True

        print(result+line)        
        if state == 0 and title == "Please add data":
            catg = input("Enter Category of Program : ").strip()
            campus = input("Enter Campus : ").strip()
            expenses = input("Enter Expenses : ").strip()
            confirm = input("Confirm Information (y/n) : ").strip().lower()
            match confirm:
                case "y":
                    n_data["university"][univ][fac][program] = {
                        "Category of Program": catg,
                        "Campus": campus,
                        "Expenses": expenses,
                    }
                    state = 1
                    return True
                case "n":
                    return True
                case _:
                    print("Invalid input Please try again")

        choice = input(f"{"-" * 22}\n|{"1. Edit data":20}|\n|{"2. Save data":20}|\n|{"3. Deleate data":20}|\n|{"4. Go Back":20}|\n{"-" * 22}\nselect : ").strip()
        match choice:
            case "1":
                n_data, univ, fac, program, catg , campus , expenses  = edit_add_data(n_data, univ, fac, program, catg = data_title[0] , campus = data_title[1] , expenses = data_title[2]) 
                print("Data Edit")
                
            case "2":
                save_data(n_data)
                print("Data Save")
            case "3":
                while True:
                    choice_d = input(f"\n1. Deleate Unversity: {univ}\n2. Deleate Faculty: {fac}\n3. Deleate Program: {program}\n4. Go Back\nselect : ").strip()
                    match choice_d:
                        case "1":
                            del n_data["university"][univ]
                            del_data(n_data)
                        case "2":
                            del n_data["university"][univ][fac]
                            del_data(n_data)
                        case "3":
                            del n_data["university"][univ][fac][program]
                            del_data(n_data)
                    print("Data Delete")
                    return True
            case "4":
                break
            case _:
                pass
        
def edit_add_data(n_data, univ, fac , program , catg = " ", campus = " ", expenses = " "):
    e_data = input("Enter the field name to edit (University) : ").strip().lower()
    if e_data in ["university","faculty","program","category of program","campus","expenses"]:
        w_data = input("Enter new data : ").strip()

        match e_data:
            case "university":
                n_data["university"][w_data] = n_data["university"].pop(univ)
                univ = w_data

            case "faculty":
                n_data["university"][univ][w_data] = n_data["university"][univ].pop(fac)
                fac = w_data

            case "program":
                n_data["university"][univ][fac][w_data]= n_data["university"][univ][fac].pop(program)
                program = w_data
                
            case "category of program":
                n_data["university"][univ][fac][program]["Category of Program"] = w_data
                catg = w_data

            case "campus":
                n_data["university"][univ][fac][program]["Campus"] = w_data
                campus = w_data
            
            case "expenses":
                n_data["university"][univ][fac][program]["Expenses"] = w_data
                catg = w_data

        print(f"{e_data} : {w_data}")
        return n_data, univ, fac, program, catg , campus , expenses 
    
    else:
        print("No field name in data")
        n_data = univ = fac = program = catg = campus = expenses = ""
        return n_data, univ, fac, program, catg , campus , expenses 
        

def save_data(n_data):
    data = []

    for univ, facs in n_data["university"].items():
        for fac, programs in facs.items():
            for program, details in programs.items():
                data.append([univ,fac,program,details.get("Category of Program",""),details.get("Campus",""),details.get("Expenses","")])
    
    with open(r"data_information/datas/data_course_info.txt","w",encoding="utf-8") as fin:
        for i in data:
            fin.writelines("|".join(i)+"\n")

def del_data(n_data):
    data = []

    for univ, facs in n_data["university"].items():
        for fac, programs in facs.items():
            for program, details in programs.items():
                data.append([univ,fac,program,details.get("Category of Program",""),details.get("Campus",""),details.get("Expenses","")])

    with open(r"data_information/datas/data_course_info.txt","w",encoding=
    "utf-8") as fin:
        for i in data:
            fin.writelines("|".join(i)+"\n")


def all_course_info():
    print()
    result = ""
    datas = data_course_info()
    head = f"|{'Report Course Infomation':^70}|"
    line = "=" * len(head)
    # title = ["สถานบัน","คณะ","หลักสูตร","ชื่อหลักสูตรภาษาอังกฤษ","ประเภทหลักสูตร","วิทยาเขต","ค่าใช้จ่ายต่อภาคเรียน"]
    title = ["University","Faculty","Program","Category of Program","Campus","Expenses"]
    result += (f"{line}\n{head}\n{line}")
    print(result)

    n = 0
    for course in datas:
        n += 1
        if n == 1: print(f"|{f" Course {n} ":^70}|\n{line}")
        else: print(f"\n{line}\n|{f" Course {n} ":^70}|\n{line}")
        for i in range(len(title)):
            # result += f"คอร์สที่ {n} {course[i]}\n"
            col_data = pad_text(course[i], 70 - 29)  # ลบ len tile กับช่องว่างก่อน col_data
            print(f"| {title[i]:25}| {col_data} |")
            # result += (f"| {title[i]:25}| {col_data} |\n")
        print(line)
        # result += line + f"{n}\n"
    print()