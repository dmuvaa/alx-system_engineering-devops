#Install Flask using puppet
package { 'Flask':
  ensure   => '2.0.1'
  provider => 'pip3'
}
