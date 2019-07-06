##n= int(input('Ile studentow: '))
##student_marks = {}
##for _ in range(n):
##    name, *line = input('Podaj nazwisko i wyniki studenta: ').split()
##    scores = list(map(float, line))
##    student_marks[name] = scores
##query_name = input('Podaj nazwisko studenta: ')
##sum = 0
##counter = 0
##for score in student_marks[query_name]:
##    sum+= float(score)
##    counter+=1
##
##
##print('%.2f' % (sum/float(counter)))

##N = int(input('Podaj liczbe: '))
##li = []
##for _ in range(N):
##    #wprowadzany ciag jest przeksztalcany na liste za pomoca split
##    s = input().split()
##    #pobieramy pierwszy element na liscie i zapisujemy jako command
##    command = s[0]
##    #pobieramy reszte elementow z listy i zapisujemy jako argumenty
##    arg = s[1:]
##    if command != 'print':
##        #tworzymy string w postac np. command(x,y)
##        #join laczy string z kazdym elementem listy arg
##        command += '('+','.join(arg)+')'
##        #eval - polecenia zapisane jako string przeksztalaca na wykonalne poecenie
##        eval('li.'+command)
##    else:
##        print(li)


##n = int(input())
###wczytanie do zmiennej input_list listy
##input_list = input().split()
###konwertowanie kazdego elementu listy na wartosc typu int
##integer_list = [int(x) for x in input_list]
###integer_list = map(int, input().split()) ta sama czynnosc tylko z uzyciem
##                                         #funkcji map ktora wola funkcje int na
##                                         #kazdym nowo dodanym elemencie  
###konwersja na krotke
##t = tuple(integer_list)
###wywolanie funkcji hash
##print(hash(t))
