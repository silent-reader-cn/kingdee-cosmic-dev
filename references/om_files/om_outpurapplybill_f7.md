# 委外采购申请单f7-om_outpurapplybill_f7

## 委外采购申请单f7-主表 t_pm_purapplybill

- **表名称：** 委外采购申请单f7-主表
- **表名：** t_pm_purapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbidstatus | fbidstatus | varchar | 5 |  | √ | ' ' |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 5 | fcancelstatus | fcancelstatus | varchar | 5 |  | √ | ' ' |  |
| 6 | fbiztime | fbiztime | timestamp | 0 |  |  | null |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fchangestatus | fchangestatus | varchar | 5 |  | √ | ' ' |  |
| 9 | fistax | fistax | bpchar | 1 |  | √ | '1' |  |
| 10 | fcancelerid | fcancelerid | int8 | 64 |  | √ | 0 |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 13 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 14 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 15 | fbillno | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fversion | fversion | varchar | 30 |  | √ | '1' |  |
| 17 | funitsrctype | funitsrctype | varchar | 30 |  | √ | ' ' |  |
| 18 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 19 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcomment | fcomment | varchar | 512 |  |  | null |  |
| 22 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 23 | fbizuserid | fbizuserid | int8 | 64 |  | √ | 0 |  |
| 24 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 25 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 26 | fbillcretype | fbillcretype | varchar | 5 |  | √ | '0' |  |
| 27 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 28 | fclosestatus | fclosestatus | varchar | 5 |  | √ | ' ' |  |
| 29 | fsubversion | fsubversion | varchar | 30 |  | √ | '1' |  |
| 30 | fcanceldate | fcanceldate | timestamp | 0 |  |  | null |  |
| 31 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 32 | finquirystatus | finquirystatus | varchar | 5 |  | √ | ' ' |  |
| 33 | ftaxinprice | ftaxinprice | bpchar | 1 |  | √ | '0' |  |
| 34 | ftotalallamount | ftotalallamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 35 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 36 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 37 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purapplybilll_org |  | forgid,fbiztime,fbillno,fid |
| 2 | idx_pm_purapplybill_org |  | forgid,fbiztime,fbillno,fid |
| 3 | idx_pm_purapply_billno_org |  | fbillno,forgid |
| 4 | idx_pm_purapplybill_biztime |  | fbiztime |
| 5 | t_pm_purapplybill_pkey |  | fid |
