import json
import func_tools
import func_trans
import func_get_info_str

if __name__ == '__main__':
    #获取系统运行信息，转成json，发送至消息队列
    while True:
        data_json=json.dumps(func_get_info_str.mfunc_get_info_all())
        func_trans.mfunc_mqtt_pub(data_json)
        #注意执行时间，计算cpu负载的函数内周期为0.5s，意味着一秒产生两条记录，后期来检查核对！！！