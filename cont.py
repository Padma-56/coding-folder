j=0
while j<3:
    if j == 1:
        print("skip")
        j+=1
        continue
    print(f"processing {j}")
    j+=1
else:
        print("while loop complete")         