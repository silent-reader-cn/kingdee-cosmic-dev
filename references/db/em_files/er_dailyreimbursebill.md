# 费用报销单-er_dailyreimbursebill

## 发票合并信息-子表 t_er_invoicemerge

- **表名称：** 发票合并信息-子表
- **表名：** t_er_invoicemerge

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkeyserialno | 发票标识序列号 | varchar | 80 |  | √ | ' ' | 发票标识序列号 |
| 3 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoicemerge_fkeyse |  | fkeyserialno |
| 2 | t_er_invoicemerge_pkey |  | fentryid |

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

## 冲申请-子表 t_er_writeoffapply

- **表名称：** 冲申请-子表
- **表名：** t_er_writeoffapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapplyproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 3 | fexpenseitemfield | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 4 | forgfield | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fapplycostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | forgiexpebalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额 |
| 7 | freimbursedamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fstd_applycostcenter | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 10 | fapplyperson | 申请人 | varchar | 200 |  | √ | ' ' | 申请人 |
| 11 | fdatefield | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 12 | fapplycostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fexpebalanceamount | 可报销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额（本位币） |
| 14 | fapplybilldate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 15 | fapplycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 16 | fsourcesign | 来源标识 | bpchar | 1 |  | √ | '0' | 来源标识 |
| 17 | fsourceapplybillid | 源单ID | varchar | 100 |  | √ | ' ' | 源单ID |
| 18 | fapplybillno | 申请单号 | varchar | 100 |  | √ | '0' | 申请单号 |
| 19 | fsourceapplyentryid | 申请明细分录ID | int8 | 64 |  | √ | 0 | 申请明细分录ID |
| 20 | fapplydescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 21 | freimbursedcurramount | 冲销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额（本位币） |
| 22 | fapplyexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fquotetype | 换算方式（冲申请） | bpchar | 1 |  | √ | '0' | 换算方式（冲申请）,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_writeoffapply_pkey |  | fentryid |
| 2 | idx_er_writeoffapply_fid |  | fid |

---

## 费用报销单-反写记录表 t_er_dailyreimbursebill_wb

- **表名称：** 费用报销单-反写记录表
- **表名：** t_er_dailyreimbursebill_wb

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
| 1 | idx_er_dyreim_wb_fid |  | fid |
| 2 | t_er_dailyreimbursebill_wb_pkey |  | fentryid |

---

## 冲借款-子表 t_er_writeoffdetail

- **表名称：** 冲借款-子表
- **表名：** t_er_writeoffdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floanperson | 借款人 | varchar | 200 |  | √ | ' ' | 借款人 |
| 3 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | floanbill | floanbill | int8 | 64 |  | √ | 0 |  |
| 5 | floanbillnov1 | 借款单号 | varchar | 100 |  | √ | '0' | 借款单号 |
| 6 | fsourceentryid | 借款明细分录ID | int8 | 64 |  | √ | 0 | 借款明细分录ID |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcurrloanamount | 借款余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额（本位币） |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | faccloanamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 11 | fcurraccloanamount | 冲销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额(本位币) |
| 12 | floanamount | 借款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额 |
| 13 | floanexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 14 | floancurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 15 | floanapplydatev1 | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 16 | fsourcesign | 是否关联申请 | bpchar | 1 |  | √ | '0' | 是否关联申请 |
| 17 | fsourcebillid | 源单id | varchar | 100 |  | √ | ' ' | 源单id |
| 18 | fsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型,枚举: er_dailyloanbill :借款单 er_tripreqbill :出差借款单 |
| 19 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | floandescriptionv1 | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fquotetype | 换算方式（冲借款） | bpchar | 1 |  | √ | '0' | 换算方式（冲借款）,枚举: 0 :直接汇率 1 :间接汇率 |
| 23 | fsourceexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_writeoffdetail_pkey |  | fentryid |
| 2 | idx_er_writeoffdetail_fid |  | fid |

---

## 摊销明细-子表 t_er_dailyresharedetail

