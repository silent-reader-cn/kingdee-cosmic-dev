# 通用单位换算-bd_measureunitconv

## 通用单位换算-主表 t_bd_measureunitconv

- **表名称：** 通用单位换算-主表
- **表名：** t_bd_measureunitconv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fdenominator | 源单位换算系数 | int8 | 64 |  |  | null | 源单位换算系数 |
| 3 | fsrcmuid | 源单位编码 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fdesmuid | 目标单位编码 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fenable | fenable | bpchar | 1 |  |  | null |  |
| 6 | fnumerator | 目标单位换算系数 | int8 | 64 |  |  | null | 目标单位换算系数 |
| 7 | fconverttype | 换算类型 | varchar | 10 |  |  | null | 换算类型,枚举: 1 :固定 2 :浮动 |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_measureunitconv_pkey |  | fid |
| 2 | idx_t_bd_measureunitconv_srcde |  | fsrcmuid,fdesmuid |
