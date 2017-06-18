# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.disksize.size = '15GB'
  config.vm.define "automation" do |automation|
    automation.vm.box = "ubuntu/xenial64"
    automation.vm.hostname = 'automan'
    automation.vm.box_url = "ubuntu/xenial64"

    automation.vm.network :private_network, ip: "192.168.56.102"

    automation.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.memory = 2048
      v.cpus = 2
      v.customize ["modifyvm", :id, "--name", "automan"]
    end
  end

  config.vm.define "db" do |db|
      db.vm.box = "ubuntu/xenial64"
      db.vm.hostname = 'database'
      db.vm.box_url = "ubuntu/precise64"

      db.vm.network :private_network, ip: "192.168.56.103"

      db.vm.provider :virtualbox do |v|
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.memory = 2048
        v.cpus = 2
        v.customize ["modifyvm", :id, "--name", "database"]
    end
  end
end