- **表名称：** 摊销明细-子表
- **表名：** t_er_dailyresharedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 3 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 5 | fsdentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 6 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 7 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 10 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '1' | 是否抵扣 |
| 11 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 12 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 13 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 15 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
| 16 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | '1' | 专票 |
| 17 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 18 | fcurprice | 核定不含税金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额本位币 |
| 19 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | '0' | 发票类型,枚举: 0 :空 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 |
| 20 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 21 | ftaxclasscodeid | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 22 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 23 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |
| 24 | fitemfrom | 来源 | varchar | 2 |  | √ | '0' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 4 :分录导入 |
| 25 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 26 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 27 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 28 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 29 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 30 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 31 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 32 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 33 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 34 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 35 | flkwaitentryid | 待摊明细id | varchar | 200 |  | √ | ' ' | 待摊明细id |
| 36 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 37 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 38 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 40 | fsdentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_dailyresharedetail |  | fdetailid |
| 2 | idx_er_dailyresharedetail_fseq |  | fid,fseq |

---

## 关联子实体-子表 t_er_writeoffdetail_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_writeoffdetail_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | faccloanamount_old | faccloanamount_old | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | faccloanamount | faccloanamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_writeoffdetail_lk_pkey |  | fpkid |
| 2 | idx_er_writeoffdetail_lk_fid |  | fentryid |

---

## 关联子实体-子表 t_er_expensedetail_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_expensedetail_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_expensedetail_lk |  | fpkid |
| 2 | idx_er_expensedetail_lk_fdid |  | fdetailid |

---

## 收款信息-子表 t_er_accountinfo

- **表名称：** 收款信息-子表
- **表名：** t_er_accountinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwriteoffamount | fwriteoffamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | faccountcurrency | 币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fbuildedamount | 已出单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已出单金额 |
| 5 | foriamount | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 6 | forgirepaidamount | forgirepaidamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fpayeraccount01 | 银行账号4位 | varchar | 100 |  | √ | ' ' | 银行账号4位 |
| 8 | fentrystatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: F :等待付款 G :已付款 I :关闭 E :审核通过 |
| 9 | fpayerdeptid | fpayerdeptid | int8 | 64 |  | √ | 0 |  |
| 10 | fpayercompid | fpayercompid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 |
| 12 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 13 | forgiapplyedreimamount | forgiapplyedreimamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | forgiwriteoffamount | forgiwriteoffamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | famount | 收款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额（本位币） |
| 16 | foriaccnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 17 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 18 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 19 | fsupplier | fsupplier | int8 | 64 |  | √ | 0 |  |
| 20 | fentryrepaydate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |
| 21 | fpayeraccountname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 22 | fpayerid | 收款人(个人) | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 23 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额（本位币） |
| 24 | fapplyedreimamount | fapplyedreimamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | facccostcompany | 付款公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fcustomer | fcustomer | int8 | 64 |  | √ | 0 |  |
| 27 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 28 | frepaidamount | frepaidamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 30 | foriaccpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 31 | foriaccbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额 |
| 32 | faccpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额（本位币） |
| 33 | fcasorg | fcasorg | int8 | 64 |  | √ | 0 |  |
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

## 关联子实体-子表 t_er_dailyreimbursebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_dailyreimbursebill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_dreimbursebill_lk_fid |  | fid |
| 2 | pk_t_er_dailyreimbursebill_lk |  | fpkid |

---

## 关联子实体-子表 t_er_writeoffapply_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_writeoffapply_lk

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
| 1 | t_er_writeoffapply_lk_pkey |  | fpkid |
| 2 | idx_er_writeoffapply_lk_fid |  | fentryid |

---

## 分摊明细-子表 t_er_dailyresharerule

- **表名称：** 分摊明细-子表
- **表名：** t_er_dailyresharerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 3 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 4 | fsharecurrency | 分摊币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 7 | fstdentrycostcenterrule | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 8 | fsharewaitseq | 待摊行号 | int4 | 32 |  | √ | 0 | 待摊行号 |
| 9 | fshareamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |
| 10 | fentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 11 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fshareappamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 13 | fentryexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 14 | fsharewaitid | 待摊明细id | int8 | 64 |  | √ | 0 | 待摊明细id |
| 15 | fshareremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_dailyresharerule_fseq |  | fid,fseq |
| 2 | pk_t_er_dailyresharerule |  | fdetailid |

