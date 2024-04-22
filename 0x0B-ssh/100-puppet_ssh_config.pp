# Configuration file to login without PasswordAuthentication

# Ensure the SSH configuration file exists
file { '/home/vagrant/.ssh/config':
  ensure  => file,
  owner   => 'vagrant',
  group   => 'vagrant',
  mode    => '0600',
  require => File['/home/vagrant/.ssh'],
}

# Disable password authentication in the SSH client configuration
file_line { 'Turn off passwd auth':
  path    => '/home/vagrant/.ssh/config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
  replace => true,
  require => File['/home/vagrant/.ssh/config'],
}

# Declare the identity file in the SSH client configuration
file_line { 'Declare identity file':
  path    => '/home/vagrant/.ssh/config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^IdentityFile',
  replace => true,
  require => File['/home/vagrant/.ssh/config'],
}
