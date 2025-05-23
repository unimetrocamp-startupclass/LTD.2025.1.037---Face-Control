# FaceControl - Documentação do Sistema

## Dados do Cliente

- **Título do Projeto:** FaceControl: Sistema facial de controle de entrada e saída  
- **Cliente:** MOVE Soluções Corporativas  
- **CNPJ/CPF:** 55.890.067/0001-30  
- **Contato:** Eduardo Henrique Barbosa  
- **Email do contato:**  

## Equipe de Desenvolvimento

| Nome Completo | Curso | Disciplina |
| :-----------: | :---: | :--------: |
| Lucas Ryan Rodrigues Barbosa | ADS | Padrões de Projetos de Software com Java |
| Lucas Guilherme Silva | ADS | Padrões de Projetos de Software com Java |
| Luiz Gustavo de Lara Freschi | ADS | Padrões de Projetos de Software com Java |
| Eduardo Alejandro Meli Aracena Bello | ADS | Padrões de Projetos de Software com Java |
| Fernando Rodrigues De Sousa | ADS | Padrões de Projetos de Software com Java |

| Professor Orientador |
| :---: |
| Kesede Rodrigues Julio |


---

## 1. Introdução

O cliente relatou que possui um depósito e não tem controle de entrada e saída, o que acaba ocasionando em perdas de materiais e consequentemente dinheiro. Sendo assim, a equipe decidiu desenvolver um sistema de controle de acesso utilizando uma ESP32-CAM com captura de imagem, e um backend Flask responsável pelo processamento e armazenamento das imagens.

Neste novo modelo, ao pressionar um botão físico conectado à ESP32-CAM, a câmera captura uma imagem do usuário e envia para o servidor via HTTP. No backend, um endpoint Flask recebe essa imagem, salva localmente e prepara para o processamento posterior, como análise facial. O sistema visa, no futuro, realizar o reconhecimento facial com bibliotecas como Face Recognition, integradas ao backend Python.

Para armazenamento, as imagens são salvas localmente no servidor por enquanto, mas há planos de utilizar um banco de dados adequado. A interface de administração e cadastro será implementada posteriormente.

---

## 2. Objetivo

O projeto tem como objetivo principal desenvolver um sistema de controle de acesso por imagem, com potencial para integração de reconhecimento facial, destinado à empresa MOVE Soluções Corporativas. O sistema visa permitir a entrada e saída apenas de pessoas previamente cadastradas, a fim de minimizar perdas de materiais e aumentar o controle interno no depósito da empresa.

O fluxo principal consiste na captura de imagem pela ESP32-CAM quando o botão é pressionado, envio para um servidor Flask via rede Wi-Fi, salvamento da imagem no backend e futura verificação por algoritmos de reconhecimento facial. A solução foca na automação acessível, com uso de hardware de baixo custo e software customizável.

---

## 3. Escopo

O sistema será composto por:

* Um microcontrolador ESP32-CAM com câmera OV2640, que realiza a captura da imagem ao pressionar de um botão físico e envia via HTTP para o backend.
* Um backend Flask com um endpoint (`/upload-image`) que recebe a imagem enviada, salva em disco com timestamp, e prepara para futura análise.

Os principais requisitos que serão implementados incluem:

1. **Captura de Imagem via ESP32-CAM**
   Ao pressionar um botão físico, a ESP32-CAM captura uma imagem do ambiente ou do usuário e envia para o servidor via rede Wi-Fi.

2. **Recebimento e Armazenamento da Imagem**
   O backend desenvolvido com Flask salva a imagem com segurança usando a biblioteca `werkzeug`, armazenando com timestamp.

3. **Registro de Acesso com Imagem**
   Cada imagem recebida será registrada em uma pasta no servidor com nome de arquivo baseado em data e hora, permitindo rastreamento de acessos.

4. **Infraestrutura Flexível para Reconhecimento Facial**
   O sistema será preparado para, futuramente, integrar bibliotecas como OpenCV e Face Recognition, para realizar a autenticação facial automática.

**Limites da Implementação**

* O reconhecimento facial ainda não está implementado nesta versão; atualmente, o sistema captura e armazena imagens apenas.
* A ESP32-CAM exige rede Wi-Fi 2.4GHz para funcionamento.
* O sistema depende de um servidor local ou em rede para o recebimento e salvamento das imagens.

---

## 4. Backlogs do Produto

1. **Captura e Envio de Imagem pela ESP32-CAM**
   Programar a ESP32-CAM para capturar imagem ao pressionar um botão e enviar via HTTP POST para o endpoint Flask.

2. **Criação do Endpoint no Backend Flask**
   Desenvolver o endpoint `/upload-image` que recebe arquivos de imagem, aplica nome seguro e timestamp, e armazena em diretório específico.

3. **Organização e Armazenamento Local de Imagens**
   Implementar salvamento organizado em uma pasta `uploads/`, mantendo controle cronológico dos acessos.

4. **Documentação do Sistema e Configuração de Rede**
   Detalhar como configurar o nome e senha da rede Wi-Fi, botão na protoboard e upload do código `.ino` para a ESP32-CAM.

5. **Preparação para Reconhecimento Facial**
   Garantir que as imagens capturadas tenham qualidade suficiente para uso futuro com Face Recognition.

6. **Autenticação e Interface de Administração (futuro)**
   Será desenvolvida interface para visualização de imagens capturadas, cadastro de usuários e, eventualmente, reconhecimento facial com autorização de entrada.

Esses requisitos compõem a versão atual do projeto, com possibilidade de evolução para integração de reconhecimento facial e interface gráfica completa no futuro.

---

## ⚙️ Tecnologias Utilizadas

- **Python** xxxx
- **X** Backend com as funcionalidades de formulários e requisições ao banco de dados.
- **X** Banco de dados.

---

## 🗓️ Cronograma (Sprint)

| Fase              | Início     | Término    |
|-------------------|------------|------------|
| Sprint 1          | [28/02]    |  [14/03]   |
| Sprint 2          | [21/03]    |  [04/04]   |
| Sprint 3          | [11/04]    |  [02/05]   |
| Sprint 4          | [02/05]    |  [16/05]   |
| Sprint 5          | [23/05]    |  [27/06]   |
| Desenvolvimento   | [28/02]    |  [27/06]   |

> _Datas devem ser preenchidas conforme planejamento no Jira._

---

## 📢 Divulgação

- **Repositório na Organization GitHub:** [\[inserir link\]](https://github.com/unimetrocamp-startupclass/LTD.2025.1.037---Face-Control/edit/main)

---

