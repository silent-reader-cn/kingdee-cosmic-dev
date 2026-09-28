# 预算报表维度group-xkbm_dimensiondetail

## 预算报表维度group-主表 t_xkbm_dimensiondetail

- **表名称：** 预算报表维度group-主表
- **表名：** t_xkbm_dimensiondetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | groupid | int8 | 64 |  | √ | 0 | groupid |
| 3 | fassistantid | 辅助资料 | varchar | 50 |  | √ | ' ' | 辅助资料 |
| 4 | fdimensiontype | 报告维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 5 | fdimensionid | 维度值 | varchar | 50 |  | √ | ' ' | 维度值 |
| 6 | fgroup | 维度组合 | varchar | 2000 |  | √ | ' ' | 维度组合 |
| 7 | fcount | 维度个数 | int4 | 32 |  | √ | 0 | 维度个数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_dimdetail_fgroup |  | fgroup |
| 2 | pk_xkbm_dimensiondetail |  | fid |
