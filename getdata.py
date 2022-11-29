import ccxt
import time
import pandas as pd

pd.set_option('display.float_format', lambda x: '%.5f' % x)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 100000)
pd.set_option('display.width', 160)

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}

# 开盘时间Open_time 开盘价格O_prince 最高价格max_prince 最低价格min_prince 收盘价格C_prince 交易量 Value
def get_price_list(symbol, time_interval):
    exchange = ccxt.binance({'proxies': proxies})
    data = exchange.fetch_ohlcv(symbol=symbol, timeframe=time_interval)
    prince_list = []
    for single in data:
        # print(single)
        timestamp = int(single[0]) / 1000
        time_localtime = time.localtime(timestamp)
        Open_time = time.strftime("%Y-%m-%d %H:%M:%S", time_localtime)
        prince_list.append(
            [Open_time, float(single[1]), float(single[2]), float(single[3]), float(single[4]), float(single[5])])
        df = pd.DataFrame(prince_list, columns=['date', 'open', 'hign', 'low', 'close', 'vol']).set_index('date')
        df['change'] = (df['close'] - df['open']) / df['open'] * 100
    return df


if __name__ == '__main__':
    symbol = "BTC/USDT"
    time_interval = '1d'
    df = get_price_list(symbol, time_interval)
    # print(df)
    df.to_csv(symbol.replace('/', '') + "日内涨幅表.csv")
