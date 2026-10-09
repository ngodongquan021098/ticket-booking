# Roadmap Tăng Trình Lên Middle/Senior Backend
*(Stack: Python, FastAPI, PostgreSQL, SQLAlchemy)*

Để vượt qua mức "thợ code" (có thể làm mọi task nhưng chỉ dừng ở mức chạy được) và tiến lên Middle/Senior, bạn cần tập trung vào **hiệu năng (performance), tính mở rộng (scalability), khả năng bảo trì (maintainability) và thiết kế hệ thống (system design)**.

Dưới đây là lộ trình chi tiết chúng ta sẽ cùng đi qua:

## 1. Nền tảng Python Chuyên Sâu (Advanced Python)
*Senior BE không chỉ viết code Python chạy được, mà viết code "Pythonic", an toàn và tối ưu bộ nhớ.*
- **Concurrency & Asyncio:** Hiểu rõ Event loop, coroutines. Phân biệt Multi-threading, Multi-processing và Asyncio. Hiểu về GIL (Global Interpreter Lock).
- **Advanced Syntax:** Decorators (viết custom decorator, class decorator), Generators, Context Managers (`with` statement).
- **Memory Management:** Cách Python quản lý bộ nhớ, Garbage Collection, Reference Counting để tránh memory leaks.
- **Typing & OOP:** Type hinting nâng cao (Generics, Protocols, Callables). Áp dụng các Design Patterns cốt lõi (Factory, Singleton, Strategy, Observer).

## 2. Làm Chủ FastAPI & Pydantic
*Chuyển từ việc viết các API rời rạc sang xây dựng một hệ thống API vững chắc.*
- **Dependency Injection (DI):** Khai thác tối đa DI của FastAPI để tái sử dụng code, quản lý DB session, và authentication.
- **Pydantic V2 Deep Dive:** Custom validators, model configs, field serializers, và tối ưu hiệu năng validation.
- **Cấu trúc Project (Project Layout):** Áp dụng Clean Architecture hoặc Domain-Driven Design (DDD) thay vì nhét mọi thứ vào router.
- **Advanced Features:** Middlewares, Background Tasks, Global Exception Handling, Lifespan events.
- **Security:** Triển khai chuẩn OAuth2, JWT, Rate Limiting, xử lý CORS an toàn.

## 3. SQLAlchemy Chuyên Sâu
*Đây là nơi phân biệt rõ nhất giữa Junior và Senior. Viết ORM không khó, tối ưu ORM mới khó.*
- **Kiến trúc SQLAlchemy:** Hiểu sự khác biệt giữa SQLAlchemy Core và ORM. Cách Engine và Connection Pool hoạt động dưới nền.
- **Quản lý Session:** Vòng đời của Session, cách commit/rollback an toàn, tránh tình trạng treo kết nối (connection leaks).
- **Giải quyết bài toán N+1 Queries:** Làm chủ Lazy loading và Eager loading (`joinedload`, `selectinload`, `contains_eager`).
- **Complex Queries:** Viết Subqueries, CTEs (Common Table Expressions), Window functions trực tiếp bằng ORM.
- **Alembic Migrations:** Quản lý migration trong môi trường team lớn, thực hiện data migration (không chỉ schema migration) an toàn.

## 4. PostgreSQL & Tối Ưu Cơ Sở Dữ Liệu
*Backend mạnh phải đi kèm với DB khỏe.*
- **Indexing Strategy:** B-Tree, Hash, GIN, GiST. Khi nào nên đánh index, khi nào không? Cấu tạo của Composite Index.
- **Explain Analyze:** Đọc hiểu query plan để biết tại sao câu query bị chậm và cách tối ưu.
- **Transactions & Concurrency:** Các mức cô lập (Isolation Levels - Read Committed, Repeatable Read, Serializable). Hiện tượng Race Condition và các loại Lock (Row-level lock, Table lock).
- **Database Design:** Chuẩn hóa (Normalization) và Phi chuẩn hóa (Denormalization).
- **Xử lý Dữ liệu lớn:** Partitioning, Table Inheritance.

## 5. System Design & Software Architecture (Tư Duy Senior)
- **Caching:** Tích hợp Redis. Các chiến lược (Write-through, Cache Aside). Vấn đề Cache Invalidation và Thundering Herd.
- **Message Brokers:** Dùng Celery, RabbitMQ hoặc Kafka để xử lý các task nặng bất đồng bộ (ví dụ: gửi mail, report generation).
- **Thiết kế API:** RESTful best practices, versioning, pagination (Offset vs Cursor).
- **Microservices vs Monolith:** Hiểu trade-offs. Giao tiếp giữa các services (Synchronous qua API vs Asynchronous qua Events).

## 6. Engineering Practices (Testing & Deployment)
- **Testing (`pytest`):** Không chỉ là Unit test, mà còn là Integration test. Làm chủ Mocking, Monkeypatching, và Pytest fixtures (đặc biệt cho DB testing).
- **Code Quality:** Sử dụng `ruff`, `mypy`, `pre-commit` hooks để chuẩn hóa code base.
- **Docker & CI/CD:** Viết Dockerfile tối ưu (multi-stage build) cho Python. Hiểu cơ bản về quy trình CI/CD.
- **Observability:** Logging có cấu trúc, Monitoring (Prometheus/Grafana), APM (Application Performance Monitoring).
