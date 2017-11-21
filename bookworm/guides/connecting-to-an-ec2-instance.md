# Connecting to an EC2 Instance

This page is part of a tutorial on installing Bookworm on an EC2 instance. This guide assumes you already have an m4.large instance with an Ubuntu operating system. If you don't have one of those, please follow the guide [here](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/guides/creating-an-ec2-instance.md) and then continue with the instructions below to connect to your instance.

The process of connecting to an EC2 instance is different for Windows and Mac operating systems. The guide below offers instructions for both operating systems.

## Connecting to an EC2 instance from Windows

To connect to an EC2 instance from a Windows machine, you can follow the guide [here](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html).

## Connecting to an EC2 instance from a Mac

To connect to an EC2 instance from a Mac, you will first need to know the address of your EC2 instance. You can find this on the AWS admin console. The address is indicated in the public IP of your instance:

![public ip](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/images/public_ip.png)

Once you have identified the public IP of your instance, move your .pem file to your Desktop, then open spotlight with COMMAND+SPACEBAR. Once spotlight opens up, type terminal. In the terminal type:

```
cd Desktop
chmod 600 bookworm.pem
ssh -i bookworm.pem ubuntu@{{your public ip}}
```

You should now see a greeting message. If you do, feel free to advance to the [next stage](https://github.com/YaleDHLab/lab-workshops/blob/master/bookworm/guides/building-a-bookworm-on-ec2.md) to install Bookworm on your server.