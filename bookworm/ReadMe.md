# Setting up the connection to the Amazon Linux machine
* Download the .pem (Mac) or .ppk (Windows) file from the Google Doc.
* Once that file has sucessfully downloaded (it's very small), click the "Launch" button.
* On the resulting screen, click the linked name of your instance to be taken to the next page. Keep this page open in your browser for now.

## Macintosh
* Open the Downloads folder and make sure that your web browswer has not suffixed .txt to the downloaded file; it should end in .pem
* Move this file from the Downloads folder to the ~/.ssh directory. 
* You can now use this file, together with some information on your web browser screen, to get a remote terminal on the newly-launched Amazon Linux instance.
*  In your Terminal, type `ssh -i ~/.ssh/MyKeyPair.pem ec2-user@` followed (without a space) by the IP number you see in the "Public IP" column on the Amazon web page. (If you lose track of that page, it's [here](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Instances)
* The entire command should look something like `ssh -i ~/.ssh/MyKeyPair.pem ec2-user@54.166.243.250`, with your own IP address instead.


## Windows
* General instructions for using Putty with Amazon are [here](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)
* Launch Putty and connect using `ec2-user@` followed by your public IP# with no space.
* In the left-hand panel, Connection > SSH > Auth > Private Key File for Authentication, browse to the key location.

# Connecting to the Amazon Linux machine
* You will need to approve connecting to the machine for the first time; hit `y` for Yes.
* Now you should see a Unix command prompt in front of you in the Terminal. We'll do some updates first:
* `sudo yum update -y`
* Next, we'll install a few pieces of software that Bookworm will need to run:
* `sudo yum install -y git gcc gcc-c++ httpd24 php56 mysql55-server mysql55-devel php56-mysqlnd`

# Customizing MySQL Install

* `sudo nano /etc/my.cnf` and insert the following lines at the end of the file:

```
[client]
max_allowed_packet=1073741824

[mysqld]
max_allowed_packet=1073741824
myisam_sort_buffer_size = 512M
read_rnd_buffer_size = 8M
read_buffer_size = 4M
max_heap_table_size = 1024M
tmp_table_size = 1024M

character_set_server = utf8
query_cache_size = 128M
query_cache_type = 1
query_cache_limit = 2M

bulk_insert_buffer_size = 512M
myisam_max_sort_file_size = 1500G
sort_buffer_size = 8M

key_buffer_size=1500M
```

# Compiling Gnu Parallel
* `wget http://ftp.gnu.org/gnu/parallel/parallel-latest.tar.bz2`
* `tar -xvjf parallel*`
* `cd parallel-20160722`
* `./configure`
* `make`
* `sudo make install`

# Running Web Server + Database
* Now that all that software is installed, we'll need to turn on the web server and database (MySQL) so that they're available:
* `sudo service httpd start`
* `sudo service mysqld start`
* (You'll see a bunch of informational messages about MySQL. You can ignore those for now; we'll return to this in a little bit.)
* We'll also want to ensure that our web server and database start back up if the machine is ever rebooted. To do that,
* `sudo chkconfig httpd on`
* `sudo chkconfig mysqld on`
* `cd ~/`
* `git clone git://github.com/Bookworm-project/BookwormDB`
* `cd BookwormDB`
* `sudo python setup.py install`

> Time Estimate: 8 mins.

* `cd ..`
* `git clone https://github.com/bmschmidt/congress_api.git`
* `cd congress_api`
* `python get_and_unzip_data.py`

> Time Estimate: 46 secs.

* `python congress_parser.py`

> Time Estimate: 30 secs.

* `mv jsoncatalog.txt ../BookwormDB`
* `mv input.txt ../BookwormDB`
* `mv field_descriptions.json ../BookwormDB`


# MySQL Database Setup

* `sudo mysql_secure_installation`
* Your database doesn't have a root password yet, so just hit return when queried.
* Answer Yes to "Set root password?"
* For this temporary instance that has no important data, you can use 'bookwormpw' as a password.
* Answer Yes to "Remove anonymous user?"
* Answer Yes to "Disallow root login remotely?"
* Answer Yes to "Remove test database?"
* Answer Yes to "Reload privelege tables?"
* Use 'bwadmin' as the name for the admin user.
* Use 'bookwormpw' as the password for user bwadmin
* Enter 'bookwormpw' again to confirm.

# Bookworm Database Setup

* `nano ~/.my.cnf` and insert the following lines:
`[client]
user = bwadmin
password = bookwormpw`


* `cd ../BookwormDB`
* `bookworm config mysql`
* Answer `/home/ec2-user` when it queries you for the home directory path.

# Initializing a new project

* `bookworm init`
* You can leave the default name of the Bookworm, or change it to something like "Congressional Data"
* The Client Password should be already set to `bookwormpw`, so you can hit return.
* The Client Usernaame should already be set to `bwadmin`, so you can hit return.

# Building the Bookworm
> Time Estimate: 8 mins.

* `bookworm build all`

# Build the LineChart Web Interface
`sudo env "PATH=$PATH" bookworm build linechartGUI`

