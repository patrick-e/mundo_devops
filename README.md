#  Teste Mundo Devops

teste criado com o intuito de mostrar minhas habilidades com o python utilizando o framework Django REST

### Começando  
##### Requisitos
Antes de começar você precisa ter instalado os seguintes programas:
 - python3.8
 - pip
 - sqlite

##### Instalando as dependências do projeto 
dentro do diretório principal do projeto use o seguinte comando para instalar os módulos  necessários para a aplicação

    pip install -r requirements.txt

 
##### Configurando o banco de dados

O projeto foi criado utilizando o sqlite3 como banco de dados. Primeiramente é necessário criar um arquivo com o nome "db.sqlite3" dentro da raiz do projeto.

Com o arquivo criado vamos rodar a primeira migração do django com o seguinte comando no terminal:

    python manage.py migrate

Em seguida, vamos rodar a migração da model da api

    python manage.py makemigrations
    python manage.py migrate
Com as bases criadas subiremos o servidor

    python manage.py runserver
seu servidor estará rodando no endereço 127.0.0.1:8000
 
 ### Utilização da aplicação 
 para consuta de ip 
 

    http://127.0.0.1:8000/api/{ip}

Para verificar as consultas antigas 

     http://127.0.0.1:8000/data/
