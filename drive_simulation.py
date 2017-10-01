int_velo = 0
limit_velo = 60
time_spent = t = int(input('Time spent on the road: '))
accel = a = input('Acceleration: ')
distance = input('Distance: ')

limit = t + 1

v = int_velo + int(a) * int(t)
s = 0.5 * float(t) * (v + int_velo)

for i in range (0, int(limit)):
    v_2 = int_velo + int(a) * i
    dis = 0.5 * i * (v_2 + int_velo)
    k = int(dis/10)
    print ("Duration: ", i, "Distance: ", "*" * k)

if v > limit_velo:
    print ('It went over the speed limit. (Max Speed was', v, 'm/s)')
else:
    print ('It did not go over the speed limit. (Max Speed was', v, 'm/s)')
if s > float(distance):
    print ('The person reached the destination. (Reached', s, 'm)')
else:
    print ('The person did not reached the destination. (Reached', s, 'm)')
