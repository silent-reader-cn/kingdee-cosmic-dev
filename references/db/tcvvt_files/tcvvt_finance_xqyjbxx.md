# 小企业会计准则基本信息-tcvvt_finance_xqyjbxx

## 小企业会计准则基本信息-主表 t_tcvvt_finance_xqyjbxx

- **表名称：** 小企业会计准则基本信息-主表
- **表名：** t_tcvvt_finance_xqyjbxx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 3 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 4 | fljjemc | 累计金额名称 | varchar | 50 |  | √ | ' ' | 累计金额名称 |
| 5 | fqsjemc | 取数金额名称 | varchar | 50 |  | √ | ' ' | 取数金额名称 |
| 6 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvvt_finance_xqyjbxx |  | fid |
| 2 | idx_tcvvt_finance_xqyjbxx |  | fsbbid |
