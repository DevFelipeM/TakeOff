 Descrição
API de registro e autenticação de usuários desenvolvida em Python com Flask, incluindo:

Registro de usuários (username, email e senha)

Login com geração de token JWT

Endpoints protegidos por autenticação

Armazenamento seguro de senhas com bcrypt

🛠️ Tecnologias
Python 3.x

Flask

Flask-SQLAlchemy (banco de dados SQLite)

Flask-JWT-Extended (autenticação JWT)

Bcrypt (hash de senhas)

Marshmallow (validação e serialização)

⚙️ Configuração
Pré-requisitos
Python 3.8+

🚀 Endpoints
Autenticação
POST /register - Registra um novo usuário

POST /login - Faz login e retorna token JWT

Usuários
GET /users - Lista todos os usuários (para testes)

GET /protected - Exemplo de endpoint protegido

🛡️ Segurança
Senhas armazenadas como hash bcrypt

Tokens JWT com expiração

Validação de entrada

CORS configurado

🤝 Contribuição
Faça um fork do projeto

Crie uma branch (git checkout -b feature/nova-feature)

Commit suas mudanças (git commit -m 'Adiciona nova feature')

Push para a branch (git push origin feature/nova-feature)

Abra um Pull Request
