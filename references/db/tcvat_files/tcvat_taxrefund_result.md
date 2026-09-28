# 留抵退税结果单据-tcvat_taxrefund_result

## 留抵退税结果单据-主表 t_tcvat_taxrefund_result

- **表名称：** 留抵退税结果单据-主表
- **表名：** t_tcvat_taxrefund_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 事项 | varchar | 1000 |  | √ | ' ' | 事项 |
| 3 | fdetail | 详情 | varchar | 1000 |  | √ | ' ' | 详情 |
| 4 | fsbbid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_taxrefund_result |  | fid |
| 2 | idx_t_tcvat_taxrefund_result |  | fsbbid |