---

## 费用报销单-主表 t_er_dailyreimbursebill

- **表名称：** 费用报销单-主表
- **表名：** t_er_dailyreimbursebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fpaycompanyid | 支付公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 5 | fnoinvoice | 无票 | bpchar | 1 |  | √ | '0' | 无票 |
| 6 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 9 | fhead_paydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 10 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 13 | forigin | 来源 | varchar | 10 |  | √ | ' ' | 来源,枚举: 1 :WEB 2 :移动端 3 :语音助手 |
| 14 | fapplierpositionstr | 职位文本 | varchar | 100 |  | √ | ' ' | 职位文本 |
| 15 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 16 | fisover | 是否超标（提交后有值） | bpchar | 1 |  | √ | '0' | 是否超标（提交后有值） |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fbilltypefield | fbilltypefield | int8 | 64 |  | √ | 0 |  |
| 19 | foffsetinvoiceno | 可抵扣发票号码 | varchar | 255 |  |  | null | 可抵扣发票号码 |
| 20 | fsourcebilltype | 源单类型(已废弃) | varchar | 30 |  | √ | ' ' | 源单类型(已废弃) |
| 21 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 22 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 23 | finvoiceoffsetamount | 抵扣税额汇总（发票信息） | numeric | 23 | 10 | √ | 0 | 抵扣税额汇总（发票信息） |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 26 | fautomapinvoice | 智能发票报销 | bpchar | 1 |  | √ | '1' | 智能发票报销 |
| 27 | foffsetamount | 抵扣税额合计 | numeric | 23 | 10 |  | null | 抵扣税额合计 |
| 28 | fimagenumber | 影像编号 | varchar | 255 |  | √ | ' ' | 影像编号 |
| 29 | fattachmentacount | fattachmentacount | int8 | 64 |  | √ | 0 |  |
| 30 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 31 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 32 | fpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 33 | fnextauditor | 下一步审核人 | varchar | 100 |  | √ | ' ' | 下一步审核人 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fbalanceamount | 借款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额 |
| 37 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 38 | ftel | 联系方式 | varchar | 100 |  | √ | ' ' | 联系方式 |
| 39 | fisshared | 是否已分摊 | bpchar | 1 |  | √ | '0' | 是否已分摊 |
| 40 | fredoffsetdes | 红冲说明 | varchar | 1000 |  | √ | ' ' | 红冲说明 |
| 41 | fpayamount | 付现 | numeric | 23 | 10 | √ | 0.0000000000 | 付现 |
| 42 | fprojectsharecount | 下游项目成本分摊单数 | int8 | 64 |  | √ | 0 | 下游项目成本分摊单数 |
| 43 | fcashier | 出纳员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fneedsuppleinvoice | 发票后补 | bpchar | 1 |  | √ | '0' | 发票后补 |
| 46 | fsharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额 |
| 47 | fspecialbill | 专项报销单类型 | varchar | 30 |  | √ | ' ' | 专项报销单类型,枚举: A :额度报销单 B :移动话费报销单 |
| 48 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 49 | fpaycurrency | 付现金额币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 50 | fisredoffset | 红冲 | bpchar | 1 |  | √ | '0' | 红冲 |
| 51 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_loanbill :出差借款单 er_tripreimbursebill :差旅费报销单 er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_dailyreimbursebill :费用报销单 er_repaymentbill :还款单 er_publicreimbursebill :对公报销单 |
| 52 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 53 | fis_all_einvoice | 发票状态 | bpchar | 1 |  | √ | '0' | 发票状态,枚举: 0 :无发票 1 :全电票 2 :含纸票 3 :其它 |
| 54 | freimbursecontrolcomany | 额度控制公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 55 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 56 | fismultireimburser | 多报销人 | bpchar | 1 |  | √ | ' ' | 多报销人 |
| 57 | fproxytax | 代扣代缴 | bpchar | 1 |  | √ | '0' | 代扣代缴 |
| 58 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 59 | fisinvoicemodified | 发票修改 | bpchar | 1 |  | √ | '0' | 发票修改 |
| 60 | freimbursetype | 报账类型 | varchar | 30 |  | √ | ' ' | 报账类型,枚举: expense :费用报账 entertainment :招待费 meetting :会议费 otherexpenses :其他 |
| 61 | fauditopinion | 审核意见 | varchar | 100 |  | √ | ' ' | 审核意见 |
| 62 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 63 | fispaybyhead | 按单头付款 | bpchar | 1 |  | √ | '0' | 按单头付款 |
| 64 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 65 | ftotalaccloanamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 66 | ftarbillstatus | 目标单据 | varchar | 30 |  | √ | '0' | 目标单据,枚举: B1 :项目成本分摊单 |
| 67 | freimbursecurrency | 报销金额币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 68 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_dreim_fbizdate_fbillno |  | fbizdate,fbillno |
| 2 | idx_er_dreim_fapplierid |  | fapplierid |
| 3 | idx_er_dreim_fcreatorid |  | fcreatorid |
| 4 | idx_er_dreim_fbillstatus |  | fbillstatus |
| 5 | t_er_dailyreimbursebill_pkey |  | fid |
| 6 | idx_er_dreim_fbillno |  | fbillno |
| 7 | idx_er_dreim_fcompanyid |  | fcompanyid |

