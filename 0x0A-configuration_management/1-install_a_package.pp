# This script installs flask 
exec { 'install_flask':
command => '/usr/bin/pip3 install flask==2.1.0'
path    => ['/usr/bin/','/usr/local/bin/','/bin']
}

