# 预付单-er_prepaybill

## 关联子实体-子表 t_er_prepaybill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_prepaybill_lk

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
| 1 | pk_t_er_prepaybill_lk |  | fpkid |
| 2 | idx_er_prepaybill_lk_fid |  | fid |

---

## 发票云附件-子表 t_er_invoiceattachinfo

- **表名称：** 发票云附件-子表
- **表名：** t_er_invoiceattachinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattstarttime | fattstarttime | timestamp | 0 |  |  | null |  |
| 3 | fattlargetxt | fattlargetxt | varchar | 255 |  |  | null |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachserialno | fattachserialno | varchar | 255 |  | √ | ' ' |  |
| 6 | fattsource | fattsource | varchar | 30 |  | √ | ' ' |  |
| 7 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 8 | frotationangle | 旋转角度 | varchar | 30 |  |  | null | 旋转角度 |
| 9 | fattaffairdiscription | fattaffairdiscription | varchar | 1024 |  |  | null |  |
| 10 | fattheadcount | fattheadcount | int8 | 64 |  | √ | 0 |  |
| 11 | fattcity | fattcity | varchar | 255 |  |  | null |  |
| 12 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 13 | fattenddate | fattenddate | timestamp | 0 |  |  | null |  |
| 14 | fattinvoiceentyid | fattinvoiceentyid | int8 | 64 |  | √ | 0 |  |
| 15 | fattfrom | fattfrom | varchar | 255 |  |  | null |  |
| 16 | fattlargetxt_tag | fattlargetxt_tag | text | 0 |  |  | null |  |
| 17 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 18 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 19 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 20 | fattto | fattto | varchar | 255 |  |  | null |  |
| 21 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 22 | fattendtime | fattendtime | timestamp | 0 |  |  | null |  |
| 23 | fattapplydate | fattapplydate | timestamp | 0 |  |  | null |  |
| 24 | fattstartdate | fattstartdate | timestamp | 0 |  |  | null |  |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fatttotalamount | fatttotalamount | numeric | 23 | 10 | √ | 0 |  |
| 27 | fsnapshoturl | 快照 url | varchar | 512 |  |  | null | 快照 url |
| 28 | fattachtype | 文件类型 | varchar | 30 |  |  | null | 文件类型,枚举: |

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

## 项目干系人-多选基础资料表 t_er_prepayower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_prepayower

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_prepayuser |  | fbasedataid |
| 2 | pk_t_er_prepayower |  | fpkid |
| 3 | idx_er_prepaybill |  | fid |

---

## 关联子实体-子表 t_er_prepaybillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_prepaybillentry_lk

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
| 1 | idx_er_prepaybill_lk_fentryid |  | fentryid |
| 2 | pk_t_er_prepaybillentry_lk |  | fpkid |

---

## 收款信息-子表 t_er_prepaybillrecentry

- **表名称：** 收款信息-子表
- **表名：** t_er_prepaybillrecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwriteoffamount | 已废弃_核销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已废弃_核销金额（本位币） |
| 3 | faccountcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fentrycurrency | fentrycurrency | int8 | 64 |  | √ | 0 |  |
| 5 | fbuildedamount | 出单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 出单金额 |
| 6 | foriamount | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 7 | forgirepaidamount | forgirepaidamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fothercontactunit | 其他往来单位 | int8 | 64 |  | √ | 0 | [其他往来单位 cas_othercontactunit](../cas_files/cas_othercontactunit.md) |
| 9 | fpayeraccount01 | 银行账号4位 | varchar | 100 |  | √ | ' ' | 银行账号4位 |
| 10 | fentrystatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: F :等待付款 G :已付款 I :关闭 E :审核通过 |
| 11 | fpayerdeptid | 收款人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fpayercompid | 收款人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 14 | forgiapplyedreimamount | forgiapplyedreimamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | forgiwriteoffamount | 已废弃_核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已废弃_核销金额 |
| 16 | famount | 收款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额（本位币） |
| 17 | foriaccnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 18 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 19 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 20 | fsupplier | 收款人（供应商） | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 21 | fentryrepaydate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |
| 22 | fpayeraccountname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 23 | fpayerid | 收款人（个人） | int8 | 64 |  | √ | 0 | [收款信息 er_payeer](../em_files/er_payeer.md) |
| 24 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额（本位币） |
| 25 | fapplyedreimamount | 已废弃_申请报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已废弃_申请报销金额(本位币) |
| 26 | fcustomer | 收款人（客户） | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 27 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 28 | frepaidamount | frepaidamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 30 | foriaccpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 31 | foriaccbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额 |
| 32 | faccpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额（本位币） |
| 33 | fcasorg | 收款人（内部公司） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | faccnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额(本位币) |
| 35 | fbanklogo | 银行卡logo图标 | varchar | 50 |  | √ | ' ' | 银行卡logo图标 |
| 36 | fentrypayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 cas_othercontactunit :其他往来单位 |
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
| 1 | pk_t_er_prepaybillrecentry |  | fentryid |
| 2 | idx_er_prepayrecentry_fseq |  | fid,fseq |

