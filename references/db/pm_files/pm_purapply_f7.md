# 采购申请单F7-pm_purapply_f7

## 采购申请单F7-主表 t_pm_purapplybill

- **表名称：** 采购申请单F7-主表
- **表名：** t_pm_purapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbidstatus | fbidstatus | varchar | 5 |  | √ | ' ' |  |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 5 | fcancelstatus | fcancelstatus | varchar | 5 |  | √ | ' ' |  |
| 6 | fbiztime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fchangestatus | fchangestatus | varchar | 5 |  | √ | ' ' |  |
| 9 | fistax | fistax | bpchar | 1 |  | √ | '1' |  |
| 10 | fcancelerid | fcancelerid | int8 | 64 |  | √ | 0 |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 13 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 14 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 15 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 16 | fversion | fversion | varchar | 30 |  | √ | '1' |  |
| 17 | fmanualclosereason | fmanualclosereason | varchar | 512 |  | √ | ' ' |  |
| 18 | funitsrctype | funitsrctype | varchar | 30 |  | √ | ' ' |  |
| 19 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 20 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcomment | fcomment | varchar | 512 |  |  | null |  |
| 23 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 24 | fbizuserid | fbizuserid | int8 | 64 |  | √ | 0 |  |
| 25 | ftrdbillno | ftrdbillno | varchar | 50 |  | √ | ' ' |  |
| 26 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 27 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 28 | fbillcretype | fbillcretype | varchar | 5 |  | √ | '0' |  |
| 29 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 30 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 31 | fsubversion | fsubversion | varchar | 30 |  | √ | '1' |  |
| 32 | fcanceldate | fcanceldate | timestamp | 0 |  |  | null |  |
| 33 | fmanualclose | fmanualclose | bpchar | 1 |  | √ | '0' |  |
| 34 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 35 | finquirystatus | finquirystatus | varchar | 5 |  | √ | ' ' |  |
| 36 | ftaxinprice | ftaxinprice | bpchar | 1 |  | √ | '0' |  |
| 37 | ftotalallamount | ftotalallamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 38 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 39 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 40 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

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
