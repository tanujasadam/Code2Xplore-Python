n=int(input("Enter number of elements:"))
mixed_list=[]
for i in range(n):
    value=input("Enter elements:")
    if value.isdigit():
     mixed_list.append(int(value))
    else:
     mixed_list.append(value)
number_list=[]
string_list=[]
count_numbers=0
count_strings=0
for item in mixed_list:
    if type(item)==int:
        number_list.append(item)
        count_numbers=count_numbers+1
    elif type(item)==str:
        if item!="":
            string_list.append(item)
            count_strings=count_strings+1
reg_no=input("Enter register number:")
last_digit=int(reg_no[len(reg_no)-1])
if last_digit%2==0:
    reversed_list=[]
    for i in range(len(number_list)-1,-1,-1):
        reversed_list.append(number_list[i])
    number_list=reversed_list
else:
    reversed_list=[]
    for i in range(len(string_list)-1,-1,-1):
        reversed_list.append(string_list[i])
    string_list=reversed_list
print("number_list:",number_list)
print("string_list:",string_list)
print("total numbers:", count_numbers)
print("total strings:", count_strings)