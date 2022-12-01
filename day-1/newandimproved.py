data = open("advent-of-code\day-1\input.txt").read()
a = [sum(int(j) for j in i.split('\n')) for i in data.strip().split("\n\n")] # split of Index!!
print(max(a), sum(sorted(a)[-3:]), sep='\n')
