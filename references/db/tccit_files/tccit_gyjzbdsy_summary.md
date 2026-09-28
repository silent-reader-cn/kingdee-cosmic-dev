# 公允价值变动损益调整底稿-tccit_gyjzbdsy_summary

## 公允价值变动损益调整底稿-主表 t_tccit_gyjzbdsy_summary

- **表名称：** 公允价值变动损益调整底稿-主表
- **表名：** t_tccit_gyjzbdsy_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 4 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 6 | fzzje | 账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 账载金额 |
| 7 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 8 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 9 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_gyjzbdsy_summary |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_gyjzbdsy_summary |  | fid |
