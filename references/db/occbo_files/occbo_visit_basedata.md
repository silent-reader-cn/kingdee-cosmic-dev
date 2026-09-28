# 拜访计划基础资料-occbo_visit_basedata

## 拜访计划基础资料-主表 t_occbo_visit

- **表名称：** 拜访计划基础资料-主表
- **表名：** t_occbo_visit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcompleteinfo | fcompleteinfo | varchar | 255 |  | √ | ' ' |  |
| 3 | fcheckouttime | fcheckouttime | timestamp | 0 |  |  | null |  |
| 4 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fparentchannelid | fparentchannelid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 8 | fprovinceid | fprovinceid | int8 | 64 |  | √ | 0 |  |
| 9 | fsourcebillld | fsourcebillld | int8 | 64 |  | √ | 0 |  |
| 10 | fsourcetype | fsourcetype | bpchar | 36 |  | √ | ' ' |  |
| 11 | fchannelid | 拜访渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 12 | fcheckintime | fcheckintime | timestamp | 0 |  |  | null |  |
| 13 | fvisitstatus | fvisitstatus | bpchar | 1 |  | √ | 'A' |  |
| 14 | fextravisitdate | fextravisitdate | timestamp | 0 |  |  | null |  |
| 15 | fcheckinaddress | fcheckinaddress | varchar | 255 |  | √ | ' ' |  |
| 16 | fbillno | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | fplanvisitdate | 拜访日期 | timestamp | 0 |  |  | null | 拜访日期 |
| 18 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 19 | fpicture6 | fpicture6 | varchar | 500 |  | √ | ' ' |  |
| 20 | fpicture5 | fpicture5 | varchar | 500 |  | √ | ' ' |  |
| 21 | fsourceentryld | fsourceentryld | int8 | 64 |  | √ | 0 |  |
| 22 | fpicture4 | fpicture4 | varchar | 500 |  | √ | ' ' |  |
| 23 | fcomment | fcomment | varchar | 2000 |  | √ | ' ' |  |
| 24 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | 'A' |  |
| 25 | fpicture3 | fpicture3 | varchar | 500 |  | √ | ' ' |  |
| 26 | fsummarize | fsummarize | varchar | 2000 |  | √ | ' ' |  |
| 27 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 28 | fpicture2 | fpicture2 | varchar | 500 |  | √ | ' ' |  |
| 29 | fpicture1 | fpicture1 | varchar | 500 |  | √ | ' ' |  |
| 30 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 31 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 32 | fdepartmentid | fdepartmentid | int8 | 64 |  | √ | 0 |  |
| 33 | fdistance | fdistance | numeric | 23 | 10 | √ | 0 |  |
| 34 | fplanbegintime | fplanbegintime | int4 | 32 |  | √ | 0 |  |
| 35 | fsourcenumber | fsourcenumber | varchar | 80 |  | √ | ' ' |  |
| 36 | fchecktimerange | fchecktimerange | numeric | 23 | 10 | √ | 0 |  |
| 37 | fvisittypeid | fvisittypeid | int8 | 64 |  | √ | 0 |  |
| 38 | flongitude | flongitude | numeric | 23 | 10 | √ | 0 |  |
| 39 | fsourcesubentryld | fsourcesubentryld | int8 | 64 |  | √ | 0 |  |
| 40 | flatitude | flatitude | numeric | 23 | 10 | √ | 0 |  |
| 41 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_visit_billno |  | fbillno |
| 2 | pk_occbo_visit |  | fid |
