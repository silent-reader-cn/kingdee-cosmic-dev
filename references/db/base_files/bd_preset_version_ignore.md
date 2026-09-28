# 预置数据版本信息忽略-bd_preset_version_ignore

## 预置数据版本信息忽略-主表 t_bd_presetverignore

- **表名称：** 预置数据版本信息忽略-主表
- **表名：** t_bd_presetverignore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 3 | fpresetverid | 预置数据版本信息 | int8 | 64 |  | √ | 0 | [预置数据版本信息 bd_predata_version](../base_files/bd_predata_version.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_presetverignore |  | fuserid |
| 2 | pk_bd_presetverignore |  | fid |
