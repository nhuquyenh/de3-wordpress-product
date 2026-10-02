# Danh sách ảnh minh chứng theo thang điểm

Mỗi ảnh cần chụp toàn bộ vùng liên quan, thấy rõ URL hoặc tên màn hình, không để lộ mật khẩu hay secret. Đặt tên theo cột Tên tệp để việc đưa vào báo cáo thống nhất.

| STT | Tên tệp | Chụp ở đâu và thao tác | Tiêu chí được chứng minh |
|---:|---|---|---|
| 1 | `01-github-repository.png` | Mở trang repository GitHub, hiển thị cây source và README | Source/config/README được quản lý trên GitHub |
| 2 | `02-git-commits.png` | Mở lịch sử commit GitHub hoặc chạy `git log --oneline -3` | Đủ 3 commit rõ ràng, có ý nghĩa |
| 3 | `03-wordpress-home.png` | Mở `http://localhost:8180` | Website WordPress hoạt động qua Nginx |
| 4 | `04-product-list.png` | Cuộn trang chủ hoặc mở trang danh sách sản phẩm | Nhiều sản phẩm có tên, mô tả, giá và hình ảnh |
| 5 | `05-wordpress-admin-products.png` | Đăng nhập `/wp-admin/`, chọn Sản phẩm | Chức năng quản lý nội dung/sản phẩm |
| 6 | `06-phpmyadmin-login.png` | Mở `http://localhost:8181` và đăng nhập | phpMyAdmin kết nối MySQL |
| 7 | `07-phpmyadmin-wordpress-data.png` | Mở database `wordpress`, bảng `wp_posts` | Dữ liệu WordPress được lưu trong MySQL |
| 8 | `08-nginx-reverse-proxy.png` | Mở website ở cổng 8180, thấy URL trình duyệt | Truy cập website qua Nginx reverse proxy |
| 9 | `09-security-headers.png` | DevTools Network, chọn request document, xem Response Headers | X-Frame-Options, X-Content-Type-Options, Referrer-Policy |
| 10 | `10-docker-compose-ps.png` | Chạy `docker compose ps -a` tại đúng project | Toàn bộ hệ thống chạy bằng Docker Compose |
| 11 | `11-prometheus-targets.png` | Mở `http://localhost:9091/targets` | Các Prometheus target ở trạng thái UP |
| 12 | `12-grafana-container.png` | Mở dashboard DE3 Container Monitoring | Giám sát container/service availability |
| 13 | `13-grafana-nginx.png` | Mở dashboard DE3 Nginx Monitoring | Giám sát web server Nginx |
| 14 | `14-grafana-mysql.png` | Mở dashboard DE3 MySQL Monitoring | Giám sát database MySQL |
| 15 | `15-loki-promtail.png` | Mở dashboard DE3 Nginx Logs hoặc trang datasource Loki | Loki nhận log do Promtail gửi |
| 16 | `16-logql-all-nginx.png` | Grafana Explore với `{job="nginx"}` | LogQL query 1 trả log |
| 17 | `17-logql-get.png` | Grafana Explore với `{job="nginx"} |= "GET"` | LogQL query 2 lọc request GET |
| 18 | `18-logql-404.png` | Grafana Explore với `{job="nginx"} |~ "404"` | LogQL query 3 trả log 404 |
| 19 | `19-hardening.png` | Ghép các vùng Compose/config hoặc terminal kiểm tra port | Network isolation, không public MySQL, secret, read-only/cap drop |

