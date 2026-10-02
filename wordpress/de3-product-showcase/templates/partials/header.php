<!doctype html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <?php wp_head(); ?>
</head>
<body <?php body_class('de3-public-site'); ?>>
<?php wp_body_open(); ?>
<a class="de3-skip-link" href="#noi-dung-chinh">Chuyển đến nội dung</a>
<header class="de3-header" data-de3-header>
    <div class="de3-container de3-header__inner">
        <a class="de3-brand" href="<?php echo esc_url(home_url('/')); ?>" aria-label="Aurora - Trang chủ">
            <span class="de3-brand__mark" aria-hidden="true">
                <svg viewBox="0 0 32 32" role="img"><path d="M25.5 5.5C15.2 5.4 7.8 10.2 7.5 19.1c-.1 3.2 1.8 6.2 5.2 7.4 7.3 2.6 13.7-4 12.8-21Z"/><path d="M7 27c3.7-6.3 8.1-10.7 14.8-14.2"/></svg>
            </span>
            <span class="de3-brand__copy"><b>Aurora</b><small>Không gian sản phẩm hiện đại</small></span>
        </a>

        <button class="de3-menu-toggle" type="button" aria-expanded="false" aria-controls="de3-primary-nav">
            <span></span><span></span><span></span>
            <span class="screen-reader-text">Mở menu</span>
        </button>

        <nav class="de3-nav" id="de3-primary-nav" aria-label="Điều hướng chính">
            <a href="<?php echo esc_url(home_url('/')); ?>">Trang chủ</a>
            <a href="<?php echo esc_url(home_url('/san-pham/')); ?>">Sản phẩm</a>
            <a href="<?php echo esc_url(home_url('/gioi-thieu/')); ?>">Giới thiệu</a>
            <a class="de3-nav__contact" href="<?php echo esc_url(home_url('/lien-he/')); ?>">Liên hệ</a>
        </nav>
    </div>
</header>
<main id="noi-dung-chinh">
