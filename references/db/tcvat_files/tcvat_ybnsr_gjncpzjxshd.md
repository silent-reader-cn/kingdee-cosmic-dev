# 购进农产品直接销售核定农产品增值税进项税额计算表-tcvat_ybnsr_gjncpzjxshd

## 购进农产品直接销售核定农产品增值税进项税额计算表-主表 t_tcvat_ybnsr_gjncpzjxshd

- **表名称：** 购进农产品直接销售核定农产品增值税进项税额计算表-主表
- **表名：** t_tcvat_ybnsr_gjncpzjxshd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fshl | 损耗率（%） | numeric | 23 | 10 | √ | 0 | 损耗率（%） |
| 3 | fkcl | 扣除率 | numeric | 23 | 10 | √ | 0 | 扣除率 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :合计 2 :2 |
| 5 | fncppjgmdj | 农产品平均购买单价（元/吨） | numeric | 23 | 10 | √ | 0 | 农产品平均购买单价（元/吨） |
| 6 | fcpmc | 产品名称 | int8 | 64 |  | √ | 0 | 税务辅助数据分录 tpo_tcvat_assist_entry |
| 7 | fshsl | 损耗数量 | numeric | 23 | 10 | √ | 0 | 损耗数量 |
| 8 | fseqno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 9 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 10 | fdqyxdkncpjxse | 当期允许抵扣农产品进项税额（元） | numeric | 23 | 10 | √ | 0 | 当期允许抵扣农产品进项税额（元） |
| 11 | fdqxsncpsl | 当期销售农产品数量（吨） | numeric | 23 | 10 | √ | 0 | 当期销售农产品数量（吨） |
| 12 | fqckcncpsl | 期初库存农产品数量（吨） | numeric | 23 | 10 | √ | 0 | 期初库存农产品数量（吨） |
| 13 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 14 | fqcpjmj | 期初平均买价（元/吨） | numeric | 23 | 10 | √ | 0 | 期初平均买价（元/吨） |
| 15 | fdqmj | 当期买价（元/吨） | numeric | 23 | 10 | √ | 0 | 当期买价（元/吨） |
| 16 | fdqgjncpsl | 当期购进农产品数量（吨） | numeric | 23 | 10 | √ | 0 | 当期购进农产品数量（吨） |
| 17 | fncpgjsl | 农产品购进数量 | numeric | 23 | 10 | √ | 0 | 农产品购进数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ybnsr_gjncpzjxshd |  | fid |
| 2 | idx_taxc_gjncpzjxshd_xh_sbbid |  | fewblxh,fsbbid |
