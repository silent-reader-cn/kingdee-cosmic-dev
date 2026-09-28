# 限额扣除的公益性捐赠支出底稿-tccit_dg_b105021_sum

## 限额扣除的公益性捐赠支出底稿-主表 t_tccit_dg_b105021_sum

- **表名称：** 限额扣除的公益性捐赠支出底稿-主表
- **表名：** t_tccit_dg_b105021_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | varchar | 50 |  | √ | ' ' | 行次 |
| 3 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 4 | fitemtype | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 5 | fmypkid | 行id | int8 | 64 |  | √ | 0 | 行id |
| 6 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 8 | fmoney | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 9 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fmyparentid | 父级id | int8 | 64 |  | √ | 0 | 父级id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_dg_b105021_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_dg_b105021_sum |  | fid |
