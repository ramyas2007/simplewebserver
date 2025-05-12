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