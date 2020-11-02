# Desafio técnico da Celero

Este código trata-se da resolução para o desafio proposto pela Atados.
O desafio proposto baseia-se na construção de uma API que comporte a 
inclusão de voluntários e ações sociais.


## Getting Started

Para iniciar, realiza-se a clonagem do projeto na máquina local.
Após baixar o projeto, para executá-lo basta rodar o comando
```
docker-compose up
``` 
e então aguardar que o container docker suba, que logo então todas as 
rotas e acessos da api estarão disponíveis para uso.

### Pré-requisitos

- Python 3
- Django

### Instalação

## Deployment

Para testa o sistema de forma local, realiza-se primeiro a clonagem 
do projeto na máquina local.
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
rotas e acessos da api estarão disponíveis para uso. Elas são:

* **/api/v1/criar-usuario/ -** Para criar usuário que será utilizado 
em fins de adição de novas instâncias de ação e voluntário no sistema.
* **/api/v1/atletas/ -** Para ter acesso ao CRUD geral de atletas.
* **/api/v1/jogos/ -** Para ter acesso ao CRUD geral de jogos.
* **/api/v1/esportes/ -** Para ter acesso ao CRUD geral de esportes.
* **/api/v1/eventos/ -** Para ter acesso ao CRUD geral de eventos.

Os métodos referentes a listagem são de acesso livre, mas aqueles relacionados 
a criação e atualização de registros necessitam de um Token para serem realizados
devidamente. Para obter esse Token, basta criar um usuário pela rota de criação dos mesmos e, feito isso,
ir na rota de geração de Token, passando o username do usuário (e-mail) e a senha.
Para mais informações sobre as rotas, acesse a documentação do sistema pelo
[Postman](https://documenter.getpostman.com/view/4328408/TVYM3F2J#ece5a9ba-24b6-46de-b3bd-718442e75b23).

## Executanto os testes

Para executar os testes, antes é preciso o projeto esteja devidamente configurado em sua máquina. Feito isso, os 
testes poderão ser executados nas seguintes formas:

* **Todos disponíveis -** _python manage.py test --pattern="test\_*.py"_ ou apenas _python manage.py test tests_
* **Por módulo -** _python manage.py test tests.autenticacao_
* **Individual -** _python manage.py test tests.autenticacao.test_api_

### Explicação dos testes

Os testes feitos tem como base avaliar o CRUD geral das 
rotas da aplicação, também verificando se as regras e políticas de 
cada uma delas está sendo seguida devidamente.


## Diagramas desenvolvidos para estabelecer a lógica de desenvolvimento dos models da api:

### Diagrama de Classe
![Diagrama de Classe](/utils/diagrama_classe.jpeg)

### Diagrama de Objeto
![]()

## Feito com

* [Django](https://www.djangoproject.com/) - Framework web escolhido para realização do desafio
* [Django Rest Framework](https://www.djangoproject.com/) - Framework web para gerenciamento da API
* [Python](https://www.python.org/) - Linguagem de programação utilizada

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
