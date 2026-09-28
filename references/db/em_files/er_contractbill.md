# 合同台账单-er_contractbill

## 关联子实体-子表 t_er_contractbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_contractbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_contractbill_lk |  | fpkid |
| 2 | idx_er_contractbill_lk_fid |  | fid |

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

## 合同条款-子表 t_er_contract_item

- **表名称：** 合同条款-子表
- **表名：** t_er_contract_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemcontent | 条款内容 | text | 0 |  |  | ' ' | 条款内容 |
| 3 | fttemname | 条款名称 | varchar | 255 |  | √ | ' ' | 条款名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fitemcode | 条款编码 | varchar | 255 |  | √ | ' ' | 条款编码 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 1 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_contract_item |  | fentryid |

---

## 付款计划-子表 t_er_contractentry

- **表名称：** 付款计划-子表
- **表名：** t_er_contractentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhappendate | 预计付款日期 | timestamp | 0 |  |  | null | 预计付款日期 |
| 3 | fentrycurrency | 分录币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 5 | forgiexpebalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 6 | fsourceentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 7 | fexppricewithtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fpushedamount | 已预付金额 | numeric | 23 | 10 | √ | 0 | 已预付金额 |
| 10 | fcanloanamount | 可预付金额 | numeric | 23 | 10 | √ | 0 | 可预付金额 |
| 11 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 13 | fnum | 数量 | int4 | 32 |  | √ | 0 | 数量 |
| 14 | fexpquotetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 15 | fexpwithholdingamount | 已预提金额(本位币) | numeric | 23 | 10 | √ | 0 | 已预提金额(本位币) |
| 16 | fsourcebillno | 源单编号 | varchar | 100 |  | √ | ' ' | 源单编号 |
| 17 | fitemfrom | 分录来源 | bpchar | 1 |  | √ | '0' | 分录来源,枚举: 0 :手工添加 1 :关联生成 |
| 18 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 19 | fcurrapplyamount | 含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 含税金额(本位币) |
| 20 | fentrycontractamount | 原合同金额 | numeric | 23 | 10 | √ | 0 | 原合同金额 |
| 21 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fcanloancurramount | 可预付金额(本位币) | numeric | 23 | 10 | √ | 0 | 可预付金额(本位币) |
| 23 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: er_contractbill :费用合同单 |
| 24 | fentryproducttype | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 25 | fentrychangeableamount | 合同可变更金额 | numeric | 23 | 10 | √ | 0 | 合同可变更金额 |
| 26 | fpaypercent | 付款比例(%) | numeric | 23 | 10 | √ | 0 | 付款比例(%) |
| 27 | freimbursedamount | 已报销金额 | numeric | 23 | 10 | √ | 0 | 已报销金额 |
| 28 | fchangetaxamount | 累计变更税额 | numeric | 23 | 10 | √ | 0 | 累计变更税额 |
| 29 | fpushedcurramount | 已预付金额(本位币) | numeric | 23 | 10 | √ | 0 | 已预付金额(本位币) |
| 30 | fexptaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 31 | fexpebalanceamount | 可报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 可报销金额(本位币) |
| 32 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型(发票云) er_invoicetype |
| 33 | fentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 34 | fentryorichangeamount | 累计变更含税金额 | numeric | 23 | 10 | √ | 0 | 累计变更含税金额 |
| 35 | fexptaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 36 | fpaymenttypeid | 付款类型 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 37 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 38 | fchangeorientryamount | 累计变更不含税 | numeric | 23 | 10 | √ | 0 | 累计变更不含税 |
| 39 | fassetunit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 40 | freimbursedcurramount | 已报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 已报销金额(本位币) |
| 41 | fexpapplyamount | 含税金额 | numeric | 23 | 10 | √ | 0 | 含税金额 |
| 42 | fentryremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 43 | fentrychangeamount | 累计变更含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 累计变更含税金额(本位币) |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 46 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0 | 已预提金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_contractentry |  | fentryid |
| 2 | idx_er_contentry_seq |  | fid,fseq |

---

## 合同干系人-多选基础资料表 t_er_contractower

- **表名称：** 合同干系人-多选基础资料表
- **表名：** t_er_contractower

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
| 1 | idx_er_contower_seq |  | fid |
| 2 | pk_t_er_contractower |  | fpkid |

---

## 关联合同-子表 t_er_contractrelation

