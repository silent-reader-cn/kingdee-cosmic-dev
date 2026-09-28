# 特殊事项调整汇总底稿-tccit_hzdg_tssxtz_sum

## 特殊事项调整汇总底稿-主表 t_tccit_hzdg_tssxtz_sum

- **表名称：** 特殊事项调整汇总底稿-主表
- **表名：** t_tccit_hzdg_tssxtz_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 展示序号 | varchar | 50 |  | √ | ' ' | 展示序号 |
| 3 | fitemtype | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 4 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 5 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 6 | famount | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |
| 7 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_hzdg_tssxtz_sum |  | fid |
| 2 | idx_tccit_hzdg_tssxtz_sum |  | forgid,fskssqq,fskssqz |
