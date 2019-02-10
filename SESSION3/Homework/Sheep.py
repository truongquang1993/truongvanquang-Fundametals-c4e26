print("Hello, my name is Quang and these are my sheep sizes")

sheep = [5,7,300,90,24,50,75]

print(sheep)

print()

sum = 0

for m in range(3):
    print("MONTH",m+1,":")

    print("Now my biggest sheep has size",max(sheep),"let's shear it")

    sheep[sheep.index(max(sheep))] = 8

    print("After shearing, here's my flock", "\n", sheep)
    
    sheep_after=[]

    for i in sheep:
        i += 50
        sheep_after.append(i)     

    sheep = sheep_after

    print("One month has passed, now here is my flock", "\n", sheep)

    print()

for i in sheep:

    sum += i

print("My flock has size in total:",sum,"\nI would get",sum,"*2$ =",sum*2)