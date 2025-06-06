# Python Script To Convert Files In Folder By Renaming Them

## Obejective
Append .pcap to the end of each file name to convert the downloaded files from .snort files to .pcap files to be opened in Wireshark. The Parent Folder has a large amount of Child Folders, so it would be tidious to do manually.


## Tools Needed
-Python



## Scenario
The parent folder has a large amount of child folders each containing a .snort file. Write a Python script that loops through each folder and appends .pcag to the end of the name to convert it from a .snort file to a .pcag file that Wireshark can read/open.





## Files Included
| File | Description |
|------|-------------|
| `script.py` | Python Script File To Rename Files |

## What I Learned
-How to filter packet traffic

## What I Did 

## Screenshots
<img src="wireshark_installation.png" alt="Wireshark Download Screenshot" width="400"/>

Downloaded Wireshark

<img src="open_file.png" alt="Opened File Screenshot" width="400"/>

Opened the packet file

<img src="filter_by_ftp.png" alt="Filter by FTP Screenshot" width="400"/>

Filter the packets by FTP

<img src="user_packet.png" alt="User Packet Screenshot" width="400"/>

The packet with the "USER" details

<img src="password_packet.png" alt="Password Packet Screenshot" width="400"/>

The packet with the "PASS" details

<img src="command_sort.png" alt="Command Sort Screenshot" width="400"/>

Sorted all packets by STORE, LIST, and RETR commands

<img src="tcp_stream.png" alt="TCP Stream Screenshot" width="400"/>

Following the TCP stream to track activity

<img src="tcp_stream_2.png" alt="TCP Stream Screenshot" width="400"/>

Following the TCP stream to track activity cont.
