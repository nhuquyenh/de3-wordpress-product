from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "docs" / "report"
FIG_DIR = OUT_DIR / "figures"
OUT_FILE = OUT_DIR / "Bao-cao-De-3-WordPress.docx"
FIG_DIR.mkdir(parents=True, exist_ok=True)

NAVY = "17365D"
LIGHT_BLUE = "DCE6F1"
PALE_BLUE = "EEF4FA"
LIGHT_GRAY = "D9D9D9"
BLACK = RGBColor(0, 0, 0)


def font(size, bold=False):
    candidates = [
        Path(r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf"),
        Path(r"C:\Windows\Fonts\calibrib.ttf" if bold else r"C:\Windows\Fonts\calibri.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def rounded_box(draw, xy, fill, outline="#d9d9d9", radius=20, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def make_architecture():
    path = FIG_DIR / "architecture.png"
    im = Image.new("RGB", (1600, 900), "white")
    d = ImageDraw.Draw(im)
    title = font(42, True)
    body = font(27)
    small = font(22)
    d.text((800, 45), "Kiến trúc Docker Compose Đề 3", anchor="ma", font=title, fill="#111827")
    boxes = {
        "user": (60, 330, 290, 470, "Người dùng\nlocalhost"),
        "nginx": (370, 150, 650, 300, "Nginx\nReverse Proxy"),
        "pma": (370, 500, 650, 650, "phpMyAdmin"),
        "wp": (760, 150, 1030, 300, "WordPress\nSản phẩm"),
        "mysql": (760, 500, 1030, 650, "MySQL\nwordpress"),
        "prom": (1190, 120, 1500, 270, "Prometheus\nExporters"),
        "grafana": (1190, 360, 1500, 510, "Grafana\nDashboards"),
        "loki": (1190, 600, 1500, 750, "Loki + Promtail\nLogQL"),
    }
    fills = {"user": "#F3F4F6", "nginx": "#E8F4F1", "pma": "#FFF6DD", "wp": "#EEF1FA", "mysql": "#F1ECE8", "prom": "#E7F3FA", "grafana": "#FBE9D5", "loki": "#EDE9FE"}
    for key, (x1, y1, x2, y2, label) in boxes.items():
        rounded_box(d, (x1, y1, x2, y2), fills[key])
        d.multiline_text(((x1 + x2) / 2, (y1 + y2) / 2), label, anchor="mm", align="center", font=body, fill="#111827", spacing=8)

    def arrow(a, b, label=""):
        d.line((a, b), fill="#334155", width=5)
        x2, y2 = b
        d.polygon([(x2, y2), (x2 - 18, y2 - 10), (x2 - 18, y2 + 10)], fill="#334155")
        if label:
            mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
            d.text((mx, my - 16), label, anchor="ms", font=small, fill="#334155")

    arrow((290, 365), (370, 240), "8180")
    arrow((290, 435), (370, 560), "8181")
    arrow((650, 225), (760, 225), "proxy")
    arrow((650, 575), (760, 575), "SQL")
    d.line((895, 300, 895, 500), fill="#334155", width=5)
    d.polygon([(895, 500), (885, 482), (905, 482)], fill="#334155")
    d.line((510, 150, 510, 105, 1130, 105, 1190, 165), fill="#334155", width=5)
    d.polygon([(1190, 165), (1170, 160), (1182, 145)], fill="#334155")
    d.text((835, 96), "Nginx metrics", anchor="ms", font=small, fill="#334155")
    arrow((1030, 555), (1190, 255), "MySQL metrics")
    d.line((1345, 270, 1345, 360), fill="#334155", width=5)
    d.polygon([(1345, 360), (1335, 342), (1355, 342)], fill="#334155")
    d.line((1345, 600, 1345, 510), fill="#334155", width=5)
    d.polygon([(1345, 510), (1335, 528), (1355, 528)], fill="#334155")
    d.text((930, 735), "Nginx logs  →  Promtail  →  Loki  →  Grafana Explore", anchor="mm", font=small, fill="#334155")
    d.text((800, 835), "frontend   |   backend internal   |   monitoring", anchor="mm", font=body, fill="#17365D")
    im.save(path)
    return path


def make_evidence(path_name, title_text, rows, footer):
    path = FIG_DIR / path_name
    im = Image.new("RGB", (1600, 900), "#F8FAFC")
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1600, 120), fill="#17365D")
    d.text((70, 60), title_text, anchor="lm", font=font(40, True), fill="white")
    y = 170
    for label, value, status in rows:
        rounded_box(d, (70, y, 1530, y + 115), "white")
        d.text((110, y + 35), label, font=font(26, True), fill="#111827")
        d.text((620, y + 35), value, font=font(25), fill="#334155")
        badge = "#D1FAE5" if status == "ĐÃ KIỂM TRA" else "#FEF3C7"
        badge_text = "#065F46" if status == "ĐÃ KIỂM TRA" else "#92400E"
        rounded_box(d, (1210, y + 26, 1490, y + 88), badge, outline=badge, radius=18, width=1)
        d.text((1350, y + 57), status, anchor="mm", font=font(20, True), fill=badge_text)
        y += 135
    d.text((80, 850), footer, font=font(20), fill="#64748B")
    im.save(path)
    return path


ARCH = make_architecture()
PHASE1 = make_evidence(
    "phase1-verification.png",
    "Kết quả kiểm tra WordPress MySQL Nginx",
    [
        ("WordPress", "HTTP 200 qua Nginx và có danh mục sản phẩm", "ĐÃ KIỂM TRA"),
        ("Dữ liệu", "6 sản phẩm publish lưu qua WordPress MySQL", "ĐÃ KIỂM TRA"),
        ("phpMyAdmin", "Trang đăng nhập truy cập được tại cổng 8181", "ĐÃ KIỂM TRA"),
        ("Security headers", "5 header an toàn xuất hiện trên response", "ĐÃ KIỂM TRA"),
    ],
    "Nguồn: kiểm tra runtime Docker Compose ngày 02/10/2026",
)
MONITORING = make_evidence(
    "monitoring-verification.png",
    "Kết quả kiểm tra Prometheus Grafana",
    [
        ("Prometheus", "prometheus, nginx, mysql đều up bằng 1", "ĐÃ KIỂM TRA"),
        ("Container", "4 probe HTTP TCP đều thành công", "ĐÃ KIỂM TRA"),
        ("Nginx", "nginx_up bằng 1", "ĐÃ KIỂM TRA"),
        ("MySQL", "mysql_up bằng 1", "ĐÃ KIỂM TRA"),
        ("Grafana", "3 dashboard metrics provision thành công", "ĐÃ KIỂM TRA"),
    ],
    "Nguồn: Prometheus HTTP API và log provision Grafana",
)
LOGGING = make_evidence(
    "logging-verification.png",
    "Kết quả kiểm tra Loki Promtail LogQL",
    [
        ("Loki", "Endpoint ready trả nội dung ready", "ĐÃ KIỂM TRA"),
        ("Promtail", "Tail access.log và error.log của Nginx", "ĐÃ KIỂM TRA"),
        ("LogQL 1", "{job=\"nginx\"} trả nhiều stream log", "ĐÃ KIỂM TRA"),
        ("LogQL 2", "Lọc GET trả request thật", "ĐÃ KIỂM TRA"),
        ("LogQL 3", "Lọc 404 trả response status 404 thật", "ĐÃ KIỂM TRA"),
    ],
    "Nguồn: Loki query_range API sau khi sinh request HTTP thật",
)
HARDENING = make_evidence(
    "hardening-overview.png",
    "Các biện pháp hardening chính",
    [
        ("Network isolation", "Backend internal và MySQL không public 3306", "ĐÃ KIỂM TRA"),
        ("Secrets", "Mật khẩu ngẫu nhiên không được Git theo dõi", "ĐÃ KIỂM TRA"),
        ("Nginx headers", "X-Frame Options, nosniff, referrer và CSP", "ĐÃ KIỂM TRA"),
        ("Quyền container", "read only, cap drop và no new privileges", "ĐÃ KIỂM TRA"),
        ("Ứng dụng", "Grafana tắt anonymous, WordPress tắt file editor", "ĐÃ KIỂM TRA"),
    ],
    "Cấu hình chi tiết nằm trong docker-compose.yml và nginx/default.conf",
)


doc = Document()
section = doc.sections[0]
section.page_width = Inches(8.5)
section.page_height = Inches(11)
section.top_margin = Inches(0.75)
section.bottom_margin = Inches(0.65)
section.left_margin = Inches(0.8)
section.right_margin = Inches(0.8)

styles = doc.styles
styles["Normal"].font.name = "Arial"
styles["Normal"].font.size = Pt(11.5)
styles["Normal"]._element.rPr.rFonts.set(qn("w:ascii"), "Arial")
styles["Normal"]._element.rPr.rFonts.set(qn("w:hAnsi"), "Arial")
styles["Normal"]._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
styles["Normal"].paragraph_format.space_after = Pt(6)
styles["Normal"].paragraph_format.line_spacing = 1.15

for style_name, size in [("Title", 24), ("Heading 1", 18), ("Heading 2", 14)]:
    style = styles[style_name]
    style.font.name = "Arial"
    style.font.size = Pt(size)
    style.font.color.rgb = BLACK
    style._element.rPr.rFonts.set(qn("w:ascii"), "Arial")
    style._element.rPr.rFonts.set(qn("w:hAnsi"), "Arial")
    style._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    style.paragraph_format.space_before = Pt(10)
    style.paragraph_format.space_after = Pt(7)
    style.paragraph_format.keep_with_next = True


def set_cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=110, start=110, bottom=110, end=110):
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for margin, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{margin}"))
        if node is None:
            node = OxmlElement(f"w:{margin}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_table_borders(table, color=LIGHT_GRAY, size="6"):
    tbl_pr = table._tbl.tblPr
    borders = tbl_pr.first_child_found_in("w:tblBorders")
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tbl_pr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        tag = qn(f"w:{edge}")
        element = borders.find(tag)
        if element is None:
            element = OxmlElement(f"w:{edge}")
            borders.append(element)
        element.set(qn("w:val"), "single")
        element.set(qn("w:sz"), size)
        element.set(qn("w:color"), color)


def add_table(headers, rows, widths=None):
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    hdr = table.rows[0].cells
    for idx, text in enumerate(headers):
        hdr[idx].text = text
        set_cell_shading(hdr[idx], NAVY)
        hdr[idx].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_margins(hdr[idx])
        p = hdr[idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.bold = True
            run.font.color.rgb = RGBColor(255, 255, 255)
            run.font.size = Pt(10)
    for row_idx, row in enumerate(rows):
        cells = table.add_row().cells
        for col_idx, value in enumerate(row):
            cells[col_idx].text = str(value)
            cells[col_idx].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cells[col_idx])
            if row_idx % 2:
                set_cell_shading(cells[col_idx], PALE_BLUE)
            p = cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.size = Pt(9.5)
    if widths:
        for row in table.rows:
            for idx, width in enumerate(widths):
                row.cells[idx].width = Inches(width)
    doc.add_paragraph()
    return table


def add_page_title(text, subtitle=None):
    p = doc.add_paragraph(style="Heading 1")
    p.add_run(text)
    if subtitle:
        s = doc.add_paragraph(subtitle)
        s.alignment = WD_ALIGN_PARAGRAPH.LEFT
        s.runs[0].italic = True


def add_body(text, bold_lead=None):
    p = doc.add_paragraph()
    if bold_lead:
        r = p.add_run(bold_lead)
        r.bold = True
    p.add_run(text)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    return p


def add_bullets(items):
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.add_run(item)


def add_figure(path, caption, width=6.65):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(path), width=Inches(width))
    cap = doc.add_paragraph(caption)
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.runs[0].italic = True
    cap.runs[0].font.size = Pt(9.5)


