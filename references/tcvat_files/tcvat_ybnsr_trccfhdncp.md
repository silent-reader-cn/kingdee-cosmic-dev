# 投入产出法核定农产品增值税进项税额计算表-tcvat_ybnsr_trccfhdncp

## 投入产出法核定农产品增值税进项税额计算表-主表 t_tcvat_ybnsr_trccfhdncp

- **表名称：** 投入产出法核定农产品增值税进项税额计算表-主表
- **表名：** t_tcvat_ybnsr_trccfhdncp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fkcl | 扣除率（%） | numeric | 23 | 10 | √ | 0 | 扣除率（%） |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :合计 2 :2 |
| 4 | fcpmc | 产品名称 | int8 | 64 |  | √ | 0 | 税务辅助数据分录 tpo_tcvat_assist_entry |
| 5 | fseqno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 6 | fpjgmdj | 平均购买单价（元/吨） | numeric | 23 | 10 | √ | 0 | 平均购买单价（元/吨） |
| 7 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 8 | fdqyxdkncpjxse | 当期允许抵扣农产品进项税额（元） | numeric | 23 | 10 | √ | 0 | 当期允许抵扣农产品进项税额（元） |
| 9 | fhyncpmc | 耗用农产品名称 | int8 | 64 |  | √ | 0 | 税务辅助数据分录 tpo_tcvat_assist_entry |
| 10 | fdqxshwsl | 当期销售货物数量（吨） | numeric | 23 | 10 | √ | 0 | 当期销售货物数量（吨） |
| 11 | fqckcncpsl | 期初库存农产品数量（吨） | numeric | 23 | 10 | √ | 0 | 期初库存农产品数量（吨） |
| 12 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 13 | fqcpjmj | 期初平均买价（元/吨） | numeric | 23 | 10 | √ | 0 | 期初平均买价（元/吨） |
| 14 | fhddhsl | 核定单耗数量（吨） | numeric | 23 | 10 | √ | 0 | 核定单耗数量（吨） |
| 15 | fdqmj | 当期买价（元/吨） | numeric | 23 | 10 | √ | 0 | 当期买价（元/吨） |
| 16 | fdqgjncpsl | 当期购进农产品数量（吨） | numeric | 23 | 10 | √ | 0 | 当期购进农产品数量（吨） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ybnsr_trccfhdncp |  | fid |
| 2 | idx_taxc_trccfhdncp_xh_sbbid |  | fewblxh,fsbbid |
