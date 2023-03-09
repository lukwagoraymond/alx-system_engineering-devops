# Increases the amount of traffic an Nginx server can handle

# Increase the ULIMIT of the default file
exec { 'ulimit':
  command  => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 5000\"/g" /etc/default/nginx',
  provider => shell,
}

# Restart Nginx
exec { 'restorenginx':
  command  => 'service nginx restart',
  provider => shell,
  require  => Exec['ulimit'],
}
