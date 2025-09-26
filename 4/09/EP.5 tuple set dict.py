print("#1")
my_tuple = (10,20,30,"Hello","World")
print(my_tuple)
print(".......................")
print("#2")
my_set = {1,2,3,4,4,5}
print(my_set)
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)
5 in my_set
print(5 in my_set)
10 in my_set
print(10 in my_set)
my_set.clear()
print(my_set)
print(".......................")
print("#3")
set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1 | set2
print(set3)
print(".......................")
print("#4")
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = set1 & set2
print(set3)
set3 = set1 - set2
print(set3)
set3 = set1 ^ set2
print(set3)
print(".......................")
print("#5")
my_dict = {"name": "Saranyu", "age": 18, "gender": "Male"}
print("a.", my_dict)
print("b.", my_dict["name"])
print("c.", my_dict["age"])
my_dict["hobby"] = "reading"
print("d.", my_dict)
my_dict["name"] = "Ice"
print("e.", my_dict)
my_dict["age"] = 19
print("f.", my_dict)
my_dict["gender"] = "male"
print("g.", my_dict)
my_dict.pop("gender")
print("i.", my_dict)
del my_dict["hobby"] 
print("j.", my_dict)
new_info = {"Weight": 80, "city": "Singburi"}
my_dict.update(new_info)
print("l.", my_dict)
print("n.", "name" in my_dict)
print("o.", "gender" not in my_dict)
print("p.", my_dict.items())
print("q.", my_dict.values())
print("r.", len(my_dict))
print(".........................")
print("#6")
pairs = [("fruit", "apple"), ("color", "red")]
dict_from_pairs = dict(pairs)
print("dictionary จาก pairs:", dict_from_pairs)
print(".........................")