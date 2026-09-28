# 日常借款单（共享审批）-er_dailyloanbill_ssc

## 日常借款单（共享审批）-反写记录表 t_er_dailyloanbill_wb

- **表名称：** 日常借款单（共享审批）-反写记录表
- **表名：** t_er_dailyloanbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_dailyloanbill_wb_pkey |  | fentryid |
| 2 | idx_er_dailyloanbill_wb_fid |  | fid |

---

## 发票云附件-子表 t_er_invoiceattachinfo

- **表名称：** 发票云附件-子表
- **表名：** t_er_invoiceattachinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 3 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 6 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 7 | frotationangle | 旋转角度 | varchar | 30 |  |  | null | 旋转角度 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 10 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 11 | fsnapshoturl | 快照 url | varchar | 512 |  |  | null | 快照 url |
| 12 | fattachtype | 文件类型 | varchar | 30 |  |  | null | 文件类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_invoiceattachinfo |  | fentryid |
| 2 | idx_er_invoiceattachinfo_fid |  | fid |

---

## 日常借款单（共享审批）-关联追踪表 t_er_dailyloanbill_tc

- **表名称：** 日常借款单（共享审批）-关联追踪表
- **表名：** t_er_dailyloanbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_dailyloanbill_tc_pkey |  | fid |
| 2 | idx_er_dailyloanbill_tc_tid |  | ftid |
| 3 | idx_er_dailyloanbill_tc_tbill |  | ftbillid |
| 4 | idx_er_dyloanb_tc_fbillid |  | ftbillid |

---

## 日常借款单（共享审批）-多语言表 t_er_dailyloanbill_l

- **表名称：** 日常借款单（共享审批）-多语言表
- **表名：** t_er_dailyloanbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapplierpositionstr | 职位文本 | varchar | 100 |  | √ | ' ' | 职位文本 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_dailyloanbill_l_pkey |  | fpkid |
| 2 | idx_dlb_l_id |  | fid,flocaleid |

---

## 收款信息-子表 t_er_accountinfo

- **表名称：** 收款信息-子表
- **表名：** t_er_accountinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwriteoffamount | 核销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核销金额（本位币） |
| 3 | faccountcurrency | 币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fbuildedamount | 已出单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已出单金额 |
| 5 | foriamount | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 6 | forgirepaidamount | 已还金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已还金额 |
| 7 | fpayeraccount01 | 银行账号4位 | varchar | 100 |  | √ | ' ' | 银行账号4位 |
| 8 | fentrystatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: F :等待付款 G :已付款 I :关闭 E :审核通过 |
| 9 | fpayerdeptid | 收款人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fpayercompid | 收款人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fpayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 |
| 12 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 13 | forgiapplyedreimamount | 申请报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请报销金额 |
| 14 | forgiwriteoffamount | 核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核销金额 |
| 15 | famount | 收款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额（本位币） |
| 16 | foriaccnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 17 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 18 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 19 | fsupplier | 收款人（供应商） | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | fentryrepaydate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |
| 21 | fpayeraccountname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 22 | fpayerid | 收款人（个人） | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 23 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额（本位币） |
| 24 | fapplyedreimamount | 申请报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 申请报销金额(本位币) |
| 25 | facccostcompany | facccostcompany | int8 | 64 |  | √ | 0 |  |
| 26 | fcustomer | 收款人（客户） | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 27 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 28 | frepaidamount | 已还金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 已还金额本位币 |
| 29 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 30 | foriaccpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 31 | foriaccbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额 |
| 32 | faccpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额（本位币） |
| 33 | fcasorg | 收款人（内部公司） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | faccnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额(本位币) |
| 35 | fbanklogo | 银行卡logo图标 | varchar | 50 |  | √ | ' ' | 银行卡logo图标 |
| 36 | faccounttype | faccounttype | varchar | 10 |  | √ | ' ' |  |
| 37 | fpayeraccount02 | 银行账号（显示_old） | varchar | 100 |  | √ | ' ' | 银行账号（显示_old） |
| 38 | fpayeraccount | 银行账号 | varchar | 100 |  | √ | ' ' | 银行账号 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_accountinfo_pkey |  | fentryid |
| 2 | idx_er_accountinfo_fseq |  | fid,fseq |

