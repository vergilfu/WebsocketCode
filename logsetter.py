#_*_coding:utf-8_*_
#!/usr/bin/env python
#Author:Vergil_Fu

import logging
def logsetter():
    logging.getLogger("requests").setLevel(logging.WARNING)
    logger2 = logging.getLogger()
    logger2.setLevel(logging.INFO)  # 设置打印级别
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    # 设置屏幕打印的格式
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger2.addHandler(sh)

    # 设置log保存
    fh = logging.FileHandler("tasklogger.log", encoding='utf8')
    fh.setFormatter(formatter)
    logger2.addHandler(fh)
    return logger2,sh,fh

