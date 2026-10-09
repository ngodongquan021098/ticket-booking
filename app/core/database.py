from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

# Khởi tạo Engine (Cánh cổng giao tiếp với DB)
# pool_size: Số lượng kết nối tối đa mở sẵn
# max_overflow: Số kết nối có thể mở thêm khi pool đã đầy (đáp ứng khi traffic tăng vọt)
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # In ra màn hình các câu SQL được sinh ra (tiện cho debug)
    pool_size=5,
    max_overflow=10
)

# Khởi tạo Session Factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,  # Ngăn SQLAlchemy xóa dữ liệu object sau khi commit
    autocommit=False,
    autoflush=False,
)

# Dependency Injection cho FastAPI
async def get_db():
    """
    Hàm này sẽ được FastAPI gọi mỗi khi có 1 request cần chọc vào DB.
    Dùng `yield` để đảm bảo kết nối luôn được đóng (close) sau khi xử lý xong,
    ngay cả khi code xảy ra lỗi (Exception).
    """
    session = AsyncSessionLocal()
    try:
        yield session
    finally:
        await session.close()

