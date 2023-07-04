# Install and configure Nginx

package {'nginx':
  ensure => installed,
}

file { '/var/www/html':
  ensure => directory,
  mode   => '0755'
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  mode    => '0644',
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
  mode    => '0644',
}

$nginx_config = @(END)
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;
	add_header X-Served-By "${hostname}";

	error_page 404 /404.html;
	location = /404.html {
		internal;
	}

	location /redirect_me {
		return 301 https://google.com;
	}

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files $uri $uri/ =404;
	}
}
END

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => $nginx_config,
  mode    => '0644',
}

service { 'nginx':
  ensure => running,
}
