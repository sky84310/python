import csv
from pyModbusTCP.client import ModbusClient
import time

c = ModbusClient(host='ModbusTCP_IP', port=502, unit_id=1, auto_open=True)
output_array = ['','','','','','','','']
input_array = c.read_discrete_inputs(0, 8)

input_array[0] = False  
input_array[1] = False 
output_array[0] = False
var_timer = False
var_money= False
while True:
    input_array = c.read_discrete_inputs(0, 8)
    if input_array[0] == True:
        var_money = True
        
    if input_array[1] == True and var_timer == True:
        output_array[0] = True
    else:
        output_array[0] = False
        
    if var_money == True: 
        if var_timer == False:
                c_time = time.time()
                compare_time = int(c_time)
                var_timer = True      
        else:
            c_time = time.time()
            current_time = int(c_time)
            if current_time >= compare_time + 3:
                compare_time = current_time 
                var_timer = False
                var_money = False

    c.write_multiple_coils(0, output_array)
