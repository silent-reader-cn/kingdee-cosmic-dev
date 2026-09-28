# 现金流量分析表-theme_cash_flow_bill

## 现金流量分析表-主表 t_theme_cash_flow

- **表名称：** 现金流量分析表-主表
- **表名：** t_theme_cash_flow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fczlc01 | 偿还债务支付的现金 | numeric | 23 | 10 |  | null | 偿还债务支付的现金 |
| 3 | fczlc02 | 分配股利、利润或偿付利息支付的现金 | numeric | 23 | 10 |  | null | 分配股利、利润或偿付利息支付的现金 |
| 4 | fjylr01 | 销售商品、提供劳务收到的现金 | numeric | 23 | 10 |  | null | 销售商品、提供劳务收到的现金 |
| 5 | fjylc07 | 支付给职工以及为职工支付的现金 | numeric | 23 | 10 |  | null | 支付给职工以及为职工支付的现金 |
| 6 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 7 | fjylc08 | 支付的各项税费 | numeric | 23 | 10 |  | null | 支付的各项税费 |
| 8 | fczlc05 | 支付其他与筹资活动有关的现金 | numeric | 23 | 10 |  | null | 支付其他与筹资活动有关的现金 |
| 9 | fjylc09 | 支付其他与经营活动有关的现金 | numeric | 23 | 10 |  | null | 支付其他与经营活动有关的现金 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fczje | 筹资活动产生的现金流量净额 | numeric | 23 | 10 |  | null | 筹资活动产生的现金流量净额 |
| 14 | fjylc01 | 购买商品、接受劳务支付的现金 | numeric | 23 | 10 |  | null | 购买商品、接受劳务支付的现金 |
| 15 | fczlc | 筹资活动现金流出小计 | numeric | 23 | 10 |  | null | 筹资活动现金流出小计 |
| 16 | fxjjzj | 现金及现金等价物净增加额 | numeric | 23 | 10 |  | null | 现金及现金等价物净增加额 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | ftzlr04 | 处置子公司及其他营业单位收到的现金净额 | numeric | 23 | 10 |  | null | 处置子公司及其他营业单位收到的现金净额 |
| 19 | ftzlr | 投资活动现金流入小计 | numeric | 23 | 10 |  | null | 投资活动现金流入小计 |
| 20 | ftzlr03 | 处置固定资产、无形资产和其他长期资产收回的现金净额 | numeric | 23 | 10 |  | null | 处置固定资产、无形资产和其他长期资产收回的现金净额 |
| 21 | fhlbd | 汇率变动对现金及现金等价物的影响 | numeric | 23 | 10 |  | null | 汇率变动对现金及现金等价物的影响 |
| 22 | fjylc | 经营活动现金流出小计 | numeric | 23 | 10 |  | null | 经营活动现金流出小计 |
| 23 | ftzlr02 | 取得投资收益收到的现金 | numeric | 23 | 10 |  | null | 取得投资收益收到的现金 |
| 24 | fjylr13 | 收到的税费返还 | numeric | 23 | 10 |  | null | 收到的税费返还 |
| 25 | ftzlr01 | 收回投资收到的现金 | numeric | 23 | 10 |  | null | 收回投资收到的现金 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fqmxj | 期末现金及现金等价物余额 | numeric | 23 | 10 |  | null | 期末现金及现金等价物余额 |
| 28 | fjylr14 | 收到其他与经营活动有关的现金 | numeric | 23 | 10 |  | null | 收到其他与经营活动有关的现金 |
| 29 | fxjfz01 | 净利润 | numeric | 23 | 10 |  | null | 净利润 |
| 30 | ftzlr06 | 收到其他与投资活动有关的现金 | numeric | 23 | 10 |  | null | 收到其他与投资活动有关的现金 |
| 31 | fczlr | 筹资活动现金流入小计 | numeric | 23 | 10 |  | null | 筹资活动现金流入小计 |
| 32 | ftzlc04 | 取得子公司及其他营业单位支付的现金净额 | numeric | 23 | 10 |  | null | 取得子公司及其他营业单位支付的现金净额 |
| 33 | ftzlc | 投资活动现金流出小计 | numeric | 23 | 10 |  | null | 投资活动现金流出小计 |
| 34 | fczlr02 | 取得借款收到的现金 | numeric | 23 | 10 |  | null | 取得借款收到的现金 |
| 35 | fczlr01 | 吸收投资收到的现金 | numeric | 23 | 10 |  | null | 吸收投资收到的现金 |
| 36 | ftzlc02 | 投资支付的现金 | numeric | 23 | 10 |  | null | 投资支付的现金 |
| 37 | ftzlc01 | 购建固定资产、无形资产和其他长期资产支付的现金 | numeric | 23 | 10 |  | null | 购建固定资产、无形资产和其他长期资产支付的现金 |
| 38 | fjylr | 经营活动现金流入小计 | numeric | 23 | 10 |  | null | 经营活动现金流入小计 |
| 39 | ftzje | 投资活动产生的现金流量净额 | numeric | 23 | 10 |  | null | 投资活动产生的现金流量净额 |
| 40 | fqcxj | 期初现金及现金等价物余额 | numeric | 23 | 10 |  | null | 期初现金及现金等价物余额 |
| 41 | fjxrate | 经营现金流占净利润比例 | numeric | 23 | 10 |  | null | 经营现金流占净利润比例 |
| 42 | fczlr05 | 收到其他与筹资活动有关的现金 | numeric | 23 | 10 |  | null | 收到其他与筹资活动有关的现金 |
| 43 | ftzlc06 | 支付其他与投资活动有关的现金 | numeric | 23 | 10 |  | null | 支付其他与投资活动有关的现金 |
| 44 | fjyje | 经营活动产生的现金流量净额 | numeric | 23 | 10 |  | null | 经营活动产生的现金流量净额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_cash_flow |  | fid |
| 2 | idx_cash_flow_report |  | fipoorgld,freportdate |
