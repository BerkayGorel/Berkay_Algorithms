sayı = 600851475143
divisor = 2
sayaç = 0

while divisor <= sayı:
    while sayı % divisor == 0:
        sayı /= divisor
        sayaç+=1
        print(divisor,"^",sayaç)
    else:
        sayaç = 0
        divisor +=1 