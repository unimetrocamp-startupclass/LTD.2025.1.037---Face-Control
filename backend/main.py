from fastapi import FastAPI, UploadFile, File
import shutil
import os
from face_recog import verificar_rosto
from db import criar_tabela, registrar_acesso

app = FastAPI()
criar_tabela()

@app.post("/verificar")
async def verificar(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resultado = verificar_rosto(temp_path)
    os.remove(temp_path)

    if resultado:
        nome = "Pessoa Reconhecida"  # DeepStack não retorna nome diretamente
        registrar_acesso(nome)
        return {"status": "autorizado", "nome": nome}
    else:
        return {"status": "desconhecido"}

