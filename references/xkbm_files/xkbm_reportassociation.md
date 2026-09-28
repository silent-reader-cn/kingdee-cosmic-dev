# 汇总表报表关系-xkbm_reportassociation

## 汇总表报表关系-主表 t_xkbm_reportassociation

- **表名称：** 汇总表报表关系-主表
- **表名：** t_xkbm_reportassociation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcid | 报表ID | varchar | 50 |  | √ | ' ' | 报表ID |
| 3 | fsrcsheetid | 报表SheetID | varchar | 50 |  | √ | ' ' | 报表SheetID |
| 4 | fvalid | 有效性 | bpchar | 1 |  | √ | '0' | 有效性 |
| 5 | fdstid | 汇总表ID | varchar | 50 |  | √ | ' ' | 汇总表ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_reportassociation |  | fdstid,fvalid |
| 2 | pk_t_xkbm_reportassociation |  | fid |
