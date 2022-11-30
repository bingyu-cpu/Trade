# Trade

数据采集
1. 更新到采集18年-至今数据，合并BTC，ETH数据
新增知识
合并前修改下列名
  pd.rename(columns=["原名""修改名”, inplace = True) 修改列名
合并数据
  df = pd.concat([btc_df, eth_df], axis=1)  合并列表 axis=1 左右合并 axis=0 上下合并
    
