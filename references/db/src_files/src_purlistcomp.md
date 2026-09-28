# 采购清单组件ID查询-src_purlistcomp

## 采购清单组件ID查询-主表 t_src_purlist

- **表名称：** 采购清单组件ID查询-主表
- **表名：** t_src_purlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 4 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 5 | fmaintainclause | fmaintainclause | varchar | 50 |  | √ | ' ' |  |
| 6 | forigin | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 7 | fchgsrcbillid | fchgsrcbillid | int8 | 64 |  | √ | 0 |  |
| 8 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 9 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 10 | fispurlistcomp | fispurlistcomp | bpchar | 1 |  | √ | '1' |  |
| 11 | fcondition | fcondition | varchar | 2000 |  | √ | ' ' |  |
| 12 | ftaxtype | 价格录入方式 | bpchar | 1 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 13 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 14 | fparentid | 寻源项目ID | varchar | 30 |  | √ | ' ' | 寻源项目ID |
| 15 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 16 | fentitykey | 组件标识 | varchar | 30 |  | √ | ' ' | 组件标识 |
| 17 | fdecisiontype | 决标方式 | bpchar | 1 |  | √ | ' ' | 决标方式,枚举: 1 :按单价决标 2 :按金额决标 |
| 18 | fsumqty | fsumqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | fbidchangeid | fbidchangeid | int8 | 64 |  | √ | 0 |  |
| 20 | fcosttypeid | fcosttypeid | int8 | 64 |  | √ | 0 |  |
| 21 | fpurtype | fpurtype | varchar | 30 |  | √ | ' ' |  |
| 22 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 23 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 24 | fsumtax | fsumtax | numeric | 23 | 10 | √ | 0 |  |
| 25 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 26 | fcompbillno | fcompbillno | varchar | 30 |  | √ | ' ' |  |
| 27 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlist_fentitykey |  | fentitykey |
| 2 | idx_src_purlist_fparentid |  | fparentid |
| 3 | pk_src_purlist |  | fid |
