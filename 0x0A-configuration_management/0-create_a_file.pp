# Creating a file in Puppet
file { '/tmp/school':
    ensure  => file,
    owner   => www-data,
    mode    => '0744',
    group   => www-data,
    content => 'I love Puppet',
}