def get_file_name(student_name, week_number, assignment_number):
    file_name = " "
    if week_number < 10:
        file_name = "week0" + str(week_number) + "assignment" + str(assignment_number) + "" + student_name
    if assignment_number < 10:
        file_name = "week" + str(week_number) + "assignment0" + str(assignment_number) + "" + student_name
    if (assignment_number < 10) and (week_number < 10):
         file_name = "week0" + str(week_number) + "assignment0" + str(assignment_number) + "" + student_name
    return file_name
        

print(get_file_name("TranVanLuat", 2, 12))  
print(get_file_name("PhiPhuongAnh", 4, 6))  
print(get_file_name("TranLeVanAnh", 2, 10))