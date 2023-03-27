# Edit a file using puppet
include stdlib

file_line { 'Set Identity file':
  ensure => present,
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^\s*IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/ssh_config',
}

file_line { 'Remove password Authentication':
  ensure => present,
  line   => '    PasswordAuthentication no',
  match  => '^\s*PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
}
