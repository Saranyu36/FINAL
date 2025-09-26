#1
x =int(input("ป้อนจำนวนเต็ม: "))
if x > 0:
    print("เลขบวก")
elif x < 0:
    print("เลขศูนย์")
else:
    print("เลขลบ")
print(".........................")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
#2
score = int(input("ป้อนคะแนน (0-100): "))
if score < 0 or score > 100:
    print("คะแนนไม่ถูกต้อง")
elif score >= 80:
    print("เกรด A")
elif score >= 60:
    print("เกรด B")
elif score >= 40:
    print("เกรด C")
elif score >= 50:
    print("เกรด D")
else:
    print("เกรด F")
print(".........................")
#3
for i in range(2,21,2):
    print(i)
print(".........................")
#4
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print("ผลรวม = ", total)
print(".........................")
#5
while True:
    s = input("ป้อนข้อความ (exit เพื่อหยุด): ")
    if s.lower() == "exit":
        print("จบการทำงาน")
        break
    print("ข้อความที่ป้อน:", s)
print(".........................")
#6
for i in range(1,11):
    if i == 7:
        break
    print(i)
print(".........................")
#7
for i in range(1,11):
    if i == 5:
        continue
    print(i)
print(".........................")
#8
def demo():
    pass
demo()
print("ฟังก์ชัน demo() ถูกเรียกใช้งานแล้ว")
print(".........................")
#9
nums = [10, 7, 3, 8, 8, -2]

total = sum(nums)
max_val = max(nums)
min_val = min(nums)
even_count = sum(1 for num in nums if num % 2 == 0)
odd_count = len(nums) - even_count

print("รายการตัวเลข:", nums)
print("ผลรวมของตัวเลข:", total)
print("ค่ามากที่สุด:", max_val)
print("ค่าน้อยที่สุด:", min_val)
print("จำนวนเลขคู่:", even_count)
print("จำนวนเลขคี่:", odd_count)
print(".........................")