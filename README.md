# API GERENCIAMENTO DE NEGÓCIOS


Este projeto é uma API de gerenciamento de pedidos, clientes e produtos, destinada a facilitar o controle de um sistema de e-commerce. Ele permite a criação, leitura, atualização e remoção de informações de clientes, pedidos e produtos, proporcionando uma plataforma robusta para gerenciar vendas e interações com clientes.

Problema que o Projeto Resolve
A API oferece uma solução para o gerenciamento de pedidos e clientes de um e-commerce, permitindo que os administradores possam:

Cadastrar novos produtos e clientes.
Atualizar as informações dos produtos, clientes e pedidos.
Remover pedidos e clientes.
Listar todos os pedidos, clientes e produtos.
Consultar as informações de um pedido, cliente ou produto específico.

# Como Instalar e Executar o Projeto

Python 3.8 ou superior
PIP (gerenciador de pacotes do Python)
Banco de dados (por exemplo, SQLite, PostgreSQL) ou configuração de banco em memória para testes
Passos

# Clone o repositório:
git clone https://github.com/seu-usuario/nome-do-repositorio.git

Instale as dependências: Navegue até o diretório do projeto e instale as dependências usando o PIP:

Configure o banco de dados (caso necessário):

Se estiver usando um banco de dados, configure as credenciais no arquivo config.py ou similar.
Execute o servidor: Inicie o servidor com o seguinte comando:
uvicorn main:app --reload

Isso fará o servidor rodar em http://127.0.0.1:8000.

# Como Testar as Rotas Usando o Postman
Abra o Postman.

Importe as coleções de rotas (se você já tiver as coleções exportadas para o Postman):

Clique em File > Import > Importar arquivo e selecione o arquivo .json da coleção de rotas.
Testar as rotas:

# Cadastrar Produto:
Método: POST
URL: http://127.0.0.1:8000/produtos
Corpo: JSON com os dados do produto.

# Listar Produtos:
Método: GET
URL: http://127.0.0.1:8000/produtos

# Atualizar Produto:
Método: PUT
URL: http://127.0.0.1:8000/produtos/{produto_id}
Corpo: JSON com os dados atualizados.

# Remover Produto:
Método: DELETE
URL: http://127.0.0.1:8000/produtos/{produto_id}

E assim por diante para as rotas de clientes e pedidos.