def page_break():
    doc.add_page_break()


footer = section.footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer.add_run("Báo cáo Đề 3 Website Quảng bá Sản phẩm   ")
fld = OxmlElement("w:fldSimple")
fld.set(qn("w:instr"), "PAGE")
footer._p.append(fld)


# Trang 1 Bìa
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(35)
r = p.add_run("TRƯỜNG ........................................................")
r.bold = True
r.font.size = Pt(14)
p = doc.add_paragraph("KHOA ........................................................")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.runs[0].bold = True
p.runs[0].font.size = Pt(13)

p = doc.add_paragraph(style="Title")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(85)
p.add_run("BÁO CÁO ĐỀ 3")
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("WEBSITE QUẢNG BÁ SẢN PHẨM BẰNG WORDPRESS")
r.bold = True
r.font.size = Pt(20)
p = doc.add_paragraph("Môn Triển khai và Quản trị Hệ thống Phần mềm")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.runs[0].font.size = Pt(14)

doc.add_paragraph()
cover_rows = [
    ("Sinh viên thực hiện", "........................................................"),
    ("Mã số sinh viên", "........................................................"),
    ("Lớp", "........................................................"),
    ("Giảng viên", "........................................................"),
]
table = add_table(["Thông tin", "Nội dung"], cover_rows, [2.0, 4.1])
for row in table.rows[1:]:
    row.cells[0].paragraphs[0].runs[0].bold = True
