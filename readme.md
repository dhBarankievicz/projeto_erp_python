🧩 Mini ERP Python — Integração com PostgreSQL

Projeto criado para estudar e praticar:

Conexão Python ↔ PostgreSQL

Estruturação de módulos

Operações básicas de CRUD (focado em usuários por enquanto)

O projeto não utiliza Flask, apenas scripts Python organizados em pastas.

📁 Estrutura do Projeto
```
Mini_ERP_python/
│
├── .gitignore
├── readme.md
├── Anotacoes.txt
│
├── Conexao_Python_SQL/
│   │   db.py                # Função central de conexão
│   │   test_conection.py    # Teste de conexão com o banco
│   │   __init__.py
│
├── CRUD/
│   ├── produtos/            # (vazio por enquanto)
│   └── usuarios/
|       |   delete_usuario.py
|       |   edit_usuario.py
│       │   insert_usuario.py
│       │   list_usuario.py
│       │   test_delete_usuario.py
│       │   test_edit_usuario.py
|       │   test_insert_usuario.py
│       │   test_list_usuario.py
│
└── __pycache__/             # ignorado pelo Git
```

🗄️ Banco de Dados
Tabela usuarios

Criada no PostgreSQL com interface + alguns ajustes manuais.

Campos:

Campo	Tipo	Observações
id	serial (PK)	gerado automaticamente
nome	varchar	
email	varchar	unique
senha	varchar	armazenada como texto
criado_em	timestamp without time zone	default now()
🔌 Conexão (psycopg2)

A pasta Conexao_Python_SQL contém:

db.py

Função get_connection()

Tenta abrir conexão usando seus parâmetros

Em caso de erro → captura via Exception e mostra no terminal

test_conection.py

Importa get_connection()

Testa se conecta

Fecha imediatamente se tudo OK

👤 CRUD — Usuários

Local: CRUD/usuarios/

Arquivo	Função
insert_usuario.py	Inserir novo usuário
list_usuario.py	Listar todos os usuários
test_insert_usuario.py	Testes simples da função de inserir
test_list_usuario.py	Testa listagem

As funções usam psycopg2, comandos SQL simples e o get_connection() do módulo principal.

▶️ Como executar
Instalar dependência
pip install psycopg2-binary

Testar conexão
python Conexao_Python_SQL/test_conection.py

Inserir usuário
python CRUD/usuarios/insert_usuario.py

Listar usuários
python CRUD/usuarios/list_usuario.py

📌 Status atual do projeto

✔ Conexão com PostgreSQL
✔ Teste de conexão
✔ CRUD básico de usuários (inserir, listar, editar e deletar)
✔ Estrutura organizada em pastas
✨ Preparando para expandir para “produtos”, “vendas”, etc.

🚀 Próximos Passos (planejados)

Adicionar update/delete de usuários

Criar CRUD de produtos

Validação de campos no Python

Organização mais modular (importações limpas)
