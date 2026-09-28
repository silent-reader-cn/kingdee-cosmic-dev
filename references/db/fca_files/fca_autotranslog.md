# 自动划拨执行日志-fca_autotranslog

## 单据体-子表 t_fca_autotranslog_entry

- **表名称：** 单据体-子表
- **表名：** t_fca_autotranslog_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpbankacctid | 母账户银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 3 | fstatus | 执行结果 | varchar | 30 |  | √ | ' ' | 执行结果,枚举: 2 :成功 3 :失败 |
| 4 | facctgroupid | 母子账户组 | int8 | 64 |  | √ | 0 | 母子账户组 fca_acctgroup |
| 5 | fdetail | 自动划拨执行详情 | varchar | 255 |  | √ | ' ' | 自动划拨执行详情 |
| 6 | ftranstrategyid | 账户划拨策略 | int8 | 64 |  | √ | 0 | 账户划拨策略 fca_transtrategy |
| 7 | fsbankacctid | 子账户银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fbillno | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 11 | finneracctid | 对应内部账号 | int8 | 64 |  | √ | 0 | 内部账户管理 ifm_inneracct |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_autotranslog_entry_pkey |  | fentryid |

---

## 自动划拨执行日志-主表 t_fca_autotranslog

- **表名称：** 自动划拨执行日志-主表
- **表名：** t_fca_autotranslog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecdetl | 执行结果 | varchar | 80 |  | √ | ' ' | 执行结果 |
| 3 | fexecstatus | 执行状态 | varchar | 80 |  | √ | ' ' | 执行状态,枚举: 1 :进行中 2 :成功 3 :失败 |
| 4 | ftype | 类别 | varchar | 30 |  | √ | ' ' | 类别,枚举: transup :上划 transdown :下拨 transfer :调拨 |
| 5 | fexcetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 6 | fopername | 执行操作 | varchar | 80 |  | √ | ' ' | 执行操作,枚举: dosubmitbei :提交银企 dosave :暂存 saveTransferApply :生成暂存调拨申请单 submitTransferApply :生成并提交调拨申请单 saveTransfer :生成暂存调拨单 生成调拨单并提交银企 :生成调拨单并提交银企 |
| 7 | fautotrans | 自动划拨设置 | varchar | 30 |  | √ | ' ' | 自动划拨设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_autotranslog_pkey |  | fid |
| 2 | idx_fca_autotranslog |  | fautotrans |

---

## 调拨明细-子表 t_fca_autotranslog_cash

- **表名称：** 调拨明细-子表
- **表名：** t_fca_autotranslog_cash

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpayeeorgid | 收款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpayeeaccbankid | 收款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 4 | fapplyorgid | fapplyorgid | int8 | 64 |  | √ | 0 |  |
| 5 | fpayeeaccbankname | fpayeeaccbankname | varchar | 50 |  | √ | ' ' |  |
| 6 | fpaycurrencyid | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fretainedamt | 留存金额 | numeric | 19 | 4 | √ | 0 | 留存金额 |
| 10 | fstatus | 执行结果 | varchar | 30 |  | √ | ' ' | 执行结果,枚举: 2 :成功 3 :失败 |
| 11 | fdetail | 自动划拨执行详情 | varchar | 255 |  | √ | ' ' | 自动划拨执行详情 |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fpayeraccbankid | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 14 | ftransferamt | 最小调拨金额 | numeric | 19 | 4 | √ | 0 | 最小调拨金额 |
| 15 | fpayeraccbankname | fpayeraccbankname | varchar | 50 |  | √ | ' ' |  |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fbillno | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fca_autotranslog_cash |  | fentryid |
| 2 | idx_t_fca_autotranslog_cash |  | fid |
