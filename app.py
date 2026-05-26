from time import sleep

titulo = "---------- MENU ----------"

def salvar_servico(cliente, modelo, servico, valor):
    # Modo "a" (append) abre o arquivo e adiciona no final dele
    # encoding="utf-8" garante que acentos nao quebrem o programa 
    with open("servicos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Cliente: {cliente} | Veículo: {modelo} | Serviço: {servico} | Valor: {valor:.2f}\n")
    print("\033[32mServiço salvo com sucesso!\033[m")
    
    
def listar_servicos():
    try:
        # Modo "r" (read) serve apenas para leitura
        with open("servicos.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            
            if conteudo.strip() == "":
                print("\033[mNenhum serviço cadastrado.")
            else:
                print("\033[34m--- LISTA DE SERVIÇOS ---\033[m")
                print(conteudo)
                print("\033[34m-------------------------\033[m")
                
    except FileNotFoundError:
        # Se o arquivo ainda não existir na pasta
        print("\033[mNenhum serviço cadastrado(arquivo não encontrado).\033[m")
                    

while True:
    sleep(1)
    print(f"{titulo:^25}")
    print("1 -> Cadastrar Nova Ordem de Serviço."
          "\n2 -> Listar Todas as Ordens"
          "\n0 -> Sair.")
    opcao = str(input("Digite o dígito da escolha: ")).strip()
    
    if opcao == "0":
        print("Encerrando Sistema...")
        sleep(0.5)
        break
    
    elif opcao == "1":
        cliente = str(input("Nome: "))
        modelo = str(input("Modelo: "))
        servico = str(input("Serviço: "))
        valor = float(input("Valor R$: "))
        salvar_servico(cliente, modelo, servico, valor)
        
        
    elif opcao == "2":
        listar_servicos()
        
    else:
        print("Opção inválida! Tente novamente.")        
    