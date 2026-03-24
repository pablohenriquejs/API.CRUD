# 🎮 API de Inventário de Jogos

## 📌 Sobre o Projeto

Esta API foi desenvolvida com o objetivo de gerenciar um inventário de jogos de forma simples e eficiente.
Com ela, é possível cadastrar novos jogos, consultar registros existentes, atualizar informações e remover itens do sistema.

O projeto segue o padrão REST e utiliza JSON para comunicação, sendo ideal para aplicações web e estudos de backend.

---

## 🔗 Repositório

https://github.com/pablohenriquejs/API.CRUD

---

## 🚀 Tecnologias Utilizadas

* Python 3
* Flask
* SQLite

---

## ⚙️ Como Executar

### 1. Clonar o repositório

```bash id="z4g8h0"
git clone https://github.com/pablohenriquejs/API.CRUD.git
cd API.CRUD
```

---

### 2. Criar ambiente virtual (recomendado)

```bash id="8kqzzi"
py -m venv venv
```

---

### 3. Ativar o ambiente

```bash id="cv9yxk"
venv\Scripts\activate
```

---

### 4. Instalar dependências

```bash id="c23g42"
pip install flask
```

---

### 5. Criar o banco de dados

```bash id="bxh64t"
python init_db.py
```

---

### 6. Executar a aplicação

```bash id="v4g9fj"
python CRUD.py
```

A API estará disponível em:

```id="v3g4ji"
http://127.0.0.1:5000
```

---

## 🔗 Endpoints

### 📥 Listar todos os jogos

```
GET /jogos
```

---

### 🔎 Buscar jogo por ID

```
GET /jogos/{id}
```

---

### ➕ Adicionar um novo jogo

```
POST /jogos
```

Exemplo de JSON:

```json id="zv9r7n"
{
  "nome": "Free Fire",
  "genero": "Battle Royale",
  "plataforma": "Mobile",
  "preco": 0
}
```

---

### ✏️ Atualizar um jogo

```
PUT /jogos/{id}
```

---

### ❌ Remover um jogo

```
DELETE /jogos/{id}
```

---

## 🧪 Testes com cURL

### Criar jogo

```bash id="3a8y4h"
curl -X POST http://127.0.0.1:5000/jogos -H "Content-Type: application/json" -d "{\"nome\":\"Free Fire\",\"genero\":\"Battle Royale\",\"plataforma\":\"Mobile\",\"preco\":0}"
```

---

### Listar jogos

```bash id="4k0a3g"
curl http://127.0.0.1:5000/jogos
```

---

### Atualizar jogo

```bash id="5y3d0q"
curl -X PUT http://127.0.0.1:5000/jogos/1 -H "Content-Type: application/json" -d "{\"nome\":\"Free Fire\",\"genero\":\"Battle Royale\",\"plataforma\":\"Mobile\",\"preco\":10}"
```

---

### Remover jogo

```bash id="c6b1r2"
curl -X DELETE http://127.0.0.1:5000/jogos/1
```

---

## 📊 Estrutura dos Dados

| Campo      | Tipo    | Descrição           |
| ---------- | ------- | ------------------- |
| id         | INTEGER | Identificador único |
| nome       | TEXT    | Nome do jogo        |
| genero     | TEXT    | Gênero do jogo      |
| plataforma | TEXT    | Plataforma do jogo  |
| preco      | REAL    | Valor do jogo       |

---

## 💡 Observações

* Projeto desenvolvido com foco educacional
* Estrutura simples para facilitar entendimento de APIs REST
* Pode ser expandido com autenticação, filtros e frontend

---

## 👨‍💻 Autor

**Pablo Henrique**
https://github.com/pablohenriquejs

---

## 📄 Licença

Uso acadêmico.
