# 费用活动方案-ocmem_activityplan_f7

## 费用活动方案-主表 t_ocmem_activityplan

- **表名称：** 费用活动方案-主表
- **表名：** t_ocmem_activityplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsumsaleamount | 预计销售总额 | numeric | 23 | 10 | √ | 0 | 预计销售总额 |
| 3 | factivityuserid | factivityuserid | int8 | 64 |  | √ | 0 |  |
| 4 | fbuyuserqty | fbuyuserqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | factivitytypeid | 活动类型 | int8 | 64 |  | √ | 0 | 活动类型 ocdbd_activitytype |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fplandescription | 方案简述 | varchar | 510 |  | √ | ' ' | 方案简述 |
| 8 | fstartactivitydate | 预计活动日期.开始 | timestamp | 0 |  |  | null | 预计活动日期.开始 |
| 9 | ffeesalerate | 预计费销比 | numeric | 23 | 10 | √ | 0 | 预计费销比 |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fbuyamount | fbuyamount | numeric | 23 | 10 | √ | 0 |  |
| 12 | fprovinceid | fprovinceid | int8 | 64 |  | √ | 0 |  |
| 13 | fplandate | 策划日期 | timestamp | 0 |  |  | null | 策划日期 |
| 14 | fuserqty | fuserqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | fimplementation_tag | fimplementation_tag | text | 0 |  |  | null |  |
| 16 | fimplementation | fimplementation | text | 0 |  |  | null |  |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fname | 方案名称 | varchar | 80 |  | √ | ' ' | 方案名称 |
| 19 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 20 | fpicture6 | fpicture6 | varchar | 255 |  | √ | ' ' |  |
| 21 | fpicture5 | fpicture5 | varchar | 255 |  | √ | ' ' |  |
| 22 | fpicture4 | fpicture4 | varchar | 255 |  | √ | ' ' |  |
| 23 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fpicture3 | fpicture3 | varchar | 255 |  | √ | ' ' |  |
| 25 | fplanorgid | 策划部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 27 | fpicture2 | fpicture2 | varchar | 255 |  | √ | ' ' |  |
| 28 | factivitystatus | factivitystatus | bpchar | 1 |  | √ | ' ' |  |
| 29 | fpicture1 | fpicture1 | varchar | 255 |  | √ | ' ' |  |
| 30 | fsettorgid | fsettorgid | int8 | 64 |  | √ | 0 |  |
| 31 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 32 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 33 | fsaleorgid | fsaleorgid | int8 | 64 |  | √ | 0 |  |
| 34 | ftotalapplyamount | ftotalapplyamount | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsumfeeamount | 预计费用总额 | numeric | 23 | 10 | √ | 0 | 预计费用总额 |
| 36 | fendactivitydate | 预计活动日期.结束 | timestamp | 0 |  |  | null | 预计活动日期.结束 |
| 37 | fapproveamount | fapproveamount | numeric | 23 | 10 | √ | 0 |  |
| 38 | faccamount | faccamount | numeric | 23 | 10 | √ | 0 |  |
| 39 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 40 | fplantarget | 方案目标 | varchar | 510 |  | √ | ' ' | 方案目标 |
| 41 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 42 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_activityplan |  | fid |
| 2 | idx_ocmem_activityplan_billno |  | fbillno |
