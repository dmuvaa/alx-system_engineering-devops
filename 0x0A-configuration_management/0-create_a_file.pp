#creating a puppet file
#details given

file { 'resource title':
  path    => #/tmp/school
  mode    => #0744
  'owner'   => #www-data
  group   => #www-data
  content => #I love Puppet
}
