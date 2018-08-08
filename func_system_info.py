import psutil
import socket
import time

def mfunc_time_now():
    time_now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return time_now

def mfunc_hostname():
    #此函数用于获取hostname
    hostname1=str(socket.gethostname())
    return hostname1

def mfunc_getipaddress():
    #此函数用于获取ipaddress，包括所有的网络接口

    #gethostbyname_ex函数获取ip地址需要传入参数hostname，此处hostname从mfunc_hostname自定义函数里取得
    ipaddr=socket.gethostbyname_ex(mfunc_hostname())
    return ipaddr

def mfunc_cpu_cores():
    #此函数用于返回cpu核心数量，cpu_count为物理核心数量，cpu_count_logic为逻辑核心数量
    cpu_count_logic=psutil.cpu_count()
    cpu_count=psutil.cpu_count(logical=False)
    return cpu_count,cpu_count_logic

def mfunc_cpu_useage():
    #此函数用于返回cpu的使用率，间隔为0.5秒，返回的值为dict类型
    cpu_useage=psutil.cpu_percent(interval=1,percpu=True)
    return cpu_useage

def mfunc_memory_total():
    #此函数用于返回内存大小，memory_bit为比特，memory_G为G单位，并做小数点后两位四舍五入
    memory_total=psutil.virtual_memory()
    memory_bit=memory_total[0]
    memory_G=str(round(memory_bit/1024/1024/1024,2))
    #round(value,key)为将value，四舍五入为key的位数
    return memory_G

def mfunc_memory_useage():
    #此函数用于获得内存的占用情况，单位为G，包含总大小，已使用，未使用及使用率百分比
    memory_all=psutil.virtual_memory()
    memory_total=round(memory_all[0]/1024/1024/1024,2)
    memory_used=round(memory_all[3]/1024/1024/1024,2)
    memory_free=round((memory_all[1]+memory_all[4])/1024/1024/1024,2)
    memory_used_percent=memory_all[2]
    return memory_total,memory_used,memory_free,memory_used_percent

def mfunc_swap_memory():
    #此函数用于获得内存交换区的信息，单位为G，包含总大小，已使用，未使用，及使用率百分比
    swap_memory_all=psutil.swap_memory()
    swap_memory_total=round(swap_memory_all[0]/1024/1024/1024,2)
    swap_memory_used=round(swap_memory_all[1]/1024/1024/1024,2)
    swap_memory_free=round(swap_memory_all[2]/1024/1024/1024,2)
    swap_memory_percent=swap_memory_all[3]
    return swap_memory_total,swap_memory_used,swap_memory_free,swap_memory_percent

def mfunc_hdd_total():
    #此函数用于返回磁盘相关信息，包含容量、已用、空闲及使用率的统计
    disk_all=psutil.disk_usage('/')
    disk_total=round(disk_all[0]/1024/1024/1024,2)
    #读取硬盘空间大小，并换算成G单位，保留小数点后2位
    disk_used=round(disk_all[1]/1024/1024/1024,2)
    disk_free=round(disk_all[2]/1024/1024/1024,2)
    disk_used_percent=round(disk_all[3])
    return disk_total,disk_used,disk_free,disk_used_percent

def mfunc_network_io():
    #此函数用于返回网络接口IO信息，包含发送byte,接收byte，发送包，接收包，总错误包（发送+接收），总丢弃包（发送+接收）
    network_io_all=psutil.net_io_counters()
    network_io_sent=network_io_all[0]
    network_io_receive=network_io_all[1]
    network_io_packet_sent=network_io_all[2]
    network_io_packet_recevie=network_io_all[3]
    network_io_err=network_io_all[4]+network_io_all[5]
    network_io_drop=network_io_all[6]+network_io_all[7]
    return network_io_sent, \
          network_io_receive, \
          network_io_packet_sent, \
          network_io_packet_recevie, \
          network_io_err, \
          network_io_drop

#if __name__ == '__main__':
#    mfunc_memory_useage()
#    m1=mfunc_hostname()
#    print(m)
#    print(m1)