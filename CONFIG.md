# CONFIGURAÇÕES DO AMBIENTE


- [INTRODUÇÃO](#introducao)
- [PREPARANDO O AMBIENTE](#preparando-o-ambiente)
- [OPCIONAL - CONFIGURAÇÕES ADICIONAIS DO VS CODE](#opcional-configuracoes-adicionais-do-vs-code)

# INTRODUÇÃO

Configuração para trabalhar com `Django`

# PREPARANDO O AMBIENTE

Criando o ambiente virtual do Python:

```sh
$ python3 -m venv ./venv
```

Para carregar o ambiente virtual use o comando:

```sh
$ source $path/venv/bin/activate
```

Instale o `Django`:
```sh
$ pip install django
```

Para saber se o `Django` foi instalado corretamente use o comando:
```sh
$ pip freeze
```

Para criar o projeto com `Django` use o comando abaixo:
```sh
$ django-admin startproject alurareceita .
```

Sobre os arquivos:

```
introduction-to-django
.
├── alurareceita
│   ├── asgi.py
│   ├── __init__.py # indica do Django que se trata de um pacote
│   ├── settings.py # indica as principais configurações do projeto
│   ├── urls.py # indica onde estão todas as urls do projeto
│   └── wsgi.py # ponto de integração para servidores web compativeis
├── CHANGELOG.md
├── CONFIG.md
├── manage.py
└── README.md

```

# OPCIONAL - CONFIGURAÇÕES ADICIONAIS DO VS CODE

N/A
