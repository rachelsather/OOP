import insectclass as i

# this creates two separate instances
housefly = i.insect(2,4) #housefly is an insect object
mosquito = i.insect(6,8)

housefly.flight_length()
mosquito.flight_length()

print('the housefly can fly up to ', housefly.get_flight())
print('the mosquito can fly up to ', mosquito.get_flight())

