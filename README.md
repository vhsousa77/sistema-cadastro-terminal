# Sistema de Cadastro de Ordens de Serviço

Este é um sistema desenvolvido em Python para o gerenciamento de ordens de serviço via terminal. O projeto foi criado com o objetivo de praticar conceitos de lógica de programação, modularização com funções, tratamento de exceções e persistência de dados em arquivos locais de texto.

## Funcionalidades
- **Cadastrar Nova Ordem de Serviço:** Coleta dados do cliente, veículo, descrição do serviço e valor, gravando as informações de forma permanente em um arquivo `.txt`.
- **Listar Todas as Ordens:** Realiza a leitura do arquivo de texto e exibe o histórico de serviços cadastrados de maneira organizada no terminal.
- **Interface Defensiva:** Menu estruturado para evitar interrupções no programa caso o usuário digite caracteres inválidos ou deixe campos em branco.

## Tecnologias Utilizadas
- Python 3
- Biblioteca time (para controle de fluxo e pausas no terminal)
- Manipulação de arquivos nativa (uso de context managers com a estrutura 'with open')