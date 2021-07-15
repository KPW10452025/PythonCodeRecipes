list01 = ["Python", "Django", "Flask"]
with open("sample03.txt", "w", encoding="utf-8") as writefile:
    writefile.writelines(list01)

# By using .writelines, we'll get
# PythonDjangoFlask 
# in the sample03.txt