p = doc.add_paragraph("TP Hồ Chí Minh, tháng 10 năm 2026")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(55)

# Trang 2
page_break()
add_page_title("Tóm tắt báo cáo")
add_body("Báo cáo mô tả việc triển khai website quảng bá sản phẩm bằng WordPress theo đúng phạm vi Đề 3. Hệ thống dùng MySQL làm cơ sở dữ liệu, phpMyAdmin để quản trị, Nginx làm reverse proxy, Prometheus và Grafana để giám sát, Loki và Promtail để tập trung log. Tất cả thành phần chạy bằng Docker Compose trên Docker Desktop.")
add_body("Kết quả kiểm tra cục bộ cho thấy WordPress hoạt động qua Nginx, sáu sản phẩm được lưu trong MySQL, phpMyAdmin truy cập được, các target Prometheus đều UP, Grafana nhận ba dashboard giám sát và Loki trả kết quả cho ba truy vấn LogQL. Secret thật không nằm trong Git. Bước push lên GitHub được giữ lại để người thực hiện kiểm tra đúng tài khoản có tên theo mã số sinh viên trước khi nộp.")
doc.add_paragraph("Nội dung báo cáo", style="Heading 2")
add_table(
    ["Phần", "Nội dung"],
    [
        ("1", "Giới thiệu đề tài"),
        ("2", "Cấu trúc và cách hoạt động"),
        ("3", "Quản lý mã nguồn"),
        ("4", "WordPress MySQL phpMyAdmin"),
        ("5", "Nginx Reverse Proxy"),
        ("6", "Prometheus Grafana"),
        ("7", "Loki Promtail LogQL"),
        ("8", "Hardening"),
        ("9", "Kết quả và demo"),
    ],
    [0.8, 5.3],
)

