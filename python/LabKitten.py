import subprocess, socket, json, time
class LabKitten:
    def __init__(self, email, password, experimentName, exePath, port=6666, debug=False):
        self.initExe(email, password, experimentName, exePath, port, debug)
        self.client = None
        while not self.client:
            try:
                self.initClient(port)
            except:
                self.client = None; time.sleep(1)
    def initExe(self, email, password, experimentName, exePath, port, debug):
        subprocess.Popen([exePath, str(port), email, password, str(debug), experimentName])
    def initClient(self, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', port))
    def observe(self, data):
        self.client.sendall(json.dumps(data).encode())