import func_db_operation
import time

if __name__ == '__main__':
    while True:
        data_all=func_db_operation.mfunc_db_select_one()
    #    print(data_all)
        hostname1=data_all[0]
        ipaddr1=data_all[1]
        cpu_useage1=data_all[2]
        cpu_useage1_tuple=tuple(cpu_useage1.split(","))
        cpu_useage1_str=""
        for i_1 in range(0,len(cpu_useage1_tuple)):
            cpu_useage1_str=cpu_useage1_str+"Core "+str(i_1)+": "+cpu_useage1_tuple[i_1]+"%    "
        memory_useage1=data_all[3]
        memory_useage1_tuple=tuple(memory_useage1.split(","))
        memory_useage1_str="Total Memory: "+memory_useage1_tuple[0]+"G, Used: "+memory_useage1_tuple[1]+ \
                           "G, Free: "+memory_useage1_tuple[2]+"G, Used Percent: "+memory_useage1_tuple[3]+"%"
        swap_useage1=data_all[4]
        swap_useage1_tuple=tuple(swap_useage1.split(","))
        swap_useage1_str="Total Swap Memory: "+swap_useage1_tuple[0]+"G, Used: "+swap_useage1_tuple[1]+ \
                         "G, Free: "+swap_useage1_tuple[2]+"G, Free Percent: "+swap_useage1_tuple[3]+"%"
        hdd_useage1=data_all[5]
        hdd_useage1_tuple=tuple(hdd_useage1.split(","))
        hdd_useage1_str="HDD Space: "+hdd_useage1_tuple[0]+"G, Used: "+hdd_useage1_tuple[1]+ \
                        "G, Free: "+hdd_useage1_tuple[2]+"G, Used Percent: "+hdd_useage1_tuple[3]+"%"
        net_io=data_all[6]
        net_io_tuple=tuple(net_io.split(","))
        net_io_str="Send bytes: "+net_io_tuple[0]+" , Recevied bytes: "+net_io_tuple[1]+ \
                   " , Send Packets: "+net_io_tuple[2]+" , Received Packets: "+net_io_tuple[3]+ \
                   " , Error: "+net_io_tuple[4]+" , Drop: "+ net_io_tuple[5]

        #hostname1
        #ipaddr1
        #cpu_useage1_str
        #memory_useage1_str
        #swap_useage1_str
        #net_io_str
        html_strings="""
        <html>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
        <head></head>
        <body>
        <p>RE服务器实时监护系统，测试版本:v0.1</p>
        <p>Hostname: """+hostname1+ \
         """</p>
        <p>Server IP Address: """+ipaddr1+ \
         """</p>
        <p>Cpu useage: """+cpu_useage1_str+ \
         """</p>
        <p>Memory useage: """+memory_useage1_str+ \
         """</p>
        <p>Swap Memory useage: """+swap_useage1_str+ \
         """</p>
        <p>HDD useage:"""+hdd_useage1_str+ \
        """</p>
        <p>Network IO: """+net_io_str+ \
        """</p>
        <p>数据图表及前端美化即将上线，敬请期待。--2018.08.02</p>
        </body>
        </html>
        """
        with open('index.html', 'w') as file_operate:
            file_operate.write(html_strings)
        time.sleep(3)
