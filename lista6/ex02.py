# temos dois alunos a e b
# a_sorri e b_sorri indicam se a e b sorriem
# temos problemas quando ambos estão sorrindo ou ambos não estão sorrindo
# retorne True quando houver problemas
def alunos_problema(a_sorri, b_sorri):
    if a_sorri == True and b_sorri == True:
        print("Houston we have a problem")
    elif a_sorri == False and b_sorri == False:
        print("Houston we have a problem")
        return a_sorri, b_sorri


alunos_problema(False, False)
