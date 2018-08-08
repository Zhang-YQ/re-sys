import func_system_info
import func_tools

def mfunc_get_time_str():
    time_now_str=str(func_system_info.mfunc_time_now())
    return time_now_str

def mfunc_get_hostname_str():
    #此函数用于获取hostname并转换成字符串
    hostname1=func_system_info.mfunc_hostname()
    return hostname1

def mfunc_get_ipaddr_str():
    #此函数用于获取主机ip地址，并转换成字符串
    ipaddr=func_system_info.mfunc_getipaddress()
    ipaddr_list=ipaddr[2]
    ipaddr_list_len=len(ipaddr_list)
    ipaddr_str=""
    for i in range(0,ipaddr_list_len):
        ipaddr_str=ipaddr_str+"IP Address["+str(i+1)+"]:"+ipaddr_list[i]+";"
#    print(ipaddr_str)
#    print(type(ipaddr_str))
    return ipaddr_str

def mfunc_get_cpu_usage_str():
    #此函数用于将cpu使用率的值从list型浮点数，转成str
    cpu_useage_list=func_system_info.mfunc_cpu_useage()
    #将cpu_usage的值存到cpu_useage_list里，此时为list类型
    cpu_useage_list1=[]
    #创建一个新的list，cpu_useage_list1，用于存放下面保存成str的list
    len1=len(cpu_useage_list)
    for i in range(0,len1):
        cpu_useage_list1.append(str(cpu_useage_list[i]))
        #因为float类型不能使用.join命令转成str，所以此处将float类型变成str，再存入上面预先定义的cpu_useage_list1
    cpu_useage_str=','.join(cpu_useage_list1)
    #对cpu_useage_list1进行转换，转成str，此函数完成
    return cpu_useage_str

def mfunc_get_memory_usage_str():
    #此函数用于将获得的内存使用率的值进行str化
    memory_usage_list=func_system_info.mfunc_memory_useage()
    memory_usage_list1=[]
    len1=len(memory_usage_list)
    for i in range(0,len1):
        memory_usage_list1.append(str(memory_usage_list[i]))
    memory_usage_str=','.join(memory_usage_list1)
    return memory_usage_str

def mfunc_get_swap_usage_str():
    # 此函数用于将获得的swap使用率的值进行str化
    swap_useage_list=func_system_info.mfunc_swap_memory()
    swap_useage_list1=[]
    len1=len(swap_useage_list)
    for i in range(0,len1):
        swap_useage_list1.append(str(swap_useage_list[i]))
    swap_useage_str=','.join(swap_useage_list1)
    return swap_useage_str

def mfunc_get_hdd_useage_str():
    # 此函数用于将获得的hdd使用率的值进行str化
    hdd_useage_list=func_system_info.mfunc_hdd_total()
    hdd_useage_list1=[]
    len1=len(hdd_useage_list)
    for i in range(0,len1):
        hdd_useage_list1.append(str(hdd_useage_list[i]))
    hdd_useage_str=','.join(hdd_useage_list1)
    return hdd_useage_str

def mfunc_get_netio_useage_str():
    # 此函数用于将获得的网卡io的值进行str化
    netio_useage_list=func_system_info.mfunc_network_io()
    netio_useage_list1=[]
    len1=len(netio_useage_list)
    for i in range(0,len1):
        netio_useage_list1.append(str(netio_useage_list[i]))
    netio_useage_str=','.join(netio_useage_list1)
    return netio_useage_str

def mfunc_get_info_all():
    hostname1=mfunc_get_hostname_str()
    ipaddr1=mfunc_get_ipaddr_str()
    cpu1=mfunc_get_cpu_usage_str()
    memory1=mfunc_get_memory_usage_str()
    swap1=mfunc_get_swap_usage_str()
    hdd1=mfunc_get_hdd_useage_str()
    netio1=mfunc_get_netio_useage_str()
    time1=mfunc_get_time_str()

    data_all={"Hostname":hostname1, \
              "IP Address":ipaddr1, \
              "CPU Useage":cpu1, \
              "Memory":memory1, \
              "Swap":swap1, \
              "HDD":hdd1, \
              "Network IO":netio1, \
              "Time":time1
              }
    return data_all

#if __name__ == '__main__':
    #m=mfunc_get_swap_usage_str()
    #print(m)