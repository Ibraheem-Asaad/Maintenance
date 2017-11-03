# Maintenance script

## Automatic Weekly System Maintainance (AWSM) - spelled 'Awesome'

### 1) Back up folders:

Back up predefined folders in the current machine to: Dropbox / OneDrive / Flash Drive (or any combination of them).
    
Store the folders named as their relative path on the machine.
    
Copies only a shell of files bigger than a predefined limit.
    
Keeps up to one old backup.


### 2) Update Antivirus Software:

Fetch ESET Nod32 credentials - username and password (using web scraping).

Convert the credentials to ESET Smart Security license key from the official ESET website.

Copy the license key to clipboard.


### 3) Clean the system:

Run CCleaner software.


#### Used libraries:

fnmatch, glob, lxml, os, random, requests, shutil , sys, time, Tkinter