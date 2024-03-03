# TLS-Lower-Version-Script

1.	Open terminal from there and run below command
sslyze --targets_in input.txt --tlsv1 --sslv2 --sslv3 --tlsv1_1 > ssl_tls_scan_results.txt 2>&1
(you will get output text file on same path. It takes approx. 1 hour depending upon number of application in input file).
2.	Copy that output file and paste into one folder and also save TLS_Script.py on same directory.  python TLS_Script.py
3.	Run below command to extract fixed result. You will get separate fixed output result.
4.	Check if application have any specific port other than 443 then check using below steps that application got fixed or not.
  a.	Open Kali linux and use command “testssl -p application_name.com:port_number”
  b.	If application have multiple ports, checks individually.
  c.	If you look that application not supporting tls 1.1, tls1 and ssl v2, ssl v3 Then consider it as fixed. 
