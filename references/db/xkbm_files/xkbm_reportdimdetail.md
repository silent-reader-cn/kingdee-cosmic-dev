# 预算维度值-xkbm_reportdimdetail

## 预算维度值-主表 t_xkbm_reportdimdetail

- **表名称：** 预算维度值-主表
- **表名：** t_xkbm_reportdimdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdimensiontype | 报告维度 | int8 | 64 |  | √ | 0 | 维度 xkrpt_dimension |
| 3 | fdimensionid | 维度值 | varchar | 50 |  | √ | ' ' | 维度值 |
| 4 | forder | 顺序 | int4 | 32 |  | √ | 0 | 顺序 |
| 5 | fisbudgetorg | 是否预算组织 | bpchar | 1 |  | √ | '0' | 是否预算组织 |
| 6 | fisadjust | 是否调整 | bpchar | 1 |  | √ | '0' | 是否调整 |
| 7 | frptschemeid | 模板样式方案 | int8 | 64 |  | √ | 0 | 预算模板样式方案 xkbm_rptscheme |
| 8 | fsheetid | sheet页id | varchar | 50 |  | √ | ' ' | sheet页id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_rptdim_sheetid |  | fsheetid |
| 2 | pk_xkbm_reportdimdetail |  | fid |
