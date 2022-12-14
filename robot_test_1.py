import pandas as pd
import matplotlib.pyplot as plt
import time


def selectMax(tmp):
    # tmp = tmp.copy()
    # nlargest 取元素最大 ； nsmallest 取元素最小
    # change = tmp.nsmallest(1)[0]
    symbols = tmp.nlargest(1).index
    tmp[symbols] = 1
    return tmp


if __name__ == '__main__':
    df = pd.read_csv('BTCETH轮动.csv')
    df_add = df[['Date_btc', 'R_net_value_1', 'Q_net_value']]
    df = df[['Date_btc', 'btc_change', 'eth_change']].set_index('Date_btc')
    df_add = pd.DataFrame(df_add, columns=['Date_btc', 'R_net_value_1', 'Q_net_value']).set_index('Date_btc')
    # 构建因子矩阵
    df_factory = df[['btc_change', 'eth_change']].shift(1)  # 往后一天
    # 构建x信号矩阵
    df_signal = df_factory.apply(selectMax, axis=1)

    df_pnl = (df_signal * df).sum(axis=1)  # 根据涨幅 * 需要购买的币种，得出净值
    df_pnl = pd.DataFrame(df_pnl, columns=['pnl'])
    # df_pnl['pnl_cum'] = df_pnl['pnl'].cumsum()  # 累计净值增长
    df_pnl['net_value'] = (df_pnl['pnl'] + 1).cumprod()  # 累计复利增长
    df_all = pd.concat([df_add, df_pnl], axis=1)
    # print(df_all)
    df_all.rename(columns={"R_net_value_1": "R_net_value"}, inplace=True)
    df_all[['R_net_value', 'Q_net_value', 'net_value']].plot()
    plt.show()
