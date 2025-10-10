# Startup Kit - Backend API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Backend API cho nền tảng Startup Kit, được xây dựng để kết nối các Founder, Nhà đầu tư và Mentor trong hệ sinh thái khởi nghiệp Việt Nam.

## Giới thiệu

Startup Kit là một nền tảng nhằm hỗ trợ các Founder và đội ngũ khởi nghiệp bằng cách:
- Giúp tạo hồ sơ khởi nghiệp chuyên nghiệp với sự hỗ trợ của AI.
- Cung cấp các mẫu hồ sơ đa dạng, tùy chỉnh dễ dàng.
- Kết nối Startup với Nhà đầu tư và Mentor, rút ngắn khoảng cách và mở rộng cơ hội.
- Ứng dụng công nghệ blockchain để bảo mật dữ liệu và đăng ký bản quyền ý tưởng.

## Tính năng chính

- **Xác thực an toàn**: Đăng ký, đăng nhập sử dụng JWT (JSON Web Tokens).
- **Quản lý người dùng**: Tạo tài khoản theo vai trò (Founder, Investor, Mentor), xem và cập nhật thông tin cá nhân.
- **Bảo mật**: Đổi mật khẩu, vô hiệu hóa tài khoản (xóa mềm).
- **Quản lý Hồ sơ**: Xem và cập nhật hồ sơ cá nhân chi tiết.
- **Kiến trúc Module hóa**: Dễ dàng bảo trì và mở rộng các tính năng mới (Quản lý dự án, Kết nối, Tin nhắn,...).

## Công nghệ sử dụng

- **Framework**: FastAPI
- **ORM**: SQLAlchemy 2.0
- **Database**: MySQL (tương thích với PostgreSQL, SQLite)
- **Migrations**: Alembic
- **Data Validation**: Pydantic
- **Authentication**: JWT & Passlib
- **Package Manager**: UV (Astral) - Python package manager cực nhanh

## Cấu trúc dự án

```
.
└── Startup-kit-BE/
    ├── alembic/
    ├── docs/
    │   └── API_DOCUMENTATION.md
    ├── src/
    │   ├── auth/         # Logic xác thực và JWT
    │   ├── core/         # Cấu hình chung và bảo mật
    │   ├── database/     # Models và kết nối CSDL
    │   └── users/        # APIs và services cho người dùng
    ├── .env
    ├── .env.example
    ├── alembic.ini
    └── main.py
```

## Hướng dẫn cài đặt và khởi chạy

### Phương pháp 1: Sử dụng UV (Khuyến nghị) ⚡

**Yêu cầu:**
- Python 3.12+
- UV package manager
- MySQL Server đang hoạt động

**1. Cài đặt UV:**

- Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

- macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Hoặc với pip:

```bash
pip install uv
```

**2. Clone repository:**
```bash
git clone https://github.com/NHD04072004/Startup-Kit-BE.git
cd Startup-Kit-BE
```

**3. Cài đặt dependencies:**
```bash
# UV tự động tạo virtual environment và cài đặt dependencies
uv sync
```

**4. Cấu hình biến môi trường:**
```bash
cp .env.example .env

# Chỉnh sửa .env với thông tin của bạn
```

**5. Chạy migrations:**
```bash
uv run alembic upgrade head
```

**6. Khởi chạy server:**
```bash
uv run main.py

# Hoặc sử dụng uvicorn
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API sẽ chạy tại `http://0.0.0.0:8000`

---

### Phương pháp 2: Sử dụng Docker 🐳

**Yêu cầu:**
- Docker Engine 20.10+
- Docker Compose 2.0+

**Khởi chạy nhanh:**

```bash
# 1. Copy và cấu hình file môi trường
cp .env.example .env

# 2. Chỉnh sửa .env với thông tin của bạn
# 3. Build và khởi chạy containers
docker-compose up -d

# 4. Ứng dụng sẽ chạy tại http://localhost:8000
```

**Xem logs:**
```bash
docker-compose logs -f app
```

**Chạy migrations:**
```bash
docker-compose exec app alembic upgrade head
```

**Dừng ứng dụng:**
```bash
docker-compose down
```

📖 **Chi tiết đầy đủ**: Xem [DOCKER_GUIDE.md](./DOCKER_GUIDE.md) để biết thêm về development mode, production mode, và best practices.

---

### Phương pháp 3: Cài đặt truyền thống với pip

**Yêu cầu:**
- Python 3.12+
- Pip & Venv
- MySQL Server đang hoạt động

**1. Clone repository:**
```bash
git clone https://github.com/NHD04072004/Startup-Kit-BE.git
cd Startup-Kit-BE
```

**2. Tạo và kích hoạt môi trường ảo:**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Cài đặt dependencies:**
```bash
pip install -r requirements.txt
```

**4. Cấu hình môi trường:**
```bash
cp .env.example .env
# Chỉnh sửa .env với thông tin của bạn
```

**5. Chạy migrations:**
```bash
alembic upgrade head
```

**6. Khởi chạy server:**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API sẽ chạy tại `http://localhost:8000`

## Tài liệu API

Tài liệu chi tiết về tất cả các endpoint, bao gồm request body và response examples, có sẵn tại đây:

➡️ **[Tài liệu API chi tiết](./docs/API_DOCUMENTATION.md)**

Bạn cũng có thể truy cập tài liệu API tương tác (Swagger UI) do FastAPI tự động tạo ra tại: `http://0.0.0.0:8000/docs`

## Quản lý Database Migrations

Khi bạn thay đổi các models trong `src/database/models.py`, hãy tạo một migration mới:

**Với UV:**
```bash
uv run alembic revision --autogenerate -m "Mô tả thay đổi của bạn"
uv run alembic upgrade head
```

**Với pip/venv truyền thống:**
```bash
alembic revision --autogenerate -m "Mô tả thay đổi của bạn"
alembic upgrade head
```

## Đóng góp

Vui lòng tạo Pull Request nếu bạn có bất kỳ cải tiến nào.

## Giấy phép

Dự án này được cấp phép theo [Giấy phép MIT](LICENSE).
