from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
import logging

from app.core.config import settings

# Cấu hình logging cơ bản
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code chạy khi Server khởi động (Startup)
    logger.info("🚀 Ứng dụng %s đang khởi động...", settings.PROJECT_NAME)
    yield
    # Code chạy khi Server tắt (Shutdown)
    logger.info("🛑 Ứng dụng %s đang tắt và dọn dẹp tài nguyên...", settings.PROJECT_NAME)

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
    docs_url="/docs",      # Swagger UI
    redoc_url="/redoc"    # Redoc UI
)

# Global Exception Handler cho các lỗi không mong muốn (500)
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error("Lỗi chưa được xử lý tại endpoint %s: %s", request.url.path, str(exc), exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "Đã xảy ra lỗi hệ thống, vui lòng thử lại sau."
            }
        }
    )

# Endpoint kiểm tra trạng thái hoạt động của server
@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "ok",
        "project": settings.PROJECT_NAME
    }
