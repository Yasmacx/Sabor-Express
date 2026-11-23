import os
from selectors import SelectSelector

restaurantes = [{'nome': 'Mcdonald', 'categoria': 'Lanches', 'ativo':True},
               {'nome': 'Pizarria Master', 'categoria': 'Italiana', 'ativo':False},
               {'nome': 'Arabialanches', 'categoria': 'Arabe', 'ativo':False}] #dados globais
#dicionarios seperado por virgula

def voltar_menu():
    input("Digite qualquer tecla para ir ao menu principal ")
    main()

def subtitulo(texto):
    print("\n" * 150)
    linha = '=' * len(texto)
    #cada letra do titulo vai ter um *
    print(linha)
    print(texto)
    print(linha)
    print()

def iniciar():
    print("""
 █▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▒█▀▀▀ █ █ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
 ▀▀▀▄▄ █▄▄█ █▀▀▄ █  █ █▄▄▀ 　 ▒█▀▀▀ ▄▀▄ █  █ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
 █▄▄▄█ ▀  ▀ ▀▀▀  ▀▀▀▀ ▀ ▀▀ 　 ▒█▄▄▄ ▀ ▀ █▀▀▀ ▀ ▀▀ ▀▀▀ ▀▀▀ ▀▀▀\n""")

def opcoes():
    print("1.Cadastrar restaurante")
    print("2.Listar restaurantes")
    print("3.Alterar estado do restaurante")
    print("4.Sair\n")

def cadastrar_restaurante():
    print("\n" * 100)
    subtitulo('Cadastrar restaurante')

    nome_dos_restaurantes = input("Digite o nome do restaurantes que deseja cadastrar: ")
    tipo_restaurante = input(f"Digite a categoria do restaurante do restaurante {nome_dos_restaurantes}: ")

    novo_restaurantes = {'nome': nome_dos_restaurantes,
                    'categoria': tipo_restaurante,
                    'ativo': False
                    }

    restaurantes.append(novo_restaurantes)

    print(f"O restaurante: {nome_dos_restaurantes} foi cadastrado com sucesso!\n")
    voltar_menu()

    # append add dados na lista = o input que vai guardar o dados da lista
    #para voltar ao def principal

def listar_restaurante():
    print("\n" * 100)
    subtitulo('Listar restaurantes')

    print('Nome / Categoria / Status\n2')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        tipo_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante ['ativo'] else 'desativado'
        print(f"- {nome_restaurante.ljust(20)} | {tipo_restaurante.ljust(20)} | {ativo_restaurante.ljust(20)}")
                                    #.ljust() coloca a quantidade de espaçamento, 20 fica parecendo tabela
    voltar_menu()

def opcao_invalida():
    print("\n" * 100)
    print("Escolha invalida!")
    voltar_menu()

def alterar_estado_restaurante():
    print("\n" * 100)
    subtitulo('Alterar estado de restaurante')
    nome_restaurante = input("Digite o nome do resturante que deseja alterar: ")

    restaurante_encontrado = False
    for restaurante in restaurantes:
            if restaurante['nome'] == nome_restaurante:
                restaurante_encontrado = True
                restaurante['ativo'] = not restaurante['ativo']
                                    #not inverte o true e desliga o restaurante que esta true
                mensagem = (
                    f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo']
                    else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
                )

                print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado!')

    voltar_menu()

def input_usuario():
    try: #ele volta a fazer isso quando o usuario nao coloca o mesmo tipo de caractere
        while True:
            usuario = int(input("Escolha uma opção: \n"))
            print(f"Você escolheu: ")
            if usuario == 1:
                print("Cadastrar restaurante")
                cadastrar_restaurante()
                break
            elif usuario == 2:
                print("Listar restaurante")
                listar_restaurante()
                break
            elif usuario == 3:
                print("Ativar restaurante")
                alterar_estado_restaurante()
                break
            elif usuario == 4:
                finalizar()
                break
            else:
                opcao_invalida()
                continue
    except Exception as erro:
        print(erro)

def finalizar():
    os.system('cls')
    print("\n" * 100)
    subtitulo('Finalizar Sabor express...')

def main():
    print("\n" * 100)
    iniciar()
    opcoes()
    input_usuario()

if __name__ == '__main__':
    main()