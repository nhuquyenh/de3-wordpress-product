<?php
/**
 * Plugin Name: DE3 Product Showcase
 * Description: Nội dung và chức năng quảng bá sản phẩm cho thương hiệu Aurora.
 * Version: 2.0.0
 * Author: Aurora
 */

if (!defined('ABSPATH')) {
    exit;
}

require_once plugin_dir_path(__FILE__) . 'includes/public-site.php';

function de3_register_product_type() {
    register_post_type('de3_product', [
        'labels' => [
            'name' => 'Sản phẩm',
            'singular_name' => 'Sản phẩm',
            'add_new_item' => 'Thêm sản phẩm',
            'edit_item' => 'Sửa sản phẩm',
        ],
        'public' => true,
        'has_archive' => true,
        'rewrite' => ['slug' => 'san-pham'],
        'menu_icon' => 'dashicons-products',
        'supports' => ['title', 'editor', 'excerpt'],
        'show_in_rest' => true,
    ]);
}
add_action('init', 'de3_register_product_type');

function de3_aurora_products() {
    return [
        ['Bình giữ nhiệt Aurora', 'Giữ nóng 8 giờ, giữ lạnh 12 giờ, dung tích 600 ml, thiết kế hiện đại.', '329.000 đ', 'aurora.svg'],
        ['Tai nghe Nova', 'Tai nghe không dây gọn nhẹ, thời lượng pin đến 24 giờ.', '1.290.000 đ', 'nova.svg'],
        ['Sạc không dây Zen', 'Sạc nhanh, thiết kế mỏng, tương thích nhiều thiết bị.', '490.000 đ', 'zen.svg'],
        ['Bàn phím cơ Alpha', 'Trải nghiệm gõ mượt mà, độ bền cao, đèn RGB.', '890.000 đ', 'alpha.svg'],
        ['Chuột không dây M5', 'Thiết kế công thái học, độ nhạy cao, pin lâu.', '450.000 đ', 'm5.svg'],
        ['Loa Bluetooth Echo', 'Âm thanh mạnh mẽ, nhỏ gọn, thời lượng pin đến 18 giờ.', '690.000 đ', 'echo.svg'],
    ];
}

