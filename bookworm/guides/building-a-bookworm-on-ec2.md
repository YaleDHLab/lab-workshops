This guide assume you have a .pem file that corresponds to an Ubuntu 14.04 m4.large instance. 

If you don't have one of those, please follow [this guide](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/guides/creating-an-ec2-instance.md) to create the required pem file, then continue below.

# Installing Bookworm

```
# access the instance
ssh -i {{my-pem-file.pem}} ubuntu@{{my-public-dns}}

# enter a screen
screen

# install dependencies
wget https://raw.githubusercontent.com/YaleDHLab/lab-workshops/master/bookworm/utils/prepare_ubuntu_bookworm.sh
sudo bash prepare_ubuntu_bookworm.sh

# you can use the following responses to the prompt questions
New password for the MySQL "root" user -> {{ passwordA }}
Repeat password for the MySQL "root" user -> {{ passwordA }}
Enter current password for root (enter for none) -> {{ passwordA }}
Change the root password? -> n
Remove anonymous users? -> y
Disallow root login remotely? -> y
Remove test database and access to it? -> y
Reload privilege tables now? -> y
Type a name for a MySQL User with all writing priveleges -> dbadmin
Type a password for [dbadmin], then hit [Enter] -> {{ passwordB }}
Retype the password for [dbadmin], then hit [Enter] -> {{ passwordB }}
Type a name for a MySQL User with read only priveleges, then hit [Enter] -> dbuser
Type a password for [dbuser], then hit [Enter] -> {{ passwordC }}
Retype the password for [dbuser] then hit [Enter] -> {{ passwordC }}
Log into MySQL with your origin root password -> {{ passwordA }}

# obtain bookworm source code
git clone https://github.com/Bookworm-project/BookwormDB
cd BookwormDB
git reset --hard 50113e9afe49595cb9d99f406e2d31f98e310da0

# install bookworm
sudo python setup.py install

# create a bookworm
cd ~
git clone https://github.com/bmschmidt/federalist-bookworm.git
mv federalist-bookworm federalist
make -C federalist

# relocate the cgi-bin script
sudo cp ~/BookwormDB/bookwormDB/bin/dbbindings.py /usr/lib/cgi-bin/

# build the gui
cd federalist
sudo chown ubuntu /var/www
bookworm build linechartGUI

# enable cgi-bin
sudo a2enmod cgi
sudo service apache2 restart

# move the installed web app to the proper location
sudo mv /var/www/federalist /var/www/html/

# identify your instance's public ip address
wget http://ipinfo.io/ip -qO -

# navigate to {{ your instance's public ip address/federalist }}
# e.g. http://52.43.181.52/federalist/
```

To see some meaningful trends in this data, click on the gear in the upper right,
select date_day from the Time dropdown, increase the smoothing if desired, and query
for 'federal'. You may need to query twice to get the visualization to load the
first time.

# Troubleshooting

#### Visualization doesn't load

If the visualization doesn't load, you might try:
Open devtools in Chrome with COMMAND+OPTION+i, then refresh the page. 
Navigate to the Network tab of the dev tools, and check the requests that 
begin with dbbindings.py?query=...

If you click on those requests and get a json file that indicates there was a database error,
then the user requesting the data for the client does not have permission to query the database.
You may want to figure out which user is making those requests and then add them to the db.

To figure out the user that's making database requests, take a look at the logs (`sudo vim /var/log/apache2/error.log`) Then, to grant that user read permissions to the database, you
can do:

```
mysql -u root -p
{{ enter your root password when prompted }}
GRANT SELECT ON *.* TO '{{ the user that needs access }}'@'localhost';
FLUSH PRIVILEGES;
quit;
```
You can then try restarting apache2 (`sudo service apache2 restart`) and reloading the page.

If these suggestions don't help or troubles persist, please feel free to [open an issue](https://github.com/YaleDHLab/lab-workshops/issues)!