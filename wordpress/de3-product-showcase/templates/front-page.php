<?php
/**
 * Modern public landing page for the product showcase.
 */

if (!defined('ABSPATH')) {
    exit;
}

$products = de3_get_showcase_products(6);
$visuals = de3_get_product_visuals($products, 3);
$template_dir = plugin_dir_path(__FILE__);

require $template_dir . 'partials/header.php';
?>

<section class="de3-hero">
    <div class="de3-hero__orb de3-hero__orb--one"></div>
    <div class="de3-hero__orb de3-hero__orb--two"></div>
    <div class="de3-container de3-hero__grid">
        <div class="de3-hero__content">
            <span class="de3-eyebrow"><i></i>Sản phẩm chất lượng</span>
            <h1>Khám phá sản phẩm<br>phù hợp với <span>phong cách</span><br>của bạn</h1>
            <p>Bộ sưu tập sản phẩm được chọn lọc với thiết kế hiện đại, thông tin rõ ràng và trải nghiệm trực quan.</p>
            <div class="de3-actions">
                <a class="de3-button de3-button--primary" href="#san-pham">Xem sản phẩm <span aria-hidden="true">→</span></a>
                <a class="de3-button de3-button--secondary" href="<?php echo esc_url(home_url('/gioi-thieu/')); ?>">Tìm hiểu thêm</a>
            </div>
            <div class="de3-hero__proof">
                <div><strong>✓</strong><span>Giao hàng nhanh</span></div>
                <div><strong>✓</strong><span>Thông tin rõ ràng</span></div>
                <div><strong>✓</strong><span>Hỗ trợ 24/7</span></div>
            </div>
        </div>

        <div class="de3-hero__visual" aria-label="Bộ sưu tập sản phẩm nổi bật">
            <div class="de3-visual__backdrop"></div>
            <?php foreach ($visuals as $index => $visual) : ?>
                <article class="de3-floating-product de3-floating-product--<?php echo esc_attr((string) ($index + 1)); ?>">
                    <span class="de3-floating-product__label"><?php echo $index === 0 ? 'Nổi bật' : 'Khám phá'; ?></span>
                    <img src="<?php echo esc_url($visual['image']); ?>" alt="<?php echo esc_attr($visual['title']); ?>">
                    <div><strong><?php echo esc_html($visual['title']); ?></strong><span><?php echo esc_html($visual['price']); ?></span></div>
                </article>
            <?php endforeach; ?>
            <span class="de3-visual__note"><i>✓</i> Lựa chọn hiện đại từ Aurora</span>
        </div>
    </div>
</section>

<section class="de3-section de3-products" id="san-pham">
    <div class="de3-container">
        <div class="de3-section-heading">
            <div>
                <span class="de3-kicker">Bộ sưu tập</span>
                <h2>Sản phẩm nổi bật</h2>
                <p>Những lựa chọn được yêu thích dành cho bạn</p>
            </div>
            <a class="de3-text-link de3-text-link--top" href="<?php echo esc_url(get_post_type_archive_link('de3_product')); ?>">Xem tất cả sản phẩm <span aria-hidden="true">→</span></a>
        </div>

        <div class="de3-grid">
            <?php if ($products->have_posts()) : ?>
                <?php while ($products->have_posts()) : $products->the_post(); ?>
                    <?php echo de3_get_product_card(get_the_ID()); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
                <?php endwhile; ?>
            <?php else : ?>
                <p>Danh mục sản phẩm đang được cập nhật.</p>
            <?php endif; ?>
        </div>
        <?php wp_reset_postdata(); ?>
    </div>
</section>

<section class="de3-section de3-benefits" aria-label="Điểm nổi bật">
    <div class="de3-container de3-benefits__grid">
        <article><span class="de3-benefit-icon" aria-hidden="true">✓</span><div><h3>Sản phẩm chọn lọc</h3><p>Thông tin sản phẩm rõ ràng và dễ theo dõi.</p></div></article>
        <article><span class="de3-benefit-icon" aria-hidden="true">◇</span><div><h3>Thiết kế hiện đại</h3><p>Trải nghiệm trực quan trên mọi thiết bị.</p></div></article>
        <article><span class="de3-benefit-icon" aria-hidden="true">→</span><div><h3>Giao hàng nhanh</h3><p>Đảm bảo an toàn và đúng thời gian.</p></div></article>
        <article><span class="de3-benefit-icon" aria-hidden="true">♡</span><div><h3>Hỗ trợ tận tâm</h3><p>Luôn sẵn sàng giải đáp mọi thắc mắc.</p></div></article>
    </div>
</section>

<section class="de3-section de3-about" id="gioi-thieu">
    <div class="de3-container de3-about__grid">
        <div class="de3-about__visual">
            <div class="de3-about__panel">
                <?php foreach (array_slice($visuals, 0, 2) as $visual) : ?>
                    <img src="<?php echo esc_url($visual['image']); ?>" alt="<?php echo esc_attr($visual['title']); ?>" loading="lazy">
                <?php endforeach; ?>
            </div>
            <div class="de3-about__stat"><strong>6+</strong><span>Sản phẩm<br>nổi bật</span></div>
        </div>
        <div class="de3-about__content">
            <span class="de3-kicker">Về chúng tôi</span>
            <h2>Aurora – Không gian sản phẩm hiện đại</h2>
            <p>Aurora là website giới thiệu và quảng bá các sản phẩm nổi bật, được xây dựng trên WordPress và quản lý dữ liệu bằng MySQL.</p>
            <p>Chúng tôi mang đến những sản phẩm được chọn lọc với thiết kế hiện đại, thông tin rõ ràng và trải nghiệm trực quan cho người dùng.</p>
            <a class="de3-button de3-button--dark" href="<?php echo esc_url(home_url('/gioi-thieu/')); ?>">Tìm hiểu thêm <span aria-hidden="true">→</span></a>
        </div>
    </div>
</section>

<section class="de3-section de3-cta">
    <div class="de3-container">
        <div class="de3-cta__inner">
            <div>
                <span class="de3-kicker de3-kicker--light">Bắt đầu ngay hôm nay</span>
                <h2>Bạn đã sẵn sàng khám phá?</h2>
                <p>Khám phá ngay toàn bộ sản phẩm để tìm lựa chọn phù hợp với bạn.</p>
            </div>
            <a class="de3-button de3-button--white" href="<?php echo esc_url(home_url('/san-pham/')); ?>">Xem tất cả sản phẩm <span aria-hidden="true">→</span></a>
        </div>
    </div>
</section>

<?php require $template_dir . 'partials/footer.php'; ?>
