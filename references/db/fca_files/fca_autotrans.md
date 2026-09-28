# 自动划拨设置-fca_autotrans

## 自动划拨设置-主表 t_fca_autotrans

- **表名称：** 自动划拨设置-主表
- **表名：** t_fca_autotrans

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 7 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fopername | 执行操作 | varchar | 80 |  | √ | ' ' | 执行操作,枚举: dosave :生成暂存划拨单 dosubmitbei :生成划拨单并提交银企 saveTransferApply :生成暂存调拨申请单 submitTransferApply :生成并提交调拨申请单 saveTransfer :生成暂存调拨单 saveTransferSubmitBei :生成调拨单并提交银企 |
| 10 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 11 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 12 | fstatus | 数据状态 | varchar | 80 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftype | 划拨类型 | varchar | 80 |  | √ | ' ' | 划拨类型,枚举: transup :上划 transdown :下拨 transfer :调拨 |
| 16 | fenable | 使用状态 | varchar | 80 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | ftxtdesc | 执行计划 | varchar | 400 |  | √ | ' ' | 执行计划 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 21 | fexceplan | 调度计划id | varchar | 80 |  | √ | ' ' | 调度计划id |
| 22 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_autotrans_pkey |  | fid |
| 2 | idx_fca_autotrans |  | ftxtdesc |

---

## 调拨明细-子表 t_fca_autotrans_entry

- **表名称：** 调拨明细-子表
- **表名：** t_fca_autotrans_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpayeeorgid | 收款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpayeeaccbankid | 收款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 4 | fpayeeaccbankname1 | fpayeeaccbankname1 | varchar | 50 |  | √ | ' ' |  |
| 5 | fapplyorgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fpaycurrencyid | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fpayeraccbankno1 | fpayeraccbankno1 | varchar | 50 |  | √ | ' ' |  |
| 8 | fpayeraccbankname1 | fpayeraccbankname1 | varchar | 50 |  | √ | ' ' |  |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fusage | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |
| 12 | fretainedamt | 留存金额 | numeric | 19 | 4 | √ | 0 | 留存金额 |
| 13 | fcreatorid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fpayeraccbankid | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 15 | ftransferamt | 最小调拨金额 | numeric | 19 | 4 | √ | 0 | 最小调拨金额 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pk_fca_autotrans_entry_fid |  | fid,fseq |
| 2 | pk_fca_autotrans_entry |  | fentryid |

---

## 母子账户信息-子表 t_fca_autotrans_acctgroup

- **表名称：** 母子账户信息-子表
- **表名：** t_fca_autotrans_acctgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctgroupid | 母子账户组 | int8 | 64 |  | √ | 0 | 母子账户组 fca_acctgroup |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fbankacctid | 子账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 6 | fcompanyid | 成员单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fca_autotrans_bankacct |  | fbankacctid |
| 2 | idx_fca_autotrans_company |  | fcompanyid |
| 3 | idx_fca_autotrans_acctgroup |  | facctgroupid |
| 4 | idx_t_fca_autotrans_fid |  | fid |
| 5 | pk_t_fca_autotrans_ag |  | fentryid |

---

## 自动划拨设置-多语言表 t_fca_autotrans_l

- **表名称：** 自动划拨设置-多语言表
- **表名：** t_fca_autotrans_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_autotrans_l_pkey |  | fpkid |
| 2 | idx_fca_autotrans_l |  | fid,flocaleid |
