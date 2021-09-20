print("This is a program for testing booleans for student tests")
grade1=float(input("type the grade of the first test"))
grade2=float(input("type the grade of the first test"))
absence=int(input("type the grade of abesences"))
total_classes=int(input("type the number of classes"))
avg_grade=(grade1 + grade2)/2
attendance=(total_classes-absence)/total_classes
if(av_grade>=6):
    if(attendance>=0.8):
        print("The student has been approved")
    else:
        print("The student has failed due to attendance rate lower than 80%")
elif(attendance>=0.8):
    print("The student has failed due to average grade less that 6")
else:
    print("The student has failed due to average grade less that 6 and attendance rate lower than 80%")

