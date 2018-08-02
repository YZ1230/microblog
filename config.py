#/user/bin/env/python
#-*- coding:utf-8 -*-
'''
author：baizhou
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # 配置数据库
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置发生错误后，立刻发送电子邮件给我，邮件正文中显示错误的堆栈跟踪

    # 设置mail服务
    MAIL_SERVER = 'smtp.qq.com'
    # 设置端口
    MAIL_PORT = 465  # 端口
    # MAIL_USE_TLS = int(os.environ.get('MAIL_USE_TLS')) is not None
    MAIL_USE_SSL = True
    MAIL_USERNAME = '2493310038@qq.com'
    MAIL_PASSWORD = 'dzgtvwmdeykweajd'


    # app.config['MAIL_DEBUG'] = True  # 开启debug，便于调试看信息
    # app.config['MAIL_SUPPRESS_SEND'] = False  # 发送邮件，为True则不发送
    # app.config['MAIL_SERVER'] = 'smtp.qq.com'  # 邮箱服务器
    # app.config['MAIL_PORT'] = 465  # 端口
    # app.config['MAIL_USE_SSL'] = True  # 重要，qq邮箱需要使用SSL
    # app.config['MAIL_USE_TLS'] = False  # 不需要使用TLS
    # app.config['MAIL_USERNAME'] = '2493310038@qq.com'  # 填邮箱
    # app.config['MAIL_PASSWORD'] = 'dzgtvwmdeykweajd'  # 填授权码
    # app.config['MAIL_DEFAULT_SENDER'] = '2493310038@qq.com'  # 填邮箱，默认发送者


    # 设置分页
    POSTS_PER_PAGE = 25

    # 设置支持翻译的语言
    LANGUAGES = ['en','es']














