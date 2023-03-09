# Increases the amount of traffic an Nginx server can handle

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
    command  => 'sed -i "s/15/4096" /etc/default/nginx',
    provider => shell,
}

# Restart Nginx
exec { 'restorenginx':
    command  => 'service nginx restart',
    provider => shell,
    require  => Exec['fix--for-nginx'],
}
