# Item Catalog

Its an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system using (Google Accounts). Registered users will have the ability to post, edit and delete their own items.

## Requirements

To run this project you are required to have a database software (provided by a Linux virtual machine) and the data to analyze. For this we recommend

- Vagrant
- VirtualBox

[You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
You do not need to launch VirtualBox after installing it; Vagrant will do that.
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem [ Download vagrant from vagrantup.com](https://www.vagrantup.com/downloads.html)

To download the VM configuration, you can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your `Downloads` folder.

You should have a new directory containing the VM files. Change to this directory in your terminal with `cd`. Inside, you will find another directory called `vagrant`. Change directory to the vagrant directory.
Now you need to bring the virtual machine online (with `vagrant up`), do so now. Then log into it with `vagrant ssh`.

## Database

The database named `itemcatalog` consist of three tables
- The `user` table includes information about the users.
- The `category` table includes the categories of catalog.
- The `category_item` table includes items in each category.

## Setup project

Clone the project into the`vagrant` directory, which is shared with your virtual machine.

Run the following command to set up the database:
```
python database_setup.py
```
To fill the database with dummy data, use the following command
```
python fill_database.py
```

## Running the project

Project can be run just by the following command, given the database has been set up.

```
python project.py
```
Open http://localhost:5000/ in your favorite Web browser to see the application running.

## JSON APIs

The project implements `JSON endpoint` where you can get the same information as displayed in
`HTML endpoints` for list of `categories` and list of `category items`
To get list of categories in catalog
```
http://localhost:5000/category/json
```
To get items in a particular category
```
http://localhost:5000/category/1/items/json
```
