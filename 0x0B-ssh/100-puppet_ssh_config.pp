# Configuration file to login without PasswordAuthentication

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'vagrant',
  group   => 'vagrant',
  mode    => '0600',
  content => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}

file_line { 'Turn off passwd auth':
  path => '/home/ubuntu/.ssh/config',
  line => '  PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path => '/home/ubuntu/.ssh/config',
  line => '  IdentityFile ~/.ssh/school',
}
