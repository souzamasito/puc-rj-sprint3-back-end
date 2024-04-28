# Source 2 Sea

Este é o MVP (Minimum Viable Product) de um projeto desenvolvido para a sprint 3 do curso de Full Stack da PUC/RJ. Tem como objetivo o cadatramento de informaçoes sobre poluição nas praias do Brasil. 

A poluição dos oceanos é uma ameaça aos sistemas marinhos e à saúde humana. Uma maior vigilância por parte da sociedade pode contribuir na mitigação deste problema.

Com esse sistema o usuário será possível conhecer melhor este problema para o acionamento das autoridades para providências.

Benefícios deste sistema:

-Mapear os locais das praias com ocorrência de descarte irregular de resíduos; 
-Criar um repositório de informação sobre as áreas problemáticas para banhistas e autoridades; e
-Contribuir para as políticas públicas de saneamento básico.

## Descrição

O sistema permite que o usuário registre informações sobre a praia, CEP, cidade, UF, tipo de lixo e a data onde foi observado. Estas informações ficam registradas em uma lista e podem ser excluídas a qualquer tempo. Funcionalidades de adicionar, visualizar e remover itens. Foi feito com a linguagem Python e o Framework Flask.

---
## Como executar no modo de desenvolvimento

Clonar o repositório e acessar o diretório raiz, pelo terminal.

Criar um ambiente virtual do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Instalar as libs python listadas no `requirements.txt`, com o comando:

(env)$ pip install -r requirements.txt


Para executar a API, a aplicação Flask deverá ser iniciada pelo comando:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```
Para consultar a documentação abra o http://localhost:5000/# no navegador.

##Como executar através do Docker
Certifique-se de ter o Docker instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile no terminal e seus arquivos de aplicação e Execute como administrador o seguinte comando para construir a imagem Docker:

$ docker build -t nome_da_sua_imagem .
Uma vez criada a imagem, para executar o container basta executar, como administrador, seguinte o comando:

$ docker run -d -p 8080:80 nome_da_sua_imagem
Uma vez executando, para acessar o front-end, basta abrir o http://localhost:8080/#/ no navegador.

### Versão

Versão 1.0.1 (abril/2024)
Exibe, insere, edita e exclui registros de praias com lixo.

### Autor

Este projeto foi desenvolvido por Marco Antonio de Souza e pode ser encontrado no gihub.