- **表名称：** 关联合同-子表
- **表名：** t_er_contractrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | 关联合同ID | int8 | 64 |  | √ | 0 | 关联合同ID |
| 3 | fsid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbillno | 关联合同单据编号 | varchar | 100 |  | √ | ' ' | 关联合同单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_contractrelation |  | fentryid |
| 2 | idx_er_contrelation_seq |  | fid |

---

## 付款计划-分表 t_er_contractentry_s

- **表名称：** 付款计划-分表
- **表名：** t_er_contractentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foriexpnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 3 | fexppayprogress | 付款进度(%) | numeric | 23 | 10 | √ | 0 | 付款进度(%) |
| 4 | fexppayedamount | 已付金额(本位币) | numeric | 23 | 10 | √ | 0 | 已付金额(本位币) |
| 5 | facexpeapprovecurramount | 变更后含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 变更后含税金额(本位币) |
| 6 | facorientryamount | 变更后不含税 | numeric | 23 | 10 | √ | 0 | 变更后不含税 |
| 7 | fexpnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0 | 未付金额(本位币) |
| 8 | facexpeapproveamount | 变更后含税金额 | numeric | 23 | 10 | √ | 0 | 变更后含税金额 |
| 9 | factaxamount | 变更后税额 | numeric | 23 | 10 | √ | 0 | 变更后税额 |
| 10 | fpayterms | 付款条件 | varchar | 255 |  | √ | ' ' | 付款条件 |
| 11 | foriexppayedamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fexpisoverpay | 超期待付 | bpchar | 1 |  | √ | '0' | 超期待付 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_contentry_s_seq |  | fid,fentryid |
| 2 | pk_t_er_contractentry_s |  | fentryid |

---

## 合同台账单-主表 t_er_contractbill

- **表名称：** 合同台账单-主表
- **表名：** t_er_contractbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fbilltaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 4 | forgid | 经办人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fpartother | 其他方 | varchar | 100 |  | √ | ' ' | 其他方 |
| 7 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fenddate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 10 | fapplierpositionstr | 经办人职位 | varchar | 100 |  | √ | ' ' | 经办人职位 |
| 11 | foriapplyamount | 合同总额(变更后) | numeric | 23 | 10 | √ | 0 | 合同总额(变更后) |
| 12 | fdetailtype | 单据类型 | varchar | 50 |  | √ | 'biztype_applybill' | 单据类型,枚举: biztype_applybill :合同台账 biztype_changebill :合同变更 biztype_stopbill :合同终止 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fversion | 版本号 | varchar | 100 |  | √ | ' ' | 版本号 |
| 15 | fcontracttype | 合同类型 | int8 | 64 |  | √ | 0 | 合同类型 conm_type |
| 16 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fstdbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 18 | fbilltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 19 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :执行中 J :冻结 G :已付款 H :废弃 I :关闭 |
| 20 | fcontractname | 合同名称 | varchar | 500 |  | √ | ' ' | 合同名称 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fdescription | 合同说明 | varchar | 1000 |  | √ | ' ' | 合同说明 |
| 23 | fapplyamount | 合同总额(变更后)本位币 | numeric | 23 | 10 | √ | 0 | 合同总额(变更后)本位币 |
| 24 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 25 | fstartdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 26 | frameworkcontract | 框架合同 | bpchar | 1 |  | √ | '0' | 框架合同 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fcontractcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fcontractcode | 合同号 | varchar | 500 |  | √ | ' ' | 合同号 |
| 31 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 32 | ftel | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |
| 33 | fisshared | 是否分摊 | bpchar | 1 |  | √ | '0' | 是否分摊 |
| 34 | fpaybyrata | 按比例（%） | varchar | 10 |  | √ | ' ' | 按比例（%） |
| 35 | fpartbnew | 乙方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 36 | fchangetype | 变更类型 | bpchar | 1 |  | √ | ' ' | 变更类型,枚举: A :变更金额 B :变更税率 C :补充明细 D :其他 |
| 37 | fparta | 甲方(old) | varchar | 100 |  | √ | ' ' | 业务单元 bos_org |
| 38 | fpartb | fpartb | varchar | 100 |  |  | ' ' |  |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 41 | fisimport | 是否导入 | bpchar | 1 |  | √ | '0' | 是否导入 |
| 42 | fcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 43 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_contractbill :费用合同单 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fiscurrency | 多币别 | varchar | 10 |  | √ | ' ' | 多币别 |
| 47 | fsignaddressdetail | 详细签约地址 | varchar | 255 |  | √ | ' ' | 详细签约地址 |
| 48 | fchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 49 | fprorataamount | 合同金额 | numeric | 23 | 10 | √ | 0 | 合同金额 |
| 50 | fapplierid | 经办人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 51 | fsrcsourceid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 52 | fsignaddress | 签约地址 | varchar | 50 |  | √ | ' ' | 签约地址 |
| 53 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 54 | fpartbtype | 乙方类型 | varchar | 50 |  | √ | ' ' | 乙方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司（行政组织） bos_org :公司 |
| 55 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | 业务分类 er_projecttype |
| 56 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 57 | fquotetype | 换算方式(单头) | bpchar | 1 |  | √ | ' ' | 换算方式(单头),枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_contract_fbsta |  | fbillstatus |
| 2 | pk_t_er_contractbill |  | fid |
| 3 | idx_er_contract_fbno |  | fbillno |
| 4 | idx_er_contract_fcompanyid |  | fcompanyid |

