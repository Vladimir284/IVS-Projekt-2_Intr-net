from random import seed
from random import randint

my_data = open('../src/data.txt', 'w')

seed(1)
rnd_num = []
for i in range(10000000):
    rnd_num.append(randint(0, 9999))

i = 0
for i in range(10000000):
    print(rnd_num[i], end=" ", file=my_data)

my_data.close()