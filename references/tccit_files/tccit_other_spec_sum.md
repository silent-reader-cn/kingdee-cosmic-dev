# 其他特别纳税调整底稿-tccit_other_spec_sum

## 其他特别纳税调整底稿-主表 t_tccit_other_spec_sum

- **表名称：** 其他特别纳税调整底稿-主表
- **表名：** t_tccit_other_spec_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | int8 | 64 |  | √ | 0 | 行次 |
| 3 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 4 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 5 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 6 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 7 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 8 | fitemname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 9 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_other_spec_sum |  | fid |
| 2 | idx_tccit_other_spec_sum |  | forgid,fskssqq,fskssqz |
