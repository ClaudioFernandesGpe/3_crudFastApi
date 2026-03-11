from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title= "API de Tarefas")

# MODELO DE DADOS
class tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    concluida: bool = False

# BANCO EM MEMÓRIA
db_tarefas = []

