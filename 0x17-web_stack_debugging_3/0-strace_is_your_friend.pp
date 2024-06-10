# Puppet manifest to fix a bug in wp-setting.php
 
 exec { 'fix the php extension issue':
 command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
 path => '/ur/local/bin/:/bin/'
 }