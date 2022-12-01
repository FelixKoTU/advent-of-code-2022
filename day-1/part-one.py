def read_file(file):
    f = open(file, "r")
    data_into_list = f.read().split('\n')
    f.close()
    return data_into_list

if __name__ == '__main__':
    input_file = "advent-of-code\day-1\part-one\part-1_input.txt"
    sumlist = []
    calsum = 0
    for i in read_file(input_file):
        if i != '':
            calsum += int(i)
        else:
            sumlist.append(calsum)
            calsum = 0
    sumlist.append(calsum)
    
    print(max(sumlist))
