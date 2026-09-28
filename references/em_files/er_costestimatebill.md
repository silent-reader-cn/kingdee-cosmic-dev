# 暂估单-er_costestimatebill

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

## 分摊明细-子表 t_er_costestimaterule

- **表名称：** 分摊明细-子表
- **表名：** t_er_costestimaterule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 2 | fshareremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 5 | fstdentrycostcenterrule | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fshareamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |
| 11 | fentrycostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fshareappamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_csestimaterl_fseq |  | fentryid,fseq |
| 2 | pk_t_er_costestimaterule |  | fdetailid |

---

## 暂估单-反写记录表 t_er_costestimatebill_wb

- **表名称：** 暂估单-反写记录表
- **表名：** t_er_costestimatebill_wb

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
| 1 | pk_er_costestimatebill_wb |  | fentryid |
| 2 | idx_er_costest_wb_fid |  | fid |

---

## 关联子实体-子表 t_er_costestimateentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_costestimateentry_lk

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
| 1 | pk_er_costestimateentry_lk |  | fpkid |
| 2 | idx_er_costestet_lk_fetid |  | fentryid |

---

## 关联子实体-子表 t_er_costestimatecontract_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_costestimatecontract_lk

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
| 1 | idx_er_costestimatecontract_lk |  | fsbillid |
| 2 | pk_t_costestimatecontract_lk |  | fpkid |

---

## 暂估单-多语言表 t_er_costestimatebill_l

- **表名称：** 暂估单-多语言表
- **表名：** t_er_costestimatebill_l

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
| 1 | idx_er_costest_l_flcid |  | fid,flocaleid |
| 2 | pk_er_costestimatebill_l |  | fpkid |

---

## 项目干系人-多选基础资料表 t_er_costestimateower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_costestimateower

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
| 1 | pk_er_costestimateower |  | fpkid |
| 2 | idx_er_costestower_fid |  | fid |

---

## 关联子实体-子表 t_er_costestimatebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_costestimatebill_lk

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
| 1 | idx_er_costest_lk_fid |  | fid |
| 2 | pk_er_costestimatebill_lk |  | fpkid |

---

## 关联合同-子表 t_er_costestimatecontract

- **表名称：** 关联合同-子表
- **表名：** t_er_costestimatecontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontractcode | 合同号 | varchar | 500 |  | √ | ' ' | 合同号 |
| 3 | fcontractapplier | 经办人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcontractcurrreimamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已付金额（本位币） |
| 5 | fsourceentryid | fsourceentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fsigndate | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 7 | fcontractproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fcontractexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 10 | fcontractpartatypenew | 甲方类型 | varchar | 50 |  | √ | ' ' | 甲方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司(行政组织) bos_org :公司 |
| 11 | fcontractdescription | 合同说明 | varchar | 1000 |  | √ | ' ' | 合同说明 |
| 12 | fcontractexpquotetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 13 | fcontractcanamount | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 14 | fcontractsrcentryid | 关联合同分录id | int8 | 64 |  | √ | 0 | 关联合同分录id |
| 15 | fcontractpaytypeid | 付款类型 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 16 | fcontractpartbtype | 乙方类型 | varchar | 50 |  | √ | ' ' | 乙方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司(行政组织) bos_org :公司 |
| 17 | fentryprepayedamount | 已预付金额 | numeric | 23 | 10 | √ | 0 | 已预付金额 |
| 18 | fcontractsid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 19 | fcontractpartanew | 甲方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | fentryinvoiceamount | 到票金额 | numeric | 23 | 10 | √ | 0 | 到票金额 |
| 21 | fentrycurrprepayedamount | 已预付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已预付金额（本位币） |
| 22 | fcontractentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 23 | fcontractnotpayamount | 未付金额（本位币） | numeric | 23 | 10 | √ | 0 | 未付金额（本位币） |
| 24 | fcontractcostorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fcontractname | 合同名称 | varchar | 500 |  | √ | ' ' | 合同名称 |
| 26 | fcontracthappendate | 预计付款日期 | timestamp | 0 |  |  | null | 预计付款日期 |
| 27 | fcontractwriteoff | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 28 | fcontractpartb | 乙方 | varchar | 100 |  | √ | ' ' | 供应商 bd_supplier |
| 29 | fcontractnonpayamount | 待付金额（本位币） | numeric | 23 | 10 | √ | 0 | 待付金额（本位币） |
| 30 | fcontractparta | 甲方(old) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 32 | fcontractentrychangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 33 | fcontractcurrcanamount | 可报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 可报销金额(本位币) |
| 34 | fcontractcurrwriteoff | 冲销金额（本位币） | numeric | 23 | 10 | √ | 0 | 冲销金额（本位币） |
| 35 | fcontractreimamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_costestimatecontract |  | fentryid |
| 2 | idx_er_costestimate_fcode |  | fcontractcode |

