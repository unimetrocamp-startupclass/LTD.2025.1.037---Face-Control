import requests
import os

DEEPSTACK_URL = "http://localhost:5000/v1/vision/face"

def verificar_rosto(caminho_imagem):
    with open(caminho_imagem, "rb") as img:
        response = requests.post(
            f"{DEEPSTACK_URL}/match",
            files={"image1": img, "image2": img}  # image1: referência, image2: foto tirada
        )
        if response.status_code != 200:
            return None
        data = response.json()
        if data.get("success") and data.get("matched"):
            return True
    return False

def cadastrar_rosto(nome, caminho_imagem):
    with open(caminho_imagem, "rb") as img:
        response = requests.post(
            f"{DEEPSTACK_URL}/register",
            files={"image": img},
            data={"userid": nome}
        )
        return response.ok

