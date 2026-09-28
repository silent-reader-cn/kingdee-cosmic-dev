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
| 3 | fwithholdingtaxrate | 预扣税率 | numeric | 23 | 10 | √ | 0 | 预扣税率 |
| 4 | fentrycurrency | 分录币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | forgiexpebalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 6 | fsourceentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 7 | fexppricewithtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fpushedamount | 已预付金额 | numeric | 23 | 10 | √ | 0 | 已预付金额 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 11 | fsourcebillno | 源单编号 | varchar | 100 |  | √ | ' ' | 源单编号 |
| 12 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 13 | fcurrapplyamount | 含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 含税金额(本位币) |
| 14 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 15 | fcanloancurramount | 可预付金额(本位币) | numeric | 23 | 10 | √ | 0 | 可预付金额(本位币) |
| 16 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: er_contractbill :费用合同单 |
| 17 | fentryproducttype | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 18 | fpaypercent | 付款比例(%) | numeric | 23 | 10 | √ | 0 | 付款比例(%) |
| 19 | fpushedcurramount | 已预付金额(本位币) | numeric | 23 | 10 | √ | 0 | 已预付金额(本位币) |
| 20 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 21 | fentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 22 | fexptaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 23 | fexpapplyamount | 含税金额 | numeric | 23 | 10 | √ | 0 | 含税金额 |
| 24 | fentryremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 25 | fentrychangeamount | 累计变更含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 累计变更含税金额(本位币) |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0 | 已预提金额 |
| 28 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 29 | fcanloanamount | 可预付金额 | numeric | 23 | 10 | √ | 0 | 可预付金额 |
| 30 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fcurwithholdingtaxamount | 预扣税额（本位币） | numeric | 23 | 10 | √ | 0 | 预扣税额（本位币） |
| 32 | fnum | 数量 | int4 | 32 |  | √ | 0 | 数量 |
| 33 | fexpquotetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 34 | fexpwithholdingamount | 已预提金额(本位币) | numeric | 23 | 10 | √ | 0 | 已预提金额(本位币) |
| 35 | fitemfrom | 分录来源 | bpchar | 1 |  | √ | '0' | 分录来源,枚举: 0 :手工添加 1 :关联生成 |
| 36 | fentrycontractamount | 原合同金额 | numeric | 23 | 10 | √ | 0 | 原合同金额 |
| 37 | fentrychangeableamount | 合同可变更金额 | numeric | 23 | 10 | √ | 0 | 合同可变更金额 |
| 38 | freimbursedamount | 已报销金额 | numeric | 23 | 10 | √ | 0 | 已报销金额 |
| 39 | fchangetaxamount | 累计变更税额 | numeric | 23 | 10 | √ | 0 | 累计变更税额 |
| 40 | fexptaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 41 | fexpebalanceamount | 可报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 可报销金额(本位币) |
| 42 | fentryorichangeamount | 累计变更含税金额 | numeric | 23 | 10 | √ | 0 | 累计变更含税金额 |
| 43 | fwithholdingtaxamount | 预扣税额 | numeric | 23 | 10 | √ | 0 | 预扣税额 |
| 44 | fpaymenttypeid | 付款类型 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 45 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 46 | fchangeorientryamount | 累计变更不含税 | numeric | 23 | 10 | √ | 0 | 累计变更不含税 |
| 47 | fassetunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 48 | freimbursedcurramount | 已报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 已报销金额(本位币) |
| 49 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_contractentry |  | fentryid |
| 2 | idx_er_contentry_seq |  | fid,fseq |
| 3 | idx_er_contentry_fsrcbillid |  | fsourcebillid |

---

## 合同干系人-多选基础资料表 t_er_contractower

