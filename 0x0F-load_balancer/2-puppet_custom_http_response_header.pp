# Automation: creates a custom HTTP header response with Puppet.
exec { 'command':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sudo sed -i '0,/location \/ {/ s//location \/ {\n\tadd_header X-Served-By $HOSTNAME;\n/' /etc/nginx/sites-available/default
  sudo service nginx restart
  provider => shell,
}
