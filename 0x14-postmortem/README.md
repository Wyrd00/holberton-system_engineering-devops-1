# 0x11. Postmortem

### Issue Summary
From 4:45 PM to 5:28 PM PST, Nginx failed to restart on both servers `web-01` and `web-02`, resulting in 500 response messages returned. The domain, `holbertonschool.online` was inaccessbile to user(s), affecting 100% of the traffic. The root cause of this outage was an invalid syntax on the nginx configuration file, causing nginx to fail to restart properly. 

### Timeline (All Pacific Standard Time)
- **4:45 PM:** Configuration changes made and pushed to implement a new user, `Nginx`
- **4:50 PM:** Outage begins when the Engineer notices the servers failed to restart
- **4:55 PM:** Engineer stops `web-01` and rollsback to the backup configuration file, `nginx.conf.bak`
- **4:56 PM:** Engineer run a nginx script to detect if the issue were changes made to the configuration file
- **4:57 PM:** Nginx script returns an error stating the configuration file’s syntax is incorrect
- **5:02 PM:** Engineer re-implements changes made to the default file under sites-enabled.
- **5:15 PM:** Syntax was corrected, and nginx script ran again to recheck syntax errors. No errors returned.
- **5:17 PM:** Engineer re-implements changes and deems it unnecessary to escalate issue
- **5:20 PM:** `web-01` restarts successfully and engineer reimplements changes to server `web-02`
- **5:28 PM:** Both servers are back up and 100% of traffic is back online

### Root Cause
At 4:33 PM PST, changes were made to add a new user, `Nginx`, into the configuration fle, `nginx.conf` along with changing the listening port from `80` to `8080`. Changes were tested locally to ensure correct syntax, but they were not tested on the configuration file nor the default file itself. At 4:50 PM PST, the engineer notices the servers were unable to restart when the configuration changes where made. When adding a new user, the engineer missed a semi-colon to close the line and did not run the nginx -t script to check if the syntax was correct before implementing new changes. Changes were implemented, causing the servers unable to restart properly. 

Since only two files were changed, at 4:56 PM PST the engineer ran `service nginx -c /etc/nginx/nginx.conf -t` to check if the root cause stemmed from changes made to the `nginx.conf` file. An error was returned stating the syntax was not correct, which caused the server to fail restart. The engineer checks the syntax and finds a missing semi-colon upon creating the new user, `Nginx` - the semi-colon was added and changes reimplemented. At 5:28 PM PST, `web-01` started successfully and changes were then made to server `web-02`. 

### Corrective and Preventative Measures

After a day of internal review and analysis, the following preventative measures were made: 
- After local testing, testing should be made on the files itself before implementation via script. 
- When changes are made on the `nginx.conf` file, the engineer should run the nginx script (`service nginx -c /etc/nginx/nginx.conf -t`) to check if there were any syntax issues.



#### Sincerely,

#### Kimberly Wong [tweet me](https://twitter.com/kjowong)

---
###### Click for postmortem with a [twist](https://medium.com/@kjowong/postmortem-with-a-twist-f6940fd81528)
