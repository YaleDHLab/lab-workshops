# Creating an EC2 Instance on AWS

**To create an EC2 Instance, you'll first need to sign into your AWS account.**

![account signin](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/images/sign_in.png)

**Once signed in, click on "Services" in the top navigation bar, then select "EC2" in the menu.**

![navigation menu](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/images/navigation.png)

**Click "Launch Instance":**

![launch instance](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/images/launch_instance.png)

**Click the "Select" button next to the Ubuntu Server 14.04 LTS (ami-d732f0b7):**

![choose ubuntu](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/images/choose_ubuntu.png)

**Choose the m4.large option and click "Review and Launch":**

![use m4.large](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/images/use_m4.large.png)

**Scroll down to "Security Groups" and click "Edit security groups":**

![edit security groups](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/images/edit_security_groups.png)

**Click "Add Rule", select the HTTP rule with all default settings, and click "Review and Launch":**

![add http](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/images/add_http.png)

**Scroll down to Storage and click "Edit storage". In the following screen, change the value in the "Size (GiB)" input field to 16, then click Review and Launch:**

![add storage](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/images/add_storage.png)

**Finally, click "Launch":**

![launch the instance](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/images/launch.png)

**On the following screen, select "Create a new key pair" from the dropdown, set the Key pair name to bookworm, click "Download Key Pair", accept the terms and conditions, and click "Launch Instance":**

![get the pem file](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/images/get_pem.png)

Make sure to save the downloaded .pem file in a location you can remember--you'll need it for the next steps.

That's it! You're now ready to connect to your Linux server! To do so, you can follow the guide [here](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/guides/connecting-to-an-ec2-instance.md).