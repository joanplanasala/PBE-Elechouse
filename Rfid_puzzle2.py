import gi
import threading
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk
from Rfid_puzzle1 import Rfidpuzzle1
from pn532pi import Pn532, pn532
from pn532pi import Pn532Hsu

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Puzzle2 using Gtk") #Create window
        self.connect("destroy", Gtk.main_quit)  
        
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)  #Create box inside window
        self.box.set_homogeneous(False)
        
        
        self.label = Gtk.Label(label="Please, login with your university card.")  #Create label
        self.label.set_name("label")
        self.box.pack_start(self.label, True, True, 0)
        
        self.button = Gtk.Button(label="Clear")  #Create button
        self.button.connect("clicked", self.on_button_clicked)  
        self.box.pack_start(self.button, True, True, 0)
        self.add(self.box)  #Adding box to window
        
        #define blue style
        self.blue = b""" 
                    
                    button{
                        background-color: #E0D4D4;
                        box-shadow:#00000 5px 5px 1px;
                        }
                
                    #label{
                      background-color: #3393FF;
                      font: bold 24px Verdana;
                      border-radius:20px;
                      color:#FFFFFF;
                    }
                    
                """
        
        #define red style    
        self.red = b"""
                    
                    button{
                        background-color: #E0D4D4;
                        box-shadow:#00000 5px 5px 1px;
                        }
                    #label{
                      background-color: #FA0000;
                      font: bold 24px Verdana;
                      border-radius:20px;
                      color:#FFFFFF;
                    }
                    
                """
    
        self.css_provider = Gtk.CssProvider() #Adding styles
        self.css_provider.load_from_data(self.blue) 
        self.context = Gtk.StyleContext()
        self.screen = Gdk.Screen.get_default()
        self.context.add_provider_for_screen(self.screen, self.css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.thread = threading.Thread(target=self.uid)  #Starting threads
        self.thread.daemon = True
        self.thread_in_use = True
        self.thread.start()
        
    def on_button_clicked(self, widget):  #function when "clear" button is clicked
         if (self.thread_in_use == False):
            
            self.label.set_text("Please, login with your university card")
            self.css_provider.load_from_data(self.blue)
            self.thread = threading.Thread(target=self.uid)
            self.thread.start()
            self.thread_in_use = True
            
    def uid(self):
        self.rfid = Rfidpuzzle1()  #object from the class of puzzle1
        uid = self.rfid.read_uid()
        self.label.set_text("UID: "+uid)
        self.css_provider.load_from_data(self.red)
        self.thread_in_use = False


if __name__ == "__main__":
  win = Window()
  win.show_all()
  Gtk.main()
            
        