* Click [here](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#) to launch the Amazon EC2 Console.
* Click Launch Instance
* Select the top option, "Amazon Linux AMI 2016.03.3 (HVM), SSD Volume Type"
* Leave the default choice selected (the second from the top that says "Free tier eligible".
* Choose "Next: Configure Instance Details"
* Choose "Next: Add Storage"
* Change the default 8 gigabytes to 16
* Choose "Review and Launch"
* Choose "Launch" at the bottom of the screen
* You will now set up a key pair so that you can securely log in to the server.
* Choose "Create a new key pair" from the menu. Name it something like "Bookworm Workshop"
* Click the "Download Key Pair" button.
* Once that file has sucessfully downloaded (it's very small), click the "Launch" button.
* On the resulting screen, click the linked name of your instance to be taken to the next page. Keep this page open in your browser for now.
* MAC:
* Open the Downloads folder and make sure that your web browswer has not suffixed .txt to the downloaded file; it should end in .pem
* Move this file from the Downloads folder to the ~/.ssh directory. 
* You can now use this file, together with some information on your web browser screen, to get a remote terminal on the newly-launched Amazon Linux instance.
*  In your Terminal, type `ssh -i ~/.ssh/MyKeyPair.pem ec2-user@` followed (without a space) by the IP number you see in the "Public IP" column on the Amazon web page. (If you lose track of that page, it's [here](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Instances)
* The entire command should look something like `ssh -i ~/.ssh/MyKeyPair.pem ec2-user@54.166.243.250`, with your own IP address instead.
* PC:
* General instructions for using Putty with Amazon are [here](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)
* Start Menu > All Apps > Putty > PuttyGen
* Load, and choose "all files".
* Press "Save private key"
* Launch Putty and connect using `ec2-user@` followed by your public IP# with no space.
* In the left-hand panel, Connection > SSH > Auth > Private Key File for Authentication, browse to the key location.
* RETURN TO ALL PLATFORMS:
* You will need to approve connecting to the machine for the first time; hit `y` for Yes.
* Now you should see a Unix command prompt in front of you in the Terminal. We'll do some updates first:
* `sudo yum update -y`
* Next, we'll install a few pieces of software that Bookworm will need to run:
* `sudo yum install -y git gcc gcc-c++ httpd24 php56 mysql55-server mysql55-devel php56-mysqlnd`
* Now that all that software is installed, we'll need to turn on the web server and database (MySQL) so that they're available:
* `sudo service httpd start`
* `sudo service mysqld start`
* (You'll see a bunch of informational messages about MySQL. You can ignore those for now; we'll return to this in a little bit.)
* We'll also want to ensure that our web server and database start back up if the machine is ever rebooted. To do that,
* `sudo chkconfig httpd on`
* `sudo chkconfig mysqld on`
* And finally, we'll need to open up Amazon's default network security to allow us to actually visit the new web server in our browsers. To do that, we'll need to go [here](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#SecurityGroups:sort=groupId)
* You'll probably have only one Security Group listed, unless you've created other Amazon servers in the past.
* We're going to reduce the number of the files to save time. Type `nano get_and_unzip_data.py`
* Change the 2nd-to-last line to say `pool.map(getCongressData, range(93, 98))`
* Control-X to save.
* `python get_and_unzip_data.py`
* `python congress_parser.py`
