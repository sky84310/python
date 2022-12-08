#3.14

from pyModbusTCP.client import ModbusClient
import time

c = ModbusClient(host='ModbusTCP_IP', port=502, unit_id=1, auto_open=True)
output_array = ['','','','','','','','']
input_array = c.read_discrete_inputs(0, 8)

input_array[0] = False  
input_array[1] = False 
input_array[2] = False
input_array[3] = False
output_array[0] = False
output_array[1] = False
var_timer = False
var_learn = False
var_auto = False
var_refresh = False
var_learning_time = 0

while True:
    input_array = c.read_discrete_inputs(0, 8)
    if input_array[0] == True:
        var_learn = True
    else:
        var_learn = False
        var_refresh = True
        var_timer = False
    if var_learn == True:
        if var_timer == False :
                c_time = time.time()
                compare_time = int(c_time)
                var_timer = True
                print(var_timer)                  
        else:
            c_time = time.time()
            current_time = int(c_time)
            var_learning_time = current_time - compare_time
    
    c.write_multiple_coils(0, output_array)
