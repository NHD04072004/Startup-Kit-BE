<div align="center">

# Startup Investment Platform API

RESTful backend xây dựng bằng FastAPI để kết nối startup, nhà đầu tư, mentor và admin thông qua lớp xác thực và quản lý người dùng an toàn. Tài liệu này tập trung vào cách thiết lập và phát triển backend trong môi trường local.

</div>

## Mục lục

- [Tổng quan](#tổng-quan)
- [Tính năng](#tính-năng)
- [Công nghệ sử dụng](#công-nghệ-sử-dụng)
- [Cấu trúc dự án](#cấu-trúc-dự-án)
- [Bắt đầu](#bắt-đầu)
  - [Pre-requirement](#prerequirement)
  - [Cài đặt](#cài-đặt)
  - [Biến môi trường](#biến-môi-trường)
  - [Migration cơ sở dữ liệu](#migration-cơ-sở-dữ-liệu)
  - [Chạy ứng dụng](#chạy-ứng-dụng)
- [Phát triển nội bộ](#phát-triển-nội-bộ)
  - [Tài liệu API tương tác](#tài-liệu-api-tương-tác)
  - [Tạo migration mới](#tạo-migration-mới)
  - [Làm việc với cơ sở dữ liệu](#làm-việc-với-cơ-sở-dữ-liệu)
  - [Khắc phục sự cố](#khắc-phục-sự-cố)
- [Tài liệu API](#tài-liệu-api)
- [Ghi chú triển khai](#ghi-chú-triển-khai)
- [Các bước tiếp theo](#các-bước-tiếp-theo)

## Tổng quan

Startup Investment Platform API cung cấp nền tảng để giúp các startup có thể xây dựng hồ sơ ý tưởng đồng thời kết nối với các nhà đầu tư cùng với các bên khác như: mentor, các bên tổ chức cuộc thi khởi nghiệp.

## Tính năng

- Đăng ký người dùng kèm phân quyền (startup, investor, mentor, admin).

## Công nghệ sử dụng

- **Ngôn ngữ:** Python 3.12+
- **Framework:** FastAPI, Starlette
- **ORM:** SQLAlchemy 2.x
- **Auth:** OAuth2 + JWT (thông qua `python-jose`)
- **Database:** MySQL (sử dụng `mysql-connector-python`) — có thể thay `DATABASE_URL` sang driver tương thích khác của SQLAlchemy nếu cần.
- **Migration:** Alembic
- **Quản lý biến môi trường:** `python-dotenv`, `pydantic-settings`

## Cấu trúc dự án

```
.
├── alembic/                 # Alembic configuration & 
│   └── versions/
├── main.py                  # FastAPI app entrypoint
├── requirements.txt         # Python dependencies
├── src/
│   ├── auth/                # Authentication routers, schemas, 
│   ├── core/                # Config & security utilities
│   ├── database/            # DB engine, session, and models
│   └── users/               # User-facing routers, schemas
└── README.md
```

## Bắt đầu

### Yêu cầu

- Python 3.12 trở lên
- MySQL 8.x (hoặc tương thích) chạy local hoặc có thể truy cập từ xa
- PowerShell (Windows) hoặc shell tương thích POSIX

### Cài đặt

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

### Biến môi trường

Tạo file `.env` ở thư mục gốc dự án với cấu hình tối thiểu:

```
DATABASE_URL=mysql+mysqlconnector://username:password@localhost:3306/startup_db
SECRET_KEY=change-me
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Hoặc

```
cp .env.example .env
```

- `DATABASE_URL` phải đúng định dạng URL của SQLAlchemy. Tùy chỉnh driver, thông tin đăng nhập, host và tên database theo môi trường.
- `SECRET_KEY` nên là chuỗi dài, ngẫu nhiên. Hãy thay đổi định kỳ trong môi trường production nếu bị lộ.

### Migration cơ sở dữ liệu

Áp dụng schema mới nhất vào cơ sở dữ liệu:

```powershell
alembic upgrade head
```

### Chạy ứng dụng

```powershell
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Sau khi chạy, tài liệu API tương tác có tại [http://localhost:8000/docs](http://localhost:8000/docs).

## Phát triển nội bộ

### Tài liệu API tương tác

- Truy cập `/docs` (Swagger UI) hoặc `/redoc` để xem tài liệu trực tuyến và thử nghiệm thủ công.
- Với endpoint được bảo vệ, bấm **Authorize** và dán bearer token lấy từ `/auth/token`.

### Tạo migration mới

Khi chỉnh sửa model trong `src/database/models.py`, tạo migration mới:

```powershell
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

Hãy xem lại script migration trước khi áp dụng để đảm bảo thay đổi schema chính xác.

### Làm việc với cơ sở dữ liệu

- Ứng dụng yêu cầu MySQL đang chạy và truy cập được theo `DATABASE_URL`.
- Trong môi trường local, có thể dùng bất kỳ MySQL client nào để kiểm tra bảng hoặc mở Python shell tương tác:

```python
from src.database.core import SessionLocal
from src.database.models import User

with SessionLocal() as session:
    users = session.query(User).all()
    print(users)
```

### Khắc phục sự cố

- **401 “Could not validate credentials” khi gọi `/users/me`:** kiểm tra header `Authorization` đúng định dạng `Bearer <access_token>`.
- **Không kết nối được cơ sở dữ liệu:** xác nhận `DATABASE_URL`, database đã tồn tại và user có quyền truy cập. Sau khi tạo database mới hãy chạy `alembic upgrade head`.
- **Lỗi độ dài mật khẩu:** dịch vụ auth từ chối mật khẩu dài hơn 72 ký tự để tương thích với bcrypt.

## Tài liệu API

### Xác thực

#### Đăng ký người dùng

- **Endpoint:** `POST /auth/register`
- **Body:**

```json
{
    "full_name": "Ada Lovelace",
    "email": "ada@example.com",
    "password": "supersecret",
    "password_confirm": "supersecret",
    "role": "investor"
}
```

#### Lấy access token

- **Endpoint:** `POST /auth/token`
- **Form data:**
  - `username`: email người dùng
  - `password`: mật khẩu dạng plaintext

Ví dụ request:

```powershell
Invoke-RestMethod -Method Post -Uri "http://localhost:8000/auth/token" -Body @{ username = "ada@example.com"; password = "supersecret" } -ContentType "application/x-www-form-urlencoded"
```

Response:

```json
{
    "access_token": "<jwt>",
    "token_type": "bearer"
}
```

### Người dùng

#### Lấy thông tin người dùng hiện tại

- **Endpoint:** `GET /users/me`
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:** schema `UserRead` gồm id, full_name, email, role và timestamp.

## Ghi chú triển khai

- Mật khẩu được hash bằng bcrypt thông qua `passlib`. Không lưu mật khẩu dạng plaintext.
- Thời hạn JWT được điều khiển bởi `ACCESS_TOKEN_EXPIRE_MINUTES` (mặc định 30). Điều chỉnh tùy nhu cầu triển khai.
- Khi thêm model hoặc field mới, tạo migration Alembic (`alembic revision --autogenerate -m "message"`) và áp dụng.
- Mặc định dự án cho phép tất cả origin qua CORS. Hạn chế lại trước khi đưa vào production.

## Các bước tiếp theo

- Bổ sung automated test (ví dụ pytest) cho flow xác thực và các route bảo vệ.
- Phát triển thêm tính năng domain: hồ sơ startup, cơ hội đầu tư, gợi ý mentor.
- Tăng cường bảo mật bằng HTTPS, cấu hình rate limiting và tích hợp monitoring/logging.

---

Cần hỗ trợ hoặc có ý tưởng mở rộng nền tảng? Hãy tạo issue hoặc gửi pull request!
