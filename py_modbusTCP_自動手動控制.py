from pyModbusTCP.client import ModbusClient
import time

c = ModbusClient(host='ModbusTCP_IP', port=502, unit_id=1, auto_open=True)
output_array = ['','','','','','','','']

input_array = c.read_discrete_inputs(0, 8)
input_array[0] = False  #自動
input_array[1] = False  #手動
input_array[2] = False  #夾取
input_array[3] = False  #轉移
input_array[4] = False  #釋放

output_array[0] = False #自動 
output_array[1] = False #手動
output_array[2] = False #夾取為on 釋放為off 
output_array[3] = False #轉移
var_timer = False
automode = 0
manualmode = 0
aclampon = 0
aclampoff = 0
mclampon = 0
mdelivery = 0
mclampoff = 0

while True:
    input_array = c.read_discrete_inputs(0, 8)
    if input_array[0] == True:
        automode = 1
        manualmode = 0
    if input_array[1] == True:
        automode = 0
        manualmode = 1
    if automode == True:
        if var_timer is False:            
            c_time = time.time()
            compare_time = int(c_time)
            var_timer = True
        c_time = time.time()
        current_time = int(c_time)
        if current_time >= compare_time +2:
            compare_time = current_time
            timeup = True
        if timeup == False:
            adelivery = 1
            aclampon == 1
        else:
            adelivery = 0
            aclampon == 0
            aclampoff = 1
            automode = 0
    else:
        adelivery = 0
        aclampon = 0
        aclampoff = 0
    if manualmode == True:
        mclampon = input_array[2]
        mdelivery = input_array[3]
        mclampoff = input_array[4]
    else:
        mclampon = 0
        mdelivery = 0
        mclampoff = 0
    if aclampon == 1 or mclampon == 1:
        output_array[0] = True        
    if aclampoff == 1 or mclampoff == 1:
        output_array[0] = False
    output_array[1] = adelivery == 1 or mdelivery == 1      
    c.write_multiple_coils(0, output_array)
