# PHilita Legacy Simulation
## _Prototype London Sim 2019/20 repository_
---
This repository holds the codebase the prototype simulation of London run for the Thales Tech challenge, and all associated files:
- OTP build and source
- Source files 
- File structure
- Python wrapper
- O.D. Generator

This is stored for posterity and shouldn't really be worked on - it was super botched together. 
The ATOC and LDN GTFS files have been removed since they are over 100MB. You can obtain them from:
- ATOC website
- TFL Website > Convert from TransXChange to GTFS

Only the non-binary files have been added. This means that to run this you need to create a bunch of custom GTFS files - relational stuff. 
In v2.0 this dependency is being removed as we are using a SQL database. 
This version is therefore not runnable as is from the github without a lot of work. Email me if you want the source files to run it 
> (If i still have them)