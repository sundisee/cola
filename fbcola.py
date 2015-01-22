#!/usr/bin/env python
# encoding: utf-8

from fabric.api import *

#操作一致的服务器可以放在一组，同一组的执行同一套操作
env.roledefs = {
            'ucloud1':['ubuntu@ucloud1:2233',],
            'ucloud2':['ubuntu@ucloud2:2233',],
            'ucloud3':['ubuntu@ucloud3:2233',],
            }

#env.password = '这里不要用这种配置了，不可能要求密码都一致的，明文编写也不合适。打通所有ssh就行了'
env.user=['ubuntu']
env.key_filename=['~/.ssh/ucloud_rsa']
env.hosts=['ucloud1','ucloud2','ucloud3']

def local_commit():
    with lcd('/var/web/qyer/nutspider/cola/'):
        # local('git add fbcola.py')
        local('git commit -m "fb"')
        local('git pull origin')
        local('git push origin')

@roles('ucloud1','ucloud3','ucloud3')
def task1():
    with cd('/var'):
        run('sudo mkdir -p /var/web/qyer/nutspider/')
        run('sudo chown -R ubuntu /var/web/ ')

@roles('ucloud1','ucloud2','ucloud3')
def task2():
    # run('mkdir -p /home/ubuntu/.ssh')
    # with cd('/home/ubuntu/.ssh'):
    #     run('ssh-keygen -t rsa')
    #     run('touch config')
    #     ssh_443 = """Host github.com\n    Hostname ssh.github.com\n    Port 443\n    IdentityFile ~/.ssh/github_rsa"""
    #     run('echo "%s">config' % ssh_443)
    #     run('eval "$(ssh-agent -s)"')
    #     run('chmod 700 github_rsa')
    #     run('ssh-add ~/.ssh/github_rsa')
    with settings(warn_only=True):
        run('ssh -T git@github.com')
    # put('/var/web/qyer/nutspider/manage.py','/var/web/qyer/nutspider/manage.py')

@roles('ucloud1','ucloud2','ucloud3')
def task3():
    with cd('/var/web/qyer/nutspider/'):
        run('git clone git@github.com:sundisee/cola.git')

#ucloud pull
@roles('ucloud1','ucloud2','ucloud3')
def task4():
    with cd('/var/web/qyer/nutspider/cola/'):
        run('git pull')

def dotask():
    # execute(local_commit)
    # execute(task1)
    # execute(task2)
    # execute(task3)
    execute(task4)

if __name__ == '__main__':
    dotask()