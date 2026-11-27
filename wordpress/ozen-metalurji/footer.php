<?php
/** Özen Metalurji — alt kısım */
?>
</main>
<?php
if ( ozen_show_cta() ) {
	echo ozen_partial( 'cta' ); // phpcs:ignore
}
echo ozen_partial( 'footer' ); // phpcs:ignore
wp_footer();
?>
</body>
</html>