---

## 预付单-主表 t_er_prepaybill

- **表名称：** 预付单-主表
- **表名：** t_er_prepaybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fpaycompanyid | 支付公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | finvokeinvoicecloud | 与发票云交互 | bpchar | 1 |  | √ | '0' | 与发票云交互 |
| 5 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbillpayertype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 8 | fhasvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 9 | fstd_costcenter | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 10 | fhead_paydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 13 | fapplierpositionstr | fapplierpositionstr | varchar | 100 |  | √ | ' ' |  |
| 14 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | ftotalwhtaxamount | 预扣税原币合计（费用） | numeric | 23 | 10 | √ | 0 | 预扣税原币合计（费用） |
| 16 | fneeduploadinvoice | 有待上传的纸票/附件 | bpchar | 1 |  | √ | '0' | 有待上传的纸票/附件 |
| 17 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fstdbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 20 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0 | 已预提金额 |
| 21 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 24 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 25 | fisenableinvoice | 启用发票云 | bpchar | 1 |  | √ | '0' | 启用发票云 |
| 26 | fimagenumber | 影像编码 | varchar | 80 |  | √ | ' ' | 影像编码 |
| 27 | frameworkcontract | 框架合同 | bpchar | 1 |  | √ | '0' | 框架合同 |
| 28 | fappliedreimburseamount | 已申请报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已申请报销金额 |
| 29 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 30 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 33 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fbalanceamount | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 35 | fisoverbudget | 超预算 | bpchar | 1 |  | √ | '0' | 超预算 |
| 36 | fcontractsconn | 关联合同 | varchar | 1000 |  | √ | ' ' | 关联合同 |
| 37 | ftel | 联系方式 | varchar | 100 |  | √ | ' ' | 联系方式 |
| 38 | fbillpayerid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 39 | fpayamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 40 | freturnedamount | 退款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 退款金额 |
| 41 | ftotalcurwhtaxamount | 预扣税合计（费用） | numeric | 23 | 10 | √ | 0 | 预扣税合计（费用） |
| 42 | fcreatorid | 创建人 | int8 | 64 |  | √ | 1 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fusedamount | 已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额 |
| 44 | fisimport | 导入 | bpchar | 1 |  | √ | '0' | 导入 |
| 45 | fcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fispush | 下推合同台账 | bpchar | 1 |  | √ | '0' | 下推合同台账 |
| 47 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_prepaybill :预付单 |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 1 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | fwhtaxbear | 往来方承担预扣税 | bpchar | 1 |  | √ | '1' | 往来方承担预扣税 |
| 51 | fiscurrency | 多币种 | bpchar | 1 |  | √ | '0' | 多币种 |
| 52 | fisstopreim | 止付单 | bpchar | 1 |  | √ | '0' | 止付单 |
| 53 | floanamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 54 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fispaybyhead | 按单头付款 | bpchar | 1 |  | √ | '0' | 按单头付款 |
| 56 | fprepaytype | 关联业务 | varchar | 50 |  | √ | ' ' | 关联业务,枚举: biztype_project :立项 biztype_contract :合同 biztype_other :其他 |
| 57 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 58 | fstopdescription | 止付说明 | varchar | 1000 |  | √ | ' ' | 止付说明 |
| 59 | fisurgent | 紧急付款 | bpchar | 1 |  | √ | '0' | 紧急付款 |
| 60 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | [业务分类 er_projecttype](../em_files/er_projecttype.md) |
| 61 | fcurrencyid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 62 | frepaymentdate | 预计冲销日期 | timestamp | 0 |  |  | null | 预计冲销日期 |
| 63 | fbillpayeramount | 往来单位预付余额 | numeric | 23 | 10 | √ | 0 | 往来单位预付余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_perpaybill_fdate_no |  | fbizdate,fbillno |
| 2 | idx_er_perpaybill_fapplyerid |  | fapplierid |
| 3 | idx_er_perpaybill_fcreatorid |  | fcreatorid |
| 4 | idx_er_perpaybill_fcompanyid |  | fcompanyid |
| 5 | pk_t_er_prepaybill |  | fid |
| 6 | idx_er_perpaybill_fbillno |  | fbillno |
| 7 | idx_er_perpaybill_fbpayer_cp |  | fbillpayerid,fcostcompanyid |
| 8 | idx_er_perpaybill_fstatus |  | fbillstatus |

