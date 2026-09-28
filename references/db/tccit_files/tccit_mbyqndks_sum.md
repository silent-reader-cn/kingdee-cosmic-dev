# 境内弥补亏损-tccit_mbyqndks_sum

## 境内弥补亏损-主表 t_tccit_mbyqndks_sum

- **表名称：** 境内弥补亏损-主表
- **表名：** t_tccit_mbyqndks_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 3 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :减免后境内所得 2 :本年使用境内所得弥补亏损额 3 :弥补以前年度亏损后的应纳税所得额 |
| 5 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 7 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 8 | famount | 金额 | varchar | 50 |  | √ | ' ' | 金额 |
| 9 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_mbyqndks_sum |  | fid |
| 2 | idx_t_tccit_mbyqndks_sum |  | forgid,fskssqq,fskssqz,fitemtype |
