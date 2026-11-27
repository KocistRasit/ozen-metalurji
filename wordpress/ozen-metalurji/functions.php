<?php
/**
 * Özen Metalurji teması.
 *
 * - Sayfa içerikleri content/ klasöründen gelir (tek kaynak: depo içindeki src/ üreticisi).
 * - Tema ilk etkinleştirildiğinde tüm sayfalar, sayfa hiyerarşisi ve ana sayfa ayarı otomatik kurulur.
 * - "Önizleme modu" (varsayılan AÇIK): noindex + robots.txt Disallow + site haritası kapalı.
 *   Yayına alırken: Ayarlar > Özen Metalurji > "Önizleme modu" kutusunu kaldırın.
 * - SEO eklentisi (Yoast / Rank Math) kuruluysa başlık ve açıklama onlara bırakılır, şema (JSON-LD) tema tarafından verilir.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'OZEN_VER', '1.0.0' );
define( 'OZEN_DIR', get_template_directory() );
define( 'OZEN_URI', get_template_directory_uri() );

/* ------------------------------------------------------------------ yardımcılar */

function ozen_preview() {
	return (bool) get_option( 'ozen_onizleme', 1 );
}

function ozen_seo_plugin() {
	return defined( 'WPSEO_VERSION' ) || class_exists( 'RankMath' ) || defined( 'AIOSEO_VERSION' );
}

function ozen_fill( $html ) {
	$home = trailingslashit( home_url( '/' ) );
	$hidden = wp_nonce_field( 'ozen_teklif', '_ozen_nonce', true, false ) . '<input type="hidden" name="action" value="ozen_teklif">';
	return strtr(
		$html,
		array(
			'[[B]]'           => esc_url( $home ),
			'[[A]]'           => esc_url( OZEN_URI . '/assets/' ),
			'[[S]]'           => esc_url( $home ),
			'[[FORM_HIDDEN]]' => $hidden,
			'[[FORM]]'        => esc_url( admin_url( 'admin-post.php' ) ),
		)
	);
}

function ozen_partial( $name ) {
	$f = OZEN_DIR . '/partials/' . $name . '.html';
	return file_exists( $f ) ? ozen_fill( file_get_contents( $f ) ) : ''; // phpcs:ignore
}

function ozen_has_content( $key ) {
	return file_exists( OZEN_DIR . '/content/' . $key . '.html' );
}

function ozen_content( $key ) {
	$f = OZEN_DIR . '/content/' . $key . '.html';
	return file_exists( $f ) ? ozen_fill( file_get_contents( $f ) ) : ''; // phpcs:ignore
}

function ozen_meta( $key ) {
	static $cache = array();
	if ( ! isset( $cache[ $key ] ) ) {
		$f             = OZEN_DIR . '/content/' . $key . '.json';
		$cache[ $key ] = file_exists( $f ) ? json_decode( file_get_contents( $f ), true ) : null; // phpcs:ignore
	}
	return $cache[ $key ];
}

/** Geçerli isteğe karşılık gelen içerik anahtarı: ana sayfa = home, alt sayfalar = ebeveyn__cocuk */
function ozen_current_key() {
	if ( is_404() ) {
		return '404';
	}
	if ( is_front_page() ) {
		return 'home';
	}
	if ( is_page() ) {
		$uri = get_page_uri( get_queried_object_id() );
		return str_replace( '/', '__', $uri );
	}
	return '';
}

function ozen_body_class() {
	$m = ozen_meta( ozen_current_key() );
	return ( $m && ! empty( $m['body_class'] ) ) ? array( $m['body_class'] ) : array();
}

function ozen_show_cta() {
	$k = ozen_current_key();
	if ( ! $k ) {
		return true;
	}
	$m = ozen_meta( $k );
	return $m ? ! empty( $m['cta'] ) : true;
}

/* ------------------------------------------------------------------ kurulum */

add_action(
	'after_setup_theme',
	function () {
		add_theme_support( 'title-tag' );
		add_theme_support( 'post-thumbnails' );
		add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );
		add_theme_support( 'responsive-embeds' );
	}
);

