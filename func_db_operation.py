import pymysql

def mfunc_db_insert(out_hostname,out_ipaddr,out_cpu,out_memory,out_swap,out_hdd,out_network,out_time):
    conn=pymysql.Connect(host="192.168.2.204", \
                             user="root", \
                             password="zghhr666", \
                             db="re_database", \
                             port=3306, \
                             charset="utf8")

    sql_str="INSERT INTO server_info (hostname," \
            "ipaddress_list," \
            "cpu_useage," \
            "memory_useage," \
            "swap_useage," \
            "hdd_useage," \
            "nework_io," \
            "time) VALUES ('"+out_hostname+"','"+out_ipaddr+"','"+out_cpu+"','"+out_memory+"','"+out_swap+"','"+ \
            out_hdd+"','"+out_network+"','"+out_time+"')"
    cur = conn.cursor()
    cur.execute(sql_str)
    conn.commit()

def mfunc_db_select_one():
    conn = pymysql.Connect(host="192.168.2.204", \
                           user="root", \
                           password="zghhr666", \
                           db="re_database", \
                           port=3306, \
                           charset="utf8")
    sql_str="SELECT hostname," \
            "ipaddress_list," \
            "cpu_useage,memory_useage," \
            "swap_useage," \
            "hdd_useage," \
            "nework_io," \
            "time FROM server_info ORDER BY sn DESC"
    cur=conn.cursor()
    cur.execute(sql_str)
    result1=cur.fetchone()
#    print(result1)
    return result1

#if __name__ == '__main__':
#    mfunc_db_select_one()