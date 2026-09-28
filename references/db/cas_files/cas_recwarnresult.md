# 收款重复结果-cas_recwarnresult

## 收款重复结果-主表 t_cas_recwarnresult

- **表名称：** 收款重复结果-主表
- **表名：** t_cas_recwarnresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :待确认 1 :已确认 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fbatchno | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 5 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_recwarnresult_pkey |  | fid |
| 2 | index_recwarn_fcreater |  | fcreaterid |
| 3 | index_recwarn_fbatchno |  | fbatchno |

---

## 单据体-子表 t_cas_recwarnresultentry

- **表名称：** 单据体-子表
- **表名：** t_cas_recwarnresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhassave | 是否当前提交单 | bpchar | 1 |  | √ | '0' | 是否当前提交单 |
| 3 | fbillstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 D :已收款 |
| 4 | fcreatetime | 创建时间 | varchar | 50 |  | √ | ' ' | 创建时间 |
| 5 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 记录 | varchar | 50 |  | √ | ' ' | 记录 |
| 8 | fpayer | 付款人 | varchar | 200 |  | √ | ' ' | 付款人 |
| 9 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 10 | fpayernum | 付款账号 | varchar | 100 |  | √ | ' ' | 付款账号 |
| 11 | frecamount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 12 | fbizdate | 业务日期 | varchar | 30 |  | √ | ' ' | 业务日期 |
| 13 | fdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fbillno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 16 | frecnum | 收款账号 | varchar | 100 |  |  | ' ' | 收款账号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_recwarnresultentry_pkey |  | fentryid |
| 2 | index_recwarn_fbillno |  | fbillno |
