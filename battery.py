battery = int(input("battery left?? : "))
lenght = int(input("lenght of battery?? : "))

sum_battery = int((battery * lenght) // 100)
loss = lenght - sum_battery

print("(" + "0"*sum_battery + "_"*loss + ") " + str(battery) + "%")
print("{} / {}".format(str(sum_battery),str(lenght)))