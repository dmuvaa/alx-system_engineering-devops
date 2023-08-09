#puppet file for apache
class fix_apache_error {

  # Ensure correct permission for WordPress configuration
  file { '/var/www/html/wordpress/wp-config.php':
    ensure  => 'file',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0644',
  }

  # Ensure Apache is restarted if the file's permissions are corrected
  ~> Service['apache2']:
    ensure    => 'running',
    enable    => true,
    subscribe => File['/var/www/html/wordpress/wp-config.php'],
  }

}

include fix_apache_error
