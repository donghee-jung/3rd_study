from functools import reduce

no_cpu = int(input('NO of CPU? '))
work_tuple = input('Every processing time: ')

total = reduce(lambda x,y:x+y, work_tuple)

print("Type of result variable", type(total))
print(total)

