# 固定资产加速折旧汇总-tccit_assert_acce_total

## 固定资产加速折旧汇总-主表 t_tccit_assert_acce_total

- **表名称：** 固定资产加速折旧汇总-主表
- **表名：** t_tccit_assert_acce_total

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fispredata | 是否取上期数据 | bpchar | 1 |  | √ | '0' | 是否取上期数据 |
| 3 | fewblxh | 加速折旧摊销类型编码 | varchar | 30 |  | √ | ' ' | 加速折旧摊销类型编码,枚举: JSZJ0010 :固定资产加速折旧 JSZJ0020 :重要行业固定资产加速折旧 JSZJ0030 :其他行业研发设备加速折旧 JSZJ0040 :固定资产一次性扣除 JSZJ1010 :500万元以下设备器具一次性扣除 JSZJ1020 :疫情防控重点保障物资生产企业单价500万元以上设备一次性扣除 JSZJ1030 :海南自由贸易港企业固定资产一次性扣除 JSZJ1040 :海南自由贸易港企业无形资产一次性扣除 JSZJ1070 :中小微企业单价500万元以上设备器具一次性扣除（折旧年限为3年） JSZJ1080 :中小微企业单价500万元以上设备器具50%部分一次性扣除（折旧年限为4、5年） JSZJ1090 :中小微企业单价500万元以上设备器具50%部分一次性扣除（折旧年限为10年） |
| 4 | fbntotalzzdepre | 本年累计账载折旧\摊销 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计账载折旧\摊销 |
| 5 | fzcyz | 1.资产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 1.资产原值 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ftaxlimit | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: month :按月申报 season :按季申报 |
| 8 | fzzzjje1 | 本期取数金额-账载折旧金额 | numeric | 23 | 10 | √ | 0 | 本期取数金额-账载折旧金额 |
| 9 | fzzzjje | 2.账载折旧金额 | numeric | 23 | 10 | √ | 0.0000000000 | 2.账载折旧金额 |
| 10 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 11 | fewblname | 加速折旧摊销类型名称 | varchar | 50 |  | √ | ' ' | 加速折旧摊销类型名称 |
| 12 | fcurrentadjustamount1 | 本期取数金额-本期纳税调整金额 | numeric | 23 | 10 | √ | 0 | 本期取数金额-本期纳税调整金额 |
| 13 | fxsjszjyhjsdzjje | 4.享受加速折旧优惠计算的折旧金额 | numeric | 23 | 10 | √ | 0.0000000000 | 4.享受加速折旧优惠计算的折旧金额 |
| 14 | fcurrentadjustamount | 本期纳税调整金额 | numeric | 23 | 10 | √ | 0 | 本期纳税调整金额 |
| 15 | fxsjszjyhjsdzjje1 | 本期取数金额-享受加速折旧优惠计算的折旧金额 | numeric | 23 | 10 | √ | 0 | 本期取数金额-享受加速折旧优惠计算的折旧金额 |
| 16 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 17 | fbntotalsfdepre | 本年累计税法折旧\摊销 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计税法折旧\摊销 |
| 18 | fbntotaljsdepre | 本年累计加速折旧\摊销 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计加速折旧\摊销 |
| 19 | fruleid | 规则 | int8 | 64 |  | √ | 0 | [资产加速折旧摊销取数规则 tccit_depreciate_rule](../tccit_files/tccit_depreciate_rule.md) |
| 20 | ftaxorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fazssybgdjsdzjje | 3.按照税收一般规定计算的折旧金额 | numeric | 23 | 10 | √ | 0.0000000000 | 3.按照税收一般规定计算的折旧金额 |
| 22 | fpreadjustamount | 上期纳税调整金额 | numeric | 23 | 10 | √ | 0 | 上期纳税调整金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tccit_assert_acce_total_pkey |  | fid |
| 2 | idx_tccit_assert_acce_total |  | forgid,fskssqq,fskssqz |
