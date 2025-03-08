#update the file limit for holberton user
exec { 'holberton-hard-limit':
  command => 'sed -i "/holberton hard/s/4/40000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin'],
}

#update the file limit for holberton user
exec { 'holberton-soft-limit':
  command => 'sed -i "/holberton soft/s/4/40000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin'],
}