# Trang 3
page_break()
add_page_title("1 Giới thiệu đề tài")
add_body("Mục tiêu của Đề 3 là triển khai một website có chức năng và có cơ sở dữ liệu, không phải trang HTML tĩnh. Website giới thiệu sản phẩm được xây dựng trên WordPress để người quản trị có thể thêm, sửa và xuất bản nội dung. MySQL lưu bài viết, metadata và cấu hình; phpMyAdmin cung cấp giao diện kiểm tra dữ liệu.")
add_body("Phạm vi kỹ thuật gồm quản lý mã nguồn bằng Git, Nginx reverse proxy, Prometheus và Grafana, Loki và LogQL, cùng các biện pháp hardening cơ bản. Các thành phần hỗ trợ như exporter và Blackbox Exporter chỉ phục vụ yêu cầu giám sát, không làm thay đổi yêu cầu chính của đề.")
doc.add_paragraph("Mục tiêu triển khai", style="Heading 2")
add_bullets([
    "Website chạy ổn định tại cổng 8180 và chỉ đi qua Nginx.",
    "Dữ liệu sản phẩm được quản lý trong WordPress và lưu tại MySQL.",
    "Prometheus thu metrics container, Nginx và MySQL; Grafana hiển thị dashboard tương ứng.",
    "Promtail gửi log Nginx tới Loki; Grafana truy vấn được bằng LogQL.",
    "Ít nhất bốn biện pháp hardening được cấu hình và có thể giải thích khi demo.",
])
add_table(["Hạng mục", "Cổng máy chủ"], [("Website Nginx", "8180"), ("phpMyAdmin", "8181"), ("Grafana", "3001"), ("Prometheus", "9091"), ("Loki", "3101"), ("MySQL", "Không public")], [3.1, 3.0])

