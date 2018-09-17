day = '星期一星期二星期三星期四星期五星期六星期天'
n = input('请输入星期几(1~7l):')
val = (int(n)-1) * 3
dayabbrev = day[val:val+3]
print('今天日期是：',dayabbrev)
