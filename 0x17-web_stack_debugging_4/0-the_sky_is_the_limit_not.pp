# Using Puppet to up the ULIMIT in the /etc/default/nginx file
exec { 'update_ulimit':
      command =>  'sed -i \'s/-n 15/-n 15000/\' /etc/default/nginx'\
                  '&& service nginx restart',
      path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}

