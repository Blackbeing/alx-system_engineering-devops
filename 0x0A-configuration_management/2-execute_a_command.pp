# Execute a command, kill process

exec { 'pkill':
  command => '/usr/bin/pkill killmenow',
}