add_action(
	'wp_enqueue_scripts',
	function () {
		wp_enqueue_style( 'ozen-fonts', 'https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&family=IBM+Plex+Mono:wght@500&display=swap', array(), null ); // phpcs:ignore
		wp_enqueue_style( 'ozen', OZEN_URI . '/assets/css/site.css', array(), OZEN_VER );
		wp_enqueue_script( 'ozen', OZEN_URI . '/assets/js/site.js', array(), OZEN_VER, array( 'strategy' => 'defer', 'in_footer' => true ) );
		// Klasik tema: blok kütüphanesi stilleri gerekmiyorsa kaldır (hız).
		if ( ! is_singular( 'post' ) ) {
			wp_dequeue_style( 'wp-block-library' );
			wp_dequeue_style( 'global-styles' );
			wp_dequeue_style( 'classic-theme-styles' );
		}
	}
);

add_filter(
	'wp_resource_hints',
	function ( $urls, $rel ) {
		if ( 'preconnect' === $rel ) {
			$urls[] = 'https://fonts.googleapis.com';
			$urls[] = array( 'href' => 'https://fonts.gstatic.com', 'crossorigin' );
		}
		return $urls;
	},
	10,
	2
);

// Emoji betiklerini kaldır (hız).
remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );
remove_action( 'wp_head', 'wp_generator' );

/** Tema etkinleştirildiğinde sayfaları oluştur ve ayarları yap. */
add_action( 'after_switch_theme', 'ozen_install' );
function ozen_install() {
	$list = json_decode( file_get_contents( OZEN_DIR . '/content/_pages.json' ), true ); // phpcs:ignore
	$ids  = array();
	foreach ( $list as $p ) {
		$parent = ( $p['parent'] && isset( $ids[ $p['parent'] ] ) ) ? $ids[ $p['parent'] ] : 0;
		$path   = ( 'home' === $p['key'] ) ? 'ana-sayfa' : str_replace( '__', '/', $p['key'] );
		$exists = get_page_by_path( $path );
		if ( $exists ) {
			$ids[ $p['key'] ] = $exists->ID;
			continue;
		}
		$ids[ $p['key'] ] = wp_insert_post(
			array(
				'post_type'    => 'page',
				'post_status'  => 'publish',
				'post_title'   => wp_strip_all_tags( $p['title'] ),
				'post_name'    => $p['slug'],
				'post_parent'  => $parent,
				'post_content' => '<!-- İçerik Özen Metalurji temasından gelir (wp-content/themes/ozen-metalurji/content/). -->',
			)
		);
	}
	// Yeni kurulumdaki örnek içerikleri çöp kutusuna taşı (kalıcı silme yapılmaz).
	foreach ( array( 'sample-page', 'ornek-sayfa' ) as $s ) {
		$sp = get_page_by_path( $s );
		if ( $sp ) {
			wp_trash_post( $sp->ID );
		}
	}
	foreach ( array( 'hello-world', 'merhaba-dunya' ) as $s ) {
		$hp = get_page_by_path( $s, OBJECT, 'post' );
		if ( $hp ) {
			wp_trash_post( $hp->ID );
		}
	}
	if ( ! empty( $ids['home'] ) ) {
		update_option( 'show_on_front', 'page' );
		update_option( 'page_on_front', $ids['home'] );
	}
	if ( ! get_option( 'permalink_structure' ) ) {
		update_option( 'permalink_structure', '/%postname%/' );
	}
	if ( false === get_option( 'ozen_onizleme', false ) ) {
		add_option( 'ozen_onizleme', 1 );
	}
	update_option( 'blog_public', ozen_preview() ? 0 : 1 );
	update_option( 'blogname', 'Özen Metalurji' );
	update_option( 'blogdescription', 'Alüminyum, pirinç, bronz, zamak ve anot döküm — 1974\'ten beri' );
	flush_rewrite_rules();
}

/* ------------------------------------------------------------------ SEO / AEO / GEO */

