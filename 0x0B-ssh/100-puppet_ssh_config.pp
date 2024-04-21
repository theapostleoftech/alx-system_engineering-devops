# Configure the SSH client configuration file
file { '/home/ubuntu/.ssh/config':
  ensure => 'file',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
}

# Disable password authentication
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => 'PasswordAuthentication no',
}

# Declare the identity file
file_line { 'Declare identity file':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}