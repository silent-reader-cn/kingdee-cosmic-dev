# 变动类型-ds_changetype

## 变动类型-主表 t_ds_changetype

- **表名称：** 变动类型-主表
- **表名：** t_ds_changetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 20 |  | √ | ' ' | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fssid | 来源系统 | int8 | 64 |  | √ | 0 | [来源系统 ds_srcsys](../ds_files/ds_srcsys.md) |
| 4 | fdirection | 借贷方向 | varchar | 100 |  | √ | ' ' | 借贷方向 |
| 5 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 6 | fsoid | 来源对象ID | varchar | 100 |  | √ | ' ' | 来源对象ID |
| 7 | fcurrencytype | 币种类型 | varchar | 30 |  | √ | ' ' | 币种类型,枚举: for :原币 local :本位币 rpt :报告币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ds_changetype_key |  | fsoid,fssid |
| 2 | t_ds_changetype_pkey |  | fid |