---

## 借款明细-子表 t_er_dailyloandetail

- **表名称：** 借款明细-子表
- **表名：** t_er_dailyloandetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexporiusedamount | 冲账金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲账金额 |
| 3 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 4 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 5 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | forgiexpebalanceamount | 借款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额 |
| 7 | fsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 8 | fcurrloanamount | 借款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 借款金额(本位币) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 11 | fapplyprojectno | 立项号 | varchar | 80 |  | √ | ' ' | 立项号 |
| 12 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 14 | fapplybillno | 关联申请单号 | varchar | 100 |  | √ | '0' | 关联申请单号 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 17 | fremark | 借款用途 | varchar | 255 |  | √ | ' ' | 借款用途 |
| 18 | fexpehasreimamount | 暂冲金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 暂冲金额（本位币） |
| 19 | fexpebillstatus | 单据状态 | bpchar | 1 |  | √ | 'G' | 单据状态,枚举: F :等待付款 G :已付款 I :关闭 E :审核通过 |
| 20 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fexpeorirepayamount | 还款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 还款金额 |
| 23 | freimburser | 借款人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | floanamount | 借款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款金额 |
| 25 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 26 | fexpebalanceamount | 借款余额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额(本位币) |
| 27 | fexperepayamount | 还款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 还款金额（本位币） |
| 28 | fexpeorihasreimamount | 暂冲金额 | numeric | 23 | 10 | √ | 0.0000000000 | 暂冲金额 |
| 29 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 30 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 31 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 33 | fexpusedamount | 冲账金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 冲账金额（本位币） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_dailyloandetail_pkey |  | fdetailid |
| 2 | idx_er_loandetail_fsrcbillid |  | fsourcebillid |
| 3 | idx_er_loandetail_fseq |  | fid,fseq |

---

## 关联子实体-子表 t_er_dailyloandetail_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_dailyloandetail_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_loandetail_lk_fdetailid |  | fdetailid |
| 2 | t_er_dailyloandetail_lk_pkey |  | fpkid |

---

## 付款信息-子表 t_er_loanbillpayentry

- **表名称：** 付款信息-子表
- **表名：** t_er_loanbillpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetpayorg | 付款人 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftargetbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | ftargetbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 5 | fdpcurrency | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ffee | 手续费 | numeric | 23 | 10 | √ | 0.0000000000 | 手续费 |
| 8 | ftargetentrustorg | 委托付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fdpexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 付款汇率 |
| 10 | flossamt | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 11 | fdpamt | 付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额 |
| 12 | fagreedrate | 兑换汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 兑换汇率 |
| 13 | ftargetlocalamount | 收款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额(本位币) |
| 14 | ftargetpayacctid | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 15 | ftargetexchange | 收款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 收款汇率 |
| 16 | ftargetpaybank | 付款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 17 | ffeecurrency | 手续费币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fdplocalamt | 付款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额(本位币) |
| 19 | ftargetpayamt | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 20 | ftargetpayacct | 付款账号（文本） | varchar | 50 |  | √ | ' ' | 付款账号（文本） |
| 21 | ftargetopenorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | ftargetbillid | 目标单据id | int8 | 64 |  | √ | 0 | 目标单据id |
| 23 | ftargetpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 24 | ftargetcurrency | 收款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | ftargetsettletype | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_lbpe_targetbillid_no |  | ftargetbillid,ftargetbillno |
| 2 | t_er_loanbillpayentry_pkey |  | fentryid |
| 3 | idx_er_lbpe_feq |  | fid,fseq |

---

## 项目干系人-多选基础资料表 t_er_dailyloanower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_dailyloanower

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_dailyloanuserid |  | fbasedataid |
| 2 | pk_t_er_dailyloanower |  | fpkid |
| 3 | idx_er_dailyloanbillid |  | fid |

