# Docker Deployment Guide

## 📋 Mục lục
- [Tổng quan](#tổng-quan)
- [Yêu cầu](#yêu-cầu)
- [Cài đặt và chạy](#cài-đặt-và-chạy)
- [Development Mode](#development-mode)
- [Production Mode](#production-mode)
- [Quản lý Database](#quản-lý-database)
- [Monitoring và Logs](#monitoring-và-logs)
- [Best Practices](#best-practices)

## 🎯 Tổng quan

Dự án này sử dụng Docker để containerize ứng dụng FastAPI với các best practices sau:
- **Multi-stage build** để giảm kích thước image
- **Non-root user** để tăng bảo mật
- **Health checks** cho container monitoring
- **Docker Compose** để orchestrate nhiều services
- **Separate configurations** cho dev và production
- **Nginx reverse proxy** cho production

## 📦 Yêu cầu

- Docker Engine 20.10+
- Docker Compose 2.0+
- Make (optional, để sử dụng Makefile commands)

## 🚀 Cài đặt và chạy

### 1. Clone repository và setup environment

```bash
# Copy file .env.example thành .env
cp .env.example .env

# Chỉnh sửa .env với thông tin thực tế
nano .env  # hoặc notepad .env trên Windows
```

### 2. Build Docker images

```bash
docker-compose build
# hoặc
make build
```

## 💻 Development Mode

Chế độ development bao gồm:
- Hot reload khi code thay đổi
- Volume mounting để sync code
- Debug-friendly configuration

### Khởi động:

```bash
docker-compose up -d
# hoặc
make up
```

### Xem logs:

```bash
docker-compose logs -f app
# hoặc
make logs
```

### Truy cập container:

```bash
docker-compose exec app /bin/bash
# hoặc
make shell
```

### Dừng services:

```bash
docker-compose down
# hoặc
make down
```

## 🏭 Production Mode

Production mode sử dụng:
- Multi-worker Uvicorn
- Nginx reverse proxy
- No hot reload
- Optimized for performance

### Khởi động:

```bash
docker-compose -f docker-compose.prod.yml up -d
# hoặc
make up-prod
```

### Environment Variables (Production)

Đảm bảo set các biến môi trường sau trong `.env`:

```env
# Strong passwords
MYSQL_ROOT_PASSWORD=<strong-random-password>
MYSQL_PASSWORD=<strong-random-password>

# Secure secret key (generate với: openssl rand -hex 32)
SECRET_KEY=<your-secure-secret-key>

# Database
MYSQL_DATABASE=startup_kit
MYSQL_USER=appuser
```

## 🗄️ Quản lý Database

### Chạy migrations:

```bash
docker-compose exec app alembic upgrade head
# hoặc
make migrate
```

### Tạo migration mới:

```bash
docker-compose exec app alembic revision --autogenerate -m "description"
# hoặc
make migration
```

### Truy cập MySQL shell:

```bash
docker-compose exec db mysql -u root -p
# hoặc
make db-shell
```

### Backup database:

```bash
docker-compose exec db mysqldump -u root -p startup_kit > backup.sql
```

### Restore database:

```bash
docker-compose exec -T db mysql -u root -p startup_kit < backup.sql
```

## 📊 Monitoring và Logs

### Xem logs của tất cả services:

```bash
docker-compose logs -f
```

### Xem logs của một service cụ thể:

```bash
docker-compose logs -f app
docker-compose logs -f db
docker-compose logs -f nginx
```

### Kiểm tra health status:

```bash
docker-compose ps
```

### Xem resource usage:

```bash
docker stats
```

## 🔒 Best Practices

### Security

1. **Không commit file .env** vào Git
2. **Sử dụng strong passwords** cho production
3. **Update dependencies** thường xuyên
4. **Run as non-root user** (đã được implement)
5. **Limit container resources** khi cần:

```yaml
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M
```

### Performance

1. **Multi-stage builds** để giảm image size
2. **Layer caching** bằng cách copy requirements trước
3. **Multi-worker Uvicorn** trong production
4. **Nginx caching** và load balancing

### Maintenance

1. **Regular backups** của database
2. **Monitor logs** cho errors
3. **Update images** thường xuyên:

```bash
docker-compose pull
docker-compose up -d
```

4. **Clean up unused resources**:

```bash
docker system prune -af
# hoặc
make clean
```

## 🔧 Troubleshooting

### Container không start được:

```bash
docker-compose logs app
docker-compose ps
```

### Database connection errors:

1. Kiểm tra database đã ready chưa:
```bash
docker-compose logs db
```

2. Verify DATABASE_URL trong .env

### Port conflicts:

Thay đổi ports trong `.env`:
```env
APP_PORT=8001  # thay vì 8000
MYSQL_PORT=3307  # thay vì 3306
```

## 📝 Useful Commands

```bash
# Rebuild image without cache
docker-compose build --no-cache

# View all running containers
docker ps

# Remove all stopped containers
docker container prune

# View image sizes
docker images

# Export container logs
docker-compose logs app > app.log

# Execute command in running container
docker-compose exec app python -c "print('Hello')"
```

## 🌐 Endpoints

- **Application**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **MySQL**: localhost:3306 (from host)

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/)
- [MySQL Docker Hub](https://hub.docker.com/_/mysql)