add_filter(
	'pre_get_document_title',
	function ( $t ) {
		if ( ozen_seo_plugin() ) {
			return $t;
		}
		$m = ozen_meta( ozen_current_key() );
		return $m ? $m['title'] : $t;
	},
	20
);

add_action(
	'wp_head',
	function () {
		$key = ozen_current_key();
		$m   = $key ? ozen_meta( $key ) : null;
		if ( ! ozen_seo_plugin() && $m ) {
			$url = ( 'home' === $key ) ? home_url( '/' ) : get_permalink();
			echo '<meta name="description" content="' . esc_attr( $m['description'] ) . "\">\n";
			echo '<meta property="og:locale" content="tr_TR"><meta property="og:type" content="' . esc_attr( $m['og_type'] ) . '"><meta property="og:site_name" content="Özen Metalurji">' . "\n";
			echo '<meta property="og:title" content="' . esc_attr( $m['title'] ) . '"><meta property="og:description" content="' . esc_attr( $m['description'] ) . '"><meta property="og:url" content="' . esc_url( $url ) . '">' . "\n";
			echo '<meta property="og:image" content="' . esc_url( OZEN_URI . '/assets/img/og-ozen-metalurji.jpg' ) . '"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">' . "\n";
		}
		echo '<meta name="theme-color" content="#111317">' . "\n";
		echo '<meta name="geo.region" content="TR-37"><meta name="geo.placename" content="Abana, Kastamonu"><meta name="geo.position" content="41.970276;34.004076"><meta name="ICBM" content="41.970276, 34.004076">' . "\n";
		echo '<link rel="icon" href="' . esc_url( OZEN_URI . '/assets/img/favicon.svg' ) . '" type="image/svg+xml"><link rel="apple-touch-icon" href="' . esc_url( OZEN_URI . '/assets/img/apple-touch-icon.png' ) . '">' . "\n";
		echo '<link rel="alternate" type="text/plain" title="LLM özeti" href="' . esc_url( home_url( '/llms.txt' ) ) . '">' . "\n";

		// JSON-LD: kurum + iki konum + sayfaya özel şema
		$base  = json_decode( file_get_contents( OZEN_DIR . '/content/_base_schema.json' ), true ); // phpcs:ignore
		$graph = array_merge( $base, ( $m && ! empty( $m['schema'] ) ) ? $m['schema'] : array() );
		if ( is_singular( 'post' ) ) {
			$graph[] = array(
				'@type'         => 'Article',
				'headline'      => get_the_title(),
				'datePublished' => get_the_date( 'c' ),
				'dateModified'  => get_the_modified_date( 'c' ),
				'author'        => array( '@id' => '[[S]]#organizasyon' ),
				'publisher'     => array( '@id' => '[[S]]#organizasyon' ),
				'mainEntityOfPage' => get_permalink(),
			);
		}
		$json = wp_json_encode( array( '@context' => 'https://schema.org', '@graph' => $graph ), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
		$json = str_replace( array( '[[S]]', '[[B]]' ), trailingslashit( home_url( '/' ) ), $json );
		echo '<script type="application/ld+json">' . $json . "</script>\n"; // phpcs:ignore
	},
	5
);

/* Önizleme modu: arama motorlarına kapalı */
add_filter(
	'wp_robots',
	function ( $robots ) {
		if ( ozen_preview() ) {
			return array( 'noindex' => true, 'nofollow' => true, 'noarchive' => true, 'nosnippet' => true, 'noimageindex' => true );
		}
		if ( is_404() || is_search() ) {
			$robots['noindex'] = true;
		}
		$robots['max-image-preview'] = 'large';
		return $robots;
	}
);

add_action(
	'send_headers',
	function () {
		if ( ozen_preview() ) {
			header( 'X-Robots-Tag: noindex, nofollow', true );
		}
	}
);

add_filter(
	'robots_txt',
	function ( $out, $public ) {
		if ( ozen_preview() ) {
			return "# Önizleme modu — arama motorlarına kapalı\nUser-agent: *\nDisallow: /\n";
		}
		$out  = "User-agent: *\nDisallow: /wp-admin/\nAllow: /wp-admin/admin-ajax.php\n\n";
		$out .= "# Yapay zekâ arama botlarına izin (GEO)\nUser-agent: GPTBot\nAllow: /\nUser-agent: OAI-SearchBot\nAllow: /\nUser-agent: ChatGPT-User\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: Claude-SearchBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\nUser-agent: Applebot-Extended\nAllow: /\n\n";
		$out .= 'Sitemap: ' . home_url( '/wp-sitemap.xml' ) . "\n";
		return $out;
	},
	99,
	2
);

add_filter(
	'wp_sitemaps_enabled',
	function ( $on ) {
		return ozen_preview() ? false : $on;
	}
);
// Site haritasından kullanıcı listesini çıkar.
add_filter(
	'wp_sitemaps_add_provider',
	function ( $provider, $name ) {
		return 'users' === $name ? false : $provider;
	},
	10,
	2
);

/* llms.txt ve llms-full.txt */
add_action(
	'init',
	function () {
		$path = wp_parse_url( isset( $_SERVER['REQUEST_URI'] ) ? wp_unslash( $_SERVER['REQUEST_URI'] ) : '', PHP_URL_PATH ); // phpcs:ignore
		$home = wp_parse_url( home_url( '/' ), PHP_URL_PATH );
		$home = $home ? trailingslashit( $home ) : '/';
		foreach ( array( 'llms.txt', 'llms-full.txt' ) as $file ) {
			if ( $path === $home . $file ) {
				header( 'Content-Type: text/plain; charset=utf-8' );
				if ( ozen_preview() ) {
					header( 'X-Robots-Tag: noindex', true );
				}
				echo str_replace( '[[S]]', trailingslashit( home_url( '/' ) ), file_get_contents( OZEN_DIR . '/' . $file ) ); // phpcs:ignore
				exit;
			}
		}
	},
	1
);

/* ------------------------------------------------------------------ teklif formu */

add_action( 'admin_post_nopriv_ozen_teklif', 'ozen_teklif' );
add_action( 'admin_post_ozen_teklif', 'ozen_teklif' );
function ozen_teklif() {
	$back = wp_get_referer() ? wp_get_referer() : home_url( '/iletisim/' );
	$back = remove_query_arg( 'gonderildi', $back );
	$back = preg_replace( '/#.*$/', '', $back );
	$ok   = isset( $_POST['_ozen_nonce'] ) && wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST['_ozen_nonce'] ) ), 'ozen_teklif' );
	if ( ! $ok || ! empty( $_POST['website'] ) || empty( $_POST['kvkk'] ) ) {
		wp_safe_redirect( add_query_arg( 'gonderildi', '0', $back ) . '#teklif' );
		exit;
	}
	$f = array(
		'Ad soyad'   => sanitize_text_field( wp_unslash( $_POST['ad'] ?? '' ) ),
		'Firma'      => sanitize_text_field( wp_unslash( $_POST['firma'] ?? '' ) ),
		'Telefon'    => sanitize_text_field( wp_unslash( $_POST['telefon'] ?? '' ) ),
		'E-posta'    => sanitize_email( wp_unslash( $_POST['eposta'] ?? '' ) ),
		'Döküm türü' => sanitize_text_field( wp_unslash( $_POST['hizmet'] ?? '' ) ),
		'Adet'       => sanitize_text_field( wp_unslash( $_POST['adet'] ?? '' ) ),
		'Mesaj'      => sanitize_textarea_field( wp_unslash( $_POST['mesaj'] ?? '' ) ),
	);
	if ( ! $f['Ad soyad'] || ! $f['Telefon'] || ! is_email( $f['E-posta'] ) || ! $f['Mesaj'] ) {
		wp_safe_redirect( add_query_arg( 'gonderildi', '0', $back ) . '#teklif' );
		exit;
	}
	$body = '';
	foreach ( $f as $k => $v ) {
		$body .= $k . ': ' . $v . "\n";
	}
	$attach = array();
	if ( ! empty( $_FILES['dosya']['name'] ) && $_FILES['dosya']['size'] <= 10 * MB_IN_BYTES ) {
		require_once ABSPATH . 'wp-admin/includes/file.php';
		$up = wp_handle_upload(
			$_FILES['dosya'], // phpcs:ignore
			array(
				'test_form' => false,
				'mimes'     => array(
					'pdf'      => 'application/pdf',
					'jpg|jpeg' => 'image/jpeg',
					'png'      => 'image/png',
					'zip'      => 'application/zip',
					'dwg'      => 'application/octet-stream',
					'dxf'      => 'application/octet-stream',
					'step|stp' => 'application/octet-stream',
				),
			)
		);
		if ( empty( $up['error'] ) && ! empty( $up['file'] ) ) {
			$attach[] = $up['file'];
		}
	}
	$to   = apply_filters( 'ozen_teklif_alici', 'info@ozenmetalurji.com.tr' );
	$sent = wp_mail( $to, 'Web sitesi teklif talebi: ' . ( $f['Firma'] ? $f['Firma'] : $f['Ad soyad'] ), $body, array( 'Reply-To: ' . $f['Ad soyad'] . ' <' . $f['E-posta'] . '>' ), $attach );
	foreach ( $attach as $a ) {
		wp_delete_file( $a );
	}
	wp_safe_redirect( add_query_arg( 'gonderildi', $sent ? '1' : '0', $back ) . '#teklif' );
	exit;
}

