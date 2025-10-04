# Tài liệu API - Startup Kit

Chào mừng đến với tài liệu API của Startup Kit. API này tuân thủ theo tiêu chuẩn RESTful và sử dụng WebSocket cho các tính năng thời gian thực.

**Base URL**: `http://0.0.0.0:8000`

Tất cả các endpoint RESTful yêu cầu xác thực đều phải có header `Authorization: Bearer <YOUR_ACCESS_TOKEN>`. WebSocket yêu cầu token qua query parameter.

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

**Request Body:**
```json
{
  "full_name": "Nguyen Van A Updated",
  "bio": "Founder of Startup X. We are changing the world!",
  "location": "Ho Chi Minh City, Vietnam"
}
```

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

---

## 3. Projects (REST API)

Các endpoint để tạo và quản lý dự án khởi nghiệp.

### **`POST /projects`**

Tạo một dự án khởi nghiệp mới. Endpoint này sẽ tự động tạo ra các section mặc định cho dự án (Pitch Deck, BMC,...).

**Authentication:** Required (Bearer Token)
**Permissions:** Chỉ người dùng có vai trò `founder` mới có thể tạo.

**Request Body:**
```json
{
  "name": "Dự án AI Phân tích Thị trường",
  "tagline": "Sử dụng AI để đưa ra quyết định kinh doanh thông minh.",
  "stage": "idea"
}
```
* `stage` có thể là một trong các giá trị: `idea`, `prototype`, `seed`, `series_a`.

**Success Response (201 Created):**
```json
{
    "id": 1,
    "founder_id": 1,
    "name": "Dự án AI Phân tích Thị trường",
    "tagline": "Sử dụng AI để đưa ra quyết định kinh doanh thông minh.",
    "stage": "idea",
    "created_at": "2025-10-05T10:00:00Z",
    "updated_at": "2025-10-05T10:00:00Z",
    "sections": [
        {
            "id": 1,
            "type": "PITCH_DECK",
            "title": "Pitch Deck",
            "content": {},
            "file_url": null,
            "updated_at": "2025-10-05T10:00:00Z"
        },
        {
            "id": 2,
            "type": "BUSINESS_MODEL_CANVAS",
            "title": "Business Model Canvas (BMC)",
            "content": {},
            "file_url": null,
            "updated_at": "2025-10-05T10:00:00Z"
        }
    ]
}
```

**Error Responses:**
- `403 Forbidden`: Người dùng không phải là `founder`.

---

### **`GET /projects`**

Lấy danh sách tất cả các dự án của người dùng đã đăng nhập.

**Authentication:** Required (Bearer Token)

**Success Response (200 OK):**
*   Trả về một mảng các đối tượng dự án, có cấu trúc tương tự response của `POST /projects`.

---

### **`GET /projects/{project_id}`**

Lấy thông tin chi tiết của một dự án cụ thể.

**Authentication:** Required (Bearer Token)

**Path Parameter:**
- `project_id` (integer): ID của dự án cần xem.

**Success Response (200 OK):**
*   Trả về một đối tượng dự án duy nhất.

**Error Responses:**
- `404 Not Found`: Không tìm thấy dự án hoặc người dùng không có quyền truy cập.

---

## 4. WebSocket API (Auto-Save)

Hệ thống sử dụng WebSocket để cung cấp chức năng tự động lưu nội dung dự án theo thời gian thực.

### **`WS /projects/ws/{section_id}`**

Thiết lập một kết nối WebSocket để chỉnh sửa một phần (section) của dự án.

**Giao thức**: `ws://` (hoặc `wss://` trong môi trường production)

**Endpoint URL Example:**
`ws://0.0.0.0:8000/projects/ws/1?token=<YOUR_ACCESS_TOKEN>`

**Authentication:**
-   Yêu cầu xác thực.
-   Access Token (JWT) phải được truyền qua một **query parameter** có tên là `token`.

**Luồng hoạt động:**
1.  Client khởi tạo kết nối đến endpoint với `section_id` và token hợp lệ.
2.  Server xác thực token và kiểm tra xem người dùng có phải là chủ sở hữu của `section_id` đó không. Nếu không, kết nối sẽ bị từ chối.
3.  Sau khi kết nối thành công, client có thể bắt đầu gửi các message cập nhật.

---

#### **Messages từ Client đến Server**

Client gửi một đối tượng JSON mỗi khi có thay đổi nội dung.

**Định dạng Message:**
```json
{
  "title": "Pitch Deck phiên bản mới",
  "content": {
    "slide1": "Nội dung slide 1 đã được cập nhật.",
    "slide2": "Nội dung slide 2."
  }
}
```
*   `title`: (Tùy chọn) Chuỗi string, tiêu đề mới của section.
*   `content`: (Tùy chọn) Một đối tượng JSON, chứa cấu trúc nội dung chi tiết của section.

---

#### **Messages từ Server đến Client**

**Xác nhận lưu thành công:**
Sau khi nhận và lưu thành công dữ liệu, server sẽ gửi lại:
```json
{
  "status": "saved",
  "section_id": 1
}
```

**Lỗi định dạng dữ liệu:**
Nếu client gửi dữ liệu không đúng định dạng:
```json
{
  "status": "error",
  "message": "Invalid data format"
}
```
