# fixes typo 'phpp' (should be 'php')

exec { 'wordpress-fix':
  command  => 'sudo sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  provider => shell,
}
