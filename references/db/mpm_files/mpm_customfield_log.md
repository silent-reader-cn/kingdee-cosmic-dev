# 自定义字段操作日志-mpm_customfield_log

## 自定义字段操作日志-主表 t_mpm_custfieldlog

- **表名称：** 自定义字段操作日志-主表
- **表名：** t_mpm_custfieldlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizobjectid | 业务对象 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fcusfield | 自定义字段 | varchar | 255 |  | √ | ' ' | 自定义字段 |
| 4 | fusenum | 使用次数 | int8 | 64 |  | √ | 0 | 使用次数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_custfieldlog |  | fid |
| 2 | idx_mpm_cusfieldlog_ocus |  | fbizobjectid,fcusfield |
