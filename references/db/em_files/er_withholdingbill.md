# 费用预提单-er_withholdingbill

## 关联子实体-子表 t_er_withholdingentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_withholdingentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_withholdingentry_lk |  | fpkid |
| 2 | idx_er_wh_en_l_id |  | fseq,fentryid,fsbillid |

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

## 项目干系人-多选基础资料表 t_er_withholdingower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_withholdingower

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
| 1 | pk_er_withholdingower |  | fpkid |
| 2 | idx_er_withholdingower_fid |  | fid |

---

## 费用预提单-多语言表 t_er_withholdingbill_l

- **表名称：** 费用预提单-多语言表
- **表名：** t_er_withholdingbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapplierpositionstr | 职位文本 | varchar | 80 |  | √ | ' ' | 职位文本 |
| 3 | flocaleid | flocaleid | varchar | 80 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_wh_l_id |  | fid,flocaleid |
| 2 | pk_er_withholdingbill_l |  | fpkid |

---

## 费用预提单-主表 t_er_withholdingbill

- **表名称：** 费用预提单-主表
- **表名：** t_er_withholdingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 4 | fwltype | 单头往来类型 | varchar | 80 |  | √ | ' ' | 单头往来类型,枚举: bd_supplier :供应商 bd_customer :客户 |
| 5 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 6 | ftel | 联系方式 | varchar | 80 |  | √ | ' ' | 联系方式 |
| 7 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | floanedamount | 已废弃_已预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已废弃_已预付金额 |
| 9 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 11 | fwlunit | 单头往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 12 | fstd_costcenter | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fapplierpositionstr | 职位文本 | varchar | 80 |  | √ | ' ' | 职位文本 |
| 17 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 18 | fusedamount | 已冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已冲销金额 |
| 19 | fcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fformid | 表单ID | varchar | 80 |  | √ | ' ' | 表单ID,枚举: er_withholdingbill :预提单 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fstdbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 24 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 H :废弃 I :关闭 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | ffiperiod | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 27 | fwithholdingtype | 预提类型 | int8 | 64 |  | √ | 0 | 预提类型 er_withholdingtype |
| 28 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fdescription | 事由 | varchar | 500 |  | √ | ' ' | 事由 |
| 31 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 32 | fisenableinvoice | 是否启用发票云 | bpchar | 1 |  | √ | '0' | 是否启用发票云 |
| 33 | fiswriteoff | 是否冲销单 | bpchar | 1 |  | √ | '0' | 是否冲销单 |
| 34 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 36 | fbillcanloanamount | 已废弃_可预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已废弃_可预付金额 |
| 37 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 38 | fapproveamount | 核定总额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定总额 |
| 39 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | 业务分类 er_projecttype |
| 40 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fbilltype | fbilltype | int8 | 64 |  | √ | 0 |  |
| 43 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 44 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fbalanceamount | 冲销余额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_wh_billno |  | fbillno |
| 2 | pk_er_withholdingbill |  | fid |
| 3 | idx_er_wh_billstatus |  | fbillstatus |

---

## 费用预提单-关联追踪表 t_er_withholdingbill_tc

- **表名称：** 费用预提单-关联追踪表
- **表名：** t_er_withholdingbill_tc

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
| 1 | idx_er_withholdingbill_tc_tbill |  | ftbillid |
| 2 | idx_er_withholdingbill_tc_tid |  | ftid |
| 3 | idx_er_wh_tc_id |  | ftbillid |
| 4 | pk_er_withholdingbill_tc |  | fid |

---

## 费用预提单-反写记录表 t_er_withholdingbill_wb

- **表名称：** 费用预提单-反写记录表
- **表名：** t_er_withholdingbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 80 |  | √ | ' ' |  |
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
| 1 | idx_er_wh_wb_id |  | fid,fseq |
| 2 | pk_er_withholdingbill_wb |  | fentryid |

---

## 费用明细-子表 t_er_withholdingentry

- **表名称：** 费用明细-子表
- **表名：** t_er_withholdingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 3 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 4 | fentrywlunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 5 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 7 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 8 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 9 | ftripitem | 差旅项目 | int8 | 64 |  | √ | 0 | 差旅项目 er_tripexpenseitem |
| 10 | forgiexpebalanceamount | 冲销余额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销余额 |
| 11 | fsourceentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 12 | fentryfiaccount | 会计科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 13 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 14 | fpushedamount | 已废弃_已预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已废弃_已预付金额 |
| 15 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 16 | fcanloanamount | 已废弃_可预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已废弃_可预付金额 |
| 17 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 18 | fentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 19 | fisvactax | 专票 | bpchar | 1 |  | √ | '0' | 专票 |
| 20 | fentrycostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 22 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额（本位币） |
| 23 | fsourcebillno | 源单编码 | varchar | 80 |  | √ | ' ' | 源单编码 |
| 24 | fstd_entrycostcenter | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 25 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 26 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 27 | fcurrapplyamount | 申请金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(本位币) |
| 28 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 29 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 30 | fcanloancurramount | 已废弃_可预付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已废弃_可预付金额(本位币) |
| 31 | fsourcebilltype | 源单类型 | varchar | 80 |  | √ | ' ' | 源单类型,枚举: er_withholdingbill :费用预提 er_dailyreimbursebill :费用报销 er_tripreimbursebill :差旅报销 er_publicreimbursebill :对公报销 er_applyprojectbill :立项单 er_dailyapplybill :费用申请单 |
| 32 | fentryproducttype | 产品分类 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 33 | freimbursedamount | 已冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已冲销金额 |
| 34 | fpushedcurramount | 已废弃_已预付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已废弃_已预付金额(本位币) |
| 35 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 36 | fexpeapprovecurramount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额(本位币) |
| 37 | fexpebalanceamount | 冲销余额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 冲销余额(本位币) |
| 38 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 39 | freimbursedcurramount | 已冲销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已冲销金额(本位币) |
| 40 | fdesc | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 43 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 44 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 45 | fentrywltype | 往来类型 | varchar | 80 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_wh_en_comid |  | fentrycostcompanyid |
| 2 | pk_er_withholdingentry |  | fentryid |
| 3 | idx_er_wh_en_deptid |  | fentrycostdeptid |
| 4 | idx_er_wh_en_pid |  | fid |

---

## 关联子实体-子表 t_er_withholdingbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_withholdingbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_withholdingbill_lk |  | fpkid |
| 2 | idx_er_wh_lk_id |  | fid,fseq |
