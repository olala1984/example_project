##n = int(input())
##arr = map(int, input().split())
##li = list(arr)
##li.sort()
##li.reverse()
##for i in range(len(li)+1):
##    max = li[i]
##    if max > li[i+1]:
##        max = li[i+1]
##        break;
##print(max)

students = []
set_score = set()
for i in range(int(input('How many students: '))):
    name = input('Enter name: ')
    score = float(input('Enter score: '))
    students.append([name, score])
    set_score.add(score)

students = sorted(students)
second_score = sorted(list(set_score), reverse = True)[1]
for name, value in students:
    if value == second_score:
        print(name)
##second_highest.reverse()
#second_highest=set([marks for name, marks in students])
##second_highest=set(students)
#print(second_highest)
