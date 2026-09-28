# 套利业务收益分析-lc_arbitrage

## 套利业务收益分析-主表 t_lc_arbitrage

- **表名称：** 套利业务收益分析-主表
- **表名：** t_lc_arbitrage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fswapincome | 掉期汇率收入 | numeric | 23 | 10 | √ | 0 | 掉期汇率收入 |
| 3 | fterm | 期限 | numeric | 23 |  | √ | 0 | 期限 |
| 4 | fendtermamout | 到期人民币本金金额 | numeric | 23 | 10 | √ | 0 | 到期人民币本金金额 |
| 5 | fswterm | 期限 | numeric | 23 |  | √ | 0 | 期限 |
| 6 | fdisterm | 期限 | numeric | 23 |  | √ | 0 | 期限 |
| 7 | ffxcurrency | 外币币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fpfcost | 后置资金成本 | numeric | 23 | 10 | √ | 0 | 后置资金成本 |
| 10 | fenddate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 11 | fbankcost | 银行费用 | numeric | 23 | 10 | √ | 0 | 银行费用 |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | freleaseamount | 到期释放资金 | numeric | 23 | 10 | √ | 0 | 到期释放资金 |
| 14 | fforwardrate | 远端汇率 | numeric | 23 | 10 | √ | 0 | 远端汇率 |
| 15 | ftimedeposit | 存款端：定存金额 | numeric | 23 | 10 | √ | 0 | 存款端：定存金额 |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fswendate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 18 | flcfee | 开证费用 | numeric | 23 | 10 | √ | 0 | 开证费用 |
| 19 | fdisstartdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 20 | fyearbizprofitrate | 年化净收益率 | numeric | 23 | 10 | √ | 0 | 年化净收益率 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fdiscount | 贴现端：贴现金额 | numeric | 23 | 10 | √ | 0 | 贴现端：贴现金额 |
| 23 | fswapexchange | 掉期汇兑收益 | numeric | 23 | 10 | √ | 0 | 掉期汇兑收益 |
| 24 | fswwithdraw | 掉期端：近端存款本金 | numeric | 23 | 10 | √ | 0 | 掉期端：近端存款本金 |
| 25 | fstartdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 26 | fspotpurchase | 即期购汇（离岸） | numeric | 23 | 10 | √ | 0 | 即期购汇（离岸） |
| 27 | fswfxwithdraw | 外币（欧元）本金 | numeric | 23 | 10 | √ | 0 | 外币（欧元）本金 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | ffinaldiscount | 息后贴现金额 | numeric | 23 | 10 | √ | 0 | 息后贴现金额 |
| 30 | fswstartdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 31 | fdisfee | 银行手续费 | numeric | 23 | 10 | √ | 0 | 银行手续费 |
| 32 | ffxprofixrate | 外币存款收益率 | numeric | 23 | 10 | √ | 0 | 外币存款收益率 |
| 33 | ffee | 银行手续费 | numeric | 23 | 10 | √ | 0 | 银行手续费 |
| 34 | fbizprofitrate | 净收益率 | numeric | 23 | 10 | √ | 0 | 净收益率 |
| 35 | fyearprofitrate | 年化净收益率 | numeric | 23 | 10 | √ | 0 | 年化净收益率 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | finterest | 定存利息收益 | numeric | 23 | 10 | √ | 0 | 定存利息收益 |
| 38 | fbizprofit | 业务净收益 | numeric | 23 | 10 | √ | 0 | 业务净收益 |
| 39 | fprofitrate | 净收益率 | numeric | 23 | 10 | √ | 0 | 净收益率 |
| 40 | faftertaxamount | 税后利息折人民币 | numeric | 23 | 10 | √ | 0 | 税后利息折人民币 |
| 41 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 42 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fdisenddate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fwithdrawal | 出金 | numeric | 23 | 10 | √ | 0 | 出金 |
| 46 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 47 | fdisinterest | 贴现利息支出 | numeric | 23 | 10 | √ | 0 | 贴现利息支出 |
| 48 | fsuretybillid | 关联保证金 | int8 | 64 |  | √ | 0 | [保证金存入处理F7 fbd_suretybill_f7](../fbd_files/fbd_suretybill_f7.md) |
| 49 | fbillcost | 单据成本 | numeric | 23 | 10 | √ | 0 | 单据成本 |
| 50 | fdisinterestrate | 利率 | numeric | 23 | 10 | √ | 0 | 利率 |
| 51 | flcamount | 开证金额 | numeric | 23 | 10 | √ | 0 | 开证金额 |
| 52 | fendtermtotal | 到期人民币总金额 | numeric | 23 | 10 | √ | 0 | 到期人民币总金额 |
| 53 | finterestrate | 利率 | numeric | 23 | 10 | √ | 0 | 利率 |
| 54 | fprofit | 净收益 | numeric | 23 | 10 | √ | 0 | 净收益 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_arbitrage |  | fid |
| 2 | idx_lc_arbitrage |  | fbillno |