---

## 暂估单-关联追踪表 t_er_costestimatebill_tc

- **表名称：** 暂估单-关联追踪表
- **表名：** t_er_costestimatebill_tc

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
| 1 | idx_er_costest_tc_fsbld |  | fsbillid |
| 2 | idx_er_costest_tc_ftbld |  | ftbillid |
| 3 | idx_er_costestimatebill_tc_tbill |  | ftbillid |
| 4 | idx_er_costestimatebill_tc_tid |  | ftid |
| 5 | pk_er_costestimatebill_tc |  | fid |

---

## 暂估明细-子表 t_er_costestimateentry

- **表名称：** 暂估明细-子表
- **表名：** t_er_costestimateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 3 | facprice | 变更后核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定不含税金额 |
| 4 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 6 | forgiexpebalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额 |
| 7 | fsourceentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fpushedamount | 已预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预付金额 |
| 10 | facexpeapproveamount | 变更后核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定金额 |
| 11 | fentrycontractname | 合同名称 | varchar | 500 |  | √ | ' ' | 合同名称 |
| 12 | faccurprice | 变更后核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定不含税金额（本位币） |
| 13 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 14 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额（本位币） |
| 15 | fsourcebillno | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |
| 16 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 17 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 18 | fcurrapplyamount | 申请金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(本位币) |
| 19 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 20 | fcanloancurramount | 可预付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 可预付金额(本位币) |
| 21 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: er_costestimatebill :费用暂估单 er_contractbill :合同台账 |
| 23 | fentryproducttype | 产品类别 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 24 | facexpeapprovecurramount | 变更后核定金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定金额(本位币) |
| 25 | fpushedcurramount | 已预付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已预付金额(本位币) |
| 26 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 27 | fexpeapprovecurramount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额(本位币) |
| 28 | fentryapplyprojectamount | 暂估金额 | numeric | 23 | 10 | √ | 0.0000000000 | 暂估金额 |
| 29 | fentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 30 | fentryremark | 说明 | varchar | 500 |  | √ | ' ' | 说明 |
| 31 | fentrychangeamount | 累计变更金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更金额(本位币) |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 34 | fentryprojectno | 立项号 | varchar | 200 |  | √ | ' ' | 立项号 |
| 35 | fentrywltype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 |
| 36 | fentrywlunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 37 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 38 | fcanloanamount | 可预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可预付金额 |
| 39 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 40 | fentrycostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fexpwithholdingamount | 已预提金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额(本位币) |
| 42 | fentrycontractno | 合同号 | varchar | 500 |  | √ | ' ' | 合同号 |
| 43 | fchangecurprice | 累计变更核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更核定不含税金额（本位币） |
| 44 | fitemfrom | 分录来源 | bpchar | 1 |  | √ | '0' | 分录来源,枚举: 0 :手工添加 5 :关联生成 |
| 45 | fentrychangeableamount | 可变更金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可变更金额 |
| 46 | freimbursedamount | 已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额 |
| 47 | facorientryamount | 变更后不含税 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后不含税 |
| 48 | fchangetaxamount | 累计变更税额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更税额 |
| 49 | fchangeprice | 累计变更核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更核定不含税金额 |
| 50 | factaxamount | 变更后税额 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后税额 |
| 51 | fexpebalanceamount | 可报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额(本位币) |
| 52 | fentryorichangeamount | 累计变更金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更金额 |
| 53 | fwbpaytype | 付款类型 | varchar | 100 |  | √ | ' ' | 付款类型,枚举: PREPAYMENT :预付款 PROGRESSPAYMENT :进度款 SETTLEPAYMENT :结算款 BOND :保证金 REWORDORPUNISH :奖惩 OTHERS :其它 |
| 54 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 55 | fchangeorientryamount | 累计变更不含税 | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更不含税 |
| 56 | freimbursedcurramount | 已报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额(本位币) |
| 57 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 58 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 59 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_costestentry_fseq |  | fid,fseq |
| 2 | pk_er_costestimateentry |  | fentryid |

---

## 摊销明细-子表 t_er_costestimateshared

