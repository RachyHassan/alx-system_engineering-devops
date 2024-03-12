# Enable user holberton to login and open files without error

# Increase hard file limit for holberton user
exec { 'increase-hard-file-limit':
    command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",
    path    => '/usr/local/bin/:/bin/',
}

# Increase soft limit
exec { 'increase-soft-file-limit':
    command => "sed -i '/^holberton soft/s/4/50000/' /etc/security/limits.conf",
    path    => '/usr/local/bin/:/bin/',
}
