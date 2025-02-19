def onConnect(dat, peer):
    print(f"Connected to {peer.address}:{peer.port}")
    return

def onReceive(dat, rowIndex, message, byteData, peer):
    if not message:
        print("Received empty message.")
        return

    print(f"Received: {message} from {peer.address}:{peer.port}")

    # Set the message to a Text DAT
    textDAT = op('message_text')
    textDAT.text = message  # Update text dynamically

    return

def onClose(dat, peer):
    print(f"Connection closed from {peer.address}:{peer.port}")
    return
