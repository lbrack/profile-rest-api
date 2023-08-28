# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Vagrant Box
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_version = "~> 20200304.0.0"
  config.vm.network "forwarded_port", guest: 8000, host: 8000, host_ip: "127.0.0.1"

  # Provisioning Directives
  config.vm.provision "shell", inline: <<-SHELL
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer
    export DEBIAN_FRONTEND=noninteractive
    sudo apt-get update
    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_38_ADDED /home/vagrant/.bash_aliases; then
       sudo apt-get install -y python3.8
       sudo apt-get install -y python3-venv
       sudo apt-get install -y python3.8-venv
       sudo apt-get install -y zip
       echo "# PYTHON_38_ADDED" >> /home/vagrant/.bash_aliases
       echo "alias python='python3.8'" >> /home/vagrant/.bash_aliases
       echo "# PYTHON_38_ADDED END" >> /home/vagrant/.bash_aliases
    fi
    if ! grep -q PDM_INSTALLED /home/vagrant/.bashrc; then
     runuser -l vagrant -c 'curl -sSL https://pdm.fming.dev/install-pdm.py | python3.8 -'
     echo "# PDM_INSTALLED" >> /home/vagrant/.bashrc
     echo 'export PATH=/home/vagrant/.local/bin:$PATH'  >> /home/vagrant/.bashrc
     echo 'source /vagrant/.aliases' >> /home/vagrant/.bashrc
     echo 'cd /vagrant' >> /home/vagrant/.bashrc
     echo "# PDM_INSTALLED END" >> /home/vagrant/.bashrc
    fi
    runuser -l vagrant -c 'export PATH=/home/vagrant/.local/bin:$PATH;cd /vagrant;pdm venv remove --yes vagrant;pdm venv create --force --name vagrant 3.8;pdm use --venv vagrant'
    runuser -l vagrant -c 'export PATH=/home/vagrant/.local/bin:$PATH;cd /vagrant;pdm install'
  SHELL
end
