# Desafio técnico da Celero

Este código trata-se da resolução para o desafio proposto pela Celero.
O desafio proposto baseia-se na construção de uma API que comporte a 
inclusão de atletas, eventos e jogos, segundo o modelo estabelecido em 
[“120 years of Olympic history: athletes and results”](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results#athlete_events.csv) 
do Kaggle, e que aceite também fazer a importação de dados via arquivo CSV nesse mesmo padrão.


## Getting Started

Para iniciar, realiza-se a clonagem do projeto na máquina local.

### Pré-requisitos

- Python 3
- Django
- k6

### Instalação
O k6 será utilizado para rodar os testes na API, como será melhor visto mais abaixo.
Para instalar o k6 basta [baixar o binário](https://github.com/loadimpact/k6/releases) para o seu
sistema operacional (Windows, Linux ou Mac).

## Deployment

Após baixar o projeto, os seguintes passos devem ser devidamente seguidos:
1. Criar um ambiente virtual com Python;
2. Dentro do ambiente virtual, executar: 
```
pip install -r requirements.txt
``` 
3. Criar um arquivos settings.ini e colocá-lo no mesmo nível do settings.py. 
Esse arquivo deve conter:
```
DEBUG
SECRET_KEY
ALLOWED_HOSTS
DATABASE_DEV_URL
```

E então, com as configurações feitas, todas as 
rotas e acessos da api estarão disponíveis para uso, 
bastando rodar o comando:
```
python manage.py runserver
```
Para que o projeto comece a rodar em sua máquina local.
As principais rotas presentes na api são:

* **/api/v1/criar-usuario/ -** Para criar usuário que será utilizado 
em fins de adição de novas instâncias de ação e voluntário no sistema.
* **/api/v1/atletas/ -** Para ter acesso ao CRUD geral de atletas.
* **/api/v1/jogos/ -** Para ter acesso ao CRUD geral de jogos.
* **/api/v1/esportes/ -** Para ter acesso ao CRUD geral de esportes.
* **/api/v1/eventos/ -** Para ter acesso ao CRUD geral de eventos.
* **/import/upload/ -** Para fazer upload de um arquivo CSV que servirá no 
povoamento dos models cadastrados.

Os métodos referentes a listagem são de acesso livre, mas aqueles relacionados 
a criação e atualização de registros necessitam de um Token para serem realizados
devidamente. Para obter esse Token, basta criar um usuário pela rota de criação dos mesmos e, feito isso,
ir na rota de geração de Token, passando o username do usuário (e-mail) e a senha.
Para mais informações sobre as rotas, acesse a documentação do sistema pelo
[Postman](https://documenter.getpostman.com/view/4328408/TVYM3F2J#ece5a9ba-24b6-46de-b3bd-718442e75b23).

## Executanto os testes

Para executar os testes, antes é preciso o projeto esteja devidamente configurado em sua máquina e 
que além disso você tenha o k6 instalado. Feito isso, os 
testes poderão ser executados da seguinte forma:
```
k6 run -e API_BASE='http://0.0.0.0:8000' tests-open.js  
```
Observando-se que para que os testes sejam executados, 
é preciso que o servidor já esteja rodando localmente.

### Explicação dos testes

Os testes feitos tem como base avaliar o CRUD geral das 
rotas da aplicação, também verificando se as regras e políticas de 
cada uma delas está sendo seguida devidamente.


## Diagramas desenvolvidos para estabelecer a lógica de desenvolvimento dos models da API:

### Diagrama de Classes
![Diagrama de Classe](/utils/diagrama_classes.jpeg)

### Diagrama de Objetos
![Diagrama de Objetos](/utils/diagrama_objetos.jpeg)

## Versão online
Para fazer um teste online dessa api, pode-se acessar a versão dela que está disponível no [Heroku](https://desafio-celero.herokuapp.com/).

## Feito com

* [Django](https://www.djangoproject.com/) - Framework web escolhido para realização do desafio
* [Django Rest Framework](https://www.djangoproject.com/) - Framework web para gerenciamento da API
* [Python](https://www.python.org/) - Linguagem de programação utilizada

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
