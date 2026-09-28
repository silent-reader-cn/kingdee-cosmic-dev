# 价值报告-ipop_prod_report

## 价值报告-主表 t_ipop_prod_report

- **表名称：** 价值报告-主表
- **表名：** t_ipop_prod_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frptsrc | 报告来源 | varchar | 50 |  | √ | ' ' | 报告来源,枚举: EGP :企业成长平台 other :其他 |
| 3 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :启用 0 :禁用 |
| 4 | frptcreatetime | 报告时间 | timestamp | 0 |  |  | null | 报告时间 |
| 5 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | freportid | 报告ID | int8 | 64 |  | √ | 0 | 报告ID |
| 8 | frptname | 报告名称 | varchar | 255 |  | √ | ' ' | 报告名称 |
| 9 | frpturl | 报告链接 | varchar | 2000 |  | √ | ' ' | 报告链接 |
| 10 | frpttype | 报告类型 | varchar | 50 |  | √ | ' ' | 报告类型 |
| 11 | fcustomparam | 自定义参数 | varchar | 2000 |  | √ | ' ' | 自定义参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_prod_report |  | fstatus |
| 2 | pk_t_ipop_prod_report |  | fid |