---

## 关联子实体-子表 t_er_prepaycontract_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_prepaycontract_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_prepaycontract_lk |  | fpkid |
| 2 | idx_er_prepaycontract_lk |  | fsbillid |

---

## 关联合同-子表 t_er_prepaycontract

- **表名称：** 关联合同-子表
- **表名：** t_er_prepaycontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontractcode | 合同号 | varchar | 500 |  | √ | ' ' | 合同号 |
| 3 | fcontractapplier | 经办人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcontractcurrreimamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已付金额（本位币） |
| 5 | fsourceentryid | fsourceentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fconcurrcanloanamount | 可预付金额(本位币) | numeric | 23 | 10 | √ | 0 | 可预付金额(本位币) |
| 7 | fsigndate | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 8 | fcontractproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fcontractexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 11 | fcontractpartatypenew | 甲方类型 | varchar | 50 |  | √ | ' ' | 甲方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 bos_adminorg :公司(行政组织) cas_othercontactunit :其他往来单位 |
| 12 | fcontractdescription | 合同说明 | varchar | 1000 |  | √ | ' ' | 合同说明 |
| 13 | fcontractexpquotetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 14 | fcontractcanamount | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 15 | fcontractsrcentryid | 关联合同分录id | int8 | 64 |  | √ | 0 | 关联合同分录id |
| 16 | fcontractpaytypeid | 付款类型 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 17 | fcontractpartbtype | 乙方类型 | varchar | 50 |  | √ | ' ' | 乙方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 bos_adminorg :公司(行政组织) cas_othercontactunit :其他往来单位 |
| 18 | fentryprepayedamount | 已预付金额 | numeric | 23 | 10 | √ | 0 | 已预付金额 |
| 19 | fcontractsid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 20 | fcontractpartanew | 甲方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 21 | fentryinvoiceamount | 到票金额 | numeric | 23 | 10 | √ | 0 | 到票金额 |
| 22 | fentrycurrprepayedamount | 已预付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已预付金额（本位币） |
| 23 | fcontractentrycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fcontractnotpayamount | 未付金额（本位币） | numeric | 23 | 10 | √ | 0 | 未付金额（本位币） |
| 25 | fconrepayamount | 退款金额本位币 | numeric | 23 | 10 | √ | 0 | 退款金额本位币 |
| 26 | fcontractcostorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fcontractname | 合同名称 | varchar | 500 |  | √ | ' ' | 合同名称 |
| 28 | fcontracthappendate | 预计付款日期 | timestamp | 0 |  |  | null | 预计付款日期 |
| 29 | fcontractwriteoff | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 30 | fcontractpartb | 乙方 | varchar | 100 |  | √ | ' ' | 供应商 bd_supplier |
| 31 | fcontractnonpayamount | 待付金额（本位币） | numeric | 23 | 10 | √ | 0 | 待付金额（本位币） |
| 32 | fcontractparta | 甲方(old) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | foriconrepayamount | 退款金额 | numeric | 23 | 10 | √ | 0 | 退款金额 |
| 34 | fcontractcanloanamount | 可预付金额 | numeric | 23 | 10 | √ | 0 | 可预付金额 |
| 35 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 36 | fcontractentrychangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 37 | fcontractcurrcanamount | 可报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 可报销金额(本位币) |
| 38 | fcontractcurrwriteoff | 冲销金额（本位币） | numeric | 23 | 10 | √ | 0 | 冲销金额（本位币） |
| 39 | fcontractreimamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_prepaycontract |  | fentryid |
| 2 | idx_er_prepaycontract_fcode |  | fcontractcode |

---

## 预付信息-子表 t_er_prepaybillentry

