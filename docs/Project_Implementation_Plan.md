## Goal Description
Chúng ta sẽ cùng xây dựng một dự án **Event Ticketing / Flash Sale (Hệ thống bán vé sự kiện / Flash sale e-commerce)**. 

Mình đề xuất dự án này vì đây là "bài test" hoàn hảo để bạn chuyển mình từ "thợ code" sang "Senior BE". Những hệ thống CRUD bình thường (như quản lý sinh viên, to-do list) sẽ không có đất diễn cho các kỹ thuật nâng cao. Nhưng với một hệ thống bán vé, bạn sẽ phải đối mặt với các bài toán thực tế của kỹ sư cấp cao:
- **FastAPI:** Tận dụng Asynchronous programming để xử lý hàng ngàn lượt truy cập cùng lúc khi mở bán vé.
- **SQLAlchemy & PostgreSQL:** Xử lý **Race Conditions** (làm sao để 1000 người cùng bấm mua 1 vé cuối cùng mà hệ thống không bị bán âm vé? Áp dụng Transaction, Row-level lock `SELECT FOR UPDATE`).
- **Redis:** Làm Caching. Nếu ai vào cũng query DB để xem còn bao nhiêu vé thì DB sẽ "chết". Ta cần cache số lượng vé vào Redis.
- **Background Tasks:** Khi thanh toán xong, hệ thống không thể bắt user chờ 5 giây để gửi email. Phải dùng Message Queue (RabbitMQ/Celery) để xử lý ngầm.
- **Advanced SQL:** Viết các báo cáo doanh thu phức tạp cho Admin bằng CTEs, Window Functions, và tối ưu bằng Index.

## User Review Required
> [!IMPORTANT] 
> 1. **Dự án này đã đúng ý bạn chưa?** Nếu bạn có một idea khác (ví dụ: Mạng xã hội thu nhỏ, Hệ thống quản lý task dạng Jira, v.v.), hãy báo cho mình biết để mình điều chỉnh nhé!
> 2. **Docker:** Bạn muốn chúng ta setup mọi thứ vào Docker ngay từ đầu (chuẩn DevOps), hay chạy local (cài Postgres/Redis trực tiếp lên máy tính) trước cho dễ hiểu rồi mới đưa vào Docker ở phase cuối?

## Proposed Execution Phases (Step-by-step)

Dự án sẽ được chia thành các Giai đoạn (Phases) nhỏ. Bạn sẽ là người trực tiếp code, mình sẽ đưa ra requirements, hướng dẫn chi tiết từng bước, review code và giải thích kiến thức nền tảng.

---

### Phase 1: Project Setup & Core Architecture (Xây dựng móng)
- Cấu trúc thư mục theo chuẩn **Clean Architecture / Domain-Driven Design**. Không viết mọi thứ trong file `main.py` hay `router.py`.
- Tích hợp FastAPI với SQLAlchemy (Sử dụng AsyncEngine, AsyncSession để đạt hiệu năng cao nhất).
- Setup Alembic để quản lý Database Migrations.
- Xây dựng hệ thống cấu hình (Pydantic BaseSettings) và Global Exception Handler.

### Phase 2: Authentication & RBAC (Bảo mật & Phân quyền)
- Viết API Đăng ký / Đăng nhập.
- Implement JWT (JSON Web Token) authentication.
- Xây dựng Role-Based Access Control (RBAC): Phân chia rõ ràng quyền Admin (tạo sự kiện) và Customer (mua vé) bằng hệ thống Dependency Injection của FastAPI.

### Phase 3: Core Business & Race Conditions (Trái tim của hệ thống)
- Quản lý Sự kiện (Events) và Loại vé (Ticket Types).
- **Thử thách Senior:** Xây dựng API Đặt vé (`POST /bookings`). 
- Thực hành xử lý đồng thời (Concurrency Control): Dùng Isolation Levels và pessimistic locking trong SQLAlchemy để đảm bảo tính nhất quán dữ liệu (Data Integrity).

### Phase 4: Performance & Caching (Tối ưu hiệu năng)
- Tích hợp Redis.
- Caching các API đọc dữ liệu nhiều (List Events, Event Detail).
- Xử lý bài toán hóc búa: **Cache Invalidation** (Khi có người mua vé, làm sao để cập nhật lại cache số lượng vé tồn mà không gây ra lỗi?).

### Phase 5: Asynchronous Background Processing
- Tích hợp hệ thống hàng đợi (Task Queue) như Celery hoặc background tasks của FastAPI.
- Xử lý các tác vụ tốn thời gian: Gửi Email xác nhận, Xử lý Webhook thanh toán một cách bất đồng bộ để API phản hồi ngay lập tức.

### Phase 6: Advanced Queries & Reporting (SQL nâng cao)
- Viết API Dashboard cho Admin: Thống kê doanh thu theo ngày/tháng, top sự kiện bán chạy nhất.
- Thực hành viết các câu lệnh SQL phức tạp (CTEs, Subqueries) thông qua ORM SQLAlchemy.
- Phân tích Query Plan (`EXPLAIN ANALYZE`) và đánh Index cho DB để tối ưu các báo cáo bị chậm.

## Verification Plan

### Automated Tests
Ở mỗi Phase, chúng ta sẽ viết **Pytest**. Mình sẽ hướng dẫn bạn cách viết Integration Test cho API mà có sử dụng test database riêng biệt (tạo db mới trước test, xóa sau test) và cách mock các external services (như mock hàm gửi email).

### Manual Verification
Sau khi code xong, bạn sẽ chạy thử bằng Postman/Swagger UI. Thậm chí chúng ta có thể viết 1 script Python nhỏ (dùng `aiohttp`) để "bắn" hàng ngàn request cùng lúc vào hệ thống nhằm kiểm tra xem API có chịu tải được không và có bị bán lố vé không.
