# A manifest to kill a running process killmenow from every process table

exec { 'killing a process using pkill':
command => 'pkill -9 killmenow',
path => '/usr/bin:/bin',
onlyif => 'pgrep killmenow',
provider => 'shell',
}