---

## 签约方分录-子表 t_er_contractparty

- **表名称：** 签约方分录-子表
- **表名：** t_er_contractparty

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontractparty | 签约方名称 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | fpartperson | 签约人 | varchar | 80 |  | √ | ' ' | 签约人 |
| 4 | ftaxcertificate | 纳税人资质 | varchar | 200 |  | √ | ' ' | 纳税人资质 |
| 5 | fpartytype | 签约方类型 | varchar | 50 |  | √ | ' ' | 签约方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司(行政组织) bos_org :公司 |
| 6 | fsigntel | 联系电话 | varchar | 255 |  | √ | ' ' | 联系电话 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcontactperson | 联系人 | varchar | 100 |  | √ | ' ' | 联系人 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fsigncontract | 签约方 | varchar | 50 |  |  | ' ' | 签约方,枚举: 0 :甲方 1 :乙方 2 :其他方 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_contractparty |  | fentryid |
| 2 | idx_er_contparty_seq |  | fid,fseq |

---

## 关联立项-子表 t_er_contractproject

- **表名称：** 关联立项-子表
- **表名：** t_er_contractproject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectwunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | foriprojectcanamount | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 4 | fprojectbillno | 立项号 | varchar | 50 |  | √ | ' ' | 立项号 |
| 5 | fsourceentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 6 | fprojectdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fprojectitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 9 | fprojectcurrency | 立项币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fprojectcanamount | 可用金额 （本位币） | numeric | 23 | 10 | √ | 0 | 可用金额 （本位币） |
| 11 | fprojectapplier | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fprojectname | 立项名称 | varchar | 50 |  | √ | ' ' | 立项名称 |
| 13 | fprojectwriteoffamount | 冲销金额（本位币） | numeric | 23 | 10 | √ | 0 | 冲销金额（本位币） |
| 14 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 15 | fprojectcostorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fprojectno | fprojectno | varchar | 50 |  | √ | ' ' |  |
| 17 | fprojectwtype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 |
| 18 | fprojectbizdate | fprojectbizdate | timestamp | 0 |  |  | null |  |
| 19 | fprojectquotetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 20 | fsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型,枚举: er_applyprojectbill :立项单 |
| 21 | fprojectchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fprojectdescription | 事由 | varchar | 500 |  | √ | ' ' | 事由 |
| 24 | foriprojectwriteoffamount | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_contractpro_fprojectno |  | fprojectno |
| 2 | pk_t_er_contractproject |  | fentryid |

---

## 关联子实体-子表 t_er_contractproject_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_contractproject_lk

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
| 1 | pk_t_er_contractproject_lk |  | fpkid |
| 2 | idx_er_contractproject_lk |  | fsbillid |

---

## 合同台账单-多语言表 t_er_contractbill_l

- **表名称：** 合同台账单-多语言表
- **表名：** t_er_contractbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapplierpositionstr | 经办人职位 | varchar | 100 |  | √ | ' ' | 经办人职位 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_contractbill_l_flcid |  | fid,flocaleid |
| 2 | pk_er_contractbill_l |  | fpkid |

---

## 合同台账单-分表 t_er_contractbill_s

