#coding=utf-8
from . import main

@main.app_template_filter('replace_none')
def replace_none(data):
    if not data:
        return ""
    return data

# @main.app_template_filter('replace_type')
# def replace_type(data):
#     if not data:
#         return ''
#     type_dict = {
#         1: '服务器设备',
#         2: '存储设备',
#         3: '网络设备',
#         4: '传输设备'
#     }
#     return type_dict[data]
#
# @main.app_template_filter('replace_serial')
# def replace_serial(data):
#     return [data-9766]
#
# @main.app_template_filter('replace_idc')
# def replace_idc(data):
#     if not data:
#         return ''
#     idc_dict = {
#         1: '转塘',
#         2: '三墩',
#         3: '白马湖',
#     }
#     return idc_dict[data]
#
# @main.app_template_filter('replace_state')
# def replace_state(data):
#     if not data:
#         return ''
#     state_dict = {
#         1: '开机',
#         4: '关机',
#     }
#     return state_dict[data]
#
# @main.app_template_filter('replace_evaluation')
# def replace_evaluation(data):
#     if not data:
#         return ''
#     evaluation_dict = {
#         1: '不下架',
#         4: '下架',
#     }
#     return evaluation_dict[data]
#
# @main.app_template_filter('replace_ip')
# def replace_ip(data):
#     if not data:
#         return ""
#     ch2 = lambda x: '.'.join([str(x / (256 ** i) % 256) for i in range(3, -1, -1)])
#     return ch2(int(data))