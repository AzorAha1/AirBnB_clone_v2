# sets up web servers for the deployment of web_static
file { '/data/':
  ensure => created,
  owner  => 'ubuntu',
  group  => 'ubuntu'
}
file { '/data/web_static/':
  ensure => created,
}
file { '/data/web_static/releases/':
  ensure => created,
}
file { '/data/web_static/releases/test/':
  ensure => created,
}
file { '/data/web_static/index.html':
  ensure  => created,
  content => "'<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>'"
}


