# Event Ticketing / Flash Sale System

Dự án backend hệ thống bán vé sự kiện, thiết kế theo chuẩn Clean Architecture với FastAPI, PostgreSQL, và SQLAlchemy.

## Hướng dẫn cài đặt cho máy mới (Local Development)

### Bước 1: Clone project và tạo môi trường ảo
```bash
git clone https://github.com/ngodongquan021098/ticket-booking.git
cd ticket-booking
python -m venv venv

# Kích hoạt venv (Windows):
.\venv\Scripts\activate
# Kích hoạt venv (Mac/Linux):
# source venv/bin/activate
```

### Bước 2: Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### Bước 3: Chuẩn bị Database
1. Cài đặt PostgreSQL trên máy cá nhân.
2. Mở pgAdmin (hoặc DBeaver).
3. Tạo một database mới (rỗng) có tên là: `ticket_booking_db`.

### Bước 4: Cấu hình biến môi trường (.env)
1. Trong thư mục gốc của dự án, bạn sẽ thấy file `.env.example`.
2. Hãy copy hoặc đổi tên file đó thành `.env`.
3. Mở file `.env` lên và thay đổi giá trị `POSTGRES_PASSWORD` thành mật khẩu thực tế của bạn trên máy cá nhân.
```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=mat_khau_postgres_cua_ban
POSTGRES_DB=ticket_booking_db
```

*(Lưu ý: Không bao giờ push file `.env` lên git).*

### Bước 5: Khởi chạy dự án (Sẽ cập nhật thêm)
*(Các lệnh Migration và Start server sẽ được bổ sung sau khi hoàn thiện code phase 1).*

