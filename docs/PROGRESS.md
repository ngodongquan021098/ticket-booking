# Tiến Độ Dự Án & Kiến Thức Đã Học (Progress Tracker)

File này dùng để lưu lại tiến độ thực hiện dự án **Event Ticketing / Flash Sale** và các kiến thức Core đã đi qua. Khi chuyển sang máy tính khác hoặc bắt đầu buổi học mới, chỉ cần mở file này lên là bạn và AI có thể bắt nhịp tiếp ngay lập tức.

---

## Phương Pháp Học Tập Thống Nhất
1. **Không tự động sinh code tràn lan:** Tập trung giải thích bản chất cốt lõi (Core concepts), nguyên lý hoạt động bên dưới, và các câu hỏi phỏng vấn Middle/Senior trước.
2. **Làm tới đâu hiểu tới đó:** Chỉ khi bạn yêu cầu code hoặc sau khi đã hiểu rõ lý thuyết thì mới tiến hành viết code.
3. **Quy tắc 80/20:** Tập trung xoáy sâu vào 20% công cụ cốt lõi của Python, FastAPI, SQLAlchemy 2.0 và PostgreSQL giải quyết 95% bài toán thực tế.
4. **Cập nhật tiến độ:** Chỉ tổng hợp và cập nhật file này vào **cuối mỗi buổi học** để đảm bảo mạch học tập liền mạch.

---

## Trạng Thái Các Phase

### Phase 1: Project Setup & Core Architecture (Đã hoàn thành ✅)
- [x] **Bước 1.1: Khởi tạo cấu trúc thư mục Clean Architecture** (`api`, `core`, `models`, `schemas`, `services`, `tests`).
- [x] **Bước 1.2: Cài đặt thư viện cốt lõi** (`requirements.txt`: FastAPI, Uvicorn, SQLAlchemy 2.0, asyncpg, greenlet, Alembic, Pydantic Settings).
  - *Kiến thức đã nắm:* SQLAlchemy AsyncIO bắt buộc cần thư viện `greenlet` làm cầu nối giữa async event loop và engine C bên dưới.
- [x] **Bước 1.3: Cấu hình biến môi trường (`app/core/config.py`)**
  - *Kiến thức đã nắm:* Tại sao dùng `BaseSettings` của Pydantic thay vì `os.getenv()` (Fail-fast, ép kiểu tự động), `@property` trong Python (giống getter trong JS/TS), Singleton pattern cho `settings`.
- [x] **Bước 1.4: Khởi tạo Database Engine & Async Session (`app/core/database.py`)**
  - *Kiến thức đã nắm:* 
    - Phân biệt `Engine` (Connection Pool: `pool_size`, `max_overflow` để chống sập DB khi quá tải) và `Session` (phiên làm việc cho từng request).
    - Tại sao cần `expire_on_commit=False` trong Async.
    - Cơ chế `yield` (Generator) kết hợp `try...finally` trong Dependency Injection `get_db()` để chống rò rỉ kết nối (Connection Leak).
- [x] **Bước 1.5: Tạo `DeclarativeBase` cho SQLAlchemy 2.0**
  - *Kiến thức đã nắm:*
    - Sự khác biệt giữa `DeclarativeBase` (SQLAlchemy 2.0 kế thừa class trực tiếp, type-hinting chuẩn) và `declarative_base()` (SQLAlchemy 1.4 cũ dạng factory function).
    - Vai trò của `Base.metadata`: "Bản đồ danh bạ" lưu trữ toàn bộ schema/bảng trong bộ nhớ RAM, phục vụ Alembic auto-generate migrations.
- [x] **Bước 1.6: Cấu hình Alembic (Database Migration) với Async Engine**
  - *Kiến thức đã nắm:*
    - So sánh `create_all()` vs Database Migration: Migration là version control cho DB, an toàn cho production, hỗ trợ rollback và team workflow.
    - Bảo mật: Không hardcode database URL trong `alembic.ini`, ghi đè động bằng `config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)` trong `alembic/env.py`.
    - **Gotcha kinh điển:** Phải có `import app.models` trong `alembic/env.py` thì `Base.metadata` mới nạp đầy đủ các bảng vào bộ nhớ để sinh migration.
    - Cầu nối `connection.run_sync(do_run_migrations)` để thực thi DDL đồng bộ trong kết nối asyncpg.
