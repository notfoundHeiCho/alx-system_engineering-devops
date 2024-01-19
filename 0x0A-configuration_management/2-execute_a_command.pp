# Using Puppet, creating a manifest
# kills a process named Killmenow

exec { 'Killmenow':
    command => 'pkill Killmenow',
    provider => 'shell',
}
