# Enable the user holberton to login and open files without error

# Increase hard file limit for Holberton user
exec { 'increase file limit hard':
    command  => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
    provider => shell,
}

exec { 'increase file limit soft':
    command  => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
    provider => shell,
}
