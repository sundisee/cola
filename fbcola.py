#!/usr/bin/env python
# encoding: utf-8

from fabric.api import *

#操作一致的服务器可以放在一组，同一组的执行同一套操作
env.roledefs = {
            'ucloud': ['ubuntu@ucloud1:2233','ubuntu@ucloud2:2233','ubuntu@ucloud3:2233',],
            }

#env.password = '这里不要用这种配置了，不可能要求密码都一致的，明文编写也不合适。打通所有ssh就行了'
env.user=['ubuntu']
env.key_filename=['~/.ssh/ucloud_rsa']
env.hosts=['ucloud2','ucloud1','ucloud3']

def local_commit():
    with lcd('/var/web/qyer/nutspider/cola/'):
        local('git add fbcola.py')
        local('git commit -m "fb"')
        local('git pull origin')
        local('git push origin')

@roles('ucloud')
def task1():
    run('ls -l | wc -l')




def dotask():
    execute(local_commit)
    # execute(task1)

if __name__ == '__main__':
    dotask()