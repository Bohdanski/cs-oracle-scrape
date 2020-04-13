# CS Oracle Scrape

CS Oracal Scrape is essentially a webcrawler script that will automatically log into the C&S Oracle database, navigate to the out of stock dashboard, and export the current WTD out of stock report. The export will be in plan text/csv format and will be placed on a drive for the out of stock SSIS package to pick up and import.



# Installation

This program is mostly self contained within its folder. Where-ever you decide to place the folder, the path must be manually adjusted within the launcher.bat script.



# Usage

step 1 - Make sure the user credentials are correct in the credentials.py script
step 2 - Make sure the path is correct within the "launcher.bat" file
step 3 - Double click the "launcher.bat" file



# Versions

v1.0 - 04/13/2020 - Initial stable release



# Author

Bohdan Tkachenko