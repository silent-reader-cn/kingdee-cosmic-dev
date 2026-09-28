# 维度填充数据_私有-xkbm_rptdimself

## 维度填充数据_私有-主表 t_xkbm_rptdimself

- **表名称：** 维度填充数据_私有-主表
- **表名：** t_xkbm_rptdimself

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeptorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fgroup | 维度组合 | varchar | 2000 |  | √ | ' ' | 维度组合 |
| 4 | fschemeid | 模板样式方案 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 5 | fdimentryid | 维度分录ID | varchar | 255 |  | √ | ' ' | 维度分录ID |
| 6 | fdata | 数据 | text | 0 |  |  | '' | 数据 |
| 7 | fsheetid | 表页ID | varchar | 255 |  | √ | ' ' | 表页ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_rptdimself |  | fschemeid,fsheetid,fdeptorgid |
| 2 | pk_t_xkbm_rptdimself |  | fid |
