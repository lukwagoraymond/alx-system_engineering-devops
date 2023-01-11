# Make passwordAuthentication and add new private key
file_line { 'replace passwordAuthentication':
    path    => '/etc/ssh/ssh_config',
    replace => true,
    ensure  => 'present',
    line    => 'PasswordAuthentication no',
    match   => 'PasswordAuthentication yes',
}

file_line { 'add private key':
    path    => '/etc/ssh/ssh_config',
    ensure  => 'present',
    line    => 'IndentityFile ~/.ssh/school',
}
