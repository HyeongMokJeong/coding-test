num = int(input())
num_list=[]
new_num = num
value = 0
while(new_num!=0):
    num_list.append(new_num % 10)
    new_num = new_num // 10

if num_list.count(0)==0 or sum(num_list)%3 !=0:
    print(-1)
else:
    num_list.sort(reverse=True)
    for idx,i in enumerate(num_list):
        value = value + (i*(10**(len(num_list)-idx-1)))
    print(int(value))