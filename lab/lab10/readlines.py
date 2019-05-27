def main():

    rainfall = open('rainfall.txt','r')
    rainfall_str = rainfall.readlines()
    ##print(rainfall_str)

    list_2 = []
    for line in rainfall_str:
        list_2.append(float(line[-6:-1]))
    ##print(list_2)


    max_val = max(list_2)
    min_val = min(list_2)
    avg_val = sum(list_2) / len(list_2)
    print('Max rainfall: %.2f, Min rainfall: %.2f, Average Rainfall: %.2f'\
            % (max_val, min_val,avg_val))
##    del rainfall_list[-1]
##    r_inch = []
##    for val in rainfall_list:
##    
##        ##print(val)
##        rain = val.split()
##        ##print(rain)
##        r_inch.append(float(rain[1]))
##
##    max_val = max(r_inch)
##    min_val = min(r_inch)
##    avg_val = sum(r_inch) / len(r_inch)
##
##    print('Max rainfall: %.2f, Min rainfall: %.2f, Average Rainfall: %.2f' % (max_val, min_val,avg_val))
##    
##    ##print(rainfall_list)
##
##
##
##    rainfall.close()

main()