- [x] **Bước 1.7: Viết Entrypoint (`app/main.py`), Lifespan & Global Exception Handler**
  - *Kiến thức đã nắm:*
    - Lifespan context manager (`@asynccontextmanager`) chuẩn hiện đại thay thế cho `@app.on_event` đã deprecated.
    - Global Exception Handler: Giấu thông tin nhạy cảm/stack trace với client, trả về format JSON lỗi đồng nhất, log lỗi chi tiết phía server.
    - Module `logging`: Cấu hình tập trung tại root `main.py`, cơ chế `__name__` tự động định danh module phát sinh log trong toàn bộ service.
    - Bản chất Decorator pattern trong Python (bọc hàm gốc, thêm tính năng mà không sửa code hàm gốc).
    - Ý nghĩa của `tags` trong OpenAPI/Swagger UI để gom nhóm API theo module.

---

### Phase 2: Authentication & RBAC (Đang thực hiện ⏳)
- [x] **Bước 2.1: Thiết kế bảng `User` với SQLAlchemy 2.0 (`Mapped`, `mapped_column`)**
  - *Kiến thức đã nắm:*
    - Cú pháp `Mapped[T]` của SQLAlchemy 2.0 giúp IDE và type-checker hiểu 100% kiểu dữ liệu cột.
    - `server_default=func.now()`: Lấy dấu thời gian từ máy chủ PostgreSQL (`CURRENT_TIMESTAMP`), tránh lệch múi giờ so với `datetime.now()` ở máy chạy app.
    - **Bản chất của Database Index (B-Tree):** Tăng tốc tìm kiếm từ $O(N)$ (Full Table Scan) lên $O(\log N)$ (tra cứu theo cây phân cấp và dùng con trỏ TID lấy dòng dữ liệu).
    - Trade-off của Index: Đọc nhanh hơn nhưng ghi chậm hơn (`INSERT/UPDATE/DELETE` phải cập nhật lại cây Index) và tốn dung lượng RAM/Disk.
    - Phân biệt **Non-Unique Index** (cho phép dữ liệu trùng nhau, chỉ nhằm mục đích tăng tốc tìm kiếm) vs **Unique Index** (vừa tăng tốc vừa cấm trùng lặp để bảo vệ toàn vẹn dữ liệu).
- [x] **Bước 2.2: Tạo migration đầu tiên bằng Alembic & Apply vào Database**
  - *Kiến thức đã nắm:*
    - Sự khác nhau giữa **Code-First** (dùng Model Python làm nguồn chân lý, Alembic autogenerate DDL) và **Database-First / Manual DDL** (viết file SQL thủ công ở công ty).
    - Lệnh `alembic revision --autogenerate -m "..."` và `alembic upgrade head`. Đã tạo thành công bảng `users` và `alembic_version` trong PostgreSQL.
- [ ] **Bước 2.3: Hash mật khẩu (Bcrypt/Argon2) – Hiểu về CPU-bound task trong Async** *(Đang thảo luận lý thuyết ⏳)*
  - *Kiến thức đã nắm:*
    - Bản chất Bcrypt: Tự sinh Salt, Cost Factor chống brute-force và Rainbow Table.
    - **Event Loop & Concurrency:** Node.js và FastAPI (Uvicorn) chạy Single-Thread cho Event Loop.
    - Phân biệt I/O-bound (gặp `await` thì nhả luồng cho Event Loop phục vụ request khác) vs CPU-bound (hàm đồng bộ nặng không có `await`, chiếm giữ CPU làm đơ cả Server).
    - Giải pháp của Senior: Đẩy tác vụ nặng sang Thread phụ bằng `asyncio.to_thread`.
    - Phân biệt phạm vi của `await`:
      - *Trong cùng 1 hàm:* Các dòng sau `await` bắt buộc phải đợi dòng `await` xong (tuần tự logic).
      - *Giữa các hàm/request khác nhau:* Server lập tức phục vụ các request khác trong khi tác vụ `await` đang đợi ngầm.
    - Tại sao không dùng `BackgroundTasks` cho Login/Register: Vì `BackgroundTasks` chỉ chạy sau khi đã trả response (Fire-and-forget), trong khi Login/Register bắt buộc phải có kết quả hash để kiểm tra/lưu DB trước khi phản hồi Client.
- [ ] **Bước 2.4: JWT Authentication (Access Token & Refresh Token)**
- [ ] **Bước 2.5: Phân quyền RBAC (Admin vs Customer) bằng FastAPI Dependency Injection**

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
