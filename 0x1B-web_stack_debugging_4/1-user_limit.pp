# Increase the open file limit for the holberton user
exec { 'change-os-configuration-for-holberton-user':
  command => 'echo "holberton soft nofile 4096\nholberton hard nofile 8192" > /etc/security/limits.d/holberton.conf',
  path    => '/usr/bin:/usr/sbin:/bin',
  creates => '/etc/security/limits.d/holberton.conf',
}