# 匹配中文
# 大部分的中文内容表示范围是{u4e00 - u9fa5}，不包括全角标点

import re
title = u'世界 你好，hello moto'
p = re.compile(r'[\u4e00-\u9fa5]+')
rst = p.findall(title)
print(rst)