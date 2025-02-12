from RealtimeSTT import AudioToTextRecorder
import socket
import atexit

HOST = '127.0.0.1'  # From TCP/IP DAT
PORT = 7000         # Ensure port matches TCP/IP DAT 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

atexit.register(s.close)

def process_text(text):
    s.sendall(text.encode('utf-8'))  # Send data

if __name__ == "__main__":
    print("Wait until it says 'speak now'")
    recorder = AudioToTextRecorder(model="tiny",silero_use_onnx=True,language="en")

    while True:
        recorder.text(process_text)
