#This script creates school file in tmp path
file { '/tmp/school':
ensure  => 'file',
content => 'I love Puppet',
group   => 'www-data',
owner   => 'www-data',
mode    => '0744',
}

