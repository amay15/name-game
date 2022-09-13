name = ""
name_suffix = ""

while len(name) == 0 or len(name_suffix) == 0:
    name = input("What is your name?")
    if not name or len(name) == 0:
        print("Name cannot be empty.")
        name = ""
    else:
        for i in range(0, len(name)):
            if name[i].lower() in ("a", "e", "i", "o", "u"):
                name_suffix = name[i:len(name)].lower()
                break
        if len(name_suffix) == 0:
            print("Name must contain at least one vowel.")

print(f"""{name}, {name}, bo-b{name_suffix}
Bonana-fanna fo-f{name_suffix}
Fee fi mo-m{name_suffix}
{name}!""")