---

## 关联子实体-子表 t_er_dailyloanbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_dailyloanbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | stableid | stableid | int8 | 64 |  | √ | 0 |  |
| 3 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_dailbill_lk_fid |  | fid |
| 2 | t_er_dailyloanbill_lk_pkey |  | fpkid |

---

## 日常借款单（共享审批）-主表 t_er_dailyloanbill

- **表名称：** 日常借款单（共享审批）-主表
- **表名：** t_er_dailyloanbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fpaycompanyid | 支付公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 5 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 8 | fhead_paydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 11 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 12 | fapplierpositionstr | fapplierpositionstr | varchar | 100 |  | √ | ' ' |  |
| 13 | fismanualrepay | 是否手动还款 | bpchar | 1 |  | √ | '0' | 是否手动还款 |
| 14 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fdescription | 事由 | varchar | 1000 |  |  | null | 事由 |
| 19 | fisenableinvoice | 是否启用发票云 | bpchar | 1 |  | √ | '0' | 是否启用发票云 |
| 20 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 21 | fattachmentacount | fattachmentacount | int8 | 64 |  | √ | 0 |  |
| 22 | fappliedreimburseamount | 已申请报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已申请报销金额 |
| 23 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 24 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 25 | fnextauditor | 下一步审核人 | varchar | 100 |  | √ | ' ' | 下一步审核人 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 28 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fbalanceamount | 借款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额 |
| 30 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 31 | ftel | 联系方式 | varchar | 100 |  | √ | ' ' | 联系方式 |
| 32 | fpayamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 33 | freturnedamount | 已还金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 已还金额本位币 |
| 34 | frelatedbiz | 关联业务 | varchar | 50 |  | √ | 'relatedtype_other' | 关联业务,枚举: relatedtype_contract :合同 relatedtype_project :立项 relatedtype_other :其他 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fusedamount | 已冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已冲销金额 |
| 37 | fisimport | 是否导入 | bpchar | 1 |  | √ | '0' | 是否导入 |
| 38 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_loanbill :出差借款单 er_tripreimbursebill :差旅费报销单 er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_dailyreimbursebill :费用报销单 er_repaymentbill :还款单 |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fismultireimburser | 多借款人 | bpchar | 1 |  | √ | '0' | 多借款人 |
| 43 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 44 | fisstopreim | 是否止付单 | bpchar | 1 |  | √ | '0' | 是否止付单 |
| 45 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 46 | floanamount | 借款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款金额 |
| 47 | fisbuildreimbill | 是否生成报销单 | bpchar | 1 |  | √ | '0' | 是否生成报销单 |
| 48 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 49 | fispaybyhead | 按单头付款 | bpchar | 1 |  | √ | '0' | 按单头付款 |
| 50 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 51 | fstopdescription | 止付说明 | varchar | 1000 |  | √ | ' ' | 止付说明 |
| 52 | fisadvance | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 53 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 54 | frepaymentdate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_dlb_fapplierid |  | fapplierid |
| 2 | idx_er_dlb_fcreatorid |  | fcreatorid |
| 3 | idx_er_dlb_fbillstatus |  | fbillstatus |
| 4 | idx_er_dlb_forgid |  | forgid |
| 5 | idx_er_dlb_fcompanyid |  | fcompanyid |
| 6 | t_er_dailyloanbill_pkey |  | fid |
| 7 | idx_er_dlb_fbizdate_fbillno |  | fbizdate,fbillno |
| 8 | idx_er_dlb_fbillno |  | fbillno |

---

## 关联子实体-子表 t_er_accountinfo_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_accountinfo_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | foriaccbalanceamount | foriaccbalanceamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | foriaccbalanceamount_old | foriaccbalanceamount_old | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | faccbalanceamount_old | faccbalanceamount_old | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | faccbalanceamount | faccbalanceamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_accountinfo_lk_pkey |  | fpkid |
| 2 | idx_er_accountinfo_lk_fid |  | fentryid |
