name = input("Enter your name: ")
print("NAME:", name)
code = input("Enter your code: ")
print("CODE:", code)
print("..........................")

#1
list1 = [10,20,30,40,50]
print("List1:", list1)
print("..........................")

#2
my_tuple = (1,2,3,4,5)
print("Tuple:", my_tuple)
print("..........................")

#3
my_set  = {10,20,30,40,50}
my_set2 = {40,50,60,70,80}
my_set3 = my_set ^ my_set2
print("ค่าตัวเลขที่ไม่ซ้ำกันในเซ็ต:", my_set3)
print("..........................")

#4
my_dict = {'list1': [10,20,30,40,50], 'my_tuple': (1,2,3,4,5), 'my_set': {10,20,30,40,50}}
print("ข้อมูล:", my_dict)
print("..........................")

#5
def avg_num(list1):
    return sum(list1) / len(list1)
print("ค่าเฉลี่ยของ List1:", avg_num(list1))
print("..........................")

#6
avg = int(input("Enter your average: "))
if avg >= 50:
    print("ผ่านเกณฑ์")
else:
    print("ไม่ผ่านเกณฑ์")
print("..........................")

#8
List_1 = [2,3,4,5,6,7,8,9,10]
div_by_2 = list(filter(lambda x: x % 2 == 0, List_1))
print("เลขคู่:", div_by_2)
print(".........................")