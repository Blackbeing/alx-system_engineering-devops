# Install and configure nginx

package { 'nginx':
  ensure => installed,
}

$bash_script = @(END)
#!/usr/bin/env bash

# Get document root directory of server
doc_root="$(grep -v '^#' /etc/nginx/sites-enabled/default | grep -w 'root' -m 1 | cut -d' ' -f2 | sed 's/;//')"

# create doc_root if not exists
mkdir -p "$doc_root"

# create index.html
echo "Hello World!" > "$doc_root/index.html"

# Allow Nginx HTTP in firewall
ufw allow 'Nginx HTTP'

base_location="server_name _;"
redirect_location="location /redirect_me {\n\t\treturn 301 https://google.com;\n\t}"

# Get directive server_name _;, relace it with multiple string of redirect url

sed -i "s|${base_location}|${base_location}\n\n\t${redirect_location}|" /etc/nginx/sites-enabled/default

# Reload nginx, (reload config without stopping)

# Always restart nginx
service nginx restart

END

file { 'setup nginx':
  ensure  => 'file',
  mode    => '0755',
  content => $bash_script,
  path    => '/tmp/setup-nginx',
}

exec { 'run nginx setup':
  command => '/tmp/setup-nginx',
}

exec { 'test 301 redirect':
  command => 'curl localhost/redirect_me',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

