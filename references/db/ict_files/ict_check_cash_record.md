# 现金流量记录-ict_check_cash_record

## 单据体-子表 t_ict_cf_cross_entry

- **表名称：** 单据体-子表
- **表名：** t_ict_cf_cross_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcashflowitemid | 现金流量项目 | int8 | 64 |  | √ | 0 | 现金流量项目 gl_cashflowitem |
| 3 | fvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 4 | fdc | 现金流量方向 | varchar | 2 |  | √ | '1' | 现金流量方向,枚举: b :流入流出 i :流入 o :流出 |
| 5 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fopporgid | 对方组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | frelrecordid | 交易记录id | int8 | 64 |  | √ | 0 | 交易记录id |
| 10 | fvoucherno | 凭证号 | varchar | 255 |  | √ | ' ' | 凭证号 |
| 11 | famt | 金额 | numeric | 24 | 6 | √ | 0 | 金额 |
| 12 | fvoucherentryid | 凭证分录ID | int8 | 64 |  | √ | 0 | 凭证分录ID |
| 13 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 14 | fdesc | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 15 | famtbal | 未勾稽金额 | numeric | 24 | 6 | √ | 0 | 未勾稽金额 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | famtverify | 勾稽金额 | numeric | 24 | 6 | √ | 0 | 勾稽金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ict_cf_cross_entry_fid |  | fid |
| 2 | pk_t_ict_cf_cross_entry |  | fentryid |

---

## 现金流量记录-主表 t_ict_cf_cross_record

- **表名称：** 现金流量记录-主表
- **表名：** t_ict_cf_cross_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fperiodid | 对账期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | foporgid | 对方组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fverifyschemeid | 对账方案 | int8 | 64 |  | √ | 0 | 内部交易对账方案 ict_verifyscheme |
| 7 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 8 | fcurorgid | 本方组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fchecktype | 勾稽方式 | bpchar | 1 |  | √ | '1' | 勾稽方式,枚举: 1 :自动勾稽 2 :手工勾稽 |
| 10 | fcheckstatus | 勾稽状态 | bpchar | 1 |  | √ | '2' | 勾稽状态,枚举: 2 :完全勾稽 3 :容差勾稽 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ict_cf_cross_record_org |  | fcurorgid,foporgid,fperiodid,fverifyschemeid |
| 2 | pk_t_ict_cf_cross_record |  | fid |
