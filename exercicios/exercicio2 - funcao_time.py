import time

t = int(input("Digite quantos segundos deseja: "))

for i in range(t):
    time.sleep(1)
    print(i + 1)