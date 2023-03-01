# Fixes typo `phpp` extensions to `php` in the wordpress file `wp-settings.php`

exec { 'wordpress_fix':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
}
