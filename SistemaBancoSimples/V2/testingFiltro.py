usuarios = {"nome":["Jhon","Silva"],"data_nascimento":["05-02-1998","06-02-1998"],"cpf":["123","567"], "endereco":["aaa","bbb"]}
cpf = str()

def FiltrarUser(cpf,usuarios):
    usuario_filtrados = [usuario for usuario in usuarios["cpf"] if usuario == cpf]
    return usuario_filtrados if usuario_filtrados else None

while True:
    cpf = input("cpf: ")
    usuario = FiltrarUser(cpf,usuarios)
    print(usuario, "tipo: ",type(usuario))
    if usuario:
        print("If. ")
    else:
        print("Not if. ")
    if cpf == "J":
        break