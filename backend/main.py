from fastapi import FastAPI, UploadFile, File
import shutil
import os
from db import AcessoDB
from face_recog import FaceRecognizer

app = FastAPI()
db = AcessoDB()
reconhecedor = FaceRecognizer()

@app.post("/verificar")
async def verificar(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Supondo que há uma imagem referência "ref.jpg" já registrada
    referencia_path = "ref.jpg"  
    resultado = reconhecedor.verificar_rosto(referencia_path, temp_path)
    os.remove(temp_path)

    if resultado:
        nome = "Pessoa Reconhecida"
        db.registrar_acesso(nome)
        return {"status": "autorizado", "nome": nome}
    else:
        return {"status": "desconhecido"}

@app.post("/cadastrar")
async def cadastrar(nome: str, file: UploadFile = File(...)):
    ref_path = f"ref_{file.filename}"
    with open(ref_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    sucesso = reconhecedor.cadastrar_rosto(nome, ref_path)
    os.remove(ref_path)
    return {"status": "sucesso" if sucesso else "erro"}
