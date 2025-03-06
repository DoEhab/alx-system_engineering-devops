#fix limit value
exec { 'fix-nginx-limit':
  command => 'sed -i "s/15/4000/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
}

# Restart nginx
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => ['/etc/init.d'],
}
