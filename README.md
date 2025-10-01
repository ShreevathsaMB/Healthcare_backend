# Healthcare Management API

A comprehensive Django REST API for managing healthcare data including patients, doctors, and their relationships.

## 🏥 Features

- **User Authentication** - JWT-based registration and login
- **Patient Management** - CRUD operations for patient records
- **Doctor Management** - CRUD operations for doctor profiles
- **Patient-Doctor Mapping** - Assign and manage doctor-patient relationships
- **PostgreSQL Database** - Robust data storage
- **RESTful API** - Clean, standardized endpoints

## 🛠️ Tech Stack

- **Backend**: Django 4.2.24 + Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Environment**: Python 3.9+

## 📋 API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - User login (returns JWT)
- `POST /api/auth/token/refresh/` - Refresh JWT token

### Patients
- `GET /api/patients/` - List user's patients
- `POST /api/patients/` - Create new patient
- `GET /api/patients/<id>/` - Get patient details
- `PUT /api/patients/<id>/` - Update patient
- `DELETE /api/patients/<id>/` - Delete patient

### Doctors
- `GET /api/doctors/` - List all doctors
- `POST /api/doctors/` - Create new doctor
- `GET /api/doctors/<id>/` - Get doctor details
- `PUT /api/doctors/<id>/` - Update doctor
- `DELETE /api/doctors/<id>/` - Delete doctor

### Patient-Doctor Mappings
- `GET /api/mappings/` - List all mappings
- `POST /api/mappings/` - Assign doctor to patient
- `DELETE /api/mappings/<id>/` - Remove assignment

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- PostgreSQL
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/healthcare-api.git
   cd healthcare-api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL**
   ```sql
   CREATE DATABASE healthcare_db;
   CREATE USER healthcare_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO healthcare_user;
   ```

5. **Configure environment variables**
   Create `.env` file:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
   DATABASE_NAME=healthcare_db
   DATABASE_USER=healthcare_user
   DATABASE_PASSWORD=your_password
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start server**
   ```bash
   python manage.py runserver
   ```

## 📖 Usage Examples

### Register User
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123","name":"John Doe"}'
```

### Login
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'
```

### Create Doctor
```bash
curl -X POST http://127.0.0.1:8000/api/doctors/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"name":"Dr. Smith","specialty":"Cardiology","email":"dr.smith@hospital.com"}'
```

### Create Patient
```bash
curl -X POST http://127.0.0.1:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"name":"Jane Doe","age":30,"gender":"F","medical_history":"No allergies"}'
```

## 🔐 Security Features

- JWT token authentication
- User-specific patient data access
- Password validation
- Environment variable configuration
- CORS protection ready

## 🌐 Admin Interface

Access Django admin at `http://127.0.0.1:8000/admin/` to manage data through web interface.

## 📁 Project Structure

```
healthcare_backend/
├── backend/          # Django project settings
├── core/            # Main application
│   ├── models.py    # Database models
│   ├── views.py     # API views
│   ├── serializers.py # Data serializers
│   ├── urls.py      # URL routing
│   └── admin.py     # Admin configuration
├── requirements.txt # Dependencies
├── manage.py       # Django management
└── .env           # Environment variables
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Shreevathsa** - [GitHub Profile](https://github.com/yourusername)

---

⭐ **Star this repo if you found it helpful!**