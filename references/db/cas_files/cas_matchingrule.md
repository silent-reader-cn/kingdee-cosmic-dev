# 自动匹配规则(旧)-cas_matchingrule

## 单据体-子表 t_cas_matchingruleentry

- **表名称：** 单据体-子表
- **表名：** t_cas_matchingruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpaytypeid | 付款类型 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 3 | fisinternal | 是否内部客商 | bpchar | 1 |  | √ | '0' | 是否内部客商 |
| 4 | ffundflowitem | 资金用途 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 5 | fcustomer | 对方单位 | varchar | 100 |  | √ | ' ' | 对方单位 |
| 6 | frectype | 收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 7 | fabstract | 摘要 | varchar | 200 |  |  | null | 摘要 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fpayaccount | 对方银行账户 | varchar | 100 |  | √ | ' ' | 对方银行账户 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_mre_fid |  | fid |
| 2 | t_cas_matchingruleentry_pkey |  | fentryid |

---

## 自动匹配规则(旧)-主表 t_cas_matchingrule

- **表名称：** 自动匹配规则(旧)-主表
- **表名：** t_cas_matchingrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | frulecoding | 规则编码 | varchar | 100 |  | √ | ' ' | 规则编码 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbusinesstype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: REC :收款 PAY :付款 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fschemename | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fisupdate | 是否升级 | bpchar | 1 |  | √ | '0' | 是否升级 |
| 13 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | frecaccount | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 15 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 16 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fexpirationdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_mr_acct |  | frecaccount |
| 2 | t_cas_matchingrule_pkey |  | fid |
