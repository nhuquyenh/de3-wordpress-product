<?php
if (!defined('ABSPATH')) {
    exit;
}

$products = de3_get_showcase_products(3);
$visuals = de3_get_product_visuals($products, 3);
$template_dir = plugin_dir_path(__FILE__);
require $template_dir . 'partials/header.php';
?>
<section class="de3-page-hero de3-page-hero--about">
    <div class="de3-container">
        <span class="de3-eyebrow"><i></i>Về chúng tôi</span>
        <h1>Giới thiệu Aurora</h1>
        <p>Không gian sản phẩm hiện đại, nơi thông tin rõ ràng kết hợp cùng trải nghiệm trực quan.</p>
    </div>
</section>

<section class="de3-section de3-story">
    <div class="de3-container de3-story__grid">
        <div class="de3-story__visual">
            <?php foreach ($visuals as $index => $visual) : ?>
                <img class="de3-story__image de3-story__image--<?php echo esc_attr((string) ($index + 1)); ?>" src="<?php echo esc_url($visual['image']); ?>" alt="<?php echo esc_attr($visual['title']); ?>">
            <?php endforeach; ?>
        </div>
        <div class="de3-story__content">
            <span class="de3-kicker">Câu chuyện Aurora</span>
            <h2>Giới thiệu sản phẩm bằng một trải nghiệm dễ hiểu và đáng tin cậy</h2>
            <p>Aurora là website giới thiệu và quảng bá các sản phẩm nổi bật, được xây dựng trên WordPress và quản lý dữ liệu bằng MySQL.</p>
            <p>Mục tiêu của chúng tôi là giúp người dùng khám phá sản phẩm nhanh chóng thông qua hình ảnh đồng nhất, nội dung cô đọng và bố cục thân thiện trên mọi thiết bị.</p>
            <a class="de3-button de3-button--primary" href="<?php echo esc_url(home_url('/san-pham/')); ?>">Khám phá sản phẩm <span aria-hidden="true">→</span></a>
        </div>
    </div>
</section>

<section class="de3-section de3-values">
    <div class="de3-container">
        <div class="de3-section-heading">
            <div><span class="de3-kicker">Giá trị cốt lõi</span><h2>Điều Aurora hướng đến</h2></div>
        </div>
        <div class="de3-values__grid">
            <article><span>01</span><h3>Thông tin rõ ràng</h3><p>Mỗi sản phẩm có mã, mô tả và giá tham khảo dễ theo dõi.</p></article>
            <article><span>02</span><h3>Sản phẩm chọn lọc</h3><p>Danh mục tập trung vào những sản phẩm phù hợp với lối sống hiện đại.</p></article>
            <article><span>03</span><h3>Trải nghiệm trực quan</h3><p>Giao diện responsive giúp khám phá thuận tiện trên mọi thiết bị.</p></article>
        </div>
    </div>
</section>
<?php
wp_reset_postdata();
require $template_dir . 'partials/footer.php';
?>
