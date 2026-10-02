# Bảng đối chiếu bảy tiêu chí Đề 3

Ngày kiểm tra cục bộ: 02/10/2026, múi giờ Asia/Saigon.

| Tiêu chí | Yêu cầu đề | Thành phần hoặc file đáp ứng | Trạng thái kiểm tra | Minh chứng cần chụp |
|---|---|---|---|---|
| 1 Quản lý mã nguồn 1.5 điểm | GitHub đủ source/config, README, 3 commit | Toàn repository, `README.md`, lịch sử Git | **KIỂM TRA CỤC BỘ:** đủ 3 commit sau commit cuối. **CHƯA KIỂM TRA GITHUB:** chưa push theo yêu cầu của người dùng | 01, 02 |
| 2 Ứng dụng và Database 1.5 điểm | WordPress ổn định, kết nối MySQL, phpMyAdmin hoạt động | `wordpress`, `mysql`, `phpmyadmin`, plugin `de3-product-showcase` | **ĐÃ KIỂM TRA:** container healthy, WordPress init exit 0, trang sản phẩm trả nội dung, có 6 sản phẩm publish, phpMyAdmin trả trang đăng nhập | 03 đến 07 |
| 3 Nginx Reverse Proxy 1.5 điểm | Truy cập qua Nginx, có security headers | `nginx/default.conf`, service `nginx`, chỉ Nginx public cổng website | **ĐÃ KIỂM TRA:** HTTP 200 qua Nginx; đủ X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, CSP | 08, 09 |
| 4 Prometheus và Grafana 1.5 điểm | Metrics container, web, database và dashboard | `prometheus/`, Nginx Exporter, MySQL Exporter, Blackbox Exporter, 3 dashboard JSON | **ĐÃ KIỂM TRA:** mọi target `up=1`, `nginx_up=1`, `mysql_up=1`, bốn `probe_success=1`; Grafana provision dashboard thành công | 11 đến 14 |
| 5 Loki 1.5 điểm | Loki, Promtail, 2 đến 3 LogQL query | `loki/`, `promtail/`, datasource Loki, dashboard Nginx Logs | **ĐÃ KIỂM TRA:** Loki ready, Promtail tail file Nginx; ba query cơ bản trả kết quả; log thật status 404 được truy vấn thành công | 15 đến 18 |
| 6 Hardening 1.5 điểm | Ít nhất 3 đến 4 biện pháp | Docker secrets, backend internal, MySQL không public, headers, read-only, cap drop, no-new-privileges, Grafana auth | **ĐÃ KIỂM TRA CẤU HÌNH VÀ RUNTIME:** secret không được Git theo dõi, cổng MySQL không public, security headers có trên response | 09, 10, 19 |
| 7 Tổng thể và trình bày 1.0 điểm | Compose hoàn chỉnh, demo rõ, screenshot, hiểu bài | `docker-compose.yml`, README, hướng dẫn demo, checklist ảnh, báo cáo Word | **ĐÃ KIỂM TRA HỆ THỐNG VÀ BÁO CÁO:** toàn stack chạy Compose; DOCX có 11 ngắt trang, 10 bảng và 5 hình. **CHƯA CHỤP GIAO DIỆN:** cần chụp đủ danh sách trước khi nộp | 01 đến 19 |

