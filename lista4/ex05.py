texto = (
    """The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.""".replace(
        ",", ""
    )
    .replace(".", "")
    .replace(":", "")
)

palavras = texto.split()
in_python = []
maior_que_4 = 0

for s in palavras:
    p = s.lower()
    if p[0] in "python":
        in_python.append(s)
        if len(s) > 4:
            maior_que_4 += 1

print(maior_que_4)
