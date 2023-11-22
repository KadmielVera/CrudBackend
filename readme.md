to run in your device

cmd on this file directory
py -m venv venv
.\venv\scripts\activate
cd..
cd..
py manage.py runserver


Pass to 
localhost:8000/admin
user: admin
pass: admin


POST:

 

[

    {

        "nome_responsavel":"teste",

        "nome_empresa":"sim",

        "email":teste@gmail.com,

        "telefone":"123456789",

        "cep":"123456789",

        "endereco":"rua sim",

        "cidade":"cidade sim",

        "estado":"estado sim",

        "seja":"Contratador"

    }

]


PUT:

 

{

    "nome_responsavel": "sim",

    "nome_empresa": "sim",

    "email": teste@gmail.com,

    "telefone": "123456789",

    "cep": "123456789",

    "endereco": "rua sim",

    "cidade": "cidade sim",

    "estado": "estado sim",

    "seja": "Contratador"

}
