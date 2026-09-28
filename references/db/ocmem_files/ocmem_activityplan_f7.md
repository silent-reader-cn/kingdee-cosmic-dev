# 费用活动方案-ocmem_activityplan_f7

## 费用活动方案-主表 t_ocmem_activityplan

- **表名称：** 费用活动方案-主表
- **表名：** t_ocmem_activityplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsumsaleamount | 预计销售总额 | numeric | 23 | 10 | √ | 0 | 预计销售总额 |
| 3 | factivityuserid | 活动负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbuyuserqty | fbuyuserqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | factivitytypeid | 活动类型 | int8 | 64 |  | √ | 0 | [活动类型 ocdbd_activitytype](../ocmem_files/ocdbd_activitytype.md) |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0 |  |
| 8 | fstartactivitydate | 预计活动日期.开始 | timestamp | 0 |  |  | null | 预计活动日期.开始 |
| 9 | fplandate | 策划日期 | timestamp | 0 |  |  | null | 策划日期 |
| 10 | fuserqty | fuserqty | numeric | 23 | 10 | √ | 0 |  |
| 11 | fimplementation_tag | fimplementation_tag | text | 0 |  |  | null |  |
| 12 | flocalapproveamount | flocalapproveamount | numeric | 23 | 10 | √ | 0 |  |
| 13 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 14 | flocalaccamount | flocalaccamount | numeric | 23 | 10 | √ | 0 |  |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | flocaltotalapplyamount | flocaltotalapplyamount | numeric | 23 | 10 | √ | 0 |  |
| 17 | fname | 方案名称 | varchar | 80 |  | √ | ' ' | 方案名称 |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fplanorgid | 策划部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | factivitystatus | 活动状态 | bpchar | 1 |  | √ | ' ' | 活动状态,枚举: A :计划 B :已完成 C :进行中 D :已取消 E :已结案 |
| 21 | fsettorgid | fsettorgid | int8 | 64 |  | √ | 0 |  |
| 22 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 23 | ftotalapplyamount | ftotalapplyamount | numeric | 23 | 10 | √ | 0 |  |
| 24 | fsumfeeamount | 预计费用总额 | numeric | 23 | 10 | √ | 0 | 预计费用总额 |
| 25 | fendactivitydate | 预计活动日期.结束 | timestamp | 0 |  |  | null | 预计活动日期.结束 |
| 26 | fapproveamount | fapproveamount | numeric | 23 | 10 | √ | 0 |  |
| 27 | factivityresultid | factivityresultid | int8 | 64 |  | √ | 0 |  |
| 28 | fplantarget | 方案目标 | varchar | 510 |  | √ | ' ' | 方案目标 |
| 29 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 31 | flocalsumfeeamount | flocalsumfeeamount | numeric | 23 | 10 | √ | 0 |  |
| 32 | fplandescription | 方案简述 | varchar | 510 |  | √ | ' ' | 方案简述 |
| 33 | ffeesalerate | 预计费销比 | numeric | 23 | 10 | √ | 0 | 预计费销比 |
| 34 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 35 | fbuyamount | fbuyamount | numeric | 23 | 10 | √ | 0 |  |
| 36 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fimplementation | fimplementation | text | 0 |  |  | null |  |
| 38 | fresultstatus | fresultstatus | bpchar | 1 |  | √ | 'A' |  |
| 39 | flocalsumsaleamount | flocalsumsaleamount | numeric | 23 | 10 | √ | 0 |  |
| 40 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 41 | fpicture6 | fpicture6 | varchar | 255 |  | √ | ' ' |  |
| 42 | fpicture5 | fpicture5 | varchar | 255 |  | √ | ' ' |  |
| 43 | fpicture4 | fpicture4 | varchar | 255 |  | √ | ' ' |  |
| 44 | fpicture3 | fpicture3 | varchar | 255 |  | √ | ' ' |  |
| 45 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 46 | fpicture2 | fpicture2 | varchar | 255 |  | √ | ' ' |  |
| 47 | fpicture1 | fpicture1 | varchar | 255 |  | √ | ' ' |  |
| 48 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 49 | fsaleorgid | fsaleorgid | int8 | 64 |  | √ | 0 |  |
| 50 | fbasecurrencyid | fbasecurrencyid | int8 | 64 |  | √ | 0 |  |
| 51 | flocalbuyamount | flocalbuyamount | numeric | 23 | 10 | √ | 0 |  |
| 52 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 53 | frelactivityid | frelactivityid | int8 | 64 |  | √ | 0 |  |
| 54 | faccamount | faccamount | numeric | 23 | 10 | √ | 0 |  |
| 55 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_activityplan |  | fid |
| 2 | idx_ocmem_activityplan_billno |  | fbillno |
