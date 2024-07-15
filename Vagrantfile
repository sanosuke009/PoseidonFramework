Vagrant.configure("2") do |config|
    config.vm.define 'winserver' do |winserver|
        winserver.vm.box = "gusztavvargadr/windows-server-2022-standard"
        winserver.vm.synced_folder ".", "/vagrant"
        winserver.vm.provider "virtualbox" do |v|
            v.memory = 8192
            v.cpus = 4
        end
        
        # winserver.vm.provision "vm-disable-sleepmode", type: 'shell', privileged: true, run: "always",
          # inline: %{
              # Write 'Disabling sleepmode'
              # Disable-SleepMode
          # }
        
        winserver.vm.provision "vm-install-chocolatey", type: 'shell', privileged: true, run: "always",
          inline: %{
              Write 'Installing chocolatey'
              Set-ExecutionPolicy Bypass -Scope Process
              Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))	
              
          }
          
        winserver.vm.provision "vm-install-python", type: 'shell', privileged: true, run: "always",
          inline: %{
              Write 'Installing python'
              choco install python312 --ignore-checksums -ry --no-progress		
          }
  
        winserver.vm.provision "vm-install-python-packages", type: 'shell', privileged: true, run: "always",
          inline: %{
              Write 'Installing python packages'
              python -m pip install --upgrade pip
              python -m pip install pytest
              python -m pip install pytest-xdist
              python -m pip install allure-pytest
              python -m pip install pytest-playwright
              python -m pip install pytest-rerunfailures			
          }
          
        winserver.vm.provision "vm-install-playwright-browsers", type: 'shell', privileged: true, run: "always",
          inline: %{
              Write 'Installing playwright browsers'
              python -m playwright install --with-deps			
          }
          
          
        winserver.vm.provision "vm-install-chrome", type: 'shell', privileged: true, run: "always",
          inline: %{
              Write 'Installing Google Chrome'
              choco install googlechrome --ignore-checksums -ry --no-progress	
          }
          
        winserver.vm.provision "reboot", type: 'shell', reboot: true
          
        winserver.vm.provision "vm-run-youtube-tests", type: 'shell', privileged: true, powershell_elevated_interactive: true, run: "always",
          inline: %{
              Write 'Running youtube-tests on browser'
              cd ..
              cd ..
              cd vagrant/PoseidonFramework
              python -m pytest ./web/src/test/testcases -p no:faulthandler
          }
          
    end
    config.vm.define 'client' do |client|
        client.vm.box = "generic/ubuntu2204"
        client.vm.synced_folder ".", "/vagrant"
        client.vm.provider "virtualbox" do |v|
            v.memory = 8192
            v.cpus = 4
        end
        
        client.vm.provision "vm-initialize", type: 'shell', privileged: true,
          inline: %{
              echo 'Initializing provisioner'
          }
          
        client.vm.provision "vm-install-pip", type: 'shell', privileged: true, run: "always",
          inline: %{
              echo 'Installing pip'
              sudo apt update
              sudo apt install python3-pip -y			
          }
  
        client.vm.provision "vm-install-python-packages", type: 'shell', privileged: true, run: "always",
          inline: %{
              echo 'Installing python packages'
              sudo python3 -m pip install pytest
              sudo python3 -m pip install pytest-xdist
              sudo python3 -m pip install allure-pytest
              sudo python3 -m pip install pytest-playwright
              sudo python3 -m pip install pytest-rerunfailures			
          }
          
        client.vm.provision "vm-install-playwright-browsers", type: 'shell', privileged: true, run: "always",
          inline: %{
              echo 'Installing playwright browsers'
              sudo python3 -m playwright install --with-deps			
          }
          
          
        client.vm.provision "vm-install-chrome", type: 'shell', privileged: true, run: "always",
          inline: %{
              echo 'Installing chrome'
              sudo playwright install chrome			
          }
          
          
        client.vm.provision "vm-run-youtube-tests", type: 'shell', privileged: true, run: "always",
          inline: %{
              echo 'Running youtube-tests on browser'
              cd ..
              cd ..
              cd vagrant/
              pytest web/src/test/testcases/youtube		
          }
          
    end
  end
  