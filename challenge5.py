t = input('Enter the time that the power was failing')

split_t = t.split()

hour = int(split_t[0])
minute = int(split_t[1])

h = hour + (minute / 60)


time = ((4*h)**2)/(h+2)-20#

print(time)