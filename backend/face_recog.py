import requests

class FaceRecognizer:
    def __init__(self, deepstack_url="http://localhost:5000/v1/vision/face"):
        self.url = deepstack_url

    def verificar_rosto(self, imagem1_path, imagem2_path):
        with open(imagem1_path, "rb") as img1, open(imagem2_path, "rb") as img2:
            response = requests.post(
                f"{self.url}/match",
                files={"image1": img1, "image2": img2}
            )
            if response.status_code != 200:
                return None
            data = response.json()
            return data.get("matched", False)

    def cadastrar_rosto(self, nome, imagem_path):
        with open(imagem_path, "rb") as img:
            response = requests.post(
                f"{self.url}/register",
                files={"image": img},
                data={"userid": nome}
            )
            return response.ok
