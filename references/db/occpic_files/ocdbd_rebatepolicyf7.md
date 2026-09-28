# 返利政策F7-ocdbd_rebatepolicyf7

## 返利政策F7-主表 t_occpic_rebatepolicy

- **表名称：** 返利政策F7-主表
- **表名：** t_occpic_rebatepolicy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factivityplanid | factivityplanid | int8 | 64 |  | √ | 0 |  |
| 3 | faccrualformulaid | faccrualformulaid | int8 | 64 |  | √ | 0 |  |
| 4 | fnrebateclassid | fnrebateclassid | int8 | 64 |  | √ | 0 |  |
| 5 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 6 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 7 | fbizorgid | fbizorgid | int8 | 64 |  | √ | 0 |  |
| 8 | fpushtype | fpushtype | bpchar | 1 |  | √ | 'A' |  |
| 9 | fcustomdaterange | fcustomdaterange | varchar | 2000 |  | √ | ' ' |  |
| 10 | fexpensetypeid | fexpensetypeid | int8 | 64 |  | √ | 0 |  |
| 11 | fbaselineamount | fbaselineamount | numeric | 23 | 10 | √ | 0 |  |
| 12 | fbillno | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 13 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 14 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 15 | fsettperiod | fsettperiod | bpchar | 1 |  | √ | ' ' |  |
| 16 | fbaselineqty | fbaselineqty | numeric | 23 | 10 | √ | 0 |  |
| 17 | fnladdertypeid | fnladdertypeid | int8 | 64 |  | √ | 0 |  |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 20 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 21 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 22 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 23 | fstarttime | fstarttime | timestamp | 0 |  |  | null |  |
| 24 | fcalscopetype | fcalscopetype | bpchar | 1 |  | √ | ' ' |  |
| 25 | fbalanceorgid | fbalanceorgid | int8 | 64 |  | √ | 0 |  |
| 26 | fcalbilltypeid | fcalbilltypeid | int8 | 64 |  | √ | 0 |  |
| 27 | fnrebatetypeid | fnrebatetypeid | int8 | 64 |  | √ | 0 |  |
| 28 | fendtime | fendtime | timestamp | 0 |  |  | null |  |
| 29 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 31 | fkpiid | fkpiid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebatepolicy_bno |  | fbillno |
| 2 | pk_occpic_rebatepolicy |  | fid |
