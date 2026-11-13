@echo off
echo Open  http://localhost:8000  on this PC.  On your phone (same Wi-Fi) open  http://YOUR-PC-IP:8000  (find the IP with: ipconfig, "IPv4 Address")
python -m http.server 8000
