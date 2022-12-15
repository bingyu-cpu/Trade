# week 4 

实盘：
1、ccxt 下单，链接：https://www.binance.com/zh-CN/binance-api
     获取币安的apikey，勾选交易功能，以下用合约演示
     a、获取仓位函数  fapiPrivateGetAccount
     b、开仓平仓函数 fapiPrivatePostOrder({ symbol, side, type, quantity })
      symbol 代表币种名称
      side 表示 'BUY' or 'SELL'
      type 表示 '市价' 或者其他类型
      quantity 表示下单数量，要计算最小下单数量，比如btc 合约是 0.001，eth 是0.01 等等
注：apikey存储在配置文件，可设置ip 限制，记得搞个新的币安账户，给自己的大号返佣金


加：
如何用python创建 boll_20的数据，什么是布林通道：https://baike.baidu.com/item/%E5%B8%83%E6%9E%97%E9%80%9A%E9%81%93%E6%8C%87%E6%A0%87/2067149?fr=aladdin
布林通道有 三根线，up，mid，down，我们都用收盘价做布林通道
def boll_standard(df, n=20, std=2, col='收盘价'):
    df['mid'] = df[col].rolling(n, min_periods=1).mean()
    df['std'] = df[col].rolling(n, min_periods=1).std(ddof=0)
    df['up'] = df['mid'] + df['std'] * std
    df['down'] = df['mid'] - df['std'] * std
    return df

计算得出20日的布林通道，mid 就是均线，20日价格的均线，然后算一个 20日的标准差
布林上线就是 均线 + 标准差*2
布林下线就是 均线 -  标准差*2

相关分析
与RSI等技术指标类似，布林通道线也根据价格所处于布林通道内的位置来评估走势的强弱。当价格线位于布林线中轨之趋势偏强，处于布林线中轨之下，则趋势看淡。布林通道的两极为上轨和下轨，表示极强和极弱。二，
1.当价格穿越上限压力线时,卖点信号
2.当价格穿越下限支撑线时.买点信号
3.当价格由下向上穿越中界限时,为加码信号
4.当价格由上向下穿越中界线时,为卖出信号
操作原则
布林线的最主要的理论原则有以下五条
1、价格由下向上穿越Down线时，可视为买进信号。
2、价格由下向上穿越中间线时，则有可能加速上行，是加仓买进的信号.
3、价格在中间线与Up线之间波动运行时为多头市场，可持多或加码。
4、价格长时间在中间线与Up线间运行后，由上往下跌破中间线为卖出信号5、价格在中间线与Down线之间向下波动运行时为空头市场，可持空或加抛。


简单一点就是用布林线做一个择时，什么时候开仓，什么时候平仓

2、简化流程，获取K线数据，计算开盘买哪个币
3、开仓买币
