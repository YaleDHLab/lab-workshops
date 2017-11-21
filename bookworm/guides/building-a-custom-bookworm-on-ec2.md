# Building a Bookworm with Custom Data

This guide walks users through setting up a custom Bookworm installation on an Ubuntu 14.04 server. The guide assumes you have already installed the Federalist Bookworm as described [here](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/guides/building-a-bookworm-on-ec2.md). If you haven't completed those steps already, please do so before continuing with the guide below.

#### 1) Preparing your data

The first step in creating a custom Bookworm is to format your data into three distinct data structures, an `input.txt` file, a `jsoncatalog.txt` file, and a `field_descriptions.json` file, all documented in the [official Bookworm documentation](https://github.com/Bookworm-project/BookwormDB#required-files). 

If you prepare those files on your local machine, you will then need to upload your three files to your AWS instance. To do so, you will want to open a Unix shell. On Windows, you can use [GitBash](https://git-scm.com/downloads) or [Cygwin](https://www.cygwin.com/); on Unix you can open a terminal by pressing COMMAND+SPACEBAR, then typing terminal. After changing directories to the folder that has your three files, you can load your files onto your AWS instance by running the following commands:

```
# combine the files into a zip archive
mkdir custom_bookworm
mv input.txt jsoncatalog.txt field_descriptions.json custom_bookworm
tar -zcf custom_bookworm.tar.gz custom_bookworm

# copy the zip archive to the AWS instance (note the final :)
scp -i {{my-pem-file.pem}} custom_bookworm.tar.gz ubuntu@{{my-public-dns}}:

# relocate your terminal to your AWS instance
ssh -i {{my-pem-file.pem}} ubuntu@{{my-public-dns}}

# enter a screen
screen

# unzip your data
tar -zxf custom_bookworm.tar.gz
```

#### 2) Loading your data into a Bookworm

At this point, you should have a terminal in the root directory of your AWS instance. To verify that you have the right files in the right places, you can run the following commands:

```
sudo apt-get install tree
tree -L 2
```

The output of the second command should look like the following:

```
.
├── BookwormDB
│   ├── bookwormDB
│   ├── bookwormDB.egg-info
│   ├── build
│   ├── dist
│   ├── LICENSE.md
│   ├── Makefile
│   ├── README.md
│   ├── README.rst
│   ├── setup.cfg
│   ├── setup.py
│   └── tests
├── custom_bookworm
│   ├── field_descriptions.json
│   ├── input.txt
│   └── jsoncatalog.txt
├── custom_bookworm.tar.gz
├── federalist
│   ├── bookworm.cnf
│   ├── federalist.papers.xml
│   ├── field_descriptions.json
│   ├── input.txt
│   ├── jsoncatalog.txt
│   ├── Makefile
│   ├── otherStuff
│   ├── parseXML.py
│   ├── README.md
│   └── webpages
└── prepare_ubuntu_bookworm.sh
```
You may have additional files if you have been doing custom work on your instance, but if you don't see one of those files, please try repeating the steps above.

Once you have your data in this format, you can install a custom Bookworm by running the following steps:

```
# update your MySQL settings
cd ~
wget https://raw.githubusercontent.com/YaleDHLab/lab-workshops/master/bookworm/utils/update_mysql_settings.sh
sudo bash update_mysql_settings.sh
sudo /usr/sbin/mysqld restart
sudo service mysql restart
sudo service apache2 restart

# install the custom Bookworm
cd custom_bookworm
bookworm init
bookworm build all
bookworm build linechartGUI

# relocate the app to the appropriate location
sudo mv /var/www/custom_bookworm /var/www/html/custom_bookworm

# identify your instance's public ip address
wget http://ipinfo.io/ip -qO -

# navigate to {{ your instance's public ip address/federalist }}
# e.g. http://52.43.181.52/custom_bookworm/
```

You should now see your custom data visualized!