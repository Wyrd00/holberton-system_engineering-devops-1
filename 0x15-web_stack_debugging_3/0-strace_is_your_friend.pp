# Using Puppet to create manifest to replace correct line in wp-settings.php
exec { 'debug_with_sed':
      cwd     => '/var/www/html/',
      command => 'sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php',
      path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
