sudo apt install bind9 bind9utils -y
sudo systemctl restart bind9 && sleep 2 && sudo systemctl status bind9
sudo ufw allow Bind9 
sudo ufw allow 22
sudo ufw allow 53
sudo ufw enable
dig @52.177.9.49 www.demo-tar.com



named-checkconf /etc/bind/named.conf.local
named-checkzone demo-tar.com europe/zone.conf 


# set servers
sudo cp 50-cloud-init.yaml  /etc/netplan/50-cloud-init.yaml && sudo netplan apply
systemd-resolve --status eth0
