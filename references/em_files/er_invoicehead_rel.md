# 公司与发票抬头映射-er_invoicehead_rel

## 公司与发票抬头映射-主表 t_er_invoicehead_rel

- **表名称：** 公司与发票抬头映射-主表
- **表名：** t_er_invoicehead_rel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvocieheadid | 发票抬头ID | varchar | 100 |  | √ | ' ' | 发票抬头ID |
| 3 | fcorpcompany | 公司名称 | varchar | 100 |  | √ | ' ' | 公司名称 |
| 4 | faccountid | 主账户ID | varchar | 30 |  | √ | ' ' | 主账户ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_invoicehead_rel_pkey |  | fid |
| 2 | idx_er_invhrel_ccp_acc |  | faccountid,fcorpcompany |
