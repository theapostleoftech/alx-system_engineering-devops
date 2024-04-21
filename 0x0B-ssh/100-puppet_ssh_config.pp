# Configuration file to login without PasswordAuthentication

file { '/home/vagrant/.ssh/config':
  ensure  => file,
  owner   => 'vagrant',
  group   => 'vagrant',
  mode    => '0600',
  content => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}

file_line { 'Turn off passwd auth':
  path => '/home/vagrant/.ssh/config',
  line => '  PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path => '/home/vagrant/.ssh/config',
  line => '  IdentityFile ~/.ssh/school',
}
