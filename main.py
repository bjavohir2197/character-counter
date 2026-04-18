def belgilar_soni(s):
    return len(s.replace(" ", ""))

print(belgilar_soni("Hello World"))  # 11
print(belgilar_soni("Python programming"))  # 17
print(belgilar_soni("   "))  # 0