# Trang 4
page_break()
add_page_title("2 Cấu trúc và cách hoạt động của hệ thống")
add_figure(ARCH, "Hình 1 Kiến trúc các service và luồng dữ liệu")
add_body("Request từ người dùng vào cổng 8180 được Nginx chuyển tiếp tới WordPress. WordPress kết nối MySQL bằng tài khoản ứng dụng và secret được mount tại runtime. phpMyAdmin nằm trên cả mạng frontend và backend để người dùng truy cập giao diện ở cổng 8181 nhưng MySQL vẫn không public ra máy chủ.")
add_body("Prometheus scrape Nginx Exporter, MySQL Exporter và Blackbox Exporter. Blackbox Exporter kiểm tra trực tiếp HTTP hoặc TCP của bốn container chính nên không cần truy cập Docker socket. Grafana dùng Prometheus làm datasource metrics và Loki làm datasource log. Promtail chỉ đọc volume log Nginx và đẩy từng dòng log tới Loki.")

# Trang 5
page_break()
add_page_title("3 Quản lý mã nguồn trên Git")
add_body("Repository chứa Docker Compose, cấu hình Nginx, Prometheus, Grafana, Loki, Promtail, plugin WordPress, script tạo secret, tài liệu hướng dẫn và báo cáo. `.gitignore` loại `.env`, secret thật, ảnh QA và các ảnh chụp có thể chứa dữ liệu cục bộ.")
add_table(
    ["Commit", "Nội dung"],
    [
        ("Commit 1", "WordPress MySQL phpMyAdmin và Nginx reverse proxy"),
        ("Commit 2", "Prometheus Grafana và ba dashboard giám sát"),
        ("Commit 3", "Loki Promtail hardening README minh chứng và báo cáo"),
    ],
    [1.25, 4.85],
)
add_body("Ba commit được tách theo đúng thứ tự của đề để người chấm dễ đối chiếu. Repository chưa được push tự động vì yêu cầu nộp bài bắt buộc tài khoản GitHub phải đặt tên theo mã số sinh viên. Người thực hiện cần kiểm tra tên tài khoản, tạo remote và cho phép push trước khi hoàn tất minh chứng GitHub.")
doc.add_paragraph("Cấu trúc nguồn cần kiểm tra trên GitHub", style="Heading 2")
add_bullets(["docker-compose.yml và .env.example", "nginx prometheus grafana loki promtail", "wordpress/de3-product-showcase", "README.md và docs", "Lịch sử đúng ba commit có ý nghĩa"])

# Trang 6
page_break()
add_page_title("4 WordPress MySQL và phpMyAdmin")
add_figure(PHASE1, "Hình 2 Kết quả kiểm tra giai đoạn ứng dụng và cơ sở dữ liệu")
add_body("Plugin `DE3 Product Showcase` đăng ký custom post type `de3_product`. Khi plugin được kích hoạt lần đầu, hàm seed tạo sáu sản phẩm và lưu tên, nội dung, mô tả, mã, giá, đường dẫn hình ảnh trong các bảng chuẩn của WordPress. Shortcode hiển thị sản phẩm theo dạng lưới và trang chi tiết lấy dữ liệu từ post meta.")
add_body("Service `wordpress-init` dùng WP CLI để cài WordPress, kích hoạt plugin, cấu hình permalink và URL cổng 8180. Service này kết thúc với exit code 0 sau khi hoàn tất. MySQL dùng health check trước khi WordPress hoặc phpMyAdmin khởi động.")
add_table(["Kiểm tra", "Kết quả"], [("WordPress qua Nginx", "HTTP 200"), ("Sản phẩm publish", "6"), ("Kết nối database", "Thành công"), ("phpMyAdmin", "Trang đăng nhập hoạt động")], [2.4, 3.7])