/* ------------------------------------------------------------------ ayarlar sayfası */

add_action(
	'admin_menu',
	function () {
		add_options_page( 'Özen Metalurji', 'Özen Metalurji', 'manage_options', 'ozen', 'ozen_settings_page' );
	}
);
add_action(
	'admin_init',
	function () {
		register_setting(
			'ozen',
			'ozen_onizleme',
			array(
				'type'              => 'integer',
				'sanitize_callback' => function ( $v ) {
					$v = $v ? 1 : 0;
					update_option( 'blog_public', $v ? 0 : 1 );
					return $v;
				},
				'default'           => 1,
			)
		);
	}
);
function ozen_settings_page() {
	?>
	<div class="wrap"><h1>Özen Metalurji tema ayarları</h1>
	<form method="post" action="options.php"><?php settings_fields( 'ozen' ); ?>
	<table class="form-table"><tr><th scope="row">Önizleme modu</th><td>
	<label><input type="checkbox" name="ozen_onizleme" value="1" <?php checked( ozen_preview() ); ?>> Site arama motorlarına kapalı (noindex, robots.txt Disallow, site haritası kapalı)</label>
	<p class="description">Yayına alırken bu kutuyu kaldırın. Böylece sayfalar indekslenir, <code>/wp-sitemap.xml</code> ve yapay zekâ botları için izinler açılır, <code>/llms.txt</code> yayında kalır.</p>
	</td></tr></table><?php submit_button(); ?></form>
	<h2>Kurulumu yeniden çalıştır</h2><p>Silinen sayfaları yeniden oluşturmak için temayı başka bir temaya geçirip tekrar etkinleştirin.</p></div>
	<?php
}

add_action(
	'admin_notices',
	function () {
		if ( ozen_preview() && current_user_can( 'manage_options' ) ) {
			echo '<div class="notice notice-warning"><p><strong>Özen Metalurji:</strong> Önizleme modu açık, site arama motorlarına kapalı. Yayına alırken <a href="' . esc_url( admin_url( 'options-general.php?page=ozen' ) ) . '">Ayarlar &gt; Özen Metalurji</a> ekranından kapatın.</p></div>';
		}
	}
);

/* Önizleme modu değişince WordPress'in "arama motorlarını engelle" ayarını eşitle. */
add_action(
	'update_option_ozen_onizleme',
	function ( $old, $new ) {
		update_option( 'blog_public', $new ? 0 : 1 );
	},
	10,
	2
);
