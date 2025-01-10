# This script kills a running process
exec { 'kill_process':
command => 'usr/bin/pkill -f killmenow',
}