- **表名称：** 预付信息-子表
- **表名：** t_er_prepaybillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexporiusedamount | 已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额 |
| 3 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 4 | fwithholdingtaxrate | 预扣税率 | numeric | 23 | 10 | √ | 0 | 预扣税率 |
| 5 | fentrycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | forgiexpebalanceamount | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 7 | fsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 8 | fcurrloanamount | 申请金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(本位币) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fentrycontractname | 合同名称 | varchar | 500 |  |  | ' ' | 合同名称 |
| 11 | fwhtaxusedamount | 已冲销预扣税额 | numeric | 23 | 10 | √ | 0 | 已冲销预扣税额 |
| 12 | fentrycostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fcurwithholdingtaxamount | 预扣税额（本位币） | numeric | 23 | 10 | √ | 0 | 预扣税额（本位币） |
| 14 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 15 | fexpwithholdingamount | 已预提金额（本位币） | numeric | 23 | 10 | √ | 0 | 已预提金额（本位币） |
| 16 | fentrycontractno | 合同号 | varchar | 500 |  | √ | ' ' | 合同号 |
| 17 | fcurwhtaxusedamount | 已冲销预扣税额（本位币） | numeric | 23 | 10 | √ | 0 | 已冲销预扣税额（本位币） |
| 18 | fsourcebillno | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |
| 19 | fstd_entrycostcenter | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 20 | fexpnonpayamount | 在途金额 | numeric | 23 | 10 | √ | 0 | 在途金额 |
| 21 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 22 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fexpehasreimamount | 暂冲金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 暂冲金额（本位币） |
| 24 | fexpebillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: F :等待付款 G :已付款 I :关闭 E :审核通过 |
| 25 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型 |
| 27 | fexpeorirepayamount | 退款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 退款金额 |
| 28 | floanamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 29 | fexpeapprovecurramount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额(本位币) |
| 30 | fexpebalanceamount | 未核销金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额本位币 |
| 31 | fexperepayamount | 退款金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 退款金额本位币 |
| 32 | fwithholdingtaxamount | 预扣税额 | numeric | 23 | 10 | √ | 0 | 预扣税额 |
| 33 | fexpeorihasreimamount | 暂冲金额 | numeric | 23 | 10 | √ | 0.0000000000 | 暂冲金额 |
| 34 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 37 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 39 | fexpusedamount | 已报销金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额本位币 |
| 40 | fentryprojectno | 立项号 | varchar | 50 |  | √ | ' ' | 立项号 |
| 41 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0 | 已预提金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_prepayentry_fseq |  | fid,fseq |
| 2 | pk_t_er_prepaybillentry |  | fentryid |
| 3 | idx_er_prepayentry_fsrcbillid |  | fsourcebillid |

---

## 预付单-关联追踪表 t_er_prepaybill_tc

- **表名称：** 预付单-关联追踪表
- **表名：** t_er_prepaybill_tc

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
| 1 | idx_er_prepayb_tc_fbillid |  | ftbillid |
| 2 | idx_er_prepaybill_tc_tid |  | ftid |
| 3 | pk_t_er_prepaybill_tc |  | fid |
| 4 | idx_er_prepaybill_tc_tbill |  | ftbillid |

---

## 预付单-反写记录表 t_er_prepaybill_wb

- **表名称：** 预付单-反写记录表
- **表名：** t_er_prepaybill_wb

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
| 1 | idx_er_prepaybill_wb_fid |  | fid |
| 2 | pk_t_er_prepaybill_wb |  | fentryid |

---

## 预付单-多语言表 t_er_prepaybill_l

- **表名称：** 预付单-多语言表
- **表名：** t_er_prepaybill_l

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
| 1 | pk_t_er_prepaybill_l |  | fpkid |
| 2 | idx_prepaybill_l_id |  | fid,flocaleid |

---

## 付款信息-子表 t_er_prepaybillpayentry

- **表名称：** 付款信息-子表
- **表名：** t_er_prepaybillpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetpayorg | 付款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftargetbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | ftargetbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 5 | fdpcurrency | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffee | 手续费 | numeric | 23 | 10 | √ | 0.0000000000 | 手续费 |
| 8 | ftargetentrustorg | 委托付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fdpexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 付款汇率 |
| 10 | flossamt | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 11 | fdpamt | 付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额 |
| 12 | fagreedrate | 兑换汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 兑换汇率 |
| 13 | ftargetpayacctid | 付款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 14 | ftargetlocalamount | 收款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额(本位币) |
| 15 | ftargetexchange | 收款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 收款汇率 |
| 16 | ftargetpaybank | 付款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 17 | ffeecurrency | 手续费币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fdplocalamt | 付款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额(本位币) |
| 19 | ftargetpayamt | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 20 | ftargetpayacct | 付款账号（文本） | varchar | 50 |  | √ | ' ' | 付款账号（文本） |
| 21 | ftargetopenorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | ftargetbillid | 目标单据id | int8 | 64 |  | √ | 0 | 目标单据id |
| 23 | ftargetpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 24 | ftargetcurrency | 收款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | ftargetsettletype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_payentry_feq |  | fid,fseq |
| 2 | idx_er_payentry_targetbillid |  | ftargetbillid,ftargetbillno |
| 3 | pk_t_er_prepaybillpayentry |  | fentryid |
