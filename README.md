# 🌙 Late Show API

A Flask REST API to manage a Late Night TV show system with users, guests, episodes, and appearances.

## 📦 Tech Stack

* Flask
* PostgreSQL
* SQLAlchemy + Migrations
* JWT Authentication
* Postman (for testing)

## 📁 Project Structure

```
server/
├── app.py
├── config.py
├── seed.py
├── models/
├── controllers/
```

## ⚙️ Setup Instructions

### 1. Clone & Install

```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
pipenv install 
pipenv shell
```

### 2. PostgreSQL Setup

```sql
CREATE DATABASE late_show_db;
```

In `server/config.py`, update:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://<username>:<password>@localhost:5432/late_show_db"
```

### 3. Initialize Database

```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

### 4. Run the App

```bash
flask run
```

---

## 🔐 Authentication Flow

* Register → `POST /register` with `{ "username": "yourname", "password": "yourpass" }`
* Login → `POST /login` returns JWT token
* Use JWT in headers:
  `Authorization: Bearer <token>`

---

## 🧪 API Routes

| Method | Route            | Auth? | Description                  |
| ------ | ---------------- | ----- | ---------------------------- |
| POST   | `/register`      | ❌     | Register a new user          |
| POST   | `/login`         | ❌     | Log in and get token         |
| GET    | `/episodes`      | ❌     | List all episodes            |
| GET    | `/episodes/<id>` | ❌     | Get episode + appearances    |
| DELETE | `/episodes/<id>` | ✅     | Delete episode + appearances |
| GET    | `/guests`        | ❌     | List all guests              |
| POST   | `/appearances`   | ✅     | Create a new appearance      |

---

## 📬 Sample Requests

### Register

```http
POST /register
Content-Type: application/json

{
  "username": "jane",
  "password": "password123"
}
```

### Login

```http
POST /login
Content-Type: application/json

{
  "username": "jane",
  "password": "password123"
}
```

Response:

```json
{ "token": "<jwt_token>" }
```

### Protected Request Example

```http
POST /appearances
Authorization: Bearer <jwt_token>
Content-Type: application/json

{
  "rating": 4,
  "guest_id": 1,
  "episode_id": 1
}
```

---

## 🧪 Postman Testing

1. Open Postman
2. Import: `challenge-4-lateshow.postman_collection.json`
3. Test:

   * Register and Login
   * Copy JWT token
   * Set in Authorization tab → Bearer Token
   * Test protected routes (`POST /appearances`, `DELETE /episodes/<id>`)

---