function de3_sync_aurora_content() {
    de3_register_product_type();

    $products = de3_aurora_products();
    $existing_products = get_posts([
        'post_type' => 'de3_product',
        'post_status' => 'any',
        'posts_per_page' => -1,
        'orderby' => 'menu_order',
        'order' => 'ASC',
    ]);

    foreach ($products as $index => $product) {
        $post_data = [
            'post_type' => 'de3_product',
            'post_status' => 'publish',
            'post_title' => $product[0],
            'post_name' => sanitize_title($product[0]),
            'post_excerpt' => $product[1],
            'post_content' => '<p>' . esc_html($product[1]) . '</p><p>Sản phẩm được quản lý trực tiếp trong WordPress và lưu tại MySQL.</p>',
            'menu_order' => $index,
        ];

        if (isset($existing_products[$index])) {
            $post_data['ID'] = $existing_products[$index]->ID;
            $post_id = wp_update_post($post_data);
        } else {
            $post_id = wp_insert_post($post_data);
        }

        if (!is_wp_error($post_id)) {
            update_post_meta($post_id, 'de3_price', $product[2]);
            update_post_meta($post_id, 'de3_image', plugin_dir_url(__FILE__) . 'assets/' . $product[3]);
            update_post_meta($post_id, 'de3_sku', 'AUR-' . str_pad((string) ($index + 1), 3, '0', STR_PAD_LEFT));
        }
    }

    $product_page = get_page_by_path('danh-sach-san-pham');
    if (!$product_page) {
        $product_page_id = wp_insert_post([
            'post_type' => 'page',
            'post_status' => 'publish',
            'post_title' => 'Sản phẩm Aurora',
            'post_name' => 'danh-sach-san-pham',
            'post_content' => '[de3_product_catalog]',
        ]);
    } else {
        $product_page_id = $product_page->ID;
        wp_update_post(['ID' => $product_page_id, 'post_title' => 'Sản phẩm Aurora', 'post_status' => 'publish']);
    }

    $about_page = get_page_by_path('gioi-thieu');
    if (!$about_page) {
        wp_insert_post([
            'post_type' => 'page',
            'post_status' => 'publish',
            'post_title' => 'Giới thiệu Aurora',
            'post_name' => 'gioi-thieu',
            'post_content' => '<p>Aurora là không gian giới thiệu những sản phẩm hiện đại với thông tin rõ ràng và trải nghiệm trực quan.</p>',
        ]);
    } else {
        wp_update_post([
            'ID' => $about_page->ID,
            'post_title' => 'Giới thiệu Aurora',
            'post_status' => 'publish',
            'post_content' => '<p>Aurora là không gian giới thiệu những sản phẩm hiện đại với thông tin rõ ràng và trải nghiệm trực quan.</p>',
        ]);
    }

    $contact_page = get_page_by_path('lien-he');
    if (!$contact_page) {
        wp_insert_post([
            'post_type' => 'page',
            'post_status' => 'publish',
            'post_title' => 'Liên hệ Aurora',
            'post_name' => 'lien-he',
            'post_content' => '<p>Liên hệ Aurora để tìm hiểu thêm về các sản phẩm đang được giới thiệu.</p>',
        ]);
    }

    $home_page = get_page_by_path('trang-chu');
    if (!$home_page) {
        $home_id = wp_insert_post([
            'post_type' => 'page',
            'post_status' => 'publish',
            'post_title' => 'Aurora',
            'post_name' => 'trang-chu',
            'post_content' => '[de3_product_catalog]',
        ]);
    } else {
        $home_id = $home_page->ID;
        wp_update_post(['ID' => $home_id, 'post_title' => 'Aurora', 'post_status' => 'publish']);
    }

    $sample_page = get_page_by_path('sample-page');
    if ($sample_page) {
        wp_update_post(['ID' => $sample_page->ID, 'post_status' => 'draft']);
    }

    update_option('blogname', 'Aurora');
    update_option('blogdescription', 'Không gian sản phẩm hiện đại');
    update_option('show_on_front', 'page');
    update_option('page_on_front', $home_id);
}

function de3_seed_content() {
    de3_sync_aurora_content();

    flush_rewrite_rules();
}
register_activation_hook(__FILE__, 'de3_seed_content');

function de3_run_aurora_content_migration() {
    if (get_option('de3_aurora_content_version') === '2.0.1') {
        return;
    }

    de3_sync_aurora_content();
    flush_rewrite_rules(false);
    update_option('de3_aurora_content_version', '2.0.1');
}
add_action('init', 'de3_run_aurora_content_migration', 20);

function de3_product_catalog_shortcode() {
    de3_enqueue_public_assets();

    $query = new WP_Query([
        'post_type' => 'de3_product',
        'post_status' => 'publish',
        'posts_per_page' => 12,
        'orderby' => 'menu_order',
        'order' => 'ASC',
    ]);

    ob_start();
    echo '<div class="de3-grid">';
    while ($query->have_posts()) {
        $query->the_post();
        echo de3_get_product_card(get_the_ID()); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
    }
    echo '</div>';
    wp_reset_postdata();
    return ob_get_clean();
}
add_shortcode('de3_product_catalog', 'de3_product_catalog_shortcode');

function de3_product_detail($content) {
    if (!is_singular('de3_product') || !in_the_loop() || !is_main_query()) {
        return $content;
    }
    $image = get_post_meta(get_the_ID(), 'de3_image', true);
    $price = get_post_meta(get_the_ID(), 'de3_price', true);
    $sku = get_post_meta(get_the_ID(), 'de3_sku', true);
    return '<p><img style="max-width:640px;width:100%;border-radius:12px" src="' . esc_url($image) . '" alt="' . esc_attr(get_the_title()) . '"></p>'
        . '<p><strong>Mã sản phẩm:</strong> ' . esc_html($sku) . '</p>'
        . '<p><strong>Giá tham khảo:</strong> ' . esc_html($price) . '</p>' . $content;
}
add_filter('the_content', 'de3_product_detail');

