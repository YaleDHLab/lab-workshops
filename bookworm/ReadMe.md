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
* Open the Downloads folder and make sure that your web browswer has not suffixed .txt to the downloaded file; it should end in .pem
* Move this file from the Downloads folder to the ~/.ssh directory. 
* You can now use this file, together with some information on your web browser screen, to get a remote terminal on the newly-launched Amazon Linux instance.
