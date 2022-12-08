import csv
from pyModbusTCP.client import ModbusClient
import time

c = ModbusClient(host='ModbusTCP_IP', port=502, unit_id=1, auto_open=True)
output_array = ['','','','','','','','']

input_array = c.read_discrete_inputs(0, 8)
input_array[0] = False
input_array[1] = False
input_array[2] = False
output_array[0] = False 
output_array[1] = False
dector = input_array[0]
closeLimit = input_array[1]
openlimit = input_array[2]
var_timer = False
DoorOpen = False
DoorClose = False
while True:
    input_array = c.read_discrete_inputs(0, 8)
    if input_array[2] == False:
        if input_array[0] == True:
            output_array[1] = False
            output_array[0] = True       
    else:
        output_array[0] = False
    if input_array[2] == True:
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
                output_array[1] = True
                print(output_array[1])
    else:
        var_timer = False        
    if output_array[1] == True:
        if input_array[1] == True:
            output_array[1] = False
      
    c.write_multiple_coils(0, output_array)
