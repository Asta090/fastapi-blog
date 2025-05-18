# Blog Application

A full-stack blog application with user authentication and CRUD operations.

## Project Structure

```
.
├── app/           # FastAPI backend
│   ├── core/         # Utility functions hashing,oauth2,token
│   |---db/           # DataBase Connection
|   |---models/       # Models
|   |---routers/      # Router Functions
|   |---schemas/      # Schemas(pydantic)
|   |---main.py/      # Main Function 
└── frontend/         # React frontend
|   ├── src/         # Source files
|   ├── package.json
|   └── vite.config.ts
└── requirements.txt
```

## Features

- User authentication (login/register)
- Create, read, and delete blog posts
- Dashboard view for all blogs
- Protected routes
- JWT-based authentication

## Tech Stack

### Backend
- FastAPI
- SQLModel (SQLAlchemy + Pydantic)
- JWT authentication
- SQLite database

### Frontend
- React
- TypeScript
- Vite
- Mantine UI
- React Router
- Axios

## Getting Started

### Backend Setup

1. Navigate to the project directory:
```bash
cd project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the backend server:
```bash
cd app
uvicorn blog.main:app --reload
```

The backend will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will run on `http://localhost:5173`

## API Endpoints

- `POST /login` - User login
- `POST /user` - User registration
- `GET /blog` - Get all blogs
- `POST /blog` - Create a new blog
- `DELETE /blog/{id}` - Delete a blog
- `GET /user/{id}` - Get user details

## Environment Variables

Frontend environment variables are managed through `.env` files. The following variables are required:

```env
VITE_API_URL=http://localhost:8000
```

## Authentication

The application uses JWT tokens for authentication. Upon successful login, a token is stored in localStorage and used for subsequent API requests.

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

MIT License
