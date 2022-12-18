# 练习代码合集
脚哥代码：
https://github.com/script-money/ta-learn 

wayne 代码：
https://github.com/wzwmm2006/Trade

陈勇代码：
https://github.com/yoiochen/ta-learn/tree/main/ta_learn

冰雨代码：
https://github.com/bingyu-cpu/Trade


# week 1
1.通过ccxt，拉取BTC/ETH日线交易数据，利用pandas处理数据

# week 2
逻辑判断

当日BTC涨幅大于ETH，次日买入BTC，反之买入ETH，追涨策略

当日BTC涨幅低于ETH，次日买入BTC，反之买入ETH，补涨策略

得出强净值曲线（追涨策略），弱净值曲线（补涨策略），计算最大回撤

# week 3

优化三个方向：

1、N 从1遍历到20  （N为涨跌幅的周期）

2、BTC 和ETH ，谁强买谁

3、当BTC 和ETH 涨幅都小于0的时候空仓

4、币种从2个增加到10个甚至30个,选出其中表现好的3个币种,资金分配1：1：1，之后资金分配 5：3：2，分别得出测试结果

# week 4 

实盘：
1、ccxt/币安API 链接：https://www.binance.com/zh-CN/binance-api ，获取币安的apikey，勾选交易功能，实现现货开仓/平仓，合约开仓/平仓功能

注：apikey存储在配置文件，可设置ip 限制，记得搞个新的币安账户，给自己的大号返佣金

加：
如何用python创建 boll_20的数据
相关支持库
     https://github.com/mpquant/MyTT
     
     https://github.com/HuaRongSAO/talib-document#%E5%AE%89%E8%A3%85ta-lib

2、简化流程，获取K线数据，计算开盘买哪个币
...待补充

3、开仓买币
...待补充



