from pn532pi import Pn532, pn532
from pn532pi import Pn532Hsu

PN532_HSU = Pn532Hsu(Pn532Hsu.RPI_MINI_UART)
nfc = Pn532(PN532_HSU)

class Rfidpuzzle1:
    
    def read_uid(self):
        PN532_HSU = Pn532Hsu(Pn532Hsu.RPI_MINI_UART)
        nfc = Pn532(PN532_HSU)
        
        nfc.begin()
        nfc.SAMConfig()
        print("Esperando tarjeta...")
        
        success, uid = nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)
        
        while(not success):
            success, uid = nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)
        
        id = uid.hex()
        print("Detectado\nUID en hexadecimal: ")
        return id
        
    
if __name__ == '__main__':
        rf = Rfidpuzzle1()
        uid = rf.read_uid()
        print(uid)