import csv
import socket
from pyModbusTCP.client import ModbusClient
import time
import logging
import tkinter as tk

def socket():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        addr = ('192.168.1.110', 5000)
        s.bind(addr)      
        s.listen()
        s, addr = s.accept()
        print(f'[Listening] Server is listening on {addr}.')
        try:
            ann = '來自client' + str(addr)
            receive_data, addr = s.recvfrom(1024)
            print(ann)
            print(receive_data.decode('utf-8'))
            if "exit" in receive_data.decode('utf-8'):
                s.send('You have exited the server.'.encode('utf-8'))
            else:
                msg = input('please input send to msg:')
                s.send(msg.encode('utf-8'))
        except ConnectionResetError:
            logging.warning('Someone left unexcept.')
    if __name__ == '__main__':
        print('server is starting.')
        main()
    
    
def csv_reader():
    try:
        with open('counter.csv', 'r') as csvfile:
            rows =csv.reader(csvfile)
    except:
        with open('counter.csv', 'w') as csvfile:
            var_new = csv.writer(csvfile)     
            var_new.writerow('0')
        csvfile.close()
        
def csv_writer():
    with open('counter.csv', 'w') as csvfile:
        writer =csv.writer(csvfile)
        writer.writerow([counter])
            
def modbustcp():
    c = ModbusClient(host='192.168.1.12', port=502, unit_id=1, auto_open=True)
    output_array = ['','','','','','','','']
    input_array = c.read_discrete_inputs(0, 8)
    while True:
        input_array = c.read_discrete_inputs(0, 8)
        input_array[3] = True
        print(input_array)    
        if input_array[3] == True:            
                if input_array[1] == False:                 
                    if input_array[0] == True:
                        v1 = 1
                else:
                    v1 = 0                   
                output_array[0] = v1==1 or input_array[2]==True           
        else:
            output_array[0] = False         
    c.write_multiple_coils(0, output_array)
 
def pyqt_UI_setup():
    class MainWindow_controller(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setupUI()
            
def tk_UI():
    class MyApp(tk.Tk):
        def __init__(self):
            super().__init__()
            self.setupUI()
            
        def ui_setup(self):
            #Frame
            self.mode_frame = tk.Frame(self, bg=mode_frame_color, width=200, height=150, padx=10, pady=10)#TCP Frame
            self.mode_frame.grid(column=0, row=0, sticky=tk.N)
            #Btn, Checkbutton, Radiobutton
            self.cnt_btn = tk.Button(self.type_frame, text='Connect', 
                                    command=lambda: cnt_btn(self.ip_entry.get(), self.port_entry.get()), 
                                    fg='black', bg=type_frame_color,
                                    state=tk.ACTIVE)
            self.cnt_btn.grid(column=1, row=3, padx=2, pady=5, sticky=tk.W+tk.N)
            #ttk_combobox
            self.endcode_combobox = ttk.Combobox(self.endcode_frame, textvariable=endcode_type,
                                                background=endcode_frame_color,
                                                value=['CR',
                                                        'LF',
                                                        'CR+LF'],
                                                state='readonly')
            self.endcode_combobox.bind('<<ComboboxSelected>>', endcode_box)                                     
            self.endcode_combobox.grid(column=0, row=1, padx=5, pady=30)
            #Label
            self.lab_ip = tk.Label(self.type_frame, text='Type in IP : ', fg='black', bg=type_frame_color)                                                        #IP輸入欄標題 
            self.lab_ip.grid(column=0, row=1, ipadx=2, pady=5, sticky=tk.E+tk.N)
            #變數 StringVar, IntVar
            radiovalue = tk.StringVar(None)
    if __name__ == '__main__':
    MyApp().mainloop()
    
  
def time_counter():
    if output_array[0] == True and input_array[0] == False:
        if var_timer is not True:
            c_time = time.time()
            compare_time = int(c_time)
            var_timer = True
            print(compare_time)
        else:
            c_time = time.time()
            current_time = int(c_time)
            if current_time >= compare_time + 2:
                compare_time = current_time
                output_array[0] = False
                var_timer = False
                print(current_time)
                
                
def btn_clicked():
    class StartBtn(tk.Button):
        def set_down(self,fn):
            self.bind('<Button-1>',fn)
        def set_up(self,fn):
            self.bind('<ButtonRelease-1>',fn)
    class StopBtn(tk.Button):
        def set_down(self,fn):
            self.bind('<Button-1>',fn)
        def set_up(self,fn):
            self.bind('<ButtonRelease-1>',fn)        
    class Mainframe(tk.Frame):
        def __init__(self,master,*args,**kwargs):
            tk.Frame.__init__(self,master,*args,**kwargs)
            btn = StartBtn(self,text = 'Start ')
            btn.set_up(self.start_on_up)
            btn.set_down(self.start_on_down)
            btn.pack()          
            btn = StopBtn(self,text = 'Stop ')
            btn.set_up(self.stop_on_up)
            btn.set_down(self.stop_on_down)
            btn.pack()
        def start_on_down(self,x):
            global var_start
            print("start_on")
            var_start = 1
        def start_on_up(self,x):
            global var_start
            print("start_off")
            var_start = 0                   
        def stop_on_down(self,x):
            global var_stop
            print("stop_on")
            var_stop = 1
        def stop_on_up(self,x):
            global var_stop
            print("stop_off")   
            var_stop = 0         
    class App(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)      
            self.title('My Button')
            self.geometry('250x50')    
            Mainframe(self).pack()            
    App().mainloop()
