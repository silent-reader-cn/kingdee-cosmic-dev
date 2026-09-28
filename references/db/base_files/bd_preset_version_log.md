# 预置数据版本更新记录-bd_preset_version_log

## 预置数据版本更新记录-主表 t_bd_preset_log

- **表名称：** 预置数据版本更新记录-主表
- **表名：** t_bd_preset_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frestoretime | frestoretime | timestamp | 0 |  |  | null |  |
| 3 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 4 | frestorerid | frestorerid | int8 | 64 |  | √ | 0 |  |
| 5 | fversionid | 预置数据版本 | int8 | 64 |  | √ | 0 | 预置数据版本信息 bd_predata_version |
| 6 | frestorestatus | frestorestatus | varchar | 50 |  | √ | '0' |  |
| 7 | fupdater | 更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_preset_log |  | fid |
| 2 | idx_bd_preset_log_version |  | fversionid |
