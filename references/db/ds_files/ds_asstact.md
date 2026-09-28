# 自定义核算项目-ds_asstact

## 自定义核算项目-主表 t_ds_asstact

- **表名称：** 自定义核算项目-主表
- **表名：** t_ds_asstact

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 20 |  | √ | ' ' | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fssid | 来源系统 | int8 | 64 |  | √ | 0 | [来源系统 ds_srcsys](../ds_files/ds_srcsys.md) |
| 4 | fasstacttypeid | 核算项目类型ID | varchar | 100 |  | √ | ' ' | 核算项目类型ID |
| 5 | fgroupnumber | 核算项目类型 | varchar | 100 |  | √ | ' ' | 核算项目类型 |
| 6 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 7 | fsoid | 来源对象ID | varchar | 100 |  | √ | ' ' | 来源对象ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ds_asstact_pkey |  | fid |
| 2 | idx_ds_asstact_key |  | fssid,fsoid |
