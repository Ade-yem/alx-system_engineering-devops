# Automation: creates a custom HTTP header response with Puppet.
exec {'update packages':
  command  => 'sudo apt update',
  provider => shell,
}

package {'install nginx':
  ensure   => installed,
  name     => 'nginx',
}
exec {'allow user access':
  command  => 'sudo chown -R "$USER":"$USER" /var/www',
  provider => shell
}

exec {'allow firewall access':
  command  => "sudo ufw allow 'Nginx HTTP'",
  provider => shell,
}

exec {'edit default nginx file':
  command  => 'sudo echo "Hello World!" > /var/www/html/index.nginx-debian.html',
  provider => shell,
}

exec {'add redirect':
  command  => "sudo sed -i '/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default",
  provider => shell,
}
file {'create 404 page':
  ensure    => file,
  path      => '/var/www/html/404.html',
  content   => "Ceci n'est pas une page",
}

exec {'adding 404 error':
  command   => "sudo sed -i '/^\tlocation \/ {$/a \\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\tinternal;\n\t}\n' /etc/nginx/sites-available/default",
  provider  => shell,
}  

exec {'adding 404 error':
  command   => "sudo sed -i '0,/location \/ {/ s//location \/ {\n\tadd_header X-Served-By $HOSTNAME;\n/' /etc/nginx/sites-available/default",
  provider  => shell,
}
service {'start nginx':
  ensure   => running,
  name     => 'nginx',
  restart    => 'nginx',
}
