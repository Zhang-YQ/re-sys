import paho.mqtt.client as mqtt
import paho.mqtt.publish as mqtt_pub
import json
import func_db_operation

#def mfunc_mqtt_onconnect(client,userdata,flags,rc):
#    client.subscribe("dw/test")

def mfunc_mqtt_pub(message_str):
    #此函数用于mqtt_pub发送数据，接收由message_str传来的参数，并发送给broker
    message_str1=str(message_str)

    #下面一行调用了paho.mqtt.publish as mqtt_pub
    mqtt_pub.single("dw/test", \
                    payload=message_str1, \
                    hostname="192.168.2.201", \
                    port=1883,keepalive=60, \
                    #client_id="hostname1", \
                    transport="tcp")

def mqtt_on_connect(client,userdata,flags,rc):
    client.subscribe("dw/test")

def mqtt_on_message(client,userdata,msg):
    get_str=str(msg.payload.decode("utf-8"))
    str_all=json.loads(get_str)
    hostname1=str_all['Hostname']
    ipaddr1=str_all['IP Address']
    cpu_use1=str_all['CPU Useage']
    memory_use1=str_all['Memory']
    swap_use1=str_all['Swap']
    hdd_use1=str_all['HDD']
    network_io=str_all['Network IO']
    time_now=str_all['Time']
    func_db_operation.mfunc_db_insert(hostname1, \
                                      ipaddr1, \
                                      cpu_use1, \
                                      memory_use1, \
                                      swap_use1, \
                                      hdd_use1, \
                                      network_io, \
                                      time_now)

def mfunc_mqtt_sub():
    client=mqtt.Client()
    client.on_connect=mqtt_on_connect
    client.on_message=mqtt_on_message
    client.username_pw_set("user1","password1")
    client.connect("192.168.2.201",1883,60)
    client.loop_forever()

#if __name__ == '__main__':
#    print(mqtt_on_message())