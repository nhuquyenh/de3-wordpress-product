# Kịch bản demo Đề 3

## 1 Chuẩn bị

1. Mở Docker Desktop và xác nhận engine đang chạy.
2. Tại thư mục project, chạy `docker compose up -d`.
3. Chạy `docker compose ps -a` và giải thích `wordpress-init` kết thúc mã 0 là đúng.
4. Không hiển thị nội dung file secret trên màn hình ghi hình.

## 2 Demo ứng dụng và database

1. Mở website tại `http://localhost:8180`.
2. Chỉ ra sáu sản phẩm có tên, mô tả, giá và hình ảnh.
3. Mở một trang chi tiết sản phẩm.
4. Đăng nhập WordPress Admin, mở menu Sản phẩm để chứng minh chức năng quản lý.
5. Mở phpMyAdmin, chọn database `wordpress`, bảng `wp_posts` và lọc `post_type = de3_product`.

## 3 Demo Nginx

1. Nhấn mạnh WordPress không public cổng, website đi qua Nginx cổng 8180.
2. Mở DevTools Network, tải lại trang, chọn request document.
3. Chỉ ra ba header bắt buộc và hai header bổ sung.

## 4 Demo Prometheus và Grafana

1. Mở Prometheus Targets và chỉ ra các job UP.
2. Mở lần lượt dashboard Container, Nginx và MySQL.
3. Tải lại website vài lần để đồ thị request thay đổi.

## 5 Demo Loki và LogQL

1. Mở Grafana Explore, chọn datasource Loki.
2. Chạy `{job="nginx"}`.
3. Chạy `{job="nginx"} |= "GET"`.
4. Truy cập endpoint không tồn tại `/wp-json/de3/v1/not-found` để sinh 404.
5. Chạy `{job="nginx"} |~ "404"` và `{job="nginx", status="404"}`.

## 6 Trình bày hardening

Trình bày tối thiểu bốn ý: MySQL không public, backend internal, secret không commit, Nginx security headers. Có thể bổ sung read-only filesystem, bỏ capabilities, `no-new-privileges`, Grafana tắt anonymous và WordPress tắt file editor.

