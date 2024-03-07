#!/usr/bin/env bash
# A script to make changes to configuration files using puppet

file {'/etc/ssh/ssh_config':
    ensure => present,
}

file_line { 'Turn off passwd auth':
    path  => '/etc/ssh/ssh_config',
    line  => 'PasswordAuthentication no',
    match => '^#PasswordAuthentication',
}

file_line { 'Declare identity file':
    path  => '/etc/ssh/ssh_config',
    line  => 'IdentityFile ~/.ssh/school',
    match => '^#IdentityFile',
}