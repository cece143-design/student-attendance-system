# Student names
def get_name(sid):
    match sid:
        case "1": return "John"
        case "2": return "Mary"
        case "3": return "Peter"
        case "4": return "Sarah"
        case "5": return "David"
        case "6": return "Grace"
        case "7": return "Paul"
        case "8": return "Anna"
        case "9": return "James"
        case "10": return "Ruth"
        case _: return ""


# Attendance data for 10 students
t1 = t2 = t3 = t4 = t5 = 0
t6 = t7 = t8 = t9 = t10 = 0

p1 = p2 = p3 = p4 = p5 = 0
p6 = p7 = p8 = p9 = p10 = 0

s1 = s2 = s3 = s4 = s5 = ""
s6 = s7 = s8 = s9 = s10 = ""

present = absent = late = 0


# Show students
def show_students():
    for sid in range(1, 11):
        print(sid, "-", get_name(str(sid)))


# Search for a student
def search_student():
    sid = input("Enter student ID (1-10): ")
    name = get_name(sid)

    if name == "":
        print("Invalid student ID!")
    else:
        print("Student:", name)


# Mark attendance
def mark_attendance():
    global t1, t2, t3, t4, t5, t6, t7, t8, t9, t10
    global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
    global s1, s2, s3, s4, s5, s6, s7, s8, s9, s10
    global present, absent, late

    sid = input("Enter student ID (1-10): ")
    name = get_name(sid)

    if name == "":
        print("Invalid student ID!")
        return

    status = input("P = Present, A = Absent, L = Late: ")
    status = status.upper()

    if status != "P" and status != "A" and status != "L":
        print("Invalid status! Enter P, A, or L.")
        return

    # Count the session
    match sid:
        case "1": t1 += 1
        case "2": t2 += 1
        case "3": t3 += 1
        case "4": t4 += 1
        case "5": t5 += 1
        case "6": t6 += 1
        case "7": t7 += 1
        case "8": t8 += 1
        case "9": t9 += 1
        case "10": t10 += 1

    # Save the latest status
    match sid:
        case "1": s1 = status
        case "2": s2 = status
        case "3": s3 = status
        case "4": s4 = status
        case "5": s5 = status
        case "6": s6 = status
        case "7": s7 = status
        case "8": s8 = status
        case "9": s9 = status
        case "10": s10 = status

    # Update summary
    if status == "P":
        present += 1
        match sid:
            case "1": p1 += 1
            case "2": p2 += 1
            case "3": p3 += 1
            case "4": p4 += 1
            case "5": p5 += 1
            case "6": p6 += 1
            case "7": p7 += 1
            case "8": p8 += 1
            case "9": p9 += 1
            case "10": p10 += 1
    elif status == "A":
        absent += 1
    else:
        late += 1

    print("Attendance saved for", name)


# Check attendance percentage
def show_percentage():
    sid = input("Enter student ID (1-10): ")
    name = get_name(sid)

    if name == "":
        print("Invalid student ID!")
        return

    match sid:
        case "1": total, attended = t1, p1
        case "2": total, attended = t2, p2
        case "3": total, attended = t3, p3
        case "4": total, attended = t4, p4
        case "5": total, attended = t5, p5
        case "6": total, attended = t6, p6
        case "7": total, attended = t7, p7
        case "8": total, attended = t8, p8
        case "9": total, attended = t9, p9
        case "10": total, attended = t10, p10

    if total == 0:
        print("No attendance recorded for", name)
    else:
        percentage = attended / total * 100
        print("Student:", name)
        print("Attendance:", round(percentage, 2), "%")


# Correct the latest attendance
def correct_attendance():
    global s1, s2, s3, s4, s5, s6, s7, s8, s9, s10
    global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
    global present, absent, late

    sid = input("Enter student ID (1-10): ")
    name = get_name(sid)

    if name == "":
        print("Invalid student ID!")
        return

    match sid:
        case "1": old = s1
        case "2": old = s2
        case "3": old = s3
        case "4": old = s4
        case "5": old = s5
        case "6": old = s6
        case "7": old = s7
        case "8": old = s8
        case "9": old = s9
        case "10": old = s10

    if old == "":
        print("No attendance to correct for", name)
        return

    print("Current status:", old)
    new = input("Enter corrected status (P/A/L): ")
    new = new.upper()

    if new != "P" and new != "A" and new != "L":
        print("Invalid status! Nothing changed.")
        return

    # Remove old summary count
    if old == "P":
        present -= 1
        match sid:
            case "1": p1 -= 1
            case "2": p2 -= 1
            case "3": p3 -= 1
            case "4": p4 -= 1
            case "5": p5 -= 1
            case "6": p6 -= 1
            case "7": p7 -= 1
            case "8": p8 -= 1
            case "9": p9 -= 1
            case "10": p10 -= 1
    elif old == "A":
        absent -= 1
    else:
        late -= 1

    # Add corrected summary count
    if new == "P":
        present += 1
        match sid:
            case "1": p1 += 1
            case "2": p2 += 1
            case "3": p3 += 1
            case "4": p4 += 1
            case "5": p5 += 1
            case "6": p6 += 1
            case "7": p7 += 1
            case "8": p8 += 1
            case "9": p9 += 1
            case "10": p10 += 1
    elif new == "A":
        absent += 1
    else:
        late += 1

    # Save corrected latest status
    match sid:
        case "1": s1 = new
        case "2": s2 = new
        case "3": s3 = new
        case "4": s4 = new
        case "5": s5 = new
        case "6": s6 = new
        case "7": s7 = new
        case "8": s8 = new
        case "9": s9 = new
        case "10": s10 = new

    print("Attendance corrected for", name)


# Show overall summary
def show_summary():
    print("\n--- ATTENDANCE SUMMARY ---")
    print("Present records:", present)
    print("Absent records:", absent)
    print("Late records:", late)


# Main menu
while True:
    print("\n===== STUDENT ATTENDANCE SYSTEM =====")
    print("1. Show students")
    print("2. Search student")
    print("3. Mark attendance")
    print("4. Check percentage")
    print("5. Attendance summary")
    print("6. Correct latest attendance")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    match choice:
        case "1": show_students()
        case "2": search_student()
        case "3": mark_attendance()
        case "4": show_percentage()
        case "5": show_summary()
        case "6": correct_attendance()
        case "7":
            print("Thank you for using the system!")
            break
        case _:
            print("Invalid choice!")
