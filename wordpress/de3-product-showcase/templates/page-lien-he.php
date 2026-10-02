<?php
if (!defined('ABSPATH')) {
    exit;
}

$template_dir = plugin_dir_path(__FILE__);
require $template_dir . 'partials/header.php';
?>
<section class="de3-page-hero de3-page-hero--contact">
    <div class="de3-container">
        <span class="de3-eyebrow"><i></i>Kết nối cùng Aurora</span>
        <h1>Liên hệ với chúng tôi</h1>
        <p>Aurora luôn sẵn sàng cung cấp thêm thông tin và giải đáp thắc mắc về sản phẩm.</p>
    </div>
</section>

<section class="de3-section de3-contact-page">
    <div class="de3-container de3-contact-page__grid">
        <div class="de3-contact-details">
            <span class="de3-kicker">Thông tin liên hệ</span>
            <h2>Chúng tôi rất vui khi được lắng nghe bạn</h2>
            <p>Hãy kết nối với Aurora qua các thông tin dưới đây hoặc để lại lời nhắn trong biểu mẫu minh họa.</p>
            <ul>
                <li><span aria-hidden="true">✉</span><div><small>Email</small><a href="mailto:aurora@example.com">aurora@example.com</a></div></li>
                <li><span aria-hidden="true">☎</span><div><small>Điện thoại</small><a href="tel:+84123456789">+84 123 456 789</a></div></li>
                <li><span aria-hidden="true">⌖</span><div><small>Địa chỉ</small><strong>Thái Nguyên, Việt Nam</strong></div></li>
            </ul>
        </div>
        <form class="de3-contact-form" aria-label="Biểu mẫu liên hệ minh họa">
            <div class="de3-form-row">
                <label>Họ và tên<input type="text" name="name" placeholder="Nhập họ và tên"></label>
                <label>Email<input type="email" name="email" placeholder="email@example.com"></label>
            </div>
            <label>Chủ đề<input type="text" name="subject" placeholder="Bạn muốn tìm hiểu điều gì?"></label>
            <label>Lời nhắn<textarea name="message" rows="5" placeholder="Nhập nội dung cần trao đổi"></textarea></label>
            <button class="de3-button de3-button--primary" type="button">Gửi thông tin <span aria-hidden="true">→</span></button>
            <small>Biểu mẫu dùng để minh họa giao diện, chưa gửi email thật.</small>
        </form>
    </div>
</section>
<?php require $template_dir . 'partials/footer.php'; ?>