---

## 费用报销单-关联追踪表 t_er_dailyreimbursebill_tc

- **表名称：** 费用报销单-关联追踪表
- **表名：** t_er_dailyreimbursebill_tc

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
| 1 | idx_er_dyreimbill_tc_ftbillid |  | ftbillid |
| 2 | idx_er_dailyreimbursebill_tc_tbill |  | ftbillid |
| 3 | idx_er_dailyreimbursebill_tc_tid |  | ftid |
| 4 | t_er_dailyreimbursebill_tc_pkey |  | fid |

---

## 项目干系人-多选基础资料表 t_er_dailyreimburseower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_dailyreimburseower

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
| 1 | idx_er_dailyreimburseower_fid |  | fid |
| 2 | pk_t_er_dailyreimburseower |  | fpkid |

---

## 费用明细-子表 t_er_expensedetail

- **表名称：** 费用明细-子表
- **表名：** t_er_expensedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexporiusedamount | fexporiusedamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 4 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 5 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 7 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 8 | fgoodsnum | 酒水瓶数 | int4 | 32 |  | √ | 0 | 酒水瓶数 |
| 9 | fiscreateprojectcostshare | 生成项目分摊单 | int8 | 64 |  | √ | 0 | 生成项目分摊单 |
| 10 | forgiexpebalanceamount | forgiexpebalanceamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | fpushedamount | fpushedamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '1' | 是否抵扣 |
| 14 | fproxyamt | 代扣代缴个税 | numeric | 23 | 10 | √ | 0.0000000000 | 代扣代缴个税 |
| 15 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 16 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 17 | fotherfeeamount | 酒水金额 | numeric | 23 | 10 | √ | 0 | 酒水金额 |
| 18 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 19 | fwbsrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: er_expense_recordbill :费用记录 er_trip_recordbill :差旅记录 er_vehiclecheckingbill :用车结算单 er_mealcheckingbill :用餐结算单 |
| 20 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
| 21 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | '1' | 专票 |
| 22 | fisover | 超费用标准 | bpchar | 1 |  | √ | '0' | 超费用标准 |
| 23 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额（本位币） |
| 24 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | '0' | 发票类型,枚举: 0 :空 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :酒店账单 |
| 25 | finvoicefromparent | 发票来源父节点 | bpchar | 1 |  | √ | '0' | 发票来源父节点 |
| 26 | fwbsrcentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 27 | fotherstandamount | 酒水标准金额(页面不可见) | numeric | 23 | 10 | √ | 0 | 酒水标准金额(页面不可见) |
| 28 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 29 | ftaxclasscodeid | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 30 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 31 | foverdesc | 超标说明(暂未支持) | varchar | 255 |  | √ | ' ' | 超标说明(暂未支持) |
| 32 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 33 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 34 | fexpehasreimamount | fexpehasreimamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 35 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 36 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 37 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 38 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 39 | fdaysnum | 住宿天数 | int4 | 32 |  | √ | 0 | 住宿天数 |
| 40 | fexpeorirepayamount | fexpeorirepayamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 41 | fmeetitem | 会议事项 | varchar | 10 |  | √ | ' ' | 会议事项,枚举: 1 :伙食费 2 :酒店住宿 3 :交通费 4 :其他 |
| 42 | freimburser | 报销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | ftreatnum | 招待人数 | int4 | 32 |  | √ | 0 | 招待人数 |
| 44 | fcontrolamt | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 45 | fwbsrcbillno | 源单编码 | varchar | 50 |  | √ | ' ' | 源单编码 |
| 46 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 47 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 48 | fexperepayamount | fexperepayamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 49 | ffeestandid | 费用标准基础资料 | int8 | 64 |  | √ | 0 | 费用标准 er_standard |
| 50 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 51 | ffeestandardamt | 费用标准金额(页面不可见) | numeric | 23 | 10 | √ | 0 | 费用标准金额(页面不可见) |
| 52 | fexpusedamount | fexpusedamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 53 | fcurproxyamt | 代扣代缴个税(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 代扣代缴个税(本位币) |
| 54 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 55 | ftreatway | 招待方式 | varchar | 10 |  | √ | ' ' | 招待方式,枚举: 1 :餐费 2 :酒店住宿 3 :酒水 4 :纪念品 |
| 56 | fwbsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 57 | fsplitparent | 拆分父分录 | varchar | 32 |  | √ | ' ' | 拆分父分录 |
| 58 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 59 | fotherstandarddesc | 酒水标准 | varchar | 255 |  | √ | ' ' | 酒水标准 |
| 60 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 61 | fentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 62 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 63 | fmeetlevel | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 64 | fcityarea | 城市类别 | int8 | 64 |  | √ | 0 | 出差地域 er_triparea |
| 65 | fsharedamount | 已分摊金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额（本位币） |
| 66 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 67 | fexpwithholdingamount | 已预提金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额本位币 |
| 68 | fescortnum | 陪同人数 | int4 | 32 |  | √ | 0 | 陪同人数 |
| 69 | fitemfrom | 来源 | varchar | 2 |  | √ | '0' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 4 :分录导入 |
| 70 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 71 | fexpebillstatus | fexpebillstatus | bpchar | 1 |  | √ | 'G' |  |
| 72 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | 报销级别 er_reimburselevel |
| 73 | fitemreasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 74 | fexpebalanceamount | fexpebalanceamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 75 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 76 | fexpisredoffset | 红冲(明细) | bpchar | 1 |  | √ | '0' | 红冲(明细) |
| 77 | fexpeorihasreimamount | fexpeorihasreimamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 78 | freimctldeptid | 额度控制部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 79 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 80 | forisharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额 |
| 81 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 82 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 83 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 84 | ffeestandarddesc | 费用标准 | varchar | 255 |  | √ | ' ' | 费用标准 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_expensedetail_fseq |  | fid,fseq |
| 2 | idx_er_expdetail_happendate |  | fhappendate |
| 3 | idx_er_expdetail_reimburser |  | freimburser |
| 4 | idx_er_expdetail_reimdeptid |  | freimctldeptid |
| 5 | idx_er_expdetail_expitmeid |  | fexpenseitemid |
| 6 | t_er_expensedetail_pkey |  | fdetailid |

---

## 关联子实体-子表 t_er_dailyreimwithholding_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_dailyreimwithholding_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_dailyreimwithholding_lk |  | fpkid |
| 2 | idx_er_dailyreimwithholding_lk_fk |  | fentryid |

---

## 发票明细-子表 t_er_invoiceitem

- **表名称：** 发票明细-子表
- **表名：** t_er_invoiceitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | fexcludeamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | finvoiceitemoffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fitementryid | 费用项目分录id | int8 | 64 |  | √ | 0 | 费用项目分录id |
| 8 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 9 | finvoiceheadentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 10 | funitprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 11 | fgoodscode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 12 | fspecmodel | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 13 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 14 | finvoicecloudoffset | 发票抵扣 | bpchar | 1 |  | √ | '1' | 发票抵扣 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 17 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoiceitem_fid |  | fid |
| 2 | idx_er_invoiceitem_invhead |  | finvoiceheadentryid |
| 3 | idx_er_invoiceitem_itementry |  | fitementryid |
| 4 | t_er_invoiceitem_pkey |  | fentryid |

---

## 发票与费用明细-子表 t_er_invoiceandexpense

- **表名称：** 发票与费用明细-子表
- **表名：** t_er_invoiceandexpense

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | finvoiceentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 4 | fexpenseentryid | 费用明细分录id | int8 | 64 |  | √ | 0 | 费用明细分录id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ie_finvoiceentryid |  | finvoiceentryid |
| 2 | idx_ie_fexpenseentryid |  | fexpenseentryid |
| 3 | t_er_invoiceandexpense_pkey |  | fentryid |
| 4 | idx_invoiceandexpense_id |  | fid |

---

## 发票信息-子表 t_er_invoiceinfo

- **表名称：** 发票信息-子表
- **表名：** t_er_invoiceinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmapexpenseinfo | fmapexpenseinfo | varchar | 255 |  |  | null |  |
| 3 | ftaxrate | 平均税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 平均税率（%） |
| 4 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 5 | fuploadseq | 采集顺序 | int8 | 64 |  | √ | 0 | 采集顺序 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 8 | fisred | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票,枚举: 0 :否 1 :是 |
| 9 | fbuyeraddressphone | 地址电话 | varchar | 255 |  | √ | ' ' | 地址电话 |
| 10 | fpassengername | 旅客 | varchar | 255 |  |  | null | 旅客 |
| 11 | fenddate | 通行日期止 | timestamp | 0 |  |  | null | 通行日期止 |
| 12 | fissupplement | 后补发票 | bpchar | 1 |  | √ | '0' | 后补发票,枚举: 0 :否 1 :是 |
| 13 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 14 | ffuelsurcharge | 燃油附加费 | numeric | 23 | 10 | √ | 0 | 燃油附加费 |
| 15 | fordertype | fordertype | bpchar | 1 |  | √ | ' ' |  |
| 16 | finvoicecode | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 17 | fcity | 发票所在地 | varchar | 50 |  | √ | ' ' | 发票所在地 |
| 18 | fbuyername | 收票公司 | varchar | 250 |  | √ | ' ' | 收票公司 |
| 19 | fpassverifybuyername | 发票抬头一致 | varchar | 30 |  | √ | ' ' | 发票抬头一致,枚举: 1 :是 0 :否 |
| 20 | fpassverifybuyertaxno | 发票税号一致 | varchar | 30 |  | √ | ' ' | 发票税号一致,枚举: 1 :是 0 :否 |
| 21 | finvoiceno | 发票号码 | varchar | 129 |  | √ | ' ' | 发票号码 |
| 22 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |
| 23 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 24 | freasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 25 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 26 | fseatgrade | 座位等级 | varchar | 50 |  | √ | ' ' | 座位等级,枚举: |
| 27 | foffsetamount | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 28 | fistartcity | 出发城市 | varchar | 50 |  | √ | ' ' | 出发城市 |
| 29 | finvoicecurrencyid | 发票币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 30 | fbuyerorgid | 收票公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :酒店账单 23 :通用机打电子发票 |
| 32 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 33 | ftocity | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 34 | fcustomeridnumber | 身份证 | varchar | 50 |  | √ | ' ' | 身份证 |
| 35 | fstartdate | 通行日期起 | timestamp | 0 |  |  | null | 通行日期起 |
| 36 | ffairtime | 飞机乘机时间 | varchar | 20 |  | √ | ' ' | 飞机乘机时间 |
| 37 | ftransportnote | 运输票据 | varchar | 30 |  | √ | ' ' | 运输票据,枚举: 1 :是 0 :否 |
| 38 | fsequencenum | 是否连号 | varchar | 30 |  | √ | ' ' | 是否连号,枚举: 1 :是 2 :否 |
| 39 | ffrominvoicecloud | 发票云导入 | bpchar | 1 |  | √ | '0' | 发票云导入 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | finoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 42 | fidestcity | 目的城市 | varchar | 50 |  | √ | ' ' | 目的城市 |
| 43 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 44 | fsequencenuminfo | 连号信息 | varchar | 255 |  | √ | ' ' | 连号信息 |
| 45 | fticketchanges | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :正常 2 :改签 3 :售票 4 :退票 |
| 46 | finvoicesrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 47 | fisxbrl | 是否xbrl | bpchar | 1 |  | √ | '0' | 是否xbrl |
| 48 | finvoiceischange | 是否修改 | varchar | 30 |  | √ | ' ' | 是否修改,枚举: 1 :否 2 :是 |
| 49 | falltaxrate | 税率(%) | varchar | 100 |  | √ | ' ' | 税率(%) |
| 50 | fievalidatest | 查验状态 | bpchar | 1 |  | √ | '3' | 查验状态,枚举: 1 :通过 2 :不通过 3 :- |
| 51 | fidestprovince | 目的省份 | varchar | 50 |  | √ | ' ' | 目的省份 |
| 52 | fothertotaltaxamount | 其他税费 | numeric | 23 | 10 | √ | 0 | 其他税费 |
| 53 | finvoicesrcentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 54 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 55 | finsurancepremium | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 56 | fspecmodel | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 57 | fvalidatemessage | 发票校验结果 | varchar | 255 |  | √ | ' ' | 发票校验结果 |
| 58 | fairconstfee | 机场建设费 | numeric | 23 | 10 | √ | 0 | 机场建设费 |
| 59 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 60 | finvoicealltaxcode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 61 | fislinkagedetail | 是否费用联动 | bpchar | 1 |  | √ | '0' | 是否费用联动 |
| 62 | fregion | 地域 | bpchar | 1 |  |  | null | 地域,枚举: 1 :国内 2 :国际 |
| 63 | fcount | 发票张数 | int8 | 64 |  | √ | 0 | 发票张数 |
| 64 | finvoicenotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 65 | finvoicefrom | 发票来源 | varchar | 30 |  | √ | '1' | 发票来源,枚举: 1 :发票云 2 :OCR识别 3 :商旅月结 |
| 66 | fbillcreatetime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 67 | ffromcity | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 68 | fbuyertaxno | 收票方税号 | varchar | 50 |  | √ | ' ' | 收票方税号 |
| 69 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 70 | fmakeoutcompname | 开票公司 | varchar | 250 |  | √ | ' ' | 开票公司 |
| 71 | finvoiceordernum | finvoiceordernum | varchar | 500 |  | √ | ' ' |  |
| 72 | fflighttrainnums | 航班号/车次 | varchar | 30 |  | √ | ' ' | 航班号/车次 |
| 73 | fistartprovince | 出发省份 | varchar | 50 |  | √ | ' ' | 出发省份 |
| 74 | fismapexpense | 关联费用明细 | bpchar | 1 |  | √ | '1' | 关联费用明细,枚举: 1 :是 0 :否 |
| 75 | finvoicesrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: er_expense_recordbill :费用记录 er_trip_recordbill :差旅记录 |
| 76 | fpersonalinvoice | 个人发票 | varchar | 30 |  | √ | ' ' | 个人发票,枚举: 1 :是 0 :否 |
| 77 | fendorsement | 签注 | varchar | 255 |  | √ | ' ' | 签注 |
| 78 | finvoicegoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoice_query |  | finvoicetype,finvoicedate |
| 2 | idx_er_invoice_serialno |  | fserialno |
| 3 | idx_er_invoiceinfo_fseq |  | fid,fseq |
| 4 | t_er_invoiceinfo_pkey |  | fentryid |

---

## 费用报销单-多语言表 t_er_dailyreimbursebill_l

- **表名称：** 费用报销单-多语言表
- **表名：** t_er_dailyreimbursebill_l

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
| 1 | t_er_dailyreimbursebill_l_pkey |  | fpkid |
| 2 | idx_drb_l_id |  | fid,flocaleid |

---

## 付款信息-子表 t_er_dailyreimpayentry

- **表名称：** 付款信息-子表
- **表名：** t_er_dailyreimpayentry

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
| 1 | idx_er_drpe_targetbillid_no |  | ftargetbillid,ftargetbillno |
| 2 | idx_er_drpe_feq |  | fid,fseq |
| 3 | t_er_dailyreimpayentry_pkey |  | fentryid |

---

## 费用报销单-分表 t_er_dailyreimbursebill_a

- **表名称：** 费用报销单-分表
- **表名：** t_er_dailyreimbursebill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | 报销级别 er_reimburselevel |
| 3 | fautogenshare | 自动生成分摊单 | bpchar | 1 |  | √ | '0' | 自动生成分摊单 |
| 4 | fdaysnum | 住宿天数 | int4 | 32 |  | √ | 0 | 住宿天数 |
| 5 | fisbeforeshare | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 6 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 7 | ftreatnum | 招待人数 | int4 | 32 |  | √ | 0 | 招待人数 |
| 8 | fmonthrulestartdate | 开始月份 | timestamp | 0 |  |  | null | 开始月份 |
| 9 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 10 | fmonthruleenddate | 结束月份 | timestamp | 0 |  |  | null | 结束月份 |
| 11 | fmeetgrade | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 12 | fbizitem | 业务事项 | int8 | 64 |  | √ | 0 | 业务事项 er_standard_type |
| 13 | fabovequota | 是否超额 | varchar | 30 |  | √ | ' ' | 是否超额,枚举: 1 :超额 2 :未超额 0 :- |
| 14 | fsharerule | 分摊规则 | varchar | 30 |  | √ | ' ' | 分摊规则,枚举: orgrule :按部门分摊 monthrule :按月分摊 yearrule :按年分摊 expenseitemrule :按费用项目分摊 |
| 15 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 16 | fmeetlevel | fmeetlevel | varchar | 10 |  | √ | ' ' |  |
| 17 | fcityarea | 城市类别 | int8 | 64 |  | √ | 0 | 出差地域 er_triparea |
| 18 | fsharemethod | 分摊方法 | varchar | 30 |  | √ | ' ' | 分摊方法,枚举: rate :比例分摊 avg :金额平均 amount :金额分摊 |
| 19 | fescortnum | 陪同人数 | int4 | 32 |  | √ | 0 | 陪同人数 |
| 20 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | ' ' | 需要影像扫描,枚举: 1 :是 2 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_dreim_fneedimagescan |  | fneedimagescan |
| 2 | pk_t_er_dailyreimbursebill_a |  | fid |

---

## 冲预提-子表 t_er_dailyreimwithholding

- **表名称：** 冲预提-子表
- **表名：** t_er_dailyreimwithholding

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwhdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 3 | fwhquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 4 | fwhentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fwhbillpayertype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 7 | forgiwhbalanceamount | 冲销余额 | numeric | 23 | 10 | √ | 0 | 冲销余额 |
| 8 | fwhcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | fwhbalanceamount | 冲销余额(本位币) | numeric | 23 | 10 | √ | 0 | 冲销余额(本位币) |
| 10 | fwithholdingbillno | 预提单号 | varchar | 100 |  | √ | '0' | 预提单号 |
| 11 | fwhpayername | 申请人 | varchar | 200 |  | √ | ' ' | 申请人 |
| 12 | fwhsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型 |
| 13 | fwhbillpayerid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fwhentrycostcompanyid | 分录费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fwhcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fwhbursedcurramount | 冲销金额(本位币) | numeric | 23 | 10 | √ | 0 | 冲销金额(本位币) |
| 17 | fwhbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 18 | fwithholdingtype | 预提类型 | int8 | 64 |  | √ | 0 | 预提类型 er_withholdingtype |
| 19 | fwhsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 20 | fwhentrycostdeptid | 分录费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fwhsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 22 | fwhbursedamount | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fwhexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 25 | fsourcewhitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_daily_withholding_fid |  | fid,fseq |
| 2 | pk_t_er_dailyreimwithholding |  | fentryid |
