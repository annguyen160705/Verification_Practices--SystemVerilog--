print("Cheking results ...")

f = open("log.txt", "r")
content = f.read()
f.close()

if "my_data = 0xb" in content:
    print(">>>PASS")
else:
    print(">>>FAIL")