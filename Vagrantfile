Vagrant.configure("2") do |config|
  config.vm.define "Python" do |subconfig|
    subconfig.vm.box = "sbeliakou/centos"
    subconfig.vm.hostname = "Python"
    subconfig.vm.network :private_network, ip: "192.168.56.197"
    subconfig.vm.provision "shell", path: "python.sh"
    subconfig.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.cpus = "2"
   end
  end
 end


