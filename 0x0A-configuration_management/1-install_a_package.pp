# install flask from pip3

$package = 'flask'
package { $package:
    ensure      => '2.1.0',
    provider    => 'pip3',
}


$package = 'werkzeug'
package { $package:
    ensure      => '2.1.1',
    provider    => 'pip3',
}