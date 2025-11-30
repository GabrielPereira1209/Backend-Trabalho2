# Backend - Sistema de Gerenciamento de Locação de Vagas

## Descrição do Projeto

Este backend foi desenvolvido em Django para gerenciar um sistema de locação de vagas. O sistema permite o cadastro de usuários, vagas e reservas, além de autenticação e autorização de usuários. O projeto implementa as operações CRUD para todas as entidades principais e conta com endpoints protegidos, documentação via Swagger e diferentes visões para usuários autenticados.

## Escopo do Site

- Cadastro, listagem, atualização e remoção de usuários, vagas e reservas (CRUD completo).
- Autenticação de usuários (login/logout).
- Endpoints protegidos para operações.
- Endpoints liberados como registrar e login.
- Documentação automática dos endpoints via Swagger.

## Manual do Usuário

1. **Instalação**
	 - Clone o repositório:
		 git clone [URL_DO_REPOSITORIO]
		 cd Backend-Trabalho2

	 - Crie e ative um ambiente virtual:
		 python3 -m venv venv
		 source venv/bin/activate

	 - Instale as dependências:
		 pip install -r requirements.txt

	 - Aplique as migrações:
		 python manage.py migrate

	 - Crie um superusuário (opcional, para acessar o admin):
		 python manage.py createsuperuser

	 - Inicie o servidor:
		 python manage.py runserver

2. **Uso**
	 - Acesse a API em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
	 - Acesse a documentação Swagger em: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
	 - Pode utilizar o próprio swagger para testar as APIs.

## O que funcionou

- CRUD completo para usuários, vagas e reservas.
- Autenticação e autorização de usuários.
- Endpoints protegidos.
- Documentação Swagger acessível e funcional.
