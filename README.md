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

O cliente relatou que possui um depósito e não tem controle de entrada e saída, o que acaba ocasionando em perdas de materiais e consequentemente dinheiro. Sendo assim, a equipe decidiu desenvolver um sistema de controle facial para liberar apenas a entrada de pessoas autorizadas. Para o sistema de controle facial, utilizaremos OpenCV para acessar a câmera, capturar imagens e realizar processamento dessas imagens. A biblioteca Face Recognition será usada para registrar e comparar rostos através de representações numéricas. Para o armazenamento de dados, usaremos o banco de dados MongoDB para dados biométricos. No backend, Flask para criar APIs para integração e no frontend utilizaremos Tkinter ou PyQt para construir a interface.

---

## 2. Objetivo

O projeto tem como objetivo principal desenvolver um sistema de controle de acesso por reconhecimento facial, destinado à empresa MOVE Soluções Corporativas, com foco em segurança e rastreabilidade. O sistema visa permitir a entrada e saída apenas de pessoas previamente cadastradas, a fim de minimizar perdas de materiais e aumentar o controle interno no depósito da empresa.

Por meio do uso de tecnologias como OpenCV e a biblioteca Face Recognition, será possível realizar a detecção e identificação facial dos usuários. O backend será desenvolvido com Flask, responsável por intermediar a comunicação entre os dados faciais e o banco de dados MongoDB, enquanto a interface gráfica será construída com Tkinter ou PyQt, visando praticidade e usabilidade.

---

## 3. Escopo

O sistema será composto por um aplicativo desktop com funcionalidades voltadas ao controle de acesso por reconhecimento facial em ambientes físicos. Os principais requisitos que serão implementados incluem:

1. **Cadastro de Usuários Autorizados**  
   A aplicação permitirá o cadastro de pessoas autorizadas a acessar o depósito, incluindo nome, CPF e captura da imagem facial para posterior reconhecimento.

2. **Reconhecimento Facial para Controle de Acesso**  
   O sistema realizará a verificação facial em tempo real utilizando a webcam do dispositivo. Caso o rosto seja reconhecido como autorizado, o acesso será liberado; caso contrário, o evento será registrado como tentativa de acesso não autorizada.

3. **Registro de Entradas e Saídas**  
   Cada evento de entrada e saída será registrado automaticamente, gerando um log com informações como data, hora e identidade da pessoa reconhecida, permitindo ao cliente acompanhar a movimentação no local.

4. **Interface Administrativa**  
   A aplicação contará com uma interface administrativa acessível apenas a usuários autorizados, onde será possível gerenciar cadastros, consultar registros de acesso e remover usuários do sistema.

**Limites da Implementação**  
- O sistema será executado localmente, sem funcionalidades de acesso remoto via navegador ou aplicativo mobile.  
- Não haverá integração com catracas, portões eletrônicos ou outros dispositivos físicos de controle. A liberação será simbólica ou indicada por mensagens visuais/sonoras.  
- Nesta versão, o reconhecimento será feito apenas por câmera frontal de computadores, sem suporte para múltiplas câmeras ou câmeras IP.

---

## 4. Backlogs do Produto

Principais requisitos definidos com base nas necessidades do cliente e nas discussões realizadas com a equipe de desenvolvimento:

1. **Cadastro de Usuários Autorizados**  
   O administrador poderá adicionar novas pessoas autorizadas ao sistema, informando dados como nome, CPF e imagem facial capturada via webcam.

2. **Reconhecimento Facial em Tempo Real**  
   O sistema utilizará a câmera do dispositivo para capturar imagens e comparar com os rostos cadastrados, liberando ou negando o acesso com base na correspondência.

3. **Registro de Eventos de Acesso**  
   Toda tentativa de entrada ou saída será registrada com data, hora e resultado (autorizado ou não autorizado), permitindo rastreamento completo das movimentações.

4. **Interface Administrativa com Controle de Acesso**  
   Apenas administradores terão acesso ao painel administrativo, onde poderão gerenciar usuários autorizados e consultar os logs de entrada/saída.

5. **Gerenciamento de Cadastro Facial**  
   A aplicação permitirá a atualização ou remoção de usuários cadastrados, bem como a recaptura da imagem facial, caso necessário.

6. **Sistema de Autenticação**  
   O sistema contará com autenticação para o acesso ao painel administrativo, garantindo que apenas usuários autorizados possam modificar os dados do sistema.

7. **Interface Simples e Intuitiva**  
   A interface será desenvolvida com foco em usabilidade, utilizando Tkinter ou PyQt, permitindo fácil utilização mesmo por pessoas com pouca familiaridade com tecnologia.

Esses são os requisitos iniciais definidos para o projeto. Novas funcionalidades poderão ser consideradas e adicionadas ao longo do desenvolvimento, conforme necessidade do cliente e viabilidade técnica.

    
