# 投资资产初始成本调整底稿-tccit_tzzccscbtz_summary

## 投资资产初始成本调整底稿-主表 t_tccit_tzzccscbtz_sum

- **表名称：** 投资资产初始成本调整底稿-主表
- **表名：** t_tccit_tzzccscbtz_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: cqgqtz :按权益法核算长期股权投资对初始投资成本调整确认收益 jrzccstz :交易性金融资产初始投资调整 |
| 4 | fskcyje | 税会差异金额 | numeric | 23 | 10 | √ | 0.0000000000 | 税会差异金额 |
| 5 | fskssqz | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 8 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_tzzccscbtz_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_tzzccscbtz_sum |  | fid |
