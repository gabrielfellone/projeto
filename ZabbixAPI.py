#!/usr/bin/env python
#-*-coding: utf-8-*-
from zabbix_api import ZabbixAPI
zapi=ZabbixAPI(server="SITE")
#Conexão com Zabbix Server
zapi.login("Login","Senha")
#Versao do Zabbix 
print "Version Zabbix:", zapi.api_version()
#Printa os hosts 
hosts = zapi.host.get({"output": "extend", "sortfield": "name"})
for x in hosts:
    print x['available'], "-", x['hostid'], "-", x['name']
#Printa os Triggers
trigger = zapi.trigger.get(only_true=1,
                            skipDependent=1,
                            monitored=1,
                            active=1,
                            output='extend',
                            expandDescription=1,
                            selectHosts=['host'],
                            )


for y in trigger:
	print y['description'], "--", y['host']
#Print UPTIME
uptime = zapi.item.get({'output': "extend", 'hostids': 10084, 'search': {'key_':'system.uptime'}})
print "Tempo",uptime[0]['lastvalue']
trigger = zapi.trigger.get[{'output': "extend", 'group': "HSM"}]
print "Triggers",trigger
