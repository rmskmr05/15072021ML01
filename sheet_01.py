print("-------------------------------------------------")
#########################################################
## 1.
print("Solution-2\n")
print('5**9:',5**9)
print('3//2:',3//2)
print('7//3:',7//3)
print('7/3:',7/3)
print('6 == 6:', 6 == 6)
a = 20; a+= 30; a%=3;
print("a = 20; a+= 30; a%=3;\na=", a)
print('True * False:', True * False)
print('True & False:',True & False)
print('True and False:',True and False)
print('((6>3) and (7<4) or (18==3)) and (9>3):', ((6>3) and (7<4) or (18==3)) and (9>3))
print('True is False:', (True is False))
#print('False in "False":', (False in 'False'))#error
print("((True == False) or (False > True)) and (False <= True):",((True == False) or (False > True)) and (False <= True))


#######################
## 3.
print("Solution-3\n")
s1 = "Nice to have it"
s2 = "here"
s1 = s1 + " " + s2
print(s1)

print("-------------------------------------------------")
#########################################################
## 4.
print("Solution-4\n")
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

print("-------------------------------------------------")
#########################################################
## 5.
print("Solution-5\n")
l = [s1] + a + [s2]
print(l)

print('-------------------------------------------------')
#########################################################
## 6. collect even numbers before 237
print("Solution-6\n")
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823,\
           566, 597, 978, 328, 615, 953, 345, 399, 162,\
           758, 219, 918, 237, 412, 566, 826, 248, 866,\
           950, 626, 949, 687, 217, 815, 67, 104, 58, \
           512, 24, 892, 894, 767, 553, 81, 379, 843, \
           831, 445, 742, 717, 958,743, 527]
#print(numbers)
for i in numbers:
    if i == 237:
        break
    else:
        if not i%2:
            print(i, end=' ')
print('')

print('-------------------------------------------------')
#########################################################
## 7..
print("Solution-7\n")
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

print('-------------------------------------------------')
#########################################################
## 8. Pangram String
print("Solution-8\n")
print("Enter for pangram:'The quick brown fox jumps over the lazy dog'")
print('Enter anythig for non-pangram')
test_str = input("Enter a string to test pangram:\n")

alphabets = set([chr(i) for i in range(97, 97+26)])

if alphabets.difference(set(test_str.lower())) == set():
    print("Pangram String")
else:
    print("Not a pangram string")

print('-------------------------------------------------')
#########################################################
## 9.
print("Solution-9\n")
##integer = input("Enter a value:")
integer = 5
print(sum([int(integer*i) for i in range(1,4)]))

print('-------------------------------------------------')
#########################################################
## 10.
print("Solution-10\n")
##string = input('''Enter two '#' seperated interger lists:
##        like: 23 54 12#98 3 17\n''')
string = "23 54 12#98 3 17"
string = string.split('#')
x = [eval(i) for i in string[0].split()]

print('-------------------------------------------------')
#########################################################
## 11.
print("Solution-11\n")
data = 'without,hello,bag,world'
data = data.split(',')
data.sort()
','.join(data)
print(data)


print('-------------------------------------------------')
#########################################################
## 12.
print("Solution-12\n")
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],\
    'Marks': [57,87,67,79]}
print(d.get('Student')[d.get('Marks').index(max(d.get('Marks')))])

print('-------------------------------------------------')
#########################################################
## 13.
print("Solution-13\n")
##string = input("Enter a string to count letters & digits:")
string = 'hello world! 123'
let, num = 0, 0
for i in string:
    if i.isdigit():
        num += 1
    elif i.isalpha():
        let += 1
print("LETTERS:", let)
print("DIGITS:", num)

print('-------------------------------------------------')
#########################################################
## 14.
print("Solution-14\n")
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
    'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
    'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

subject = 'Python'
indeces = [i for i in range(len(d.get('Subject'))) if d.get('Subject')[i]==subject]
keys = list(d.keys())
values = [[d.get(keys[0])[i], d.get(keys[1])[i], d.get(keys[2])[i]] for i in indeces]
newData = dict(zip(keys, zip(*values)))
print(newData)

## 14.
print("\nSolution-14\n")
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
    'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
    'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

keys = list(newData.keys())
newData = {k:[] for k in keys}
for i in range(len(d['Subject'])):
    if d['Subject'][i] == 'Python':
        for k in keys:
            newData[k].append(d[k][i])
print(newData)

print('-------------------------------------------------')
#########################################################
## 15.
print("Solution-15: Iteration of numbers divisible by 7 upto Range(including)\n ")
def gen7(Range):
    num = 1
    while num*7 <= Range:
        yield num*7
        num += 1
##r = int(input("Enter range limit:"))
r = 85
print(list(gen7(r)))
print('-------------------------------------------------')
#########################################################
## 16.
print("Solution-16\n")

def vector(t):
    return t[1] if 'UP' in t else (-t[1] if 'DOWN' in t else 0), \
           t[1] if 'RIGHT' in t else (-t[1] if 'LEFT' in t else 0)
data = [('UP', 5), ('DOWN', 3), ('LEFT', 3),('RIGHT', 2)]
x_dis, y_dis = 0, 0
for d in data:
    x, y = vector(d)
    x_dis += x; y_dis += y
print("Distance: ", round((x_dis**2 + y_dis**2)**0.5))




