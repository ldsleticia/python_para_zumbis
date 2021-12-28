texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''.lower().replace(",","").replace(".", "").replace(":","").split()

lista2= []

for i in range(0,(len(texto))):
    if texto[i].startswith(tuple("python")) or texto[i].endswith((tuple("python"))): 
        lista2.append(texto[i])

print(texto)
print('\nlista 2 - lista com as palavras que começam ou terminam com uma das letras “python”:\n', lista2)