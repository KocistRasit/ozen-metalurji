<?php
/**
 * Genel şablon: tema içeriği olan sayfalar için hazır içeriği, diğer yazı ve sayfalar için
 * WordPress editöründeki içeriği gösterir.
 */
get_header();
$ozen_key = ozen_current_key();
if ( $ozen_key && ozen_has_content( $ozen_key ) ) {
	echo ozen_content( $ozen_key ); // phpcs:ignore
} else {
	?>
	<section class="phero"><div class="phero-glow" aria-hidden="true"></div><div class="wrap">
		<p class="eyebrow"><?php echo is_singular( 'post' ) ? 'Bilgi merkezi' : 'Özen Metalurji'; ?></p>
		<h1><?php echo is_singular() ? esc_html( get_the_title() ) : wp_kses_post( get_the_archive_title() ?: 'Bilgi Merkezi' ); ?></h1>
		<?php if ( is_singular( 'post' ) ) : ?><p class="meta"><?php echo esc_html( get_the_date() ); ?></p><?php endif; ?>
	</div></section>
	<section class="section"><div class="wrap narrow prose">
	<?php
	if ( have_posts() ) {
		while ( have_posts() ) {
			the_post();
			if ( is_singular() ) {
				the_content();
			} else {
				echo '<article class="post-card" style="margin-bottom:1rem"><h2><a href="' . esc_url( get_permalink() ) . '">' . esc_html( get_the_title() ) . '</a></h2>';
				the_excerpt();
				echo '</article>';
			}
		}
		the_posts_pagination();
	}
	?>
	</div></section>
	<?php
}
get_footer();
