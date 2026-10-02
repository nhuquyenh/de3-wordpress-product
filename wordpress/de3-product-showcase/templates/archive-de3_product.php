<?php
if (!defined('ABSPATH')) {
    exit;
}

$products = de3_get_showcase_products(-1);
$template_dir = plugin_dir_path(__FILE__);
require $template_dir . 'partials/header.php';
?>
<section class="de3-page-hero">
    <div class="de3-container">
        <span class="de3-eyebrow"><i></i>Bộ sưu tập Aurora</span>
        <h1>Sản phẩm của Aurora</h1>
        <p>Khám phá các sản phẩm được quản lý trực tiếp trên WordPress và lưu trữ an toàn trong MySQL.</p>
    </div>
</section>
<section class="de3-section de3-products">
    <div class="de3-container">
        <div class="de3-grid">
            <?php while ($products->have_posts()) : $products->the_post(); ?>
                <?php echo de3_get_product_card(get_the_ID()); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
            <?php endwhile; ?>
        </div>
        <?php wp_reset_postdata(); ?>
    </div>
</section>
<?php require $template_dir . 'partials/footer.php'; ?>
