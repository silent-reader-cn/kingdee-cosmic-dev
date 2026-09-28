# 促销政策-ocdpm_promotepolicyf7

## 促销政策-主表 t_ocdpm_promotepolicy

- **表名称：** 促销政策-主表
- **表名：** t_ocdpm_promotepolicy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprioritygroup | fprioritygroup | int8 | 64 |  | √ | 1 |  |
| 3 | fdescribe | fdescribe | varchar | 1000 |  | √ | ' ' |  |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fpriority | fpriority | numeric | 23 | 10 | √ | 0 |  |
| 6 | factivityplanid | factivityplanid | int8 | 64 |  | √ | 0 |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 9 | fexpensetypeid | fexpensetypeid | int8 | 64 |  | √ | 0 |  |
| 10 | feffectivedate | feffectivedate | timestamp | 0 |  |  | null |  |
| 11 | finvalidtime | finvalidtime | timestamp | 0 |  |  | null |  |
| 12 | fbillno | 政策编号 | varchar | 80 |  | √ | ' ' | 政策编号 |
| 13 | fexpirationdate | fexpirationdate | timestamp | 0 |  |  | null |  |
| 14 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 15 | fname | 促销政策名称 | varchar | 80 |  | √ | ' ' | 促销政策名称 |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :失效 |
| 18 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 19 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 20 | fpriorityn | fpriorityn | int8 | 64 |  | √ | 0 |  |
| 21 | finvaliduserid | finvaliduserid | int8 | 64 |  | √ | 0 |  |
| 22 | fpromotetypeid | 促销类型 | int8 | 64 |  | √ | 0 | [渠道促销类型 ocdpm_promotiontype](../ocdpm_files/ocdpm_promotiontype.md) |
| 23 | fcostresponsible | fcostresponsible | bpchar | 1 |  | √ | 'A' |  |
| 24 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promotepolicy |  | fid |
| 2 | idx_ocdpm_pp_statustm |  | fbillstatus,feffectivedate,fexpirationdate |
| 3 | idx_ocdpm_promotepolicy_no |  | fbillno |
