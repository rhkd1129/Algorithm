'''
1541번 : 잃어버린 괄호
'''
s = input()
s = s.split('-')
result = 0
for i in range(len(s)):
    if i == 0:
        result += sum(list(map(int, s[i].split('+'))))
    else:
        result -= sum(list(map(int, s[i].split('+'))))

print(result)