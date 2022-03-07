#!/bin/bash

// Generate a password
PWOUT=${openssl rand -base64 32 | head -c 16)
echo "This will be the root password for your database! Note it down and save it somewhere safe!"
echo "${PWOUT}"
read -p "Press any key to continue..."

// Install Software
apt install -y mysql-server mysql-client-8.0 mysql-connector-python-py3 python3-pip python3.8-venv

// Set-up mySQL Server
{
    echo "n"; // No, we don't want password checking
    echo "${PWOUT}"; // use the password generated above
    echo "${PWOUT}"; // confirm the password
    yes;
} | mysql_secure_installation
