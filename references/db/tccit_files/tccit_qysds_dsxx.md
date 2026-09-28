# 董事情况-tccit_qysds_dsxx

## 董事情况-主表 t_tccit_qysds_dsxx

- **表名称：** 董事情况-主表
- **表名：** t_tccit_qysds_dsxx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frzrqz | 任职日期止 | timestamp | 0 |  |  | null | 任职日期止 |
| 3 | fsfzjhm | 身份证件号码 | varchar | 100 |  | √ | ' ' | 身份证件号码 |
| 4 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 |
| 5 | fzw | 职务 | varchar | 600 |  | √ | ' ' | 职务 |
| 6 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 7 | frzrqq | 任职日期起 | timestamp | 0 |  |  | null | 任职日期起 |
| 8 | fzgjnczd | 中国境内常住地 | varchar | 600 |  | √ | ' ' | 中国境内常住地 |
| 9 | fsfzjlx | 身份证件类型 | varchar | 100 |  | √ | ' ' | 身份证件类型 |
| 10 | fzgmjgrxm | 中国居民个人姓名 | varchar | 600 |  | √ | ' ' | 中国居民个人姓名 |
| 11 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_qysds_dsxx |  | fsbbid |
| 2 | t_tccit_qysds_dsxx_pkey |  | fid |
| 3 | idx_tccit_qysds_dsxx_1 |  | fewblxh,fsbbid |
