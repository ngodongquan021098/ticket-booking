# Tiến Độ Dự Án & Kiến Thức Đã Học (Progress Tracker)

File này dùng để lưu lại tiến độ thực hiện dự án **Event Ticketing / Flash Sale** và các kiến thức Core đã đi qua. Khi chuyển sang máy tính khác, chỉ cần mở file này lên là bạn và AI có thể bắt nhịp tiếp ngay lập tức.

---

## Phương Pháp Học Tập Thống Nhất
1. **Không tự động sinh code tràn lan:** Tập trung giải thích bản chất cốt lõi (Core concepts), nguyên lý hoạt động bên dưới, và các câu hỏi phỏng vấn Middle/Senior trước.
2. **Làm tới đâu hiểu tới đó:** Chỉ khi bạn yêu cầu code hoặc sau khi đã hiểu rõ lý thuyết thì mới tiến hành viết code.
3. **Quy tắc 80/20:** Tập trung xoáy sâu vào 20% công cụ cốt lõi của Python, FastAPI, SQLAlchemy 2.0 và PostgreSQL giải quyết 95% bài toán thực tế.

---

## Trạng Thái Các Phase

### Phase 1: Project Setup & Core Architecture (Đang thực hiện ⏳)
- [x] **Bước 1.1: Khởi tạo cấu trúc thư mục Clean Architecture** (`api`, `core`, `models`, `schemas`, `services`, `tests`).
- [x] **Bước 1.2: Cài đặt thư viện cốt lõi** (`requirements.txt`: FastAPI, Uvicorn, SQLAlchemy 2.0, asyncpg, Alembic, Pydantic Settings).
- [x] **Bước 1.3: Cấu hình biến môi trường (`app/core/config.py`)**
  - *Kiến thức đã nắm:* Tại sao dùng `BaseSettings` của Pydantic thay vì `os.getenv()` (Fail-fast, ép kiểu tự động), `@property` trong Python (giống getter trong JS/TS), Singleton pattern cho `settings`.
- [x] **Bước 1.4: Khởi tạo Database Engine & Async Session (`app/core/database.py`)**
  - *Kiến thức đã nắm:* 
    - Phân biệt `Engine` (Connection Pool: `pool_size`, `max_overflow` để chống sập DB khi quá tải) và `Session` (phiên làm việc cho từng request).
    - Tại sao cần `expire_on_commit=False` trong Async.
    - Cơ chế `yield` (Generator) kết hợp `try...finally` trong Dependency Injection `get_db()` để chống rò rỉ kết nối (Connection Leak).
- [ ] **Bước 1.5: Tạo `DeclarativeBase` cho SQLAlchemy 2.0** *(Đang dừng ở bước này)*
  - Cần thêm `class Base(DeclarativeBase)` vào `app/core/database.py` để quản lý `Base.metadata`.
- [ ] **Bước 1.6: Cấu hình Alembic (Database Migration) với Async Engine**
- [ ] **Bước 1.7: Viết Entrypoint (`app/main.py`) & Global Exception Handler**

---

### Phase 2: Authentication & RBAC (Chưa bắt đầu 🔒)
- [ ] Thiết kế bảng `User` với SQLAlchemy 2.0 (`Mapped`, `mapped_column`).
- [ ] Tạo migration đầu tiên bằng Alembic.
- [ ] Hash mật khẩu (Bcrypt/Argon2) – Hiểu về CPU-bound task trong Async.
- [ ] JWT Authentication (Access Token & Refresh Token).
- [ ] Phân quyền RBAC (Admin vs Customer) bằng FastAPI Dependency Injection.

---

### Phase 3: Core Business & Race Conditions (Chưa bắt đầu 🔒)
- [ ] Thiết kế bảng `Event`, `TicketType`, `Booking` và các mối quan hệ (`relationship`).
- [ ] Giải quyết bài toán **N+1 Queries** với `selectinload` / `joinedload`.
- [ ] Xây dựng API Đặt vé (`POST /bookings`).
- [ ] **Trọng tâm Senior:** Xử lý Race Condition khi nhiều người mua vé cùng lúc (Database Transaction, Isolation Levels, Row-level Locking `SELECT ... FOR UPDATE`).
- [ ] Viết script stress-test bắn 100 requests đồng thời để kiểm chứng.

---

### Phase 4: Performance & Caching với Redis (Chưa bắt đầu 🔒)
- [ ] Tích hợp Redis bất đồng bộ.
- [ ] Áp dụng chiến lược **Cache-Aside** cho API xem sự kiện/vé.
- [ ] Xử lý bài toán **Cache Invalidation** và **Thundering Herd**.

---

### Phase 5: Asynchronous Background Processing (Chưa bắt đầu 🔒)
- [ ] Xử lý tác vụ ngầm (Gửi email xác nhận vé, xử lý thanh toán).
- [ ] So sánh và thực hành `BackgroundTasks` của FastAPI vs Message Queue (Celery/RabbitMQ).

---

### Phase 6: Advanced Queries, Indexing & Docker (Chưa bắt đầu 🔒)
- [ ] Viết API thống kê doanh thu bằng SQL nâng cao (CTEs, Window Functions, Subqueries trong SQLAlchemy).
- [ ] Phân tích hiệu năng câu truy vấn với `EXPLAIN ANALYZE` và đánh Index (B-Tree, Composite Index).
- [ ] Viết Integration Tests với `pytest`.
- [ ] Đóng gói toàn bộ hệ thống vào `Dockerfile` và `docker-compose.yml`.

