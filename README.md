server
======

You can set up server.py on the same level as a ```www``` directory, which then contains your static files. Here is an example:

```
user@server:~# tree
├── server.py
└── www
    ├── index.css
    ├── index.html
    ├── index.js
    └── robots.txt
```
Now run python server.py (this runs on port 80 by default, make sure you have access privileges to that port).

Then in your browser, ```localhost``` will serve the file ```~/www/index.html``` along with its dependencies. ```localhost/robots.txt``` will serve the file ```~/www/robots.txt```.
