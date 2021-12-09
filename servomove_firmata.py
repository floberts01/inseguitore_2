import  pyfirmata


board = pyfirmata.Arduino('/dev/ttyUSB0')


iter8 = pyfirmata.util.Iterator(board)
iter8.start


#setup pin 11 e 13 come Servo Output
x = board.get_pin('d:7:s')
y = board.get_pin('d:8:s')


class servopos():
    def __init__(self):
        self.currentx,self.currenty=7,4
        x.write(self.currentx)
        y.write(self.currenty)
        

# incrementa l'angolo del valore passato alla funzione
    def setposx(self,diffx):
        self.currentx+=diffx
        self.currentx=round(self.currentx,2)
        if(self.currentx<15 and self.currentx>0):
            x.write(self.currentx)
    def setposy(self,diffy):
        self.currenty+=diffy
        self.currenty=round(self.currenty,2)
        if(self.currenty<15 and self.currenty>0):
            y.write(self.currenty)
#setta l'angolo passato alla funzione
    def setdcx(self,dcx):
        x.write(dcx)
    def setdcy(self,dcy):
        y.write(dcy)
