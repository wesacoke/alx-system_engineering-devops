# A puppet manifest installing flask vesion v2.1.0 which is a package from pip3

package {'flask':
ensre => '2.1.0',
provider => pip3,
}
