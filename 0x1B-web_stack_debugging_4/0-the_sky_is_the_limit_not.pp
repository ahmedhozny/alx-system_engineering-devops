# Fixes user limit and sets it to 2048

exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2048\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
