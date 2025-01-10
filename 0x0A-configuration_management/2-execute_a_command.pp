# This script kills a running process
exec { 'kill_process':
command => '/usr/bin/pkill -f killmenow',
path    => '/usr/bin/:/bin/:usr/local/bin/',
}

