#installing flask from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  name     => 'flask',
}

package { 'werkzeug':
  ensure   => '0.16.1',
  provider => 'pip3',
  name     => 'werkzeug',
}
