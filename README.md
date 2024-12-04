# Gerenciamento de Negócios:

Este é um projeto simples desenvolvido com **FastAPI** para gerenciar uma loja virutal. O objetivo principal é aprender os conceitos de **CRUD** (Create, Read, Update, Delete) e os métodos HTTP: **GET**, **POST**, **PUT** e **DELETE**, além de utilizar o **Postman** para testar rotas de APIs.  

---

## Tecnologias Utilizadas  
- **Python 3.10+**  
- **FastAPI**  
- **Uvicorn** (servidor ASGI)  
- **Postman** (para testar as rotas)  

---

## Como Executar  

### Pré-requisitos  
1. Tenha o **Python** instalado em sua máquina.  
2. Instale as dependências necessárias com o comando:  
   ```bash
   pip install fastapi uvicorn
3. Executar o servidor:
   ```bash
   uvicorn main:app --reload
4. Isso fará o servidor rodar em http://127.0.0.1:8000.

## Como testar as rotas no Postman

- Cadastrar Produto:
Método: POST
URL: http://127.0.0.1:8000/produtos
Corpo: JSON com os dados do produto.

- Listar Produtos:
Método: GET
URL: http://127.0.0.1:8000/produtos

- Atualizar Produto:
Método: PUT
URL: http://127.0.0.1:8000/produtos/{produto_id}
Corpo: JSON com os dados atualizados.

- Remover Produto:
Método: DELETE
URL: http://127.0.0.1:8000/produtos/{produto_id}

E assim por diante para as rotas de clientes e pedidos.
