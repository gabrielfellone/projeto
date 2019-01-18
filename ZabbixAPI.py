#!/usr/bin/env python
#-*-coding: utf-8-*-
from zabbix_api import ZabbixAPI
zapi=ZabbixAPI(server="URL ZABBIX")
zapi.login("login","senha")
print "Version Zabbix:", zapi.api_version()
hosts = zapi.host.get({"output": "extend", "sortfield": "name"})
for x in hosts:
    print x['available'], "-", x['hostid'], "-", x['name']
uptime = zapi.item.get({'output': "extend", 'hostids': 10262,'search': {'key_':'system.uptime'}})
print "Tempo",uptime[0]['lastvalue']
