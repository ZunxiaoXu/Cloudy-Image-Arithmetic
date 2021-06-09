# author: muzhan
# contact: levio.pku@gmail.com
import os
import sys
import time
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头
 
cmd1 = 'CUDA_VISIBLE_DEVICES=0 nohup python3 train.py --dataroot hd/ --name 10-200_local --resize_or_crop none --loadSize 512 --fineSize 512 --label_nc 0 --no_instance --save_epoch_freq 200 --tf_log  --netG local --load_pretrain checkpoints/10-200_global --n_downsample_global 3 &'
cmd2 = 'CUDA_VISIBLE_DEVICES=1 nohup python3 train.py --dataroot hd/ --name 10-200_local --resize_or_crop none --loadSize 512 --fineSize 512 --label_nc 0 --no_instance --save_epoch_freq 200 --tf_log  --netG local --load_pretrain checkpoints/10-200_global --n_downsample_global 3 &'
#cmd3 = 'python3 print.py' 
def gpu_info():
    gpu_status = os.popen('nvidia-smi | grep %').read().split('|')
    gpu_memory1 = int(gpu_status[2].split('/')[0].split('M')[0].strip())
    gpu_memory2 = int(gpu_status[6].split('/')[0].split('M')[0].strip())
   # gpu_power = int(gpu_status[1].split('   ')[-1].split('/')[0].split('W')[0].strip())
    return gpu_memory1, gpu_memory2
 
 
def narrow_setup(interval=2):
    gpu_memory1, gpu_memory2 = gpu_info()
    i = 0
    while gpu_memory1 > 17480 and gpu_memory2 > 17480:  # set waiting condition
        gpu_memory1, gpu_memory2 = gpu_info()
        i = i % 5
        symbol = 'monitoring: ' + '>' * i + ' ' * (10 - i - 1) + '|'
        gpu_memory1_str = 'gpu memory1:%d MiB |' % gpu_memory1
        gpu_memory2_str = 'gpu memory2:%d MiB |' % gpu_memory2
        sys.stdout.write('\r' + gpu_memory1_str + ' ' + gpu_memory2_str + ' ' + symbol)
        sys.stdout.flush()
        time.sleep(interval)
        i += 1
    if gpu_memory1 < 17480:
        print('\n' + cmd1)
        os.system(cmd1)
        # 发信方的信息：发信邮箱，QQ 邮箱授权码
        from_addr = '893205894@qq.com'
        password = 'wjnmzqiuidrjbbjf'
 
        # 收信方邮箱
        to_addr = '893205894@qq.com'
 
        # 发信服务器
        smtp_server = 'smtp.qq.com'
 
        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        msg = MIMEText('send by python','plain','utf-8')
 
        # 邮件头信息
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('python test')
 
        # 开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server,465)
        # 登录发信邮箱
        server.login(from_addr, password)
        # 发送邮件
        server.sendmail(from_addr, to_addr, msg.as_string())
        # 关闭服务器
        server.quit()
    elif gpu_memory2 < 17480:
        print('\n' + cmd2)
        os.system(cmd2)
                # 发信方的信息：发信邮箱，QQ 邮箱授权码
        from_addr = '893205894@qq.com'
        password = 'wjnmzqiuidrjbbjf'
        
        # 收信方邮箱
        to_addr = '893205894@qq.com'

        # 发信服务器
        smtp_server = 'smtp.qq.com'

        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        msg = MIMEText('send by python','plain','utf-8')

        # 邮件头信息
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('python test')

        # 开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server,465)
        # 登录发信邮箱
        server.login(from_addr, password)
        # 发送邮件
        server.sendmail(from_addr, to_addr, msg.as_string())
        # 关闭服务器
        server.quit()

 
 
if __name__ == '__main__':
    narrow_setup()
