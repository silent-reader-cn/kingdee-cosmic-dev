# 付款申请单-er_applypaybill

## 付款申请单-反写记录表 t_er_applypaybill_wb

- **表名称：** 付款申请单-反写记录表
- **表名：** t_er_applypaybill_wb

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
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_alypay_wb_fid |  | fid |
| 2 | pk_t_er_applypaybill_wb |  | fentryid |

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

## 付款申请单-关联追踪表 t_er_applypaybill_tc

- **表名称：** 付款申请单-关联追踪表
- **表名：** t_er_applypaybill_tc

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
| 1 | idx_er_applypaybill_tc_tbill |  | ftbillid |
| 2 | idx_er_applypaybill_tc_tid |  | ftid |
| 3 | idx_er_alypay_tc_fbillid |  | ftbillid |
| 4 | pk_t_er_applypaybill_tc |  | fid |

---

## 付款申请单-主表 t_er_applypaybill

- **表名称：** 付款申请单-主表
- **表名：** t_er_applypaybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fpaycompanyid | 支付公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 5 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbillpayertype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 8 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 9 | fstd_costcenter | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 10 | fhead_paydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 11 | freimburseamount | 报销总额 | numeric | 23 | 10 | √ | 0 | 报销总额 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 14 | fapplierpositionstr | fapplierpositionstr | varchar | 100 |  | √ | ' ' |  |
| 15 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fstdbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 18 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 21 | fisenableinvoice | 是否启用发票云 | bpchar | 1 |  | √ | '0' | 是否启用发票云 |
| 22 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 23 | fapproveamount | 本次核定付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次核定付款金额 |
| 24 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 27 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fbalanceamount | 可用余额（已废弃） | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额（已废弃） |
| 29 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 30 | ftel | 联系方式 | varchar | 100 |  | √ | ' ' | 联系方式 |
| 31 | fbillpayerid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 32 | fpayamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 33 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fpubnotpayamount | 当前未付金额 | numeric | 23 | 10 | √ | 0 | 当前未付金额 |
| 35 | fusedamount | 已用金额（已废弃） | numeric | 23 | 10 | √ | 0.0000000000 | 已用金额（已废弃） |
| 36 | fcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fstdreimbursetype | 关联业务 | varchar | 50 |  | √ | ' ' | 关联业务,枚举: biztype_project :立项报销 biztype_contract :合同报销 biztype_other :其他 biztype_estimate :无合同暂估 biztype_contractestimate :有合同暂估 |
| 38 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_applypaybill :付款申请单 |
| 39 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fpublicreimbillno | 报销单号 | varchar | 30 |  | √ | ' ' | 报销单号 |
| 41 | fonaccountamount | 挂账总额 | numeric | 23 | 10 | √ | 0 | 挂账总额 |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 44 | fisstopreim | 是否止付单 | bpchar | 1 |  | √ | '0' | 是否止付单 |
| 45 | floanamount | 本次申请付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次申请付款金额 |
| 46 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | fispaybyhead | 按单头付款 | bpchar | 1 |  | √ | '0' | 按单头付款 |
| 48 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 49 | fstopdescription | 止付说明 | varchar | 1000 |  | √ | ' ' | 止付说明 |
| 50 | fisurgent | 紧急付款 | bpchar | 1 |  | √ | '0' | 紧急付款 |
| 51 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 52 | frepaymentdate | 还款日期（已废弃） | timestamp | 0 |  |  | null | 还款日期（已废弃） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_alypay_fdate_no |  | fbizdate,fbillno |
| 2 | idx_er_alypay_fbillno |  | fbillno |
| 3 | idx_er_alypay_fcreatorid |  | fcreatorid |
| 4 | idx_er_alypay_fapplyerid |  | fapplierid |
| 5 | idx_er_alypay_fstatus |  | fbillstatus |
| 6 | idx_er_alypay_fcompanyid |  | fcompanyid |
| 7 | pk_t_er_applypaybill |  | fid |

---

## 付款信息-子表 t_er_applypaybillpayentry

- **表名称：** 付款信息-子表
- **表名：** t_er_applypaybillpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetpayorg | 付款人 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftargetbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | ftargetbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 5 | fdpcurrency | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffee | 手续费 | numeric | 23 | 10 | √ | 0.0000000000 | 手续费 |
| 8 | ftargetentrustorg | 委托付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fdpexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 付款汇率 |
| 10 | flossamt | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 11 | fdpamt | 付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额 |
| 12 | fagreedrate | 兑换汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 兑换汇率 |
| 13 | ftargetpayacctid | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 14 | ftargetlocalamount | 收款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额(本位币) |
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
| 1 | idx_er_alypayent_targetbillid |  | ftargetbillid,ftargetbillno |
| 2 | pk_t_er_applypaybillpayentry |  | fentryid |
| 3 | idx_er_alypayent_feq |  | fid,fseq |

