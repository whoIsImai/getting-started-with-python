i = 0
while i < 10:
    print(f"Value: {i}")
    i+=1
    if i == 5:
        print(f"Breaking at {i}")
        continue
else:
    print("Loop completed without break")