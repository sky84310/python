import tkinter as tk
from tkinter import END, ttk
import socket

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        self.winfo_toplevel().title('Socket Server')                                                              #抬頭
        default_color = 'white'
        mode_frame_color = 'red'
        type_frame_color = '#BEBEBE'
        endcode_frame_color = 'green'
        msg_frame_color = '#AAAAFF'       
        def cnt_btn(ip_entry, port_entry):
            print(self.ip_entry.get() + ' : ' + self.port_entry.get()) 
            print('Connected')
            self.ip_entry.delete(0, END)
            self.port_entry.delete(0, END)
        def dcnt_btn(self):
            print('Disconnected')
        """def udp_btn(radiovalue):
            print('UDP connecting')
        def tcp_btn(radiovalue):
            print('TCP connecting.')"""
        def endcode_box(combobox_get):
            print(self.endcode_combobox.get()) 
        #frame
        self.mode_frame = tk.Frame(self, bg=mode_frame_color, width=200, height=150, padx=10, pady=10)#TCP Frame
        self.mode_frame.grid(column=0, row=0, sticky=tk.N)
        self.mode_frame.grid_propagate(False)
        self.type_frame = tk.Frame(self, bg=type_frame_color, width=300, height=150, padx=10, pady=10)#IP&Port Frame
        self.type_frame.grid(column=1, row=0, sticky=tk.N)
        self.type_frame.grid_propagate(0)
        self.endcode_frame = tk.Frame(self, bg=endcode_frame_color, width=200, height=150, padx=10, pady=10)#Endcode Frame
        self.endcode_frame.grid(column=0, row=1, sticky=tk.N)
        self.endcode_frame.grid_propagate(0)
        self.msg_frame = tk.Frame(self, bg=msg_frame_color, width=300, height=150, padx=10, pady=10)#Endcode Frame
        self.msg_frame.grid(column=1, row=1, sticky=tk.N)
        self.msg_frame.grid_propagate(0)
        #type_frame
        self.lab_ip = tk.Label(self.type_frame, text='Type in IP : ', fg='black', bg=type_frame_color)                                                        #IP輸入欄標題 
        self.lab_ip.grid(column=0, row=1, ipadx=2, pady=5, sticky=tk.E+tk.N)                                      #IP輸入欄標題位置
        self.lab_port = tk.Label(self.type_frame, text='Type in Port : ', fg='black', bg=type_frame_color)                                                    #Port輸入欄標題 
        self.lab_port.grid(column=0, row=2, ipadx=2, pady=5, sticky=tk.E+tk.N)                                    #Port輸入欄標題位置
        self.lab_ipport = tk.Label(self.type_frame, text='IP & Port', bg=type_frame_color, fg='black')                                                        #空白佔位  
        self.lab_ipport.grid(column=0, row=0, columnspan=2, sticky=tk.N+tk.E)                                                                  #空白佔位位置
        self.ip_entry = tk.Entry(self.type_frame, width=20)                                                                  #IP輸入欄
        self.ip_entry.grid(column=1, row=1, padx=2, pady=5, sticky=tk.W+tk.N)                                    #IP輸入欄位置
        self.port_entry = tk.Entry(self.type_frame, width=20)                                                                #Port輸入欄
        self.port_entry.grid(column=1, row=2, padx=2, pady=5, sticky=tk.W+tk.N)                                  #Port輸入欄位置 
        #self.lab_typeingspace = tk.Label(self.type_frame, text='      ', bg='white')                                                     #輸入欄上方空白處
        #self.lab_typeingspace.grid(column=2, row=0)                                                               #輸入欄上方空白處位置                                                               
        self.cnt_btn = tk.Button(self.type_frame, text='Connect', 
                                command=lambda: cnt_btn(self.ip_entry.get(), self.port_entry.get()), 
                                 fg='black', bg=type_frame_color,
                                state=tk.ACTIVE)       #連線按鈕 
        self.cnt_btn.grid(column=1, row=3, padx=2, pady=5, sticky=tk.W+tk.N)                                      #連線按鈕位置
        self.dcnt_btn = tk.Button(self.type_frame, text='Disonnect', 
                                 command=lambda: dcnt_btn(self), 
                                 fg='black', bg=type_frame_color,
                                 state=tk.ACTIVE)  #斷線按鈕                                                                
        self.dcnt_btn.grid(column=1, row=3, columnspan=2, padx=2, pady=5, sticky=tk.E+tk.N)                       #斷線按鈕位置
        #self.lab_connecting_or_not = tk.Label(self, textvariable=connecting_or_not)                               #連線與否標題
        #self.lab_connecting_or_not.grid(column=2, row=0, padx=10, pady=5, sticky=tk.W)                            #連線與否標題位置
        #Mode frame
        radiovalue = tk.StringVar(None)                                                                                  #定義UPD or TCP變數                                                        
        self.lab_connection_mode = tk.Label(self.mode_frame, text='Connection Mode: ', bg=mode_frame_color)                                       #連線模式標題
        self.lab_connection_mode.grid(column=0, row=0) 
        self.udp_btn = tk.Radiobutton(self.mode_frame, text='UDP', variable=radiovalue, value='UDP', bg=mode_frame_color,
                                      )                                                           #選擇UDP按鈕
        self.tcp_btn = tk.Radiobutton(self.mode_frame, text='TCP', variable=radiovalue, value='TCP', bg=mode_frame_color)
        self.udp_btn.grid(column=0, row=1, padx=5, pady=5, sticky=tk.N)                                           #選擇UDP按鈕按鈕
        self.tcp_btn.grid(column=0, row=2, padx=5, pady=5, sticky=tk.N)                                           #選擇TCP按鈕位置
        self.lab_udptcp = tk.Label(self.mode_frame, textvariable=radiovalue, fg='black', bg=mode_frame_color)                          #顯示連線模式標題
        self.lab_udptcp.grid(column=1, row=0, padx=10, pady=5, sticky=tk.N+tk.W)                                  #顯示連線模式標題位置
        def form_btn(self):
            if radiovalue.get() == 'UDP':
                print('UDP connecting.')
            elif radiovalue.get() == 'TCP':
                print('TCP connecting.')    
        self.form_btn = tk.Button(self.mode_frame, text='Comfirmed', bg=mode_frame_color, command=lambda:form_btn(self))                                                                
        self.form_btn.grid(column=0, row=3, padx=5,pady=10, sticky=tk.N)                                           #確認連線模式按鈕位置
        endcode_type = tk.IntVar()
        #self.lab_labspace2 = tk.Label(self, text='          ', bg='yellow')                                                         #空白佔位  
        #self.lab_labspace2.grid(column=0, row=5, padx=10, pady=10, columnspan=10)
        #self.spe1 = ttk.Separator(self, orient='horizontal')
        #self.spe1.grid(column=0, row=5, pady=20, sticky=tk.N+tk.E)
        self.lab_endcode = tk.Label(self.endcode_frame, text='End Code: ', bg=endcode_frame_color, fg='yellow')
        self.lab_endcode.grid(column=0, row=0, sticky=tk.N+tk.W)
        self.endcode_combobox = ttk.Combobox(self.endcode_frame, textvariable=endcode_type,
                                             background=endcode_frame_color,
                                             value=['CR',
                                                    'LF',
                                                    'CR+LF'],
                                             state='readonly')
        self.endcode_combobox.bind('<<ComboboxSelected>>', endcode_box)                                     
        self.endcode_combobox.grid(column=0, row=1, padx=5, pady=30)
        self.endcode_combobox.current(0)
        self.lab_crlf = tk.Label(self.endcode_frame, textvariable=endcode_type, bg=endcode_frame_color, fg='yellow')
        self.lab_crlf.grid(column=0, row=0, sticky=tk.N)
        self.lab_msg = tk.Label(self.msg_frame, text='Message', bg=msg_frame_color, fg='black')
        self.lab_msg.grid(column=1, row=0, columnspan=3, sticky=tk.N)
        self.lab_send_msg = tk.Label(self.msg_frame, text='Send Message: ', bg=msg_frame_color, fg='black')
        self.lab_send_msg.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
        self.lab_recv_msg = tk.Label(self.msg_frame, text='Received Message: ', bg=msg_frame_color, fg='black')
        self.lab_recv_msg.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
        self.send_msg = tk.Entry(self.msg_frame, width=20)
        self.send_msg.grid(column=1, row=1, padx=5, pady=5)
        self.recv_msg = tk.Entry(self.msg_frame, width=20)
        self.recv_msg.grid(column=1, row=2, padx=5, pady=5)

if __name__ == '__main__':
    MyApp().mainloop()
  
