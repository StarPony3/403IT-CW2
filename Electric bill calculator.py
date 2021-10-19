# 'counter' variable. Holds the total electricity cost of successive iterations.
x = 0
while True:
    # holds price per kWh hour in pence.
    kWh_cost = input("Enter price per kWh in pence. Enter '0' to stop.") 
           
    if kWh_cost == '0':
        # stops the loop and returns the total of any previous devices to user.
        print (f"Total cost for all devices: {x}p.")
        break                                          
    else:
        # holds wattage of device
        watts = input("Enter wattage of device. Enter '0' to stop.")         
        
        if watts == '0':  
            print (print (f"Total cost for all devices: {x}p."))                                                    
            break
        else:
            # holds running time of device to nearest hour.
            run_time = input ("Enter running time of device to nearest hour. Enter '0' to stop.")         

            if run_time == '0':
                print (print (f"Total cost for all devices: {x}p."))                                                                           
                break            
            else:  
                # calculation of kW hours.
                watt_hours = float(watts) * float(run_time)                                          
                kW_hours = watt_hours / 1000                                                       
                print (f"kiloWatt hours of device: {kW_hours}") 

                # calculation of total cost of this device.                            
                total_cost = float(kWh_cost) * float(kW_hours) 
                print (f"The total cost of running this device is {total_cost}p.") 

                # calculation of total cost of all devices entered so far.
                x = x + total_cost          
                print (f"Total cost for all devices: {float(x)}p.\n")







                    
