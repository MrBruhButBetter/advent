answer = open("example.txt")

lines = [line.strip() for line in answer.readlines()]

aswr = 0


for line in lines:
    numbers = []
    for c in line:

        if c.isnumeric():
            numbers.append(c)



    aswr +=int(numbers[0] + numbers[-1])


print(aswr)
