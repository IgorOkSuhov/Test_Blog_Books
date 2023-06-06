a = []
pribavlenie_kratnyh = 0
peremnozenije = 1

for i in range(1,100):
    if i % 2 == 0:
        pribavlenie_kratnyh +=i
        #print(pribavlenie_kratnyh)
    elif i % 5 == 0:
        peremnozenije *= i
        #print(peremnozenije)
resultat = peremnozenije / pribavlenie_kratnyh

print(pribavlenie_kratnyh)
print(peremnozenije)
print(resultat)