- **表名称：** 合同干系人-多选基础资料表
- **表名：** t_er_contractower

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
| 6 | fbillno | 关联合同单据编号 | varchar | 500 |  | √ | ' ' | 关联合同单据编号 |

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
| 11 | forientrycontracttax | 原合同税额 | numeric | 23 | 10 | √ | 0 | 原合同税额 |
| 12 | foriexppayedamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fexpisoverpay | 超期待付 | bpchar | 1 |  | √ | '0' | 超期待付 |

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
| 4 | forgid | 经办人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fpartother | 其他方 | varchar | 1000 |  | √ | ' ' | 其他方 |
| 7 | fhasvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fenddate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 10 | fapplierpositionstr | 经办人职位 | varchar | 100 |  | √ | ' ' | 经办人职位 |
| 11 | fneeduploadinvoice | 有待上传的纸票/附件 | bpchar | 1 |  | √ | '0' | 有待上传的纸票/附件 |
| 12 | foriapplyamount | 合同总额(变更后) | numeric | 23 | 10 | √ | 0 | 合同总额(变更后) |
| 13 | fdetailtype | 单据类型 | varchar | 50 |  | √ | 'biztype_applybill' | 单据类型,枚举: biztype_applybill :合同台账 biztype_changebill :合同变更 biztype_stopbill :合同终止 |
| 14 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fversion | 版本号 | varchar | 100 |  | √ | ' ' | 版本号 |
| 17 | fcontracttype | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 18 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 19 | fstdbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 20 | fbilltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 21 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :执行中 J :冻结 G :已付款 H :废弃 I :关闭 |
| 22 | fcontractname | 合同名称 | varchar | 500 |  | √ | ' ' | 合同名称 |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | fdescription | 合同说明 | varchar | 1000 |  | √ | ' ' | 合同说明 |
| 25 | fapplyamount | 合同总额(变更后)本位币 | numeric | 23 | 10 | √ | 0 | 合同总额(变更后)本位币 |
| 26 | fimagenumber | 影像编码 | varchar | 80 |  | √ | ' ' | 影像编码 |
| 27 | fstartdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 28 | frameworkcontract | 框架合同 | bpchar | 1 |  | √ | '0' | 框架合同 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fcontractcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fcontractcode | 合同号 | varchar | 500 |  | √ | ' ' | 合同号 |
| 33 | fisoverbudget | 超预算 | bpchar | 1 |  | √ | '0' | 超预算 |
| 34 | ftel | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |
| 35 | fisshared | 分摊 | bpchar | 1 |  | √ | '0' | 分摊 |
| 36 | fpaybyrata | 按比例（%） | varchar | 10 |  | √ | ' ' | 按比例（%） |
| 37 | fpartbnew | 乙方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 38 | fchangetype | 变更类型 | bpchar | 1 |  | √ | ' ' | 变更类型,枚举: A :变更金额 B :变更税率 C :补充明细 D :其他 |
| 39 | fparta | 甲方(old) | varchar | 100 |  | √ | ' ' | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fpartb | fpartb | varchar | 100 |  |  | ' ' |  |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 43 | fisimport | 导入 | bpchar | 1 |  | √ | '0' | 导入 |
| 44 | fcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_contractbill :费用合同单 |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | fiscurrency | 多币种 | varchar | 10 |  | √ | ' ' | 多币种 |
| 49 | fpartbnews | 乙方(多方) | varchar | 1000 |  | √ | ' ' | 乙方(多方) |
| 50 | fsignaddressdetail | 详细签约地址 | varchar | 255 |  | √ | ' ' | 详细签约地址 |
| 51 | fchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 52 | fprorataamount | 合同金额 | numeric | 23 | 10 | √ | 0 | 合同金额 |
| 53 | fapplierid | 经办人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fsrcsourceid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 55 | fpartanews | 甲方(多方) | varchar | 1000 |  | √ | ' ' | 甲方(多方) |
| 56 | fsignaddress | 签约地址 | varchar | 50 |  | √ | ' ' | 签约地址 |
| 57 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 58 | fpartbtype | 乙方类型 | varchar | 50 |  | √ | ' ' | 乙方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司（行政组织） bos_org :公司 cas_othercontactunit :其他往来单位 |
| 59 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | [业务分类 er_projecttype](../em_files/er_projecttype.md) |
| 60 | fcurrencyid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 61 | fquotetype | 换算方式(单头) | bpchar | 1 |  | √ | ' ' | 换算方式(单头),枚举: 0 :直接汇率 1 :间接汇率 |

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
| 4 | fpartentryfrom | 分录来源 | varchar | 20 |  | √ | '0' | 分录来源,枚举: botp :关联生成 addnew :手动新增 |
| 5 | ftaxcertificate | 纳税人资质 | varchar | 200 |  | √ | ' ' | 纳税人资质 |
| 6 | fpartytype | 签约方类型 | varchar | 50 |  | √ | ' ' | 签约方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司(行政组织) bos_org :公司 cas_othercontactunit :其他往来单位 |
| 7 | fsrcpartcentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 8 | fsigntel | 联系电话 | varchar | 255 |  | √ | ' ' | 联系电话 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fcontactperson | 联系人 | varchar | 100 |  | √ | ' ' | 联系人 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fsigncontract | 签约方 | varchar | 50 |  |  | ' ' | 签约方,枚举: 0 :甲方 1 :乙方 2 :其他方 |

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
| 2 | foriprojectcanamount | 可用合同金额 | numeric | 23 | 10 | √ | 0 | 可用合同金额 |
| 3 | fprojectbillno | 立项号 | varchar | 50 |  | √ | ' ' | 立项号 |
| 4 | fsourceentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fprojectitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 7 | fprojectcanamount | 可用合同金额本位币 | numeric | 23 | 10 | √ | 0 | 可用合同金额本位币 |
| 8 | fprojectapplier | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fprojectwriteoffamount | 冲销金额（本位币） | numeric | 23 | 10 | √ | 0 | 冲销金额（本位币） |
| 10 | fprojectcostorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fprojectno | fprojectno | varchar | 50 |  | √ | ' ' |  |
| 12 | fprojectwtype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 13 | fprojectbizdate | fprojectbizdate | timestamp | 0 |  |  | null |  |
| 14 | fprojectchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 15 | foriprojectwriteoffamount | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 16 | fprojectwunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 17 | fprojectbillcanamount | 整单可用金额本位币 | numeric | 23 | 10 | √ | 0 | 整单可用金额本位币 |
| 18 | fprojectdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 19 | fprojectcurrency | 立项币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fprojectname | 立项名称 | varchar | 50 |  | √ | ' ' | 立项名称 |
| 21 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 22 | fprojectquotetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 23 | fsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型,枚举: er_applyprojectbill :立项单 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fprojectdescription | 事由 | varchar | 500 |  | √ | ' ' | 事由 |

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
| 3 | fpartanews | 甲方(多方) | varchar | 1000 |  | √ | ' ' | 甲方(多方) |
| 4 | fpartbnews | 乙方(多方) | varchar | 1000 |  | √ | ' ' | 乙方(多方) |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

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
| 2 | finvokeinvoicecloud | 与发票云交互 | bpchar | 1 |  | √ | '0' | 与发票云交互 |
| 3 | floanedamount | 已预付金额(本位币) | numeric | 23 | 10 | √ | 0 | 已预付金额(本位币) |
| 4 | fsigndate | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 5 | foriginalamount | 合同总额(不含税) | numeric | 23 | 10 | √ | 0 | 合同总额(不含税) |
| 6 | forinonpayamount | 在途待付金额 | numeric | 23 | 10 | √ | 0 | 在途待付金额 |
| 7 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 8 | ftotalcurwhtaxamount | 预扣税合计（费用） | numeric | 23 | 10 | √ | 0 | 预扣税合计（费用） |
| 9 | ftotalwhtaxamount | 预扣税原币合计（费用） | numeric | 23 | 10 | √ | 0 | 预扣税原币合计（费用） |
| 10 | fpayterms | fpayterms | varchar | 255 |  | √ | ' ' |  |
| 11 | fusedamount | 已报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 已报销金额(本位币) |
| 12 | foripayedamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 13 | fscmctype | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 14 | fsbilltype | 合同源单类型 | bpchar | 1 |  | √ | ' ' | 合同源单类型,枚举: 0 :手动新增 1 :采购合同 3 :项目云合同 4 :其他 |
| 15 | foribalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 16 | forinotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 17 | fchangeamount | 累计变更金额 | numeric | 23 | 10 | √ | 0 | 累计变更金额 |
| 18 | fabnormalpay | 付款异常 | bpchar | 1 |  | √ | '0' | 付款异常,枚举: 1 :是 0 :否 |
| 19 | fbeforefrozenstatu | 冻结前状态 | bpchar | 1 |  | √ | '0' | 冻结前状态,枚举: E :审合通过 F :执行中 |
| 20 | fwithholdingamount | 已预提金额(本位币) | numeric | 23 | 10 | √ | 0 | 已预提金额(本位币) |
| 21 | foricanloanamount | 可预付金额 | numeric | 23 | 10 | √ | 0 | 可预付金额 |
| 22 | fpartanew | 甲方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 23 | fcostimateamount | 暂估金额(本位币) | numeric | 23 | 10 | √ | 0 | 暂估金额(本位币) |
| 24 | fnonpayamount | 在途待付金额(本位币) | numeric | 23 | 10 | √ | 0 | 在途待付金额(本位币) |
| 25 | foriwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0 | 已预提金额 |
| 26 | fcontractamount | 合同总额(初始) | numeric | 23 | 10 | √ | 0 | 合同总额(初始) |
| 27 | fisenableinvoice | 启用发票云 | bpchar | 1 |  | √ | '0' | 启用发票云 |
| 28 | foriavailableamount | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 29 | foriusedamount | 已报销金额 | numeric | 23 | 10 | √ | 0 | 已报销金额 |
| 30 | finvoiceamountremain | 未到票金额 | numeric | 23 | 10 | √ | 0 | 未到票金额 |
| 31 | favailableamount | 可用金额(本位币) | numeric | 23 | 10 | √ | 0 | 可用金额(本位币) |
| 32 | fisoverpay | 超期待付 | bpchar | 1 |  | √ | '0' | 超期待付 |
| 33 | fbillcanloanamount | 可预付金额(本位币) | numeric | 23 | 10 | √ | 0 | 可预付金额(本位币) |
| 34 | finvoiceamount | 已到票金额 | numeric | 23 | 10 | √ | 0 | 已到票金额 |
| 35 | fproratataxamount | 合同税额 | numeric | 23 | 10 | √ | 0 | 合同税额 |
| 36 | fnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0 | 未付金额(本位币) |
| 37 | fpartatypenew | 甲方类型 | varchar | 50 |  | √ | ' ' | 甲方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司（行政组织） bos_org :公司 cas_othercontactunit :其他往来单位 |
| 38 | fpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已付金额（本位币） |
| 39 | fchangetimes | 变更次数 | int8 | 64 |  | √ | 0 | 变更次数 |
| 40 | foriloanedamount | 已预付金额 | numeric | 23 | 10 | √ | 0 | 已预付金额 |
| 41 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 42 | fbalanceamount | 可报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 可报销金额(本位币) |

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
