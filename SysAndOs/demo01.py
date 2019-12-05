import sys

print(sys.copyright) # 显示Python解释器有关的版权信息
# 'Copyright (c) 2001-2018 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'
print(sys.executable) # 显示Python解释器在磁盘上的存储路径
# 'C:\\Users\\xufiv\\AppData\\Local\\Programs\\Python\\Python37\\pythonw.exe'
print(sys.platform) # 显示Python解释器所在平台
# 'win32'
print(sys.version) # 显示当前Python解释器的版本信息
# '3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]'
print(sys.winver) # 返回当前Python解释器的主版本号
# '3.7'
print(sys.byteorder) # 显示本地字节序的指示符
# 'little'
sys.getfilesystemencoding() # 显示当前系统上保存文件所用的字符集
# 'utf-8'
print(sys.maxsize) # 显示Python整数支持的最大值
# 9223372036854775807
print(sys.path) # 使用 import 语句导入模块时，解释器会从这些目录中查找指定的模块
# ['', 'C:\\Users\\xufiv\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib', 'C:\\Users\\xufiv\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 'C:\\Users\\xufiv\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 'C:\\Users\\xufiv\\AppData\\Local\\Programs\\Python\\Python37\\lib', 'C:\\Users\\xufiv\\AppData\\Local\\Programs\\Python\\Python37', 'C:\\Users\\xufiv\\AppData\\Roaming\\Python\\Python37\\site-packages', 'C:\\Users\\xufiv\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages', 'C:\\Users\\xufiv\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\win32', 'C:\\Users\\xufiv\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\win32\\lib', 'C:\\Users\\xufiv\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\Pythonwin']
print(sys.argv) # 获取运行 Python 程序的命令行参数
# ['']