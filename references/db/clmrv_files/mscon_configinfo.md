# 参数配置信息-mscon_configinfo

## 参数配置信息-主表 t_mscon_configinfo

- **表名称：** 参数配置信息-主表
- **表名：** t_mscon_configinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fappparam_tag | 基础参数大文本_详情 | text | 0 |  |  | null | 基础参数大文本_详情 |
| 4 | fappparam | 基础参数大文本 | varchar | 255 |  | √ | ' ' | 基础参数大文本 |
| 5 | fcusparam | 自定义参数大文本 | varchar | 255 |  | √ | ' ' | 自定义参数大文本 |
| 6 | fcusparam_tag | 自定义参数大文本_详情 | text | 0 |  |  | null | 自定义参数大文本_详情 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mscon_configinfo |  | fid |
| 2 | idx_mscon_configinfo_m0 |  | fmodifierid |
