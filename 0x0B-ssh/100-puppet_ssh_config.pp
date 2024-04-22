# Configuration file to login without PasswordAuthentication

# Ensure the SSH configuration file exists
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  require => File['/home/ubuntu/.ssh'],
}

# Disable password authentication in the SSH client configuration
file_line { 'Turn off passwd auth':
  path    => '/home/ubuntu/.ssh/config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
  replace => true,
  require => File['/home/ubuntu/.ssh/config'],
}

# Declare the identity file in the SSH client configuration
file_line { 'Declare identity file':
  path    => '/home/ubuntu/.ssh/config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^IdentityFile',
  replace => true,
  require => File['/home/ubuntu/.ssh/config'],
}
