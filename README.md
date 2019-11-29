# Content Delivery Network (CDN)

#### Machines
    * North-America (DNS):  52.177.9.49
    * Europe (chache 1):    40.127.181.75
    * Asia (chache 2):      137.116.137.120

All machines running Ubuntu Server 18.04 LTS 

### North-America

##### System configurations
* `sudo apt update && sudo apt upgrade -y`
* `sudo apt install bind9 bind9utils -y`
* `sudo ufw allow Bind9`
* `sudo ufw allow 22`
* `sudo ufw enable`
   
##### DNS configuration files
* <i>Named</i>
    * Edit:
        * [/etc/bind/named.conf](backup/named.conf)
        * [/etc/bind/named.conf.local](backup/named.conf.local)
        * [/etc/bind/named.conf.options](backup/named.conf.options)
        
    * Check with:
        * `named-checkconf /etc/bind/named.conf.local`

    
* <i>Zones</i>
    * Set  zone configuration files:     
        * [/var/cache/bind/master/demo-tar.com/europe/zone.conf](backup/europe-zone.conf)
        * [/var/cache/bind/master/demo-tar.com/north-america/zone.conf](backup/north-america-zone.conf)
        
    * Check with:
        * `named-checkzone demo-tar.com {FILE PATH}`
        
* Restart service: `sudo systemctl restart bind9 && sleep 2 && sudo systemctl status bind9`                

<br>

##### HTTP server
* Run [HTTP server](HTTP%20server/server.py): `cd server && sudo python2 server.py`

<br>

### Europe & Asia
##### System configurations
* `sudo apt update && sudo apt upgrade -y`
* `sudo ufw allow 80`
* `sudo ufw allow 8080`
* `sudo ufw allow 22`
* `sudo ufw enable`

##### Cache server
* Run [cache server](Cache%20Server/server.py): `python3 cache/server.py`


<br>

#### (Extra) Useful commands
* Set DNS servers <br>
    * Example for US machine:
        * Keep a copy of the [file](backup/set%20servers.yaml) in the home directory
        * Run `sudo cp 50-cloud-init.yaml  /etc/netplan/50-cloud-init.yaml && sudo netplan apply`
* Check DNS resolution: `dig @52.177.9.49 www.demo-tar.com`