
from pyModbusTCP.client import ModbusClient
import time


c = ModbusClient(host='ModbusTCP_IP', port=502, unit_id=1, auto_open=True)

"""
紅A = traffic_light[0]
黃A = traffic_light[1]
綠A = traffic_light[2]
紅B = traffic_light[3]
黃B = traffic_light[4]
綠B = traffic_light[5]
"""
"""
code_01 = c.read_coils
code_02 = c.read_discrete_inputs
code_03 = c.read_holding_registers
code_04 = c.read_input_registers
code_05 = c.write_single_coil
code_06 = c.write_single_register
code_0F = c.write_multiple_coils
code_010 = c.write_multiple_registers
"""
"""
A燈號順序:紅A-綠A-黃A(閃爍)
B燈號順序:綠B-黃B(閃爍)-紅B
"""
def traffic_light():
    traffic_light = ['','','','','','']
    traffic_light[0] = True
    traffic_light[3] = False
    traffic_light[4] = False
    traffic_light[5] = True
    
    var_b = False
    a = 0
    b = ''
    while True:
        if var_b is not True:
            print('start')
            c_time = time.time()
            compare_time = int(c_time)
            var_b = True
            print('紅A On & 綠B On')
        #紅A    
        if traffic_light[5] == True and traffic_light[0] == True:
            c_time = time.time()
            current_time = int(c_time)
            if current_time >= compare_time +3:
                compare_time = current_time
                traffic_light[0] = False
                traffic_light[5] = False
                traffic_light[4] = True
                
                print('紅A Off & 綠B Off')
        #黃B閃爍        
        if traffic_light[0] ==False and traffic_light[5] == False and traffic_light[3] == False and b != 'Aoff':
            if traffic_light[4] == False:
                c_time = time.time()
                current_time = int(c_time)
                if current_time >= compare_time +1:
                    compare_time = current_time
                    traffic_light[4] = True
                                        
            elif traffic_light[4] == True:
                c_time = time.time()
                current_time = int(c_time)
                if current_time >= compare_time +1:
                    compare_time = current_time
                    traffic_light[4] = False
                    a = a+1
                    print('黃B閃爍次數:', + a)
                    
            if a == 3:
                b = 'Aoff'
                traffic_light[3] = True
                traffic_light[2] = True
                print('紅B On & 綠A On')
                a = 0
                print(a)
        #紅B        
        if traffic_light[3] == True and traffic_light[2] == True:
            c_time = time.time()
            current_time = int(c_time)
                        
            if current_time >= compare_time +3:
                compare_time = current_time
                traffic_light[3] = False
                traffic_light[2] = False
                traffic_light[1] = True
                print('off')
        #黃A閃爍
        if traffic_light[3] == False and traffic_light[2] == False and b != 'Boff':
            if traffic_light[1] == False:
                c_time = time.time()
                current_time = int(c_time)
                if current_time >= compare_time +1:
                    compare_time = current_time
                    traffic_light[1] = True
                                     
            elif traffic_light[1] == True:
                c_time = time.time()
                current_time = int(c_time)
                if current_time >= compare_time +1:
                    compare_time = current_time
                    traffic_light[1] = False
                    a = a+1
                    print('黃B閃爍次數:', + a)                    
            if a == 3:
                b = 'Boff'
                traffic_light[5] = True
                traffic_light[0] = True
                print('紅B On & 綠A On')
                a = 0
                print(a)
                    
        """if traffic_light[4] == True:
            c_time = time.time()
            current_time = int(c_time)
            if current_time >= compare_time +1:
                compare_time = current_time
                traffic_light[4] = False
                print('2')    """

        yellow_light_on = c.write_multiple_coils(0, traffic_light)
traffic_light()
