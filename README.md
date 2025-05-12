# EX01 Developing a Simple Webserver
## Date:12.5.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Layers and Protocols</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1e1e1e;
            color: #ffffff;
            text-align: center;
        }
        h2 {
            color: #0096FF;
            margin-top: 30px;
        }
        table {
            margin: 0 auto;
            border-collapse: collapse;
            width: 80%;
        }
        th, td {
            border: 1px solid #ffffff;
            padding: 12px 20px;
            font-size: 18px;
        }
        th {
            background-color: #0096FF;
            color: #000000;
        }
    </style>
</head>
<body>
    <h2>TCP/IP Layers and Protocols</h2>
    <table>
        <tr>
            <th>TCP/IP Layers</th>
            <th>Protocols (Examples)</th>
        </tr>
        <tr>
            <td>Application Layer</td>
            <td>HTTP, RDP, DNS, SMTP, Telnet, SNMP</td>
        </tr>
        <tr>
            <td>Transport Layer</td>
            <td>TCP, UDP</td>
        </tr>
        <tr>
            <td>Internet Layer</td>
            <td>ICMP, IGMP, ARP, IP, IPSec</td>
        </tr>
        <tr>
            <td>Network Access Layer</td>
            <td>Ethernet (IEEE 802.3), Token Ring, PPP, Frame Relay</td>
        </tr>
    </table>
</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:

NAME       : RAMYA S
REGISTER NO: 212224040268

![alt text](<Screenshot 2025-05-12 104813.png>)

![alt text](<Screenshot 2025-05-12 104828.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
