# 公有云数据迁移记录（弃用）-sim_sync_aws_record

## 公有云数据迁移记录（弃用）-主表 t_sim_sync_aws_record

- **表名称：** 公有云数据迁移记录（弃用）-主表
- **表名：** t_sim_sync_aws_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsynctotal | 累计同步（张） | int4 | 32 |  | √ | 0 | 累计同步（张） |
| 2 | fsyncupdatetotal | 新增同步（张） | int4 | 32 |  | √ | 0 | 新增同步（张） |
| 3 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 4 | fname | 企业名称 | varchar | 50 |  | √ | ' ' | 企业名称 |
| 5 | fapplydate | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 6 | fserialno | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 7 | fawsstarttime | aws同步起始日期 | timestamp | 0 |  |  | null | aws同步起始日期 |
| 8 | forg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fstatus | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: 0 :失败 1 :成功 |
| 10 | fisnewfinished | 是否最新完成同步批次 | varchar | 50 |  | √ | ' ' | 是否最新完成同步批次,枚举: 0 :否 1 :是 |
| 11 | flastapplyenddate | 上次同步截止日期 | timestamp | 0 |  |  | null | 上次同步截止日期 |
| 12 | ftaxno | 税号 | varchar | 50 |  | √ | ' ' | 税号 |
| 13 | fawsendtime | aws同步结束日期 | timestamp | 0 |  |  | null | aws同步结束日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_sync_aws_record |  | fid |
| 2 | idx_sim_sync_aws_record |  | ftaxno |
