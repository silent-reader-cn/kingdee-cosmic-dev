# 归档记录-fcs_archiverecord

## 归档记录-主表 t_fcs_archiverecord

- **表名称：** 归档记录-主表
- **表名：** t_fcs_archiverecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 归档开始时间 | timestamp | 0 |  |  | null | 归档开始时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | farchivestatus | 归档状态 | varchar | 30 |  | √ | ' ' | 归档状态,枚举: processing :执行中 success :执行成功 fail :执行失败 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftotalcnt | 归档数据量 | int8 | 64 |  | √ | 0 | 归档数据量 |
| 10 | farchivesettingid | 归档配置 | int8 | 64 |  | √ | 0 | [归档配置 fcs_archivesetting](../fcs_files/fcs_archivesetting.md) |
| 11 | ffinishcnt | 已归档数量 | int8 | 64 |  | √ | 0 | 已归档数量 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ffinishtime | 归档结束时间 | timestamp | 0 |  |  | null | 归档结束时间 |
| 14 | fheartbeattime | 最后心跳时间 | timestamp | 0 |  |  | null | 最后心跳时间 |
| 15 | fexceptionmsg_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |
| 16 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fpercent | 归档进度(%) | numeric | 10 | 2 | √ | 0 | 归档进度(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pk_t_fcs_archiverecord_num |  | fbillno |
| 2 | pk_t_fcs_archiverecord |  | fid |