- **表名称：** 摊销明细-子表
- **表名：** t_er_costestimateshared

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 3 | fentrywlunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 4 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 6 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 9 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 10 | freimburseamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 11 | fentrycostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 13 | fcurrreimburseamount | 申请金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(本位币) |
| 14 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额（本位币） |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |
| 17 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 18 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 19 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 21 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fentryproducttype | 产品类别 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 23 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 24 | fentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 25 | flkwaitentryid | 待摊明细id | varchar | 200 |  | √ | ' ' | 待摊明细id |
| 26 | fissharepush | 是否已生成分摊单 | bpchar | 1 |  | √ | '0' | 是否已生成分摊单 |
| 27 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 29 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 30 | fentrywltype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_costestimateshared |  | fdetailid |
| 2 | idx_er_csestimatesd_fseq |  | fid,fseq |

---

## 暂估单-主表 t_er_costestimatebill

- **表名称：** 暂估单-主表
- **表名：** t_er_costestimatebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fwltype | 单头往来类型 | varchar | 50 |  | √ | ' ' | 单头往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 4 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 5 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | floanedamount | 已预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预付金额 |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 9 | fisbeforeshare | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fprojectnamedesc | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 12 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 13 | fapplierpositionstr | 职位文本 | varchar | 100 |  | √ | ' ' | 职位文本 |
| 14 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | fisonway | 是否支持在途 | bpchar | 1 |  | √ | '0' | 是否支持在途 |
| 16 | fdetailtype | 暂估类型 | varchar | 50 |  | √ | 'biztype_applybill' | 暂估类型,枚举: biztype_applybill :费用暂估 biztype_changebill :暂估变更 biztype_sharebill :暂估分摊 biztype_applyassetbill :资产暂估 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 19 | fstdbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 20 | fischange | fischange | bpchar | 1 |  | √ | '0' |  |
| 21 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 H :废弃 I :关闭 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 25 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 26 | fisenableinvoice | 是否启用发票云 | bpchar | 1 |  | √ | '0' | 是否启用发票云 |
| 27 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 28 | fsharerule | 分摊规则 | varchar | 50 |  | √ | 'monthrule' | 分摊规则,枚举: monthrule :按月分摊 yearrule :按年分摊 orgrule :按部门分摊 |
| 29 | fbillcanloanamount | 可预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可预付金额 |
| 30 | frameworkcontract | 框架合同 | bpchar | 1 |  | √ | '1' | 框架合同 |
| 31 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 32 | fchangetimes | 变更次数 | int4 | 32 |  | √ | 0 | 变更次数 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 35 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fbalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额 |
| 37 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 38 | ftel | 联系方式 | varchar | 30 |  | √ | ' ' | 联系方式 |
| 39 | fisshared | 是否分摊 | bpchar | 1 |  | √ | '0' | 是否分摊 |
| 40 | fwlunit | 单头往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 41 | fchangetype | 变更类型 | bpchar | 1 |  | √ | '0' | 变更类型,枚举: A :不限 B :调增 C :调减 |
| 42 | frelatedbiz | 关联业务 | varchar | 30 |  | √ | 'biztype_other' | 关联业务,枚举: biztype_project :立项 biztype_contract :合同 biztype_other :无 |
| 43 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fusedamount | 已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额 |
| 45 | fisimport | 是否导入 | bpchar | 1 |  | √ | '0' | 是否导入 |
| 46 | fchangeamount | 累计变更金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更金额 |
| 47 | fcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 48 | fispush | 是否下推生成 | bpchar | 1 |  | √ | '0' | 是否下推生成 |
| 49 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_costestimatebill :费用暂估单 er_costestimatechgbill :费用暂估变更单 |
| 50 | frelationcontract | 关联合同参数 | bpchar | 1 |  | √ | '0' | 关联合同参数 |
| 51 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | ffiperiod | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 54 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 55 | facapproveamount | 变更后核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定金额 |
| 56 | fisrelatedproject | fisrelatedproject | bpchar | 1 |  | √ | '0' |  |
| 57 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 58 | fsharemethod | 分摊方法 | varchar | 50 |  | √ | 'rate' | 分摊方法,枚举: rate :比例分摊 avg :金额平均 amount :金额分摊 |
| 59 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 60 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | 业务分类 er_projecttype |
| 61 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 62 | fbilltype | fbilltype | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_costestimatebill |  | fid |
| 2 | idx_er_costest_fcompanyid |  | fcompanyid |
| 3 | idx_er_costest_fbno |  | fbillno |
| 4 | idx_er_costest_fcreateor |  | fcreatorid |
| 5 | idx_er_costest_fdate_no |  | fbizdate,fbillno |
| 6 | idx_er_costest_faper |  | fapplierid |
| 7 | idx_er_costest_fbsta |  | fbillstatus |
