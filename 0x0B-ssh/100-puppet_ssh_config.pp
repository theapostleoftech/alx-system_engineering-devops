# Configure the SSH client configuration file
file { '/home/vagrant/.ssh/config':
  ensure => 'file',
  owner  => 'vagrant',
  group  => 'vagrant',
  mode   => '0600',
}

# Disable password authentication
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/home/vagrant/.ssh/config',
  line   => 'PasswordAuthentication no',
}

# Declare the identity file
file_line { 'Declare identity file':
  ensure => present,
  path   => '/home/vagrant/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}