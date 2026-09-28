# 同步配置表-rim_his_sync_config

## 同步配置表-主表 t_rim_his_sync_config

- **表名称：** 同步配置表-主表
- **表名：** t_rim_his_sync_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 同步结果 | varchar | 4 |  | √ | ' ' | 同步结果,枚举: 0 :不同步 1 :同步 |
| 3 | fclientid | clientId | varchar | 30 |  | √ | ' ' | clientId |
| 4 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | ftax_no | 税号 | varchar | 30 |  | √ | ' ' | 税号 |
| 7 | fcompany_name | 企业名称 | varchar | 150 |  | √ | ' ' | 企业名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_his_sync_config |  | fid |
| 2 | idx_rim_his_sync_config |  | fclientid |
