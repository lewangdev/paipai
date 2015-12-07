#coding=utf8
import json
import matplotlib.pyplot as plt
marker = ['D', 's', 'p', 'o']
def get_data(filename):
    x = []
    y = []
    with open('data/%s.json' % filename, 'r') as rfile:
        records = json.loads(rfile.read())
        for row in records['rows']:
            csv_row = []
            x.append(int(row['system_time'][-2:]))
            y.append(row['lowest_price'])
    x = x[-45:]
    y = y[-45:]
    return x, y

i = 0
for f in ['201507', '201508', '201509', '201510']:
    x, y = get_data(f)
    plt.plot(x, y, '-' + marker[i], label=f)
    i += 1

plt.legend(loc=4)
plt.xlabel(u'时间')
plt.ylabel(u'可接受价格')
plt.title(u'7-10月最后60秒')
plt.grid(True)
plt.savefig("test.png")
plt.show()

