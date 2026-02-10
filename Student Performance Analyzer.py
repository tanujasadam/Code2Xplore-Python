name=input("Enter student name:")
N=int(input("Enter number of students:"))
marks=[]
total_valid=0
total_failed=0
for i in range(N):
    mark=int(input("Enter marks:"))
    marks.append(mark)
for u in marks:
    if len(name)%2==0 and 0<=u<=100:
        u=u+2
        if u>100:
            u=100
    if u<0 and u>100:
        print(u,"invalid")
    elif u>=90:
        print("updated marks:", u, "Excellent")
        total_valid=total_valid+1
    elif u>=75:
        print("updated marks:", u, "Very Good")
        total_valid=total_valid+1
    elif u>=60:
        print("updated marks:", u, "Good")
        total_valid=total_valid+1
    elif u>=40:
        print("updated marks:", u, "Average")
        total_valid=total_valid+1
    else:
        print(u,"Fail")
        total_valid=total_valid+1
        total_failed=total_failed+1
print("total valid students:",total_valid)
print("total failed students:",total_failed)