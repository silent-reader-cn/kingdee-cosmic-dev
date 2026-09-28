# 境内所得纳税调整汇总表单据-tccit_domestic_adjust

## 境内所得纳税调整汇总表单据-主表 t_tccit_domestic_adjust

- **表名称：** 境内所得纳税调整汇总表单据-主表
- **表名：** t_tccit_domestic_adjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | varchar | 50 |  | √ | ' ' | 行次 |
| 3 | fitemtype | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 4 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | famount | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |
| 7 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_domestic_adjust |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_domestic_adjust |  | fid |