- **表名称：** 合同台账单-分表
- **表名：** t_er_contractbill_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 3 | floanedamount | 已预付金额(本位币) | numeric | 23 | 10 | √ | 0 | 已预付金额(本位币) |
| 4 | fsigndate | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 5 | foriginalamount | 合同总额(不含税) | numeric | 23 | 10 | √ | 0 | 合同总额(不含税) |
| 6 | forinonpayamount | 在途待付金额 | numeric | 23 | 10 | √ | 0 | 在途待付金额 |
| 7 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 8 | fpayterms | fpayterms | varchar | 255 |  | √ | ' ' |  |
| 9 | fusedamount | 已报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 已报销金额(本位币) |
| 10 | foripayedamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 11 | fscmctype | 合同类型 | int8 | 64 |  | √ | 0 | 合同类型 conm_type |
| 12 | fsbilltype | 合同源单类型 | bpchar | 1 |  | √ | ' ' | 合同源单类型,枚举: 0 :手动新增 1 :采购合同 3 :项目云合同 4 :其他 |
| 13 | foribalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 14 | forinotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 15 | fchangeamount | 累计变更金额 | numeric | 23 | 10 | √ | 0 | 累计变更金额 |
| 16 | fabnormalpay | 付款异常 | bpchar | 1 |  | √ | '0' | 付款异常,枚举: 1 :是 0 :否 |
| 17 | fbeforefrozenstatu | 冻结前状态 | bpchar | 1 |  | √ | '0' | 冻结前状态,枚举: E :审合通过 F :执行中 |
| 18 | fwithholdingamount | 已预提金额(本位币) | numeric | 23 | 10 | √ | 0 | 已预提金额(本位币) |
| 19 | foricanloanamount | 可预付金额 | numeric | 23 | 10 | √ | 0 | 可预付金额 |
| 20 | fpartanew | 甲方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 21 | fnonpayamount | 在途待付金额(本位币) | numeric | 23 | 10 | √ | 0 | 在途待付金额(本位币) |
| 22 | foriwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0 | 已预提金额 |
| 23 | fcontractamount | 合同总额(初始) | numeric | 23 | 10 | √ | 0 | 合同总额(初始) |
| 24 | fisenableinvoice | 是否启用发票云 | bpchar | 1 |  | √ | '0' | 是否启用发票云 |
| 25 | foriavailableamount | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 26 | foriusedamount | 已报销金额 | numeric | 23 | 10 | √ | 0 | 已报销金额 |
| 27 | finvoiceamountremain | 未到票金额 | numeric | 23 | 10 | √ | 0 | 未到票金额 |
| 28 | favailableamount | 可用金额(本位币) | numeric | 23 | 10 | √ | 0 | 可用金额(本位币) |
| 29 | fisoverpay | 超期待付 | bpchar | 1 |  | √ | '0' | 超期待付 |
| 30 | fbillcanloanamount | 可预付金额(本位币) | numeric | 23 | 10 | √ | 0 | 可预付金额(本位币) |
| 31 | finvoiceamount | 已到票金额 | numeric | 23 | 10 | √ | 0 | 已到票金额 |
| 32 | fproratataxamount | 合同税额 | numeric | 23 | 10 | √ | 0 | 合同税额 |
| 33 | fnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0 | 未付金额(本位币) |
| 34 | fpartatypenew | 甲方类型 | varchar | 50 |  | √ | ' ' | 甲方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司（行政组织） bos_org :公司 |
| 35 | fpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已付金额（本位币） |
| 36 | fchangetimes | 变更次数 | int8 | 64 |  | √ | 0 | 变更次数 |
| 37 | foriloanedamount | 已预付金额 | numeric | 23 | 10 | √ | 0 | 已预付金额 |
| 38 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 39 | fbalanceamount | 可报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 可报销金额(本位币) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_contracts_fid |  | fsigndate |
| 2 | pk_t_er_contractbill_s |  | fid |

---

## 合同台账单-关联追踪表 t_er_contractbill_tc

- **表名称：** 合同台账单-关联追踪表
- **表名：** t_er_contractbill_tc

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
| 1 | pk_er_contractbill_tc |  | fid |
| 2 | idx_er_contractbill_tc_fsbld |  | fsbillid |
| 3 | idx_er_contractbill_tc_ftbld |  | ftbillid |
| 4 | idx_er_contractbill_tc_tbill |  | ftbillid |
| 5 | idx_er_contractbill_tc_tid |  | ftid |

---

## 合同台账单-反写记录表 t_er_contractbill_wb

- **表名称：** 合同台账单-反写记录表
- **表名：** t_er_contractbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
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
| 1 | idx_er_contractbill_wb_fid |  | fid |
| 2 | pk_er_contractbill_wb |  | fentryid |

---

## 关联子实体-子表 t_er_contractentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_contractentry_lk

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
| 1 | idx_er_contractentry_lk_fetid |  | fentryid |
| 2 | pk_er_contractentry_lk |  | fpkid |
