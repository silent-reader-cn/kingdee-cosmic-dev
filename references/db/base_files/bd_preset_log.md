# 行政区划更新记录列表-bd_preset_log

## 行政区划更新记录列表-主表 t_bd_preset_log

- **表名称：** 行政区划更新记录列表-主表
- **表名：** t_bd_preset_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frestoretime | 恢复时间 | timestamp | 0 |  |  | null | 恢复时间 |
| 3 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 4 | frestorerid | 恢复人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fversionid | 预置数据版本 | int8 | 64 |  | √ | 0 | [预置数据版本信息 bd_predata_version](../base_files/bd_predata_version.md) |
| 6 | frestorestatus | 是否已恢复 | varchar | 50 |  | √ | '0' | 是否已恢复,枚举: 0 : 1 :否 2 :是 |
| 7 | fupdater | 更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_preset_log |  | fid |
| 2 | idx_bd_preset_log_version |  | fversionid |
