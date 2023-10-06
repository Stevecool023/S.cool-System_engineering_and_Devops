# Declaration to ensure that "nginx" webserver package is installed and running.
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}
