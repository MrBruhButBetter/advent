answer = open("example.txt")

lines = [line.strip() for line in answer.readlines()]

aswr = 0

numbers = ["one", "two", "three", "four" , "five", "six", "seven", "eight", "nine"]




for line in lines:
    for i  in range(len(line)):
        

        print(line[i:])

print(aswr)
