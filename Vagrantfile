# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.disksize.size = '15GB'
  config.vm.define "auto1234" do |auto1234|
    auto1234.vm.box = "ubuntu/xenial64"
    auto1234.vm.hostname = 'auto1234'
    auto1234.vm.box_url = "ubuntu/xenial64"

    auto1234.vm.network :private_network, ip: "192.168.56.102"

    auto1234.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.memory = 2048
      v.cpus = 2
      v.customize ["modifyvm", :id, "--name", "auto1234"]
    end
  end

  config.vm.define "datab" do |datab|
      datab.vm.box = "ubuntu/xenial64"
      datab.vm.hostname = 'datamachine'
      datab.vm.box_url = "ubuntu/precise64"

      datab.vm.network :private_network, ip: "192.168.56.103"

      datab.vm.provider :virtualbox do |v|
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.memory = 2048
        v.cpus = 2
        v.customize ["modifyvm", :id, "--name", "datamachine"]
    end
  end
end
