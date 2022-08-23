#!/usr/bin/env python3
# coding:utf-8

#连接zookeeper测试
from kazoo.client import KazooClient
zk = KazooClient(hosts='10.96.51.12:3181')
zk.start()
node=zk.get_children('/')
print (node)
zk.stop()

