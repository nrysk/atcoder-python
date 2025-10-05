versions = {
    "Ocelot": 1,
    "Serval": 2,
    "Lynx": 3,
}

x, y = input().split()
x_ver = versions[x]
y_ver = versions[y]

if x_ver >= y_ver:
    print("Yes")
else:
    print("No")
