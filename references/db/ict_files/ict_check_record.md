# 科目记录-ict_check_record

## 科目记录-主表 t_ict_cross_record

- **表名称：** 科目记录-主表
- **表名：** t_ict_cross_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fopbookid | 对方账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 4 | fperiodid | 对账期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | foporgid | 对方组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fverifyschemeid | 对账方案 | int8 | 64 |  | √ | 0 | [内部交易对账方案 ict_verifyscheme](../ict_files/ict_verifyscheme.md) |
| 8 | fcurbookid | 本方账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 9 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 10 | fcurorgid | 本方组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fchecktype | 勾稽方式 | bpchar | 1 |  | √ | '1' | 勾稽方式,枚举: 1 :自动勾稽 2 :手工勾稽 3 :无差异勾稽 |
| 12 | fcheckstatus | 勾稽状态 | bpchar | 1 |  | √ | '2' | 勾稽状态,枚举: 2 :完全勾稽 3 :容差勾稽 4 :部分勾稽 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ict_cross_record |  | fid |
| 2 | idx_ict_cross_record_org |  | fcurorgid,foporgid,fperiodid,fverifyschemeid |

---

## 单据体-子表 t_ict_cross_entry

- **表名称：** 单据体-子表
- **表名：** t_ict_cross_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 3 | fdc | 方向 | varchar | 2 |  | √ | '1' | 方向,枚举: 1 :借 -1 :贷 |
| 4 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fopporgid | 对方组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | famtloc | 本位币金额 | numeric | 24 | 6 | √ | 0 | 本位币金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | frelrecordid | 交易记录id | int8 | 64 |  | √ | 0 | 交易记录id |
| 10 | fvoucherno | 凭证号 | varchar | 255 |  | √ | ' ' | 凭证号 |
| 11 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 12 | famt | 原币金额 | numeric | 24 | 6 | √ | 0 | 原币金额 |
| 13 | floccurid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | fvoucherentryid | 凭证分录ID | int8 | 64 |  | √ | 0 | 凭证分录ID |
| 15 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 16 | famtverifyloc | 勾稽金额本位币 | numeric | 24 | 6 | √ | 0 | 勾稽金额本位币 |
| 17 | foppbookid | 对方账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 18 | fdesc | 摘要 | varchar | 1020 |  | √ | ' ' | 摘要 |
| 19 | famtbal | 未勾稽金额原币 | numeric | 24 | 6 | √ | 0 | 未勾稽金额原币 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | famtballoc | 未勾稽金额本位币 | numeric | 24 | 6 | √ | 0 | 未勾稽金额本位币 |
| 23 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 24 | famtverify | 勾稽金额原币 | numeric | 24 | 6 | √ | 0 | 勾稽金额原币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ict_cross_entry_fid |  | fid |
| 2 | idx_ict_cross_entry_v |  | fvoucherid |
| 3 | pk_t_ict_cross_entry |  | fentryid |
