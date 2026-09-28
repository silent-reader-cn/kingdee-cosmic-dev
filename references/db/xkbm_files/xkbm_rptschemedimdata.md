# 维度填充数据-xkbm_rptschemedimdata

## 维度填充数据-主表 t_xkbm_rptschemedimdata

- **表名称：** 维度填充数据-主表
- **表名：** t_xkbm_rptschemedimdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeptorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fschemeid | 模板样式方案 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 4 | fdata | 数据 | text | 0 |  |  | null | 数据 |
| 5 | fsheetid | 表页ID | varchar | 50 |  | √ | ' ' | 表页ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_rptschdimdata_fschid |  | fschemeid,fsheetid,fdeptorgid |
| 2 | pk_xkbm_rptschemedimdata |  | fid |
