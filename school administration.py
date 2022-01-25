import csv

def write_into_csv(student_detail):
    with open ("student.csv","a",) as file:
        writer=csv.writer(file)
        if(file.tell()==0):
            writer.writerow(["Name", "Age", "Mobile","E-mail"])
        writer.writerow(student_detail)

condition="True"
count=1
while(condition=="True"):
    
    student_info=input("\nEnter the student information {} in format ( Name age mobile E-mail ) : ".format(count))
    student_info_list=student_info.split(' ')
    print("Entered split up information : ",student_info_list)
    print("\nName : {}\nAge : {}\nMobile : {}\nE-mail : {}\n".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

    info_check=input("Is the entered information correct (yes/no) : ")
    if(info_check=="yes"):
         write_into_csv(student_info_list)
         condition_check=input("Do you want to enter another information (yes/no) : ")
         if(condition_check=="yes"):
             condition="True"
             count+=1
         else:
             condition="False"
    else:
        print("Please re-enter the values !")
        
   

