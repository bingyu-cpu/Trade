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


def get_df(symbol, time_interval):
    data = get_price_list(symbol, time_interval)
    prince_list = []
    for single in data:
        print(single)
        timestamp = int(single[0]) / 1000
        time_localtime = time.localtime(timestamp)
        Open_time = time.strftime("%Y-%m-%d %H:%M:%S", time_localtime)
        # prince_list.append(
        #     [Open_time, float(single[1]), float(single[2]), float(single[3]), float(single[4]), float(single[5])])
        prince_list.append([Open_time, float(single[1]), float(single[4])])
        # df = pd.DataFrame(prince_list, columns=['date', 'open', 'hign', 'low', 'close', 'vol']).set_index('date')
        # 当前策略只需开盘价格 收盘价格
        df = pd.DataFrame(prince_list, columns=['date', 'open', 'close']).set_index('date')
        df['change'] = (df['close'] - df['open']) / df['open'] * 100
    return df


# 开盘时间Open_time 开盘价格O_prince 最高价格max_prince 最低价格min_prince 收盘价格C_prince 交易量 Value
def get_price_list(symbol, time_interval):
    exchange = ccxt.binance({'proxies': proxies})
    if exchange.has['fetchOrders']:
        end = exchange.milliseconds() - 86400000  # -1 day from now
        # alternatively, fetch from a certain starting datetime
        since = exchange.parse8601('2018-01-01T00:00:00Z')
        all_orders = []
        while since < end:
            limit = 500  # change for your limit
            orders = exchange.fetch_ohlcv(symbol, timeframe=time_interval, since=since, limit=limit)
            if len(orders):
                since = orders[len(orders) - 1][0] + 86400000
                all_orders += orders
            else:
                break
        return all_orders


if __name__ == '__main__':
    time_interval = '1d'
    btc_symbol = "BTC/USDT"
    btc_df = get_df(btc_symbol, time_interval)
    # 合并前修改下列名
    btc_df.rename(columns={"open": "btc_open", "close": "btc_close", "change": "btc_change"}, inplace=True)
    eth_symbol = "ETH/USDT"
    eth_df = get_df(eth_symbol, time_interval)
    eth_df.rename(columns={"open": "eth_open", "close": "eth_close", "change": "eth_change"}, inplace=True)
    df = pd.concat([btc_df, eth_df], axis=1)
    print(df)
    df.to_csv("日内涨幅表.csv")
