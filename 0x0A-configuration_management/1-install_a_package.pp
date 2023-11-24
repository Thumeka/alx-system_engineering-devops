# Using Puppet, install puppet-lint

# Install Flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install Werkzeug
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
