# 借款明细查询表列表-er_loanbill_ds

## 出差人-多选基础资料表 t_er_loanbilldspartner

- **表名称：** 出差人-多选基础资料表
- **表名：** t_er_loanbilldspartner

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_loanbillds_fentryid |  | fentryid |
| 2 | pk_t_er_loanbilldspartner |  | fpkid |

---

## 收款信息-子表 t_er_loanbilldsrecentry

- **表名称：** 收款信息-子表
- **表名：** t_er_loanbilldsrecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccountcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fbuildedamount | 已出单金额 | numeric | 23 | 10 | √ | 0 | 已出单金额 |
| 4 | foriamount | 收款金额 | numeric | 23 | 10 | √ | 0 | 收款金额 |
| 5 | fpayeraccount01 | 银行账号4位 | varchar | 100 |  | √ | ' ' | 银行账号4位 |
| 6 | fpayerdeptid | fpayerdeptid | int8 | 64 |  | √ | 0 |  |
| 7 | fpayercompid | fpayercompid | int8 | 64 |  | √ | 0 |  |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | famount | 收款金额（本位币） | numeric | 23 | 10 | √ | 0 | 收款金额（本位币） |
| 10 | foriaccnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 12 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 13 | fsupplier | 收款人（供应商） | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fentryrepaydate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |
| 15 | fpayeraccountname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 16 | fpayerid | 收款人（个人） | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 17 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0 | 可用余额（本位币） |
| 18 | fcustomer | 收款人（客户） | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 19 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 20 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 21 | foriaccpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 22 | foriaccbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |
| 23 | faccpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已付金额（本位币） |
| 24 | fcasorg | 收款人（内部公司） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | faccnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0 | 未付金额(本位币) |
| 26 | fbanklogo | 银行卡logo图标 | varchar | 50 |  | √ | ' ' | 银行卡logo图标 |
| 27 | fentrypayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 |
| 28 | fpayeraccount02 | 银行账号（显示_old） | varchar | 100 |  | √ | ' ' | 银行账号（显示_old） |
| 29 | fpayeraccount | 银行帐号 | varchar | 100 |  | √ | ' ' | 银行帐号 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_loabbilldsrecentry_fseq |  | fid,fseq |
| 2 | pk_t_er_loanbilldsrecentry |  | fentryid |

---

## 借款明细查询表列表-主表 t_er_loanbillds

- **表名称：** 借款明细查询表列表-主表
- **表名：** t_er_loanbillds

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  | √ | ' ' | 反审核意见 |
| 3 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 4 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbillpayertype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 7 | fhasvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 8 | fbillpayerid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 9 | fpayamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 10 | fstd_costcenter | fstd_costcenter | int8 | 64 |  | √ | 0 |  |
| 11 | fhead_paydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | freturnedamount | 已还款金额 | numeric | 23 | 10 | √ | 0 | 已还款金额 |
| 14 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 1 | 人员 bos_user |
| 16 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 17 | fusedamount | 已报销金额 | numeric | 23 | 10 | √ | 0 | 已报销金额 |
| 18 | fisimport | 是否导入 | bpchar | 1 |  | √ | '0' | 是否导入 |
| 19 | fdetailtype | fdetailtype | varchar | 50 |  | √ | ' ' |  |
| 20 | fcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_prepaybill :预付单 er_dailyloanbill :借款单 er_tripreqbill :出差申请单 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 1 | 人员 bos_user |
| 24 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 25 | ftriptypeid | 出差类型 | int8 | 64 |  | √ | 0 | 出差类型 er_triptype |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 30 | floanamount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 31 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 33 | fprepaytype | 关联业务 | varchar | 50 |  | √ | ' ' | 关联业务,枚举: biztype_project :立项 biztype_contract :合同 biztype_other :其他 |
| 34 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 35 | fappliedreimburseamount | fappliedreimburseamount | numeric | 23 | 10 | √ | 0 |  |
| 36 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 37 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 38 | fisurgent | 紧急付款 | bpchar | 1 |  | √ | '0' | 紧急付款 |
| 39 | fisadvance | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 40 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | fnextauditor | 下一步审核人 | varchar | 100 |  | √ | ' ' | 下一步审核人 |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 44 | frepaymentdate | 预计冲销日期 | timestamp | 0 |  |  | null | 预计冲销日期 |
| 45 | fbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_loanbillds_fapplyerid |  | fapplierid |
| 2 | idx_er_loanbillds_fcompanyid |  | fcompanyid |
| 3 | idx_er_loanbillds_fdate_no |  | fbillno,fbizdate |
| 4 | pk_t_er_loanbillds |  | fid |
| 5 | idx_er_loanbillds_fstatus |  | fbillstatus |

---

## 借款明细-子表 t_er_loanbilldsentry

- **表名称：** 借款明细-子表
- **表名：** t_er_loanbilldsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexporiusedamount | 已报销金额 | numeric | 23 | 10 | √ | 0 | 已报销金额 |
| 3 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 4 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | forgiexpebalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |
| 6 | fsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 7 | fcurrloanamount | 申请金额(本位币) | numeric | 23 | 10 | √ | 0 | 申请金额(本位币) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentrycontractname | 合同名称 | varchar | 200 |  |  | ' ' | 合同名称 |
| 10 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 12 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 13 | ftoplaceid | 目的地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 14 | fentrycontractno | 合同号 | varchar | 30 |  | √ | ' ' | 合同号 |
| 15 | fvehicle | 交通工具 | bpchar | 5 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他交通工具 |
| 16 | fstd_entrycostcenter | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 18 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fexpehasreimamount | 暂冲金额（本位币） | numeric | 23 | 10 | √ | 0 | 暂冲金额（本位币） |
| 20 | ffromplaceid | 出发地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 21 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型 |
| 23 | fexpeorirepayamount | 还款金额 | numeric | 23 | 10 | √ | 0 | 还款金额 |
| 24 | floanamount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 25 | fexpeapprovecurramount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0 | 核定金额(本位币) |
| 26 | fexpebalanceamount | 可用余额本位币 | numeric | 23 | 10 | √ | 0 | 可用余额本位币 |
| 27 | fexperepayamount | 还款金额本位币 | numeric | 23 | 10 | √ | 0 | 还款金额本位币 |
| 28 | fexpeorihasreimamount | 暂冲金额 | numeric | 23 | 10 | √ | 0 | 暂冲金额 |
| 29 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 30 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 33 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 35 | fexpusedamount | 已报销金额本位币 | numeric | 23 | 10 | √ | 0 | 已报销金额本位币 |
| 36 | fentryprojectno | 立项号 | varchar | 30 |  | √ | ' ' | 立项号 |
| 37 | ftripday | 行程天数 | int4 | 32 |  | √ | 0 | 行程天数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_loanbilldsentry_fseq |  | fid,fseq |
| 2 | pk_t_er_loanbilldsentry |  | fentryid |

---

## 项目干系人-多选基础资料表 t_er_loadbilldsower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_loadbilldsower

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
| 1 | idx_er_loanbilldsid |  | fid |
| 2 | pk_t_er_loadbilldsower |  | fpkid |
| 3 | idx_er_loanbilldsuserid |  | fbasedataid |

---

## 借款明细查询表列表-多语言表 t_er_loanbillds_l

- **表名称：** 借款明细查询表列表-多语言表
- **表名：** t_er_loanbillds_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_loanbillds_l |  | fpkid |
