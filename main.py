from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title= "API de Tarefas")

# MODELO DE DADOS
class Tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    concluida: bool = False

# BANCO EM MEMÓRIA
db_tarefas = []

# ROTAPARA LISTAR TODAS AS TAREFAS
@app.get("/tarefas", response_model=List[Tarefa])
async def  listar_tarefas():
    return db_tarefas

# ROTA PARA CRIAR TAREFA
@app.post("/tarefas", response_model=Tarefa, status_code=201)
async def criar_tarefa(tarefa: Tarefa):
    tarefa.id = len(db_tarefas) + 1
    db_tarefas.append(tarefa)
    return tarefa

# ROTA PARA BUSCAR TAREFA POR ID
@app.get("/tarefas/{tarefa_id}", response_model=Tarefa)
async def buscar_tarefa(tarefa_id: int):
    for tarefa in db_tarefas:
        if tarefa.id == tarefa_id:
            return tarefa
    
    raise HTTPException(status_code=404, detail="Tarefa não encontrada!")



