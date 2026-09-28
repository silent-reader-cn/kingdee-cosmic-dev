# 模拟报价取价来源-sm_simquotpricesrc

## 模拟报价取价来源-主表 t_sm_simquotpricesrc

- **表名称：** 模拟报价取价来源-主表
- **表名：** t_sm_simquotpricesrc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdefault | 是否默认 | bpchar | 1 |  | √ | ' ' | 是否默认 |
| 3 | ftype | 类型 | varchar | 20 |  | √ | ' ' | 类型,枚举: A :材料取价 B :委外取价 C :自制件取价 M :手工维护 |
| 4 | fissys | 是否系统预置 | bpchar | 1 |  | √ | ' ' | 是否系统预置 |
| 5 | fsort | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 6 | fenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用 |
| 7 | fpricesrctype | 取价来源类型 | int8 | 64 |  | √ | 0 | [模拟报价取价来源类型 sm_simquotpricesrctype](../sm_files/sm_simquotpricesrctype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_simquotpricesrc |  | fpricesrctype |
| 2 | pk_sm_simquotpricesrc |  | fid |