# Trang 7
page_break()
add_page_title("5 Nginx Reverse Proxy")
add_body("WordPress chỉ expose cổng 80 trong mạng Compose. Cổng 8180 của máy chủ được ánh xạ duy nhất vào Nginx, vì vậy mọi truy cập website đi qua reverse proxy. Nginx chuyển tiếp Host, địa chỉ IP, giao thức và cổng về WordPress, đồng thời ghi access log và error log vào volume dùng chung với Promtail.")
doc.add_paragraph("Security headers", style="Heading 2")
add_table(
    ["Header", "Giá trị"],
    [
        ("X Frame Options", "SAMEORIGIN"),
        ("X Content Type Options", "nosniff"),
        ("Referrer Policy", "strict-origin-when-cross-origin"),
        ("Permissions Policy", "Tắt camera microphone geolocation"),
        ("Content Security Policy", "Giới hạn frame object và base URI"),
    ],
    [2.5, 3.6],
)
add_body("Kiểm tra response HTTP cho thấy toàn bộ header trên xuất hiện và website trả mã 200. Nginx còn dùng filesystem chỉ đọc, tmpfs cho thư mục cache và run, chỉ giữ các capability cần thiết để bind cổng và chuyển người dùng worker.")

# Trang 8
page_break()
add_page_title("6 Prometheus và Grafana")
add_figure(MONITORING, "Hình 3 Kết quả kiểm tra metrics và dashboard")
add_body("Nginx Exporter đọc `stub_status` ở cổng nội bộ 8080. MySQL Exporter đăng nhập bằng tài khoản exporter chỉ có quyền quan sát. Blackbox Exporter kiểm tra HTTP của Nginx, WordPress và phpMyAdmin, đồng thời kiểm tra TCP của MySQL. Phương án này đáp ứng giám sát khả năng hoạt động của container mà không mount Docker socket.")
add_body("Prometheus scrape mỗi 15 giây và giữ dữ liệu bảy ngày. Grafana tự provision datasource Prometheus cùng ba dashboard theo đúng ba nhóm container, web và database. Các query runtime cho thấy `nginx_up`, `mysql_up` và bốn series `probe_success` đều bằng 1.")

# Trang 9
page_break()
add_page_title("7 Dashboard giám sát")
add_table(
    ["Dashboard", "Panel chính", "Metrics"],
    [
        ("DE3 Container Monitoring", "Số container truy cập được và lịch sử availability", "probe_success"),
        ("DE3 Nginx Monitoring", "Trạng thái, kết nối active, tổng request, request rate", "nginx_up và nginx_http_requests_total"),
        ("DE3 MySQL Monitoring", "Trạng thái, kết nối, dung lượng database, query rate", "mysql_up và mysql_global_status"),
    ],
    [1.9, 2.7, 1.8],
)
add_body("Dashboard được lưu dưới dạng JSON trong repository và được Grafana nạp tự động khi container khởi động. Cách provision này giúp kết quả demo có thể tái tạo trên máy khác mà không phải tạo dashboard bằng tay.")
doc.add_paragraph("Cách tạo dữ liệu khi demo", style="Heading 2")
add_bullets([
    "Tải lại website nhiều lần để tăng `nginx_http_requests_total`.",
    "Mở WordPress Admin và phpMyAdmin để tạo thêm kết nối ứng dụng.",
    "Chọn khoảng thời gian 15 phút gần nhất trong Grafana.",
    "Chụp riêng từng dashboard để đối chiếu ba yêu cầu monitoring.",
])
add_body("Prometheus Targets phải được chụp khi tất cả endpoint ở trạng thái UP. Nếu vừa khởi động stack, chờ ít nhất hai chu kỳ scrape trước khi chụp.")

# Trang 10
page_break()
add_page_title("8 Loki Promtail và LogQL")
add_figure(LOGGING, "Hình 4 Kết quả kiểm tra hệ thống log tập trung")
add_body("Nginx ghi log thật vào volume `nginx_logs`. Promtail mount volume này ở chế độ chỉ đọc, dùng biểu thức chính quy để tách method và status thành label rồi đẩy log tới Loki. Loki dùng TSDB schema v13, filesystem storage và retention bảy ngày.")
add_table(["Truy vấn", "Mục đích"], [("{job=\"nginx\"}", "Hiển thị toàn bộ log Nginx"), ("{job=\"nginx\"} |= \"GET\"", "Lọc request HTTP GET"), ("{job=\"nginx\"} |~ \"404\"", "Tìm log có chuỗi 404"), ("{job=\"nginx\", status=\"404\"}", "Xác nhận response status 404")], [3.1, 3.0])
add_body("Request tới endpoint REST không tồn tại đã trả HTTP 404. Sau năm giây, Loki trả đúng dòng access log với label `status=404`, chứng minh Promtail gửi log thật và LogQL truy vấn được kết quả.")

