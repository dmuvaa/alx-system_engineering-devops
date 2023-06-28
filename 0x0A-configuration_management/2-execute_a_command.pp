#kill a process using exec
exec { 'killkillmenow':
  command => '/usr/bin/pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin'],
}
