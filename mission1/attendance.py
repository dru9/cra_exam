id_by_names = {}
id_cnt = 0

points = [0] * 100
grade = [0] * 100
grade_names = ["NORMAL", "SILVER", "GOLD"]
name_by_ids = [''] * 100
wed_count = [0] * 100
weekend_count = [0] * 100

def calculate_grade(person_id:int):
    if wed_count[person_id] > 9:
        points[person_id] += 10
    if weekend_count[person_id] > 9:
        points[person_id] += 10

    if points[person_id] >= 50:
        grade[person_id] = 2
    elif points[person_id] >= 30:
        grade[person_id] = 1
    else:
        grade[person_id] = 0

def process_record(name:str, day:str):
    global id_cnt

    if name not in id_by_names:
        id_cnt += 1
        id_by_names[name] = id_cnt
        name_by_ids[id_cnt] = name

    person_id = id_by_names[name]

    if day in ["monday", "tuesday", "thursday", "friday"]:
        points[person_id] += 1
    elif day == "wednesday":
        points[person_id] += 3
        wed_count[person_id] += 1
    elif day in ["saturday", "sunday"]:
        points[person_id] += 2
        weekend_count[person_id] += 1


def input_file():
    try:
        with open("attendance_weekday_500.txt", encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                record = line.strip().split()
                if len(record) == 2:
                    process_record(name=record[0], day=record[1])

        for i in range(1, id_cnt + 1):
            calculate_grade(i)
            print(f"NAME : {name_by_ids[i]}, POINT : {points[i]}, GRADE : ", end="")
            print(grade_names[grade[i]])

        print("\nRemoved player")
        print("==============")
        for i in range(1, id_cnt + 1):
            if grade[i] not in (1, 2) and wed_count[i] == 0 and weekend_count[i] == 0:
                print(name_by_ids[i])

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

if __name__ == "__main__":
    input_file()