# Trang 11
page_break()
add_page_title("9 Hardening")
add_figure(HARDENING, "Hình 5 Các biện pháp hardening đã áp dụng")
add_body("Bốn biện pháp nên trình bày đầu tiên khi giáo viên hỏi là: MySQL không public cổng; backend internal; mật khẩu mạnh lưu ngoài Git; security headers Nginx. Các biện pháp bổ sung gồm filesystem chỉ đọc, bỏ capabilities, `no-new-privileges`, giới hạn quyền tài khoản exporter, tắt anonymous Grafana và tắt WordPress file editor.")
add_body("Secret được sinh bằng bộ tạo số ngẫu nhiên mật mã của .NET. Compose mount secret vào `/run/secrets` và ứng dụng đọc bằng biến `_FILE` hoặc file cấu hình cục bộ. `.gitignore` chặn toàn bộ nội dung thư mục secrets ngoài `.gitkeep`.")
add_table(["Rủi ro", "Biện pháp giảm thiểu"], [("Truy cập trực tiếp database", "Không ánh xạ cổng 3306 và backend internal"), ("Lộ mật khẩu trên Git", "Secret sinh cục bộ và được ignore"), ("Clickjacking và MIME sniffing", "Security headers Nginx"), ("Quyền container quá rộng", "Read only, cap drop, no new privileges"), ("Sửa mã nguồn từ Admin", "DISALLOW_FILE_EDIT")], [2.45, 3.65])

# Trang 12
page_break()
add_page_title("10 Kết quả triển khai và kết luận")
add_table(
    ["Tiêu chí", "Trạng thái"],
    [
        ("Mã nguồn và 3 commit", "Đã kiểm tra cục bộ, chờ push GitHub"),
        ("WordPress MySQL phpMyAdmin", "Đã kiểm tra runtime"),
        ("Nginx và security headers", "Đã kiểm tra runtime"),
        ("Prometheus và Grafana", "Đã kiểm tra target và dashboard"),
        ("Loki Promtail LogQL", "Đã kiểm tra với log thật"),
        ("Hardening", "Đã kiểm tra cấu hình và cổng"),
        ("Compose và tài liệu", "Đã hoàn thiện"),
    ],
    [3.25, 2.85],
)
add_body("Hệ thống hoàn thành các thành phần kỹ thuật của Đề 3 và chạy thống nhất bằng Docker Compose. Nội dung sản phẩm có thể quản lý trong WordPress; dữ liệu được lưu tại MySQL; Nginx bảo vệ và chuyển tiếp truy cập; Prometheus, Grafana, Loki và Promtail cung cấp metrics và log phục vụ vận hành.")
doc.add_paragraph("Việc cần làm trước khi nộp", style="Heading 2")
add_bullets([
    "Điền thông tin sinh viên và giảng viên trên trang bìa.",
    "Kiểm tra tên tài khoản GitHub đúng mã số sinh viên, sau đó push đúng ba commit.",
    "Chụp đủ 19 ảnh theo `docs/screenshots/README.md` và thay các ảnh minh họa kỹ thuật nếu giảng viên yêu cầu ảnh giao diện trực tiếp.",
    "Chạy lại kịch bản demo và không hiển thị secret trên màn hình.",
])
add_body("Sau khi hoàn tất ba bước trên, repository, báo cáo và minh chứng có thể dùng để đối chiếu trực tiếp bảy tiêu chí trong thang điểm.")

doc.core_properties.title = "Báo cáo Đề 3 Website Quảng bá Sản phẩm bằng WordPress"
doc.core_properties.subject = "Triển khai và Quản trị Hệ thống Phần mềm"
doc.core_properties.author = "Sinh viên thực hiện Đề 3"
doc.save(OUT_FILE)
print(OUT_FILE)
print(f"paragraphs={len(doc.paragraphs)}")
print(f"tables={len(doc.tables)}")
print(f"inline_shapes={len(doc.inline_shapes)}")
print(f"explicit_page_breaks={doc._element.xml.count('w:type=\"page\"')}")

