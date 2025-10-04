# Tài liệu API - Startup Kit

Chào mừng đến với tài liệu API của Startup Kit. API này tuân thủ theo tiêu chuẩn RESTful.

**Base URL**: `http://127.0.0.1:8000`

Tất cả các endpoint yêu cầu xác thực đều phải có header `Authorization: Bearer <YOUR_ACCESS_TOKEN>`.

---

## 1. Authentication

Các endpoint dùng để đăng ký và đăng nhập.

### **`POST /auth/register`**

Tạo một tài khoản người dùng mới.

**Request Body:**
```json
{
  "full_name": "Nguyen Van A",
  "email": "a.nguyen@example.com",
  "password": "strongpassword123",
  "password_confirm": "strongpassword123",
  "role": "founder"
}
```
* `role` có thể là một trong các giá trị: `founder`, `investor`, `mentor`, `admin`.

**Success Response (201 Created):**
```json
{
  "id": 1,
  "full_name": "Nguyen Van A",
  "email": "a.nguyen@example.com",
  "role": "founder",
  "is_active": true,
  "created_at": "2025-10-04T20:36:00.000Z",
  "profile": {
    "user_id": 1,
    "avatar_url": null,
    "bio": null,
    "website_url": null,
    "location": null
  }
}
```

**Error Responses:**
- `400 Bad Request`: Email đã tồn tại hoặc mật khẩu không khớp.

---

### **`POST /auth/token`**

Đăng nhập để nhận Access Token (JWT). Request body phải ở dạng `form-data`.

**Request Form Data:**
- `username`: Email của người dùng.
- `password`: Mật khẩu của người dùng.

**Success Response (200 OK):**

```json
{
  "access_token": "ey...",
  "token_type": "bearer"
}
```

**Error Responses:**
- `401 Unauthorized`: Sai email hoặc mật khẩu.
- `400 Bad Request`: Tài khoản người dùng đã bị vô hiệu hóa.

---

## 2. Users

Các endpoint để quản lý thông tin người dùng.

### **`GET /users/me`**

Lấy thông tin chi tiết của người dùng đang đăng nhập.

**Authentication:** Required (Bearer Token)

**Success Response (200 OK):**
```json
{
  "id": 1,
  "full_name": "Nguyen Van A",
  "email": "a.nguyen@example.com",
  "role": "founder",
  "is_active": true,
  "created_at": "2025-10-04T20:36:00.000Z",
  "profile": {
    "user_id": 1,
    "avatar_url": "https://example.com/avatar.jpg",
    "bio": "Founder of Startup X.",
    "website_url": "https://startupx.com",
    "location": "Hanoi, Vietnam"
  }
}
```

---

### **`PATCH /users/me`**

Cập nhật thông tin cá nhân của người dùng đang đăng nhập. Chỉ cần gửi những trường bạn muốn thay đổi.

**Authentication:** Required (Bearer Token)

**Request Body:**```json
{
  "full_name": "Nguyen Van A Updated",
  "bio": "Founder of Startup X. We are changing the world!",
  "location": "Ho Chi Minh City, Vietnam"
}```

**Success Response (200 OK):**
*   Trả về object người dùng đã được cập nhật, tương tự như `GET /users/me`.

---

### **`PUT /users/me/password`**

Thay đổi mật khẩu của người dùng đang đăng nhập.

**Authentication:** Required (Bearer Token)

**Request Body:**
```json
{
  "current_password": "strongpassword123",
  "new_password": "newstrongerpassword456",
  "new_password_confirm": "newstrongerpassword456"
}
```

**Success Response (200 OK):**
```json
{
  "message": "Password updated successfully"
}
```

**Error Responses:**
- `400 Bad Request`: Mật khẩu mới không khớp hoặc mật khẩu hiện tại không đúng.

---

### **`DELETE /users/me`**

Vô hiệu hóa (xóa mềm) tài khoản của người dùng đang đăng nhập.

**Authentication:** Required (Bearer Token)

**Success Response (200 OK):**
```json
{
  "message": "Account deactivated successfully"
}
```
