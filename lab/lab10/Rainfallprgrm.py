'''
Kameron Keyes
kkeyes2
'''
##def get_max():
##    
##    max_rain = max(
##    return max_rain

def main():

    rainfall = open('rainfall.txt','r')
    rainfall_str = rainfall.read()
    rainfall_list = rainfall_str.split('\n')
    del rainfall_list[-1]
    r_inch = []
    for val in rainfall_list:
    
        ##print(val)
        rain = val.split()
        ##print(rain)
        r_inch.append(float(rain[1]))

    max_val = max(r_inch)
    min_val = min(r_inch)
    avg_val = sum(r_inch) / len(r_inch)

    print('Max rainfall: %.2f, Min rainfall: %.2f, Average Rainfall: %.2f' % (max_val, min_val,avg_val))
    
    ##print(rainfall_list)


##    line = rainfall.readline()
##    while line:
##        rainfall_list = line.split()
##        if rainfall_list[0] in rain_dict:
##            rain_dict[rainfall_list[0]] += rainfall_list[1:]
##        else:
##            rain_dict[ranfall_list[0]] = [] + rainfall_list[1:]
    

    rainfall.close()

main()
