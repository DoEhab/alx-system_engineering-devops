#update the file limit for holberton user
exec { 'holberton-hard-limit':
  command => 'grep -q "^holberton hard nofile" /etc/security/limits.conf || echo "holberton hard nofile 50000" >> /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
}

#update the file limit for holberton user
exec { 'holberton-soft-limit':
  command => 'grep -q "^holberton soft nofile" /etc/security/limits.conf || echo "holberton soft nofile 50000" >> /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
}
