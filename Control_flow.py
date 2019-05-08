# Control flow
# if, else, elif
# while and for loops
#
trafficLightState = "yellow";
distanceFromLight = 15
# if trafficLightState == "green":
#     print("go")
# elif trafficLightState == "yellow" and distanceFromLight <= 15:
#     print("speed up")
# elif trafficLightState == "yellow" and distanceFromLight > 15:
#     print("slow down")
# elif trafficLightState == "red":
#     print("stop")
# else:
#     print("unkown")

if trafficLightState == "green":
    print("go")
elif trafficLightState == "yellow":
    if distanceFromLight <= 15:
        print("speed up")
    else:
        print("slow down")
elif trafficLightState == "red":
    print("stop")
else:
    print("unkown")

endPoint = 10
startPoint = 3
currentPos = startPoint
print(currentPos)

while currentPos < endPoint:
    currentPos += 1
    print(currentPos)

numArray = [13, 42, 53, 75, 12]

for num in numArray:
    print(num * 2)
