#Using Puppet, create a file in /tmp.

file { 'school':
ensure 	=> 'present',
content => 'Puppet is cool',
path	=> '/tmpw/school',
mode	=> '0744',
owner 	=> 'www-data',
group	=> 'www-data',
}
