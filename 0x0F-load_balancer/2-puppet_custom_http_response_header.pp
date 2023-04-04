# Install and configure nginx
package { 'nginx':
  ensure => installed,
}

$bash_script = @(END)
#!/usr/bin/env bash
# Install and setup nginx server on Ubuntu, setup default page

# Get document root directory of server
doc_root="$(grep -v '^#' /etc/nginx/sites-enabled/default | grep -w 'root' -m 1 | cut -d' ' -f2 | sed 's/;//')"

# create doc_root if not exists
mkdir -p "$doc_root"

# create index.html
echo "Hello World!" > "$doc_root/index.html"

# Insert directive below server_name directive
base_location="server_name _;"
custom_header="add_header X-Served-By $(hostname);\n\t"

# Get directive server_name _;, relace it with multiple string of redirect url

sed -i "s|${base_location}|${base_location}\n\n\t${custom_header}|" /etc/nginx/sites-enabled/default

# Allow Nginx HTTP in firewall
ufw allow 'Nginx HTTP'

# Always restart nginx
service nginx restart

END

file { 'Setup nginx script':
  ensure  => 'file',
  mode    => '0755',
  content => $bash_script,
  path    => '/tmp/setup-nginx',
}

exec { 'run nginx setup':
  command => '/tmp/setup-nginx',
}
