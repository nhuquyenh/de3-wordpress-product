<?php
/**
 * Public-facing templates and reusable presentation helpers.
 */

if (!defined('ABSPATH')) {
    exit;
}

function de3_is_public_showcase_view() {
    return is_front_page()
        || is_post_type_archive('de3_product')
        || is_singular('de3_product')
        || is_page(['danh-sach-san-pham', 'gioi-thieu', 'lien-he']);
}

function de3_enqueue_public_assets() {
    $asset_dir = plugin_dir_path(dirname(__FILE__)) . 'assets/';
    wp_enqueue_style(
        'de3-public-site',
        plugin_dir_url(dirname(__FILE__)) . 'assets/public.css',
        [],
        (string) filemtime($asset_dir . 'public.css')
    );
    wp_enqueue_script(
        'de3-public-site',
        plugin_dir_url(dirname(__FILE__)) . 'assets/public.js',
        [],
        (string) filemtime($asset_dir . 'public.js'),
        true
    );
}

function de3_maybe_enqueue_public_assets() {
    if (!is_admin() && de3_is_public_showcase_view()) {
        de3_enqueue_public_assets();
    }
}
add_action('wp_enqueue_scripts', 'de3_maybe_enqueue_public_assets');

function de3_public_template($template) {
    $template_dir = plugin_dir_path(dirname(__FILE__)) . 'templates/';

    if (is_front_page()) {
        return $template_dir . 'front-page.php';
    }

    if (is_post_type_archive('de3_product') || is_page('danh-sach-san-pham')) {
        return $template_dir . 'archive-de3_product.php';
    }

    if (is_singular('de3_product')) {
        return $template_dir . 'single-de3_product.php';
    }

    if (is_page('gioi-thieu')) {
        return $template_dir . 'page-gioi-thieu.php';
    }

    if (is_page('lien-he')) {
        return $template_dir . 'page-lien-he.php';
    }

    return $template;
}
add_filter('template_include', 'de3_public_template', 99);

function de3_get_showcase_products($limit = 6) {
    return new WP_Query([
        'post_type' => 'de3_product',
        'post_status' => 'publish',
        'posts_per_page' => $limit,
        'orderby' => 'menu_order',
        'order' => 'ASC',
    ]);
}

function de3_get_product_card($product_id) {
    $image = get_post_meta($product_id, 'de3_image', true);
    $price = get_post_meta($product_id, 'de3_price', true);
    $sku = get_post_meta($product_id, 'de3_sku', true);
    $title = get_the_title($product_id);
    $permalink = get_permalink($product_id);
    $excerpt = get_the_excerpt($product_id);

    ob_start();
    ?>
    <article class="de3-card">
        <a class="de3-card__media" href="<?php echo esc_url($permalink); ?>" aria-label="<?php echo esc_attr('Xem ' . $title); ?>">
            <img src="<?php echo esc_url($image); ?>" alt="<?php echo esc_attr($title); ?>" loading="lazy">
            <span class="de3-card__favorite" aria-hidden="true">♡</span>
        </a>
        <div class="de3-card__body">
            <span class="de3-card__sku"><?php echo esc_html($sku); ?></span>
            <h3><a href="<?php echo esc_url($permalink); ?>"><?php echo esc_html($title); ?></a></h3>
            <p class="de3-card__description"><?php echo esc_html($excerpt); ?></p>
            <div class="de3-card__footer">
                <strong class="de3-card__price"><?php echo esc_html($price); ?></strong>
                <a class="de3-text-link" href="<?php echo esc_url($permalink); ?>">Xem chi tiết <span aria-hidden="true">→</span></a>
            </div>
        </div>
    </article>
    <?php
    return ob_get_clean();
}

function de3_get_product_visuals($products, $limit = 3) {
    $visuals = [];

    if (!$products instanceof WP_Query) {
        return $visuals;
    }

    foreach (array_slice($products->posts, 0, $limit) as $product) {
        $visuals[] = [
            'title' => get_the_title($product),
            'image' => get_post_meta($product->ID, 'de3_image', true),
            'price' => get_post_meta($product->ID, 'de3_price', true),
        ];
    }

    return $visuals;
}
