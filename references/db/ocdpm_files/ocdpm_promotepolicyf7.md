# 促销政策-ocdpm_promotepolicyf7

## 促销政策-主表 t_ocdpm_promotepolicy

- **表名称：** 促销政策-主表
- **表名：** t_ocdpm_promotepolicy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | 促销政策名称 | varchar | 80 |  | √ | ' ' | 促销政策名称 |
| 4 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :失效 |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | fdescribe | fdescribe | varchar | 1000 |  | √ | ' ' |  |
| 8 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 9 | fpriority | fpriority | numeric | 23 | 10 | √ | 0 |  |
| 10 | factivityplanid | factivityplanid | int8 | 64 |  | √ | 0 |  |
| 11 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | finvaliduserid | finvaliduserid | int8 | 64 |  | √ | 0 |  |
| 15 | feffectivedate | feffectivedate | timestamp | 0 |  |  | null |  |
| 16 | finvalidtime | finvalidtime | timestamp | 0 |  |  | null |  |
| 17 | fpromotetypeid | 促销类型 | int8 | 64 |  | √ | 0 | 渠道促销类型 ocdpm_promotiontype |
| 18 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillno | 政策编号 | varchar | 80 |  | √ | ' ' | 政策编号 |
| 20 | fexpirationdate | fexpirationdate | timestamp | 0 |  |  | null |  |
| 21 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promotepolicy |  | fid |
| 2 | idx_ocdpm_promotepolicy_no |  | fbillno |
