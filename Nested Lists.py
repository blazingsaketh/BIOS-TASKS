def custom_key(p):
    return p[1]


nstu = int(input())
stu = [[str(input()), float(input())] for i in range(nstu)]
stu.sort(key=custom_key)
names = [i[0] for i in stu]
marks = [i[1] for i in stu]
min_marks = marks[0]
while marks[0] == min_marks:
    marks.remove(marks[0])
    names.remove(names[0])
    if len(marks) == 0:
        break
tmarks = marks[:]
min = min(tmarks)
try:
    while True:
        tmarks.remove(min)
except ValueError:
    pass
l = len(tmarks)
test = len(marks) - l
new_list = names[:test]
new_list.sort()
for i in range(len(new_list)):
    print(new_list[i])