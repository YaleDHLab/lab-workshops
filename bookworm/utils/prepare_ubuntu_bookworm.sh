#!/bin/bash

#
echo
echo "Set up the basics"
echo

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get install -y gcc
sudo apt-get install -y build-essential python-dev libmysqlclient-dev
sudo apt-get install -y parallel
sudo apt-get install git -y

#
echo
echo "Setting up a LAMP server on EC2"
echo

sudo apt-get install -y lamp-server^
sudo mysql_secure_installation

#
echo
echo "Install Python and Extensions"
echo

sudo apt-get install -y python-dev
sudo apt-get install -y python-pip
sudo pip install regex
sudo pip install nltk
sudo pip install numpy
sudo pip install mysql-python
sudo pip install python-dateutil

#
echo
echo "Setting up MySQL User Accounts"
echo
echo "Type a name for a MySQL User with all writing priveleges, then hit [Enter]:"
read keeper

pass_not_set=true
while [ $pass_not_set == true ]; do 
  echo
  echo "Type a password for [$keeper], then hit [Enter]:"
  read -s keeperpass
  echo
  echo "Retype the password for [$keeper], then hit [Enter]:"
  read -s keeperpass2
  echo
  if [ $keeperpass != $keeperpass2 ]
    then
      echo "The passwords typed were not the same."
  fi
  if [ $keeperpass == $keeperpass2 ]
    then
      pass_not_set=false
  fi
done


echo
echo "Type a name for a MySQL User with read only priveleges, then hit [Enter]:"
read reader

pass_not_set=true
while [ $pass_not_set == true ]; do 
  echo
  echo "Type a password for [$reader], then hit [Enter]:"
  read -s readerpass
  echo
  echo "Retype the password for [$reader], then hit [Enter]:"
  read -s readerpass2
  echo
  if [ $readerpass != $readerpass2 ]
    then
      echo "The passwords typed were not the same."
  fi
  if [ $readerpass == $readerpass2 ]
    then
      pass_not_set=false
  fi
done

echo
echo "Log into MySQL with your original root password:"

mysql -u root -p --execute="CREATE USER '$keeper'@'127.0.0.1' IDENTIFIED BY '$keeperpass'; \
  GRANT ALL PRIVILEGES ON *.* TO '$keeper'@'127.0.0.1' WITH GRANT OPTION; \
  CREATE USER '$keeper'@'%' IDENTIFIED BY '$keeperpass'; \
  GRANT ALL PRIVILEGES ON *.* TO '$keeper'@'%' WITH GRANT OPTION; \
  CREATE USER 'admin'@'127.0.0.1'; \
  GRANT RELOAD,PROCESS ON *.* TO 'admin'@'127.0.0.1'; \
  CREATE USER '$reader'@'127.0.0.1' IDENTIFIED BY '$readerpass'; \
  GRANT SELECT ON *.* TO '$reader'@'127.0.0.1' WITH GRANT OPTION; \
  CREATE USER '$reader'@'%' IDENTIFIED BY '$readerpass'; \
  GRANT SELECT ON *.* TO '$reader'@'%' WITH GRANT OPTION; \
  GRANT SELECT ON *.* TO 'www-data'@'localhost'; \
  GRANT SELECT ON *.* TO 'ubuntu'@'localhost'; \
  FLUSH PRIVILEGES;"

#
echo
echo "We will now create the MySQL .my.cnf file"
echo


# ****************************************************

cd ~
echo " " >> .my.cnf
echo "#" >> .my.cnf
echo "# The MySQL Database Server Configuration File" >> .my.cnf
echo "#" >> .my.cnf
echo " " >> .my.cnf
echo "[client]" >> .my.cnf
echo "user = $keeper" >> .my.cnf
echo "password = $keeperpass" >> .my.cnf
echo " " >> .my.cnf

echo "All done!"