---

## 关联子实体-子表 t_er_applypaybillrecentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_applypaybillrecentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_applypay_lk_fentryid |  | fentryid |
| 2 | pk_er_applypaybillrecentry_lk |  | fpkid |

---

## 付款申请单-多语言表 t_er_applypaybill_l

- **表名称：** 付款申请单-多语言表
- **表名：** t_er_applypaybill_l

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
| 1 | idx_alypay_l_id |  | fid,flocaleid |
| 2 | pk_t_er_applypaybill_l |  | fpkid |

---

## 立项&#x2f;合同信息-子表 t_er_applypaybillentry

- **表名称：** 立项&#x2f;合同信息-子表
- **表名：** t_er_applypaybillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fentryprojectname | 立项名称 | varchar | 500 |  | √ | ' ' | 立项名称 |
| 5 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 6 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 8 | fcurrloanamount | 申请金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(本位币) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fentrycontractname | 合同名称 | varchar | 500 |  | √ | ' ' | 合同名称 |
| 11 | floanamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 12 | fexpeapprovecurramount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额(本位币) |
| 13 | fentrycostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 15 | fwbsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: contract :合同单 project :立项单 estimate :费用暂估单 er_vehiclecheckingbill :用车结算单 pur_receipt :商城验收单 |
| 16 | fentrycontractno | 合同号 | varchar | 30 |  | √ | ' ' | 合同号 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 19 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 21 | fentryprojectno | 立项号 | varchar | 30 |  | √ | ' ' | 立项号 |
| 22 | fstd_entrycostcenter | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_applypaybillentry |  | fentryid |
| 2 | idx_er_alypayent_fseq |  | fid,fseq |

---

## 收款信息-子表 t_er_applypaybillrecentry

- **表名称：** 收款信息-子表
- **表名：** t_er_applypaybillrecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwriteoffamount | 已废弃_核销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已废弃_核销金额（本位币） |
| 3 | faccountcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fbuildedamount | 已出单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已出单金额 |
| 5 | foriamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 6 | forgirepaidamount | forgirepaidamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fpayeraccount01 | 银行账号4位 | varchar | 100 |  | √ | ' ' | 银行账号4位 |
| 8 | fentrystatus | 收款分录单据状态 | bpchar | 1 |  | √ | '0' | 收款分录单据状态,枚举: F :等待付款 G :已付款 I :关闭 E :审核通过 |
| 9 | fpayerdeptid | 收款人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fpayercompid | 收款人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 12 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 13 | forgiapplyedreimamount | forgiapplyedreimamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | forgiwriteoffamount | 已废弃_核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已废弃_核销金额 |
| 15 | famount | 申请金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额（本位币） |
| 16 | foriaccnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 17 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 18 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 19 | fsupplier | 收款人（供应商） | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | faccapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 21 | fentryrepaydate | 还款日期1 | timestamp | 0 |  |  | null | 还款日期1 |
| 22 | fpayeraccountname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 23 | fpayerid | 收款人（个人） | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 24 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额（本位币） |
| 25 | fsourcebillno | 报销单号 | varchar | 30 |  | √ | ' ' | 报销单号 |
| 26 | fapplyedreimamount | 已废弃_申请报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已废弃_申请报销金额(本位币) |
| 27 | fcustomer | 收款人（客户） | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 28 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 29 | frepaidamount | frepaidamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 30 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 31 | foriaccpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 32 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型 |
| 33 | foriaccbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额 |
| 34 | faccpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额（本位币） |
| 35 | fcasorg | 收款人（内部公司） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | faccnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额(本位币) |
| 37 | fbanklogo | 银行卡logo图标1 | varchar | 50 |  | √ | ' ' | 银行卡logo图标1 |
| 38 | fentrypayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 |
| 39 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 40 | fpayeraccount02 | 银行账号（显示_old） | varchar | 100 |  | √ | ' ' | 银行账号（显示_old） |
| 41 | fpayeraccount | 银行账号 | varchar | 100 |  | √ | ' ' | 银行账号 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 44 | faccapprovecurramount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0 | 核定金额(本位币) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_applypaybillrecentry |  | fentryid |
| 2 | idx_er_alypayrecent_fseq |  | fid,fseq |

---

## 关联子实体-子表 t_er_applypaybill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_applypaybill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | stableid | stableid | int8 | 64 |  | √ | 0 |  |
| 3 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_applypaybill_lk |  | fpkid |
| 2 | idx_er_alypay_lk_fid |  | fid |
