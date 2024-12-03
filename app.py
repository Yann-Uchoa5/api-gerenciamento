from fastapi import FastAPI # type: ignore
from typing import Optional
from pydantic import BaseModel # type: ignore

app = FastAPI()

PRODUTOS = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone inteligente",
        "preco": 1999.99,
        "disponivel": True
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um computador portátil",
        "preco": 3999.99,
        "disponivel": False
    }
]

CLIENTES = [
    {
        "id": 1,
        "nome": "Yan Uchoa Pereira",
        "endereco": "Enedina de Carvalho",
        "telefone": 88988278848
    },
    {
        "id": 2,
        "nome": "Maria Erika Costa Ribeiro",
        "endereco": "Rua Osmar de Oliveira",
        "telefone": 88988278847
    }
]


PEDIDOS = [
    {
        "id": 1,
        "status": "Pendente",
        "endereco_entrega": "Fortaleza, CE - Eusébio",
        
    },
    {
        "id": 2,
        "status": "Cancelado",
        "endereco_entrega": "Boa Viagem, CE - Enedina de Carvalho",
    }
]


class Produto(BaseModel):
    """Classe de produtos."""

    nome: str
    descricao: Optional[str] = None
    preco: float
    disponivel: Optional[bool] = True

class Clientes(BaseModel):
    """Classe de clientes."""

    nome: str
    endereco: str
    telefone: int

class Pedidos(BaseModel):
    """Classe de clientes."""

    status: str
    endereco_entrega: str

@app.get("/produtos", tags=["produtos"])
def listar_produtos() -> list:
    """Listar_produtos"""
    return PRODUTOS

@app.get("/produtos/{produto_id}", tags=["produtos"])
def obter_produto(produto_id: int) -> dict:
    """Obter produto."""
    for produto in PRODUTOS:
       if produto["id"] == produto_id:
            return produto
    return {}

@app.post("/produtos", tags=["produtos"])
def criar_produto(produto: Produto) -> dict:
    """Criar produto."""
    produto = produto.dict()
    produto["id"] = len(PRODUTOS) + 1
    PRODUTOS.append(produto)
    return produto

@app.put("/produtos/{produto_id}", tags = ["produtos"])
def atualizar_produto(produto_id: int, produto: Produto) -> dict:
    """Atualizar Produto"""
    for index, prod in enumerate(PRODUTOS):
        if prod["id"] == produto_id:
            PRODUTOS[index] = produto
            return produto
        return {}

    

@app.delete("/produtos/{produto_id}", tags = ["produtos"])
def remover_produto(produto_id:int ) -> dict:
    """Remover Produto"""
    for index, prod in enumerate(PRODUTOS):
        if prod["id"] == produto_id:
            PRODUTOS.pop(index)
            return {"message": "Produto removido com sucesso"}
    return {}
    

@app.get("/clientes", tags=["clientes"])
def listar_clientes() -> list:
    """Listar_produtos"""
    return CLIENTES

@app.get("/clientes/{cliente_id}", tags=["clientes"])
def retornar_cliente(cliente_id: int) -> dict:
    """Retornar Cliente."""
    for clientes in CLIENTES:
       if clientes["id"] == cliente_id:
            return clientes
    return {}


@app.post("/clientes", tags=["clientes"])
def cadastrar_cliente(cliente: Clientes) -> dict:
    """Cadastrar Cliente."""
    cliente_dict = cliente.dict()
    cliente_dict["id"] = len(CLIENTES) + 1
    CLIENTES.append(cliente_dict) 
    return cliente_dict


@app.put("/clientes/{cliente_id}", tags=["clientes"])
def atualizar_cliente(cliente_id: int, cliente: Clientes) -> dict:
    """Atualizar Clientes"""
    for index, clien in enumerate(CLIENTES):
        if clien["id"] == cliente_id:
            CLIENTES[index] = cliente.dict()  
            return cliente.dict()
    return {}

@app.delete("/cliente/{cliente_id}", tags = ["clientes"])
def remover_cliente(cliente_id:int ) -> dict:
    """Remover Cliente"""
    for index, clien in enumerate(CLIENTES):
        if clien["id"] == cliente_id:
            CLIENTES.pop(index)
            return {"message": "Cliente removido com sucesso"}
    return {}


@app.get("/pedidos", tags=["pedidos"])
def listar_pedidos() -> list:
    """Listar Pedidos"""
    return PEDIDOS


@app.get("/pedidos/{pedido_id}", tags=["pedidos"])
def obter_pedido(pedido_id: int) -> dict:
    """Obter pedido."""
    for pedido in PEDIDOS:
       if pedido["id"] == pedido_id:
            return pedido
    return {}


@app.post("/pedidos", tags=["pedidos"])
def criar_pedido(pedido: Pedidos) -> dict:
    """Criar pedido."""
    pedido = pedido.dict()
    pedido["id"] = len(PEDIDOS) + 1
    PEDIDOS.append(pedido)
    return pedido

@app.put("/pedidos/{pedido_id}", tags=["pedidos"])
def atualizar_pedido(pedido_id: int, pedido: Pedidos) -> dict:
    """Atualizar Pedidos"""
    for index, ped in enumerate(PEDIDOS):
        if ped["id"] == pedido_id:
            PEDIDOS[index] = pedido.dict()  
            return pedido.dict()
    return {}

@app.delete("/pedidos/{pedido_id}", tags = ["pedidos"])
def remover_pedido(pedido_id:int ) -> dict:
    """Remover Pedido"""
    for index, ped in enumerate(PEDIDOS):
        if ped["id"] == pedido_id:
            PEDIDOS.pop(index)
            return {"message": "Pedido removido com sucesso"}
    return {}