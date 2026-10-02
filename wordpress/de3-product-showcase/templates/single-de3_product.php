<?php
if (!defined('ABSPATH')) {
    exit;
}

$template_dir = plugin_dir_path(__FILE__);
require $template_dir . 'partials/header.php';

while (have_posts()) :
    the_post();
    $product_id = get_the_ID();
    $image = get_post_meta($product_id, 'de3_image', true);
    $price = get_post_meta($product_id, 'de3_price', true);
    $sku = get_post_meta($product_id, 'de3_sku', true);
    ?>
    <section class="de3-product-detail">
        <div class="de3-container">
            <a class="de3-back-link" href="<?php echo esc_url(home_url('/san-pham/')); ?>">← Quay lại danh sách sản phẩm</a>
            <div class="de3-product-detail__grid">
                <div class="de3-product-detail__image">
                    <img src="<?php echo esc_url($image); ?>" alt="<?php echo esc_attr(get_the_title()); ?>">
                </div>
                <div class="de3-product-detail__content">
                    <span class="de3-card__sku"><?php echo esc_html($sku); ?></span>
                    <h1><?php the_title(); ?></h1>
                    <p class="de3-product-detail__lead"><?php echo esc_html(get_the_excerpt()); ?></p>
                    <strong class="de3-product-detail__price"><?php echo esc_html($price); ?></strong>
                    <div class="de3-product-detail__copy"><?php echo wp_kses_post(get_post_field('post_content', $product_id)); ?></div>
                    <a class="de3-button de3-button--primary" href="<?php echo esc_url(home_url('/lien-he/')); ?>">Liên hệ tìm hiểu <span aria-hidden="true">→</span></a>
                </div>
            </div>
        </div>
    </section>
    <?php
endwhile;

require $template_dir . 'partials/footer.php';
