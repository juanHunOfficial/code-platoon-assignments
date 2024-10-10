bottles_of_beer = 99

for beer in range(bottles_of_beer, 1, -1):
    bottle = "bottles"
    if (beer - 1 == 1):
        bottle = "bottle" #take away the (s)
    print(f"{beer} bottles of beer on the wall, {beer} bottles of beer. \n" + 
          f"Take one down and pass it around, {beer -1} {bottle} of beer on the wall.")