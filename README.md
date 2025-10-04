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

### 1. Yêu cầu

- Python 3.10+
- Pip & Venv (hoặc công cụ quản lý môi trường ảo khác như Poetry)
- MySQL Server đang hoạt động

### 2. Cài đặt

1.  **Clone repository:**
    ```bash
    git clone https://your-repository-url/Startup-kit-BE.git
    cd Startup-kit-BE
    ```

2.  **Tạo và kích hoạt môi trường ảo:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Trên Windows: venv\Scripts\activate
    ```

3.  **Cài đặt các thư viện cần thiết:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Cấu hình biến môi trường:**
    -   Tạo một file `.env` bằng cách sao chép từ file `.env.example`.
        ```bash
        cp .env.example .env
        ```
    -   Mở file `.env` và chỉnh sửa các giá trị cho phù hợp với môi trường của bạn (đặc biệt là `DATABASE_URL` và `SECRET_KEY`).

5.  **Chạy Database Migrations:**
    -   Mở file `alembic.ini` và chắc chắn rằng dòng `sqlalchemy.url` trỏ đúng đến biến môi trường của bạn hoặc chuỗi kết nối CSDL.
    -   Áp dụng tất cả các migrations để tạo bảng trong CSDL:
        ```bash
        alembic upgrade head
        ```

### 3. Khởi chạy Server

Chạy server với Uvicorn:
```bash
uvicorn src.main:app --reload
```
API sẽ có sẵn tại `http://127.0.0.1:8000`.

## Tài liệu API

Tài liệu chi tiết về tất cả các endpoint, bao gồm request body và response examples, có sẵn tại đây:

➡️ **[Tài liệu API chi tiết](./docs/API_DOCUMENTATION.md)**

Bạn cũng có thể truy cập tài liệu API tương tác (Swagger UI) do FastAPI tự động tạo ra tại: `http://0.0.0.0:8000/docs`

## Quản lý Database Migrations

Khi bạn thay đổi các models trong `src/database/models.py`, hãy tạo một migration mới:
```bash
alembic revision --autogenerate -m "Mô tả thay đổi của bạn"
```
Sau đó, áp dụng migration:
```bash
alembic upgrade head
```

## Đóng góp

Vui lòng tạo Pull Request nếu bạn có bất kỳ cải tiến nào.

## Giấy phép

Dự án này được cấp phép theo [Giấy phép MIT](LICENSE).
