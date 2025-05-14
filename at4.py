alunos = []
for i in range(5):
    aluno = input("digite o nome do aluno: ")
    nota1 = float(input("digite a nota: "))
    nota2 = float(input("digite a nota: "))

    media = (nota1 + nota2) / 2 
    alunos.append({
        "aluno":aluno,
        "aluno_nota 1":nota1,
        "aluno_nota 2":nota2,
        "media":media
    })
    print("Resultado Final")
for aluno_nota in alunos:
    print(f"{aluno_nota['aluno']} - aluno_nota 1: {aluno_nota['aluno_nota 1']} | aluno_nota 2:{aluno_nota['aluno_nota 2']} | media: {aluno_nota['media']:.2}")