# Fix wordpress issue

exec { 'fix-server':
  command => "/bin/sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
