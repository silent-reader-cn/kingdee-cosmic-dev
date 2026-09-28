# 职工教育经费（限额扣除）底稿-tccit_b105014_3_summary

## 职工教育经费（限额扣除）底稿-主表 t_tccit_b105014_3_sum

- **表名称：** 职工教育经费（限额扣除）底稿-主表
- **表名：** t_tccit_b105014_3_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fitemtype | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: zzje :账载金额 kcjsjsbt :职工教育经费扣除基数计算: sjfsje :实际发生额 yqndjz :以前年度结转扣除额 kcjs :职工教育经费扣除基数（第3行+第4行） kcxejsbt :扣除限额计算: gzxj :本年实际发生的工资薪金 kcbl :扣除比例 kcxe :按工资薪金计算的扣除限额 nstzejsbt :纳税调整额计算: ssje :税收金额 tze :纳税调整金额（第1行-第11行） jzyhndkce :累计结转以后年度扣除额（第5行-第11行） |
| 5 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 7 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 9 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_b105014_3_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_b105014_3_sum |  | fid |
