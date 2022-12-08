import csv
from pyModbusTCP.client import ModbusClient
import time

c = ModbusClient(host='IP', port=502, unit_id=1, auto_open=True)
output_array = ['','','','','','','','']
res = 100/(4096-819)
input_array = c.read_discrete_inputs(0, 8)
var_timer = False

while True:
    input_array = c.read_input_registers(3, 2)
    if var_timer == False:
            c_time = time.time()
            compare_time = int(c_time)
            var_timer = True            
    else:
        c_time = time.time()
        current_time = int(c_time)
        if current_time >= compare_time + 1:
            compare_time = current_time            
            var_timer = False 
            hum = (input_array[0]-819)*res
            temp = (input_array[1]-819)*res-20
            print(f'濕度{int(hum)}%')
            print(f'溫度(攝氏){int(temp)}度')
            with open('THI.csv', 'a+', newline='') as csvfile:
                writer =csv.writer(csvfile)
                writer.writerow([int(hum),int(temp)])
                
    
            
