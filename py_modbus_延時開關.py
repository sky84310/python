#延時關閉
from pyModbusTCP.client import ModbusClient
import time
import csv

c = ModbusClient(host='ModbusTCP_IP', port=502, unit_id=1, auto_open=True)
output_array = ['','','','','','','','']

input_array = c.read_discrete_inputs(0, 8)
var_timer = False
var_on = False
var_off = False
while True:
    input_array = c.read_discrete_inputs(0, 8)
    if input_array[0] == True:
        output_array[0] = True
        print('3')
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

    c.write_multiple_coils(0, output_array)
