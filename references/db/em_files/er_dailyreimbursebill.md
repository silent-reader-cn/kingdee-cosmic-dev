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
| 2 | fattstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 3 | fattlargetxt | 长文本 | varchar | 255 |  |  | null | 长文本 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachserialno | 发票序列号 | varchar | 255 |  | √ | ' ' | 发票序列号 |
| 6 | fattsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: 1 :发票云 2 :大模型 |
| 7 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 8 | frotationangle | 旋转角度 | varchar | 30 |  |  | null | 旋转角度 |
| 9 | fattaffairdiscription | 事务描述 | varchar | 1024 |  |  | null | 事务描述 |
| 10 | fattheadcount | 人数 | int8 | 64 |  | √ | 0 | 人数 |
| 11 | fattcity | 城市 | varchar | 255 |  |  | null | 城市 |
| 12 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 13 | fattenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 14 | fattinvoiceentyid | 发票分录id | int8 | 64 |  | √ | 0 | 发票分录id |
| 15 | fattfrom | 出发地 | varchar | 255 |  |  | null | 出发地 |
| 16 | fattlargetxt_tag | 长文本_详情 | text | 0 |  |  | null | 长文本_详情 |
| 17 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 18 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 19 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 20 | fattto | 目的地 | varchar | 255 |  |  | null | 目的地 |
| 21 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 22 | fattendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 23 | fattapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 24 | fattstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fatttotalamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
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

## 冲申请-子表 t_er_writeoffapply

- **表名称：** 冲申请-子表
- **表名：** t_er_writeoffapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapplyproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fexpenseitemfield | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 4 | forgfield | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsourceapplybilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: er_dailyapplybill :费用申请单 ocmem_marketcost_apply :营销费用申请单 |
| 6 | forgiexpebalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fapplycostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fapplybilldate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 10 | fsourcesign | 来源标识 | bpchar | 1 |  | √ | '0' | 来源标识 |
| 11 | fsourceapplybillid | 源单ID | varchar | 100 |  | √ | ' ' | 源单ID |
| 12 | fapplybillno | 申请单号 | varchar | 100 |  | √ | '0' | 申请单号 |
| 13 | fapplydescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 14 | fapplyexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 15 | fapplycostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | freimbursedamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 17 | fstd_applycostcenter | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 18 | fapplyperson | 申请人 | varchar | 200 |  | √ | ' ' | 申请人 |
| 19 | fdatefield | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 20 | fexpebalanceamount | 可报销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额（本位币） |
| 21 | fapplycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fsourceapplyentryid | 申请明细分录ID | int8 | 64 |  | √ | 0 | 申请明细分录ID |
| 23 | freimbursedcurramount | 冲销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额（本位币） |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fquotetype | 换算方式（冲申请） | bpchar | 1 |  | √ | '0' | 换算方式（冲申请）,枚举: 0 :直接汇率 1 :间接汇率 |

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
| 3 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 4 | floanbill | floanbill | int8 | 64 |  | √ | 0 |  |
| 5 | floanbillnov1 | 借款单号 | varchar | 100 |  | √ | '0' | 借款单号 |
| 6 | fsourceentryid | 借款明细分录ID | int8 | 64 |  | √ | 0 | 借款明细分录ID |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fcurrloanamount | 借款余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额（本位币） |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | faccloanamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 11 | fcurraccloanamount | 冲销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额(本位币) |
| 12 | floanamount | 借款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额 |
| 13 | floanexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 14 | floancurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | floanapplydatev1 | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 16 | fsourcesign | 关联申请 | bpchar | 1 |  | √ | '0' | 关联申请 |
| 17 | fsourcebillid | 源单id | varchar | 100 |  | √ | ' ' | 源单id |
| 18 | fsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型,枚举: er_dailyloanbill :借款单 er_tripreqbill :出差借款单 |
| 19 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | floandescriptionv1 | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fquotetype | 换算方式（冲借款） | bpchar | 1 |  | √ | '0' | 换算方式（冲借款）,枚举: 0 :直接汇率 1 :间接汇率 |
| 23 | fsourceexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |

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
| 3 | fentrycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 5 | fsdentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | [商机登记F7 mpm_bizopregf7](../mpm_files/mpm_bizopregf7.md) |
| 6 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 7 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 10 | foffset | 可抵扣 | bpchar | 1 |  | √ | '1' | 可抵扣 |
| 11 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 12 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 13 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 15 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
| 16 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | '1' | 专票 |
| 17 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 18 | fcurprice | 核定不含税金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额本位币 |
| 19 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | '0' | 发票类型,枚举: 0 :空 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车销售发票 13 :二手车销售发票 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 26 :数电发票（普通发票） 27 :数电发票（增值税专用发票） 28 :数电票（航空运输电子客票行程单） 29 :数电票（铁路电子客票） 30 :形式发票 |
| 20 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 21 | ftaxclasscodeid | 税收分类编号基础资料 | int8 | 64 |  | √ | 0 | [税收分类编码 er_taxclasscode](../basedata_files/er_taxclasscode.md) |
| 22 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 23 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |
| 24 | fitemfrom | 来源 | varchar | 2 |  | √ | '0' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 4 :分录导入 |
| 25 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 26 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 27 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 28 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 29 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 30 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 31 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 32 | finvoicetypeiditem | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 33 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 34 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 35 | fairportconstructionfee | 民航发展基金及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 民航发展基金及其他 |
| 36 | flkwaitentryid | 待摊明细id | varchar | 200 |  | √ | ' ' | 待摊明细id |
| 37 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 38 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 39 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 41 | fsdentrympmtaskid | 任务号 | int8 | 64 |  |  | null | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |

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
| 1 | idx_er_writeoffdetail_lk_fid |  | fentryid |
| 2 | t_er_writeoffdetail_lk_pkey |  | fpkid |

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
| 3 | faccountcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fbuildedamount | 已出单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已出单金额 |
| 5 | foriamount | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 6 | forgirepaidamount | forgirepaidamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fpayeraccount01 | 银行账号4位 | varchar | 100 |  | √ | ' ' | 银行账号4位 |
| 8 | fentrystatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: F :等待付款 G :已付款 I :关闭 E :审核通过 |
| 9 | fpayerdeptid | fpayerdeptid | int8 | 64 |  | √ | 0 |  |
| 10 | fpayercompid | fpayercompid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 bos_user :职员 |
| 12 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 13 | forgiapplyedreimamount | forgiapplyedreimamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | forgiwriteoffamount | forgiwriteoffamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | famount | 收款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额（本位币） |
| 16 | foriaccnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 17 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 18 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 19 | fsupplier | 收款人（供应商） | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 20 | fentryrepaydate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |
| 21 | fpayeraccountname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 22 | fpayerid | 收款人(个人) | int8 | 64 |  | √ | 0 | [收款信息 er_payeer](../em_files/er_payeer.md) |
| 23 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额（本位币） |
| 24 | fapplyedreimamount | fapplyedreimamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | facccostcompany | 付款公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fcustomer | fcustomer | int8 | 64 |  | √ | 0 |  |
| 27 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 28 | frepaidamount | frepaidamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 30 | foriaccpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 31 | foriaccbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额 |
| 32 | fbosuserid | 收款人（职员） | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | faccpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额（本位币） |
| 34 | fcasorg | fcasorg | int8 | 64 |  | √ | 0 |  |
| 35 | faccnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额(本位币) |
| 36 | fbanklogo | 银行卡logo图标 | varchar | 50 |  | √ | ' ' | 银行卡logo图标 |
| 37 | faccounttype | faccounttype | varchar | 10 |  | √ | ' ' |  |
| 38 | fpayeraccount02 | 银行账号（显示_old） | varchar | 100 |  | √ | ' ' | 银行账号（显示_old） |
| 39 | fpayeraccount | 银行账号 | varchar | 100 |  | √ | ' ' | 银行账号 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

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
| 2 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | [商机登记F7 mpm_bizopregf7](../mpm_files/mpm_bizopregf7.md) |
| 3 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fsharecurrency | 分摊币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 7 | fstdentrycostcenterrule | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 8 | fsharewaitseq | 待摊行号 | int4 | 32 |  | √ | 0 | 待摊行号 |
| 9 | fshareamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |
| 10 | fentrympmtaskid | 任务号 | int8 | 64 |  |  | null | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 11 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fshareappamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 13 | fentryexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 14 | fsharewaitid | 待摊明细id | int8 | 64 |  | √ | 0 | 待摊明细id |
| 15 | fshareremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 3 | fpaycompanyid | 支付公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | finvokeinvoicecloud | 与发票云交互 | bpchar | 1 |  | √ | '0' | 与发票云交互 |
| 5 | fnoinvoice | 无票 | bpchar | 1 |  | √ | '0' | 无票 |
| 6 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fhasvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 9 | fhead_paydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 10 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 13 | forigin | 来源 | varchar | 10 |  | √ | ' ' | 来源,枚举: 1 :WEB 2 :移动端 3 :语音助手 |
| 14 | fapplierpositionstr | 职位文本 | varchar | 100 |  | √ | ' ' | 职位文本 |
| 15 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 16 | fisover | 超费用标准（提交后有值） | bpchar | 1 |  | √ | '0' | 超费用标准（提交后有值） |
| 17 | fneeduploadinvoice | 有待上传的纸票/附件 | bpchar | 1 |  | √ | '0' | 有待上传的纸票/附件 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fbilltypefield | fbilltypefield | int8 | 64 |  | √ | 0 |  |
| 20 | foffsetinvoiceno | 可抵扣发票号码 | varchar | 255 |  |  | null | 可抵扣发票号码 |
| 21 | fsourcebilltype | 源单类型(已废弃) | varchar | 30 |  | √ | ' ' | 源单类型(已废弃) |
| 22 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 23 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 24 | fmonthsettleamount | 月结金额 | numeric | 23 | 10 | √ | 0 | 月结金额 |
| 25 | finvoiceoffsetamount | 抵扣税额合计（发票） | numeric | 23 | 10 | √ | 0 | 抵扣税额合计（发票） |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 28 | fautomapinvoice | 智能发票报销 | bpchar | 1 |  | √ | '1' | 智能发票报销 |
| 29 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 30 | foffsetamount | 抵扣税额合计（费用） | numeric | 23 | 10 |  | null | 抵扣税额合计（费用） |
| 31 | fimagenumber | 影像编号 | varchar | 255 |  | √ | ' ' | 影像编号 |
| 32 | fattachmentacount | fattachmentacount | int8 | 64 |  | √ | 0 |  |
| 33 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 34 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 35 | fpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 36 | fnextauditor | 下一步审核人 | varchar | 100 |  | √ | ' ' | 下一步审核人 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fbalanceamount | 借款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额 |
| 40 | fisoverbudget | 超预算 | bpchar | 1 |  | √ | '0' | 超预算 |
| 41 | ftel | 联系方式 | varchar | 100 |  | √ | ' ' | 联系方式 |
| 42 | fisshared | 已分摊 | bpchar | 1 |  | √ | '0' | 已分摊 |
| 43 | fredoffsetdes | 红冲说明 | varchar | 1000 |  | √ | ' ' | 红冲说明 |
| 44 | fpayamount | 付现 | numeric | 23 | 10 | √ | 0.0000000000 | 付现 |
| 45 | fprojectsharecount | 下游项目成本分摊单数 | int8 | 64 |  | √ | 0 | 下游项目成本分摊单数 |
| 46 | fcashier | 出纳员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fneedsuppleinvoice | 发票后补 | bpchar | 1 |  | √ | '0' | 发票后补 |
| 49 | fsharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额 |
| 50 | fspecialbill | 专项报销单类型 | varchar | 30 |  | √ | ' ' | 专项报销单类型,枚举: A :额度报销单 B :移动话费报销单 |
| 51 | funrepaymentamount | 申请人未还款 | numeric | 23 | 10 | √ | 0 | 申请人未还款 |
| 52 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | fpaycurrency | 付现金额币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 54 | fisredoffset | 红冲 | bpchar | 1 |  | √ | '0' | 红冲 |
| 55 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_loanbill :出差借款单 er_tripreimbursebill :差旅费报销单 er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_dailyreimbursebill :费用报销单 er_repaymentbill :还款单 er_publicreimbursebill :对公报销单 |
| 56 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 57 | fis_all_einvoice | 发票状态 | bpchar | 1 |  | √ | '0' | 发票状态,枚举: 0 :无发票 1 :全电票 2 :含纸票 3 :其它 |
| 58 | freimbursecontrolcomany | 额度控制公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 59 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 60 | fismultireimburser | 多报销人 | bpchar | 1 |  | √ | ' ' | 多报销人 |
| 61 | fproxytax | 代扣代缴 | bpchar | 1 |  | √ | '0' | 代扣代缴 |
| 62 | fiscurrency | 多币种 | bpchar | 1 |  | √ | '0' | 多币种 |
| 63 | fisinvoicemodified | 发票修改 | bpchar | 1 |  | √ | '0' | 发票修改 |
| 64 | freimbursetype | 报账类型 | varchar | 30 |  | √ | ' ' | 报账类型,枚举: expense :费用报账 entertainment :招待费 meetting :会议费 otherexpenses :其他 |
| 65 | fauditopinion | 审核意见 | varchar | 100 |  | √ | ' ' | 审核意见 |
| 66 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 67 | fispaybyhead | 按单头付款 | bpchar | 1 |  | √ | '0' | 按单头付款 |
| 68 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 69 | ftotalaccloanamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 70 | ftarbillstatus | 目标单据 | varchar | 30 |  | √ | '0' | 目标单据,枚举: B1 :项目成本分摊单 |
| 71 | freimbursecurrency | 报销金额币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 72 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | [业务分类 er_projecttype](../em_files/er_projecttype.md) |
| 73 | fcurrencyid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

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
| 4 | idx_er_dreim_costcompy |  | fcostcompanyid |
| 5 | idx_er_dreim_fbillstatus |  | fbillstatus |
| 6 | t_er_dailyreimbursebill_pkey |  | fid |
| 7 | idx_er_dreim_fbillno |  | fbillno |
| 8 | idx_er_dreim_fcompanyid |  | fcompanyid |

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

## 费用明细-分表 t_er_expensedetail_a

- **表名称：** 费用明细-分表
- **表名：** t_er_expensedetail_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffeeexchangerate | 汇率(标准) | numeric | 23 | 10 | √ | 0 | 汇率(标准) |
| 3 | fisexistmonthly | 关联商旅订单 | bpchar | 1 |  | √ | '0' | 关联商旅订单 |
| 4 | ftripbookcuramount | 商旅预定金额（本位币） | numeric | 23 | 10 | √ | 0 | 商旅预定金额（本位币） |
| 5 | fwineway | 酒水来源 | varchar | 10 |  | √ | ' ' | 酒水来源,枚举: 1 :内部领用 2 :自行购买 3 :无酒水 |
| 6 | ffeequotetype | 换算方式(标准) | bpchar | 1 |  | √ | '0' | 换算方式(标准),枚举: 0 :直接汇率 1 :间接汇率 |
| 7 | fcurothercontrolamt | 酒水可报金额 | numeric | 23 | 10 | √ | 0 | 酒水可报金额 |
| 8 | fredml | 红酒（毫升） | int4 | 32 |  | √ | 0 | 红酒（毫升） |
| 9 | fisovercheck | 校验超额度报销 | bpchar | 1 |  | √ | '0' | 校验超额度报销 |
| 10 | fwhiteml | 白酒（毫升） | int4 | 32 |  | √ | 0 | 白酒（毫升） |
| 11 | fothercontrolamt | 酒水可报金额 | numeric | 23 | 10 | √ | 0 | 酒水可报金额 |
| 12 | fcurcontrolamt | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 13 | fcurotherfeeamount | 酒水金额 | numeric | 23 | 10 | √ | 0 | 酒水金额 |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 15 | ftripbookamount | 商旅预定金额 | numeric | 23 | 10 | √ | 0 | 商旅预定金额 |
| 16 | ffeecurrency | 币种(标准) | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_expdetail_a_fid |  | fid |
| 2 | pk_t_er_expensedetail_a |  | fdetailid |

---

## 项目干系人-多选基础资料表 t_er_dailyreimburseower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_dailyreimburseower

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
| 1 | idx_er_dailyreimburseower_fid |  | fid |
| 2 | pk_t_er_dailyreimburseower |  | fpkid |

---

## 商旅订单-子表 t_er_dailyremorderentry

- **表名称：** 商旅订单-子表
- **表名：** t_er_dailyremorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forderdeductibletax | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |
| 3 | ftotalamount | 订单金额 | numeric | 23 | 10 | √ | 0 | 订单金额 |
| 4 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0 | 服务费 |
| 5 | fendorsementamount | 改签费 | numeric | 23 | 10 | √ | 0 | 改签费 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | forderstatusstr | 订单状态 | varchar | 50 |  | √ | ' ' | 订单状态 |
| 8 | frefundamount | 退票/退订费 | numeric | 23 | 10 | √ | 0 | 退票/退订费 |
| 9 | ffromplace | 出发地 | varchar | 2000 |  | √ | ' ' | 出发地 |
| 10 | ftravelername | 使用人 | varchar | 255 |  | √ | ' ' | 使用人 |
| 11 | frefundamounttax | 退票费可抵扣税额 | numeric | 23 | 10 | √ | 0 | 退票费可抵扣税额 |
| 12 | fbegintime | 出发时间 | timestamp | 0 |  |  | null | 出发时间 |
| 13 | foabillnum | 审批单号 | varchar | 255 |  | √ | ' ' | 审批单号 |
| 14 | foperationtype | 业务类型 | varchar | 10 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 7 :服务费 8 :用餐 |
| 15 | fticketprice | 票价 | numeric | 23 | 10 | √ | 0 | 票价 |
| 16 | fserver | 服务商 | varchar | 50 |  | √ | ' ' | 服务商,枚举: CHAILVYIHAO :差旅壹号 DIDI :滴滴 MEITUAN :美团 XIECHENG :携程 ZHAOSHANG :招商银行 GAODE :高德 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 |
| 17 | ftoplace | 目的地 | varchar | 2000 |  | √ | ' ' | 目的地 |
| 18 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 19 | forderformid | 订单表单ID | varchar | 255 |  | √ | ' ' | 订单表单ID |
| 20 | fparentordernum | 父订单号 | varchar | 255 |  | √ | ' ' | 父订单号 |
| 21 | ffuelprice | 燃油费 | numeric | 23 | 10 | √ | 0 | 燃油费 |
| 22 | fticketstatus | 订单使用状态（机票） | varchar | 50 |  | √ | ' ' | 订单使用状态（机票）,枚举: USED :已使用 UNUSED :未使用 REFOUND :已退票 CHANGED :已改签 |
| 23 | fordercostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | forderbookeddept | 申请人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 26 | fordercompany | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fticketpricedeductibletax | 票价可抵扣税额 | numeric | 23 | 10 | √ | 0 | 票价可抵扣税额 |
| 28 | fordernumber | 订单号 | varchar | 255 |  | √ | ' ' | 订单号 |
| 29 | fordexpenseentryid | 关联费用明细id | int8 | 64 |  | √ | 0 | 关联费用明细id |
| 30 | fordercurrency | 订单币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fservicefeedeductibletax | 服务费可抵扣税额 | numeric | 23 | 10 | √ | 0 | 服务费可抵扣税额 |
| 32 | fordercostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fairportprice | 民航发展基金及其他/税费 | numeric | 23 | 10 | √ | 0 | 民航发展基金及其他/税费 |
| 35 | fassuranceamount | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 36 | fendtime | 到达时间 | timestamp | 0 |  |  | null | 到达时间 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_dailyreim_order_fid |  | fid |
| 2 | pk_er_dailyremorderentry |  | fentryid |

---

## 费用明细-子表 t_er_expensedetail

- **表名称：** 费用明细-子表
- **表名：** t_er_expensedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexporiusedamount | fexporiusedamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | [商机登记F7 mpm_bizopregf7](../mpm_files/mpm_bizopregf7.md) |
| 4 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 5 | fentrycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 7 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 8 | fgoodsnum | 酒水瓶数 | int4 | 32 |  | √ | 0 | 酒水瓶数 |
| 9 | fiscreateprojectcostshare | 生成项目分摊单 | int8 | 64 |  | √ | 0 | 生成项目分摊单 |
| 10 | forgiexpebalanceamount | forgiexpebalanceamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | fpushedamount | fpushedamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | foffset | 可抵扣 | bpchar | 1 |  | √ | '1' | 可抵扣 |
| 14 | fproxyamt | 代扣代缴个税 | numeric | 23 | 10 | √ | 0.0000000000 | 代扣代缴个税 |
| 15 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 16 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 17 | fotherfeeamount | 酒水金额 | numeric | 23 | 10 | √ | 0 | 酒水金额 |
| 18 | fitemnodeductionreason | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或个人消费 4 :遭受非正常损失 5 :其他 |
| 19 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 20 | fwbsrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: er_expense_recordbill :费用记录 er_trip_recordbill :差旅记录 er_vehiclecheckingbill :用车结算单 er_mealcheckingbill :用餐结算单 |
| 21 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
| 22 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | '1' | 专票 |
| 23 | fisover | 超费用标准 | bpchar | 1 |  | √ | '0' | 超费用标准 |
| 24 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额（本位币） |
| 25 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | '0' | 发票类型,枚举: 0 :空 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车销售发票 13 :二手车销售发票 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 26 :数电发票（普通发票） 27 :数电发票（增值税专用发票） 28 :数电票（航空运输电子客票行程单） 29 :数电票（铁路电子客票） 30 :形式发票 |
| 26 | finvoicefromparent | 发票来源父节点 | bpchar | 1 |  | √ | '0' | 发票来源父节点 |
| 27 | fwbsrcentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 28 | fotherstandamount | 酒水标准金额(页面不可见) | numeric | 23 | 10 | √ | 0 | 酒水标准金额(页面不可见) |
| 29 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 30 | ftaxclasscodeid | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | [税收分类编码 er_taxclasscode](../basedata_files/er_taxclasscode.md) |
| 31 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 32 | foverdesc | 超标说明(暂未支持) | varchar | 255 |  | √ | ' ' | 超标说明(暂未支持) |
| 33 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 34 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 35 | fexpehasreimamount | fexpehasreimamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 36 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 37 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 38 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 39 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 40 | fdaysnum | 住宿天数 | int4 | 32 |  | √ | 0 | 住宿天数 |
| 41 | fexpeorirepayamount | fexpeorirepayamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fmeetitem | 会议事项 | varchar | 10 |  | √ | ' ' | 会议事项,枚举: 1 :伙食费 2 :酒店住宿 3 :交通费 4 :其他 |
| 43 | freimburser | 报销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | ftreatnum | 招待人数 | int4 | 32 |  | √ | 0 | 招待人数 |
| 45 | fcontrolamt | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 46 | fwbsrcbillno | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |
| 47 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 48 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 49 | fexperepayamount | fexperepayamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 50 | ffeestandid | 费用标准基础资料 | int8 | 64 |  | √ | 0 | [费用标准 er_standard](../em_files/er_standard.md) |
| 51 | fairportconstructionfee | 民航发展基金及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 民航发展基金及其他 |
| 52 | ffeestandardamt | 费用标准金额(页面不可见) | numeric | 23 | 10 | √ | 0 | 费用标准金额(页面不可见) |
| 53 | fexpusedamount | fexpusedamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 54 | fcurproxyamt | 代扣代缴个税(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 代扣代缴个税(本位币) |
| 55 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 56 | ftreatway | 招待方式 | varchar | 10 |  | √ | ' ' | 招待方式,枚举: 1 :餐费 2 :酒店住宿 3 :酒水 4 :纪念品 |
| 57 | fwbsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 58 | fsplitparent | 拆分父分录 | varchar | 32 |  | √ | ' ' | 拆分父分录 |
| 59 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 60 | fotherstandarddesc | 酒水标准 | varchar | 255 |  | √ | ' ' | 酒水标准 |
| 61 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 62 | fentrympmtaskid | 任务号 | int8 | 64 |  |  | null | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 63 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 64 | fmeetlevel | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 65 | fcityarea | 城市类别 | int8 | 64 |  | √ | 0 | [出差地域 er_triparea](../em_files/er_triparea.md) |
| 66 | fsharedamount | 已分摊金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额（本位币） |
| 67 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 68 | fexpwithholdingamount | 已预提金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额本位币 |
| 69 | fescortnum | 陪同人数 | int4 | 32 |  | √ | 0 | 陪同人数 |
| 70 | fitemfrom | 来源 | varchar | 2 |  | √ | '0' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 4 :分录导入 |
| 71 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 72 | fexpebillstatus | fexpebillstatus | bpchar | 1 |  | √ | 'G' |  |
| 73 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | [报销级别 er_reimburselevel](../em_files/er_reimburselevel.md) |
| 74 | fitemreasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 75 | finvoicetypeiditem | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 76 | fexpebalanceamount | fexpebalanceamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 77 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 78 | fexpisredoffset | 红冲(明细) | bpchar | 1 |  | √ | '0' | 红冲(明细) |
| 79 | fexpeorihasreimamount | fexpeorihasreimamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 80 | freimctldeptid | 额度控制部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 81 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 82 | fexpischangeinvoice | 已解绑 | bpchar | 1 |  | √ | '0' | 已解绑 |
| 83 | forisharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额 |
| 84 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 85 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 86 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 87 | ffeestandarddesc | 费用标准 | varchar | 255 |  | √ | ' ' | 费用标准 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_expdetail_reimburser |  | freimburser |
| 2 | t_er_expensedetail_pkey |  | fdetailid |
| 3 | idx_er_expensedetail_fseq |  | fid,fseq |
| 4 | idx_er_expdetail_happendate |  | fhappendate |
| 5 | idx_er_expdetail_reimdeptid |  | freimctldeptid |
| 6 | idx_er_expdetail_costcompy |  | fentrycostcompanyid |
| 7 | idx_er_expdetail_expitmeid |  | fexpenseitemid |

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
| 2 | fexcludeamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 4 | finvoiceitemoffset | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 5 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | finvoiceitemisunbind | 解绑 | bpchar | 1 |  | √ | '0' | 解绑 |
| 8 | finvoicetaxamount | 单头税额 | numeric | 23 | 10 | √ | 0 | 单头税额 |
| 9 | finvoicecurrency | 发票币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 11 | funitprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 12 | fspecmodel | 规格型号 | varchar | 600 |  | √ | ' ' | 规格型号 |
| 13 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 14 | finvoicecloudoffset | 发票抵扣 | bpchar | 1 |  | √ | '1' | 发票抵扣 |
| 15 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 16 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 17 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |
| 18 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 19 | fitementryid | 费用项目分录id | int8 | 64 |  | √ | 0 | 费用项目分录id |
| 20 | finvoiceitemserialno | 发票序列号 | varchar | 255 |  | √ | ' ' | 发票序列号 |
| 21 | finvoiceheadentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 22 | fgoodscode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 23 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 24 | finvoicetaxrate | 单头税率 | varchar | 255 |  | √ | ' ' | 单头税率 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

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
| 2 | fkeyproperty | 关键字段 | bpchar | 1 |  | √ | '0' | 关键字段,枚举: 0 :默认值 |
| 3 | finvoiceexpisunbind | 解绑 | bpchar | 1 |  | √ | '0' | 解绑 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | finvoiceentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 6 | finvoiceexpserialno | 发票序列号 | varchar | 255 |  | √ | ' ' | 发票序列号 |
| 7 | fexpenseentryid | 费用明细分录id | int8 | 64 |  | √ | 0 | 费用明细分录id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
| 7 | fcarrierdate | 乘车/机日期 | timestamp | 0 |  |  | null | 乘车/机日期 |
| 8 | foffset | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 9 | fisred | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票,枚举: 0 :否 1 :是 |
| 10 | finvoiceitemequal | 对平 | bpchar | 1 |  | √ | '1' | 对平 |
| 11 | fbuyeraddressphone | 地址电话 | varchar | 255 |  | √ | ' ' | 地址电话 |
| 12 | fpassengername | 旅客 | varchar | 255 |  |  | null | 旅客 |
| 13 | fenddate | 通行日期止 | timestamp | 0 |  |  | null | 通行日期止 |
| 14 | fissupplement | 后补发票 | bpchar | 1 |  | √ | '0' | 后补发票,枚举: 0 :否 1 :是 |
| 15 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 16 | ffuelsurcharge | 燃油附加费 | numeric | 23 | 10 | √ | 0 | 燃油附加费 |
| 17 | fordertype | fordertype | bpchar | 1 |  | √ | ' ' |  |
| 18 | finvoicecode | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 19 | fcity | 发票所在地 | varchar | 50 |  | √ | ' ' | 发票所在地 |
| 20 | fbuyername | 收票公司 | varchar | 250 |  | √ | ' ' | 收票公司 |
| 21 | fpassverifybuyername | 发票抬头一致 | varchar | 30 |  | √ | ' ' | 发票抬头一致,枚举: 1 :是 0 :否 |
| 22 | fpassverifybuyertaxno | 发票税号一致 | varchar | 30 |  | √ | ' ' | 发票税号一致,枚举: 1 :是 0 :否 |
| 23 | finvoiceno | 发票号码 | varchar | 129 |  | √ | ' ' | 发票号码 |
| 24 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |
| 25 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 26 | fisemployee | 职员 | bpchar | 1 |  | √ | '0' | 职员 |
| 27 | freasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 28 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 29 | ftaxdetails | 多税率信息 | varchar | 500 |  | √ | ' ' | 多税率信息 |
| 30 | fseatgrade | 座位等级 | varchar | 50 |  | √ | ' ' | 座位等级,枚举: |
| 31 | foffsetamount | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 32 | fistartcity | 出发城市 | varchar | 50 |  | √ | ' ' | 出发城市 |
| 33 | finvoicecurrencyid | 发票币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 34 | fbuyerorgid | 收票公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车销售发票 13 :二手车销售发票 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 26 :数电发票（普通发票） 27 :数电发票（增值税专用发票） 28 :数电票（航空运输电子客票行程单） 29 :数电票（铁路电子客票） 30 :形式发票 |
| 36 | fairportconstructionfee | 民航发展基金及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 民航发展基金及其他 |
| 37 | ftocity | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 38 | fcustomeridnumber | 身份证 | varchar | 50 |  | √ | ' ' | 身份证 |
| 39 | fstartdate | 通行日期起 | timestamp | 0 |  |  | null | 通行日期起 |
| 40 | ffairtime | 乘车/机时间 | varchar | 20 |  | √ | ' ' | 乘车/机时间 |
| 41 | ftransportnote | 运输票据 | varchar | 30 |  | √ | ' ' | 运输票据,枚举: 1 :是 0 :否 |
| 42 | fsequencenum | 连号 | varchar | 30 |  | √ | ' ' | 连号,枚举: 1 :是 2 :否 |
| 43 | ffrominvoicecloud | 发票云导入 | bpchar | 1 |  | √ | '0' | 发票云导入 |
| 44 | fblockchain | 区块链 | bpchar | 1 |  | √ | '0' | 区块链 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | finoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 47 | fidestcity | 目的城市 | varchar | 50 |  | √ | ' ' | 目的城市 |
| 48 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 49 | fsequencenuminfo | 连号信息 | varchar | 255 |  | √ | ' ' | 连号信息 |
| 50 | fticketchanges | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :正常 2 :改签 3 :售票 4 :退票 1001 :失控 1002 :作废 1003 :红冲 1004 :异常 1005 :非正常 1006 :红字发票待确认 1007 :部分红冲 1008 :全部红冲 |
| 51 | finvoicesrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 52 | fisxbrl | xbrl | bpchar | 1 |  | √ | '0' | xbrl |
| 53 | finvoiceischange | 已修改 | varchar | 30 |  | √ | ' ' | 已修改,枚举: 1 :否 2 :是 |
| 54 | falltaxrate | 税率(%) | varchar | 100 |  | √ | ' ' | 税率(%) |
| 55 | fievalidatest | 查验状态 | bpchar | 1 |  | √ | '3' | 查验状态,枚举: 1 :通过 2 :不通过 3 :- |
| 56 | fidestprovince | 目的省份 | varchar | 50 |  | √ | ' ' | 目的省份 |
| 57 | fspecialtypemark | 特定业务类型 | varchar | 4 |  | √ | '0' | 特定业务类型,枚举: 1 :成品油发票 2 :稀土发票 3 :机动车发票 4 :农产品收购发票 5 :石脑油发票 6 :卷烟发票 7 :建筑服务发票 8 :货物运输服务发票 9 :不动产销售服务发票 10 :不动产经营租赁服务 11 :代收车船税发票 12 :旅客运输服务发票 13 :自产农产品销售发票 14 :通行费发票 15 :医疗服务（住院）发票 16 :医疗服务（门诊）发票 17 :拖拉机和联合收割机发票 18 :二手车发票 19 :光伏收购发票 20 :出口发票 21 :农产品发票 22 :稀土矿产品发票 23 :稀土产成品发票 24 :铁路电子客票 25 :航空运输电子客票行程单 26 :电子烟 27 :正常开具 28 :反向开具 |
| 58 | fothertotaltaxamount | 其他税费 | numeric | 23 | 10 | √ | 0 | 其他税费 |
| 59 | finvoicesrcentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 60 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 61 | finsurancepremium | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 62 | fspecmodel | 规格型号 | varchar | 600 |  | √ | ' ' | 规格型号 |
| 63 | fvalidatemessage | 发票校验结果 | varchar | 255 |  | √ | ' ' | 发票校验结果 |
| 64 | fairconstfee | 民航发展基金 | numeric | 23 | 10 | √ | 0 | 民航发展基金 |
| 65 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 66 | finvoicealltaxcode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 67 | fislinkagedetail | 费用联动 | bpchar | 1 |  | √ | '0' | 费用联动 |
| 68 | fregion | 地域 | bpchar | 1 |  |  | null | 地域,枚举: 1 :国内 2 :国际 |
| 69 | fcount | 发票张数 | int8 | 64 |  | √ | 0 | 发票张数 |
| 70 | finvoicenotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 71 | finvexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 72 | finvoicefrom | 发票来源 | varchar | 30 |  | √ | '1' | 发票来源,枚举: 1 :发票云 2 :OCR识别 3 :商旅月结 |
| 73 | fbillcreatetime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 74 | ffromcity | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 75 | fbuyertaxno | 收票方税号 | varchar | 50 |  | √ | ' ' | 收票方税号 |
| 76 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 77 | finvexpquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 78 | finvoicetypeid | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 79 | fmakeoutcompname | 开票公司 | varchar | 250 |  | √ | ' ' | 开票公司 |
| 80 | finvoiceordernum | finvoiceordernum | varchar | 500 |  | √ | ' ' |  |
| 81 | fflighttrainnums | 航班号/车次 | varchar | 30 |  | √ | ' ' | 航班号/车次 |
| 82 | fistartprovince | 出发省份 | varchar | 50 |  | √ | ' ' | 出发省份 |
| 83 | fnodeductionreason | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或个人消费 4 :遭受非正常损失 5 :其他 |
| 84 | fismapexpense | 关联费用明细 | bpchar | 1 |  | √ | '1' | 关联费用明细,枚举: 1 :是 0 :否 |
| 85 | finvoicesrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: er_expense_recordbill :费用记录 er_trip_recordbill :差旅记录 |
| 86 | fcurrtotalamount | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 87 | fpersonalinvoice | 个人发票 | varchar | 30 |  | √ | ' ' | 个人发票,枚举: 1 :是 0 :否 |
| 88 | fendorsement | 签注 | varchar | 255 |  | √ | ' ' | 签注 |
| 89 | finvoicegoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |

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
| 5 | idx_er_invoice_invq |  | finvoiceno,finvoicecode |

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
| 2 | ftargetpayorg | 付款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftargetbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | ftargetbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 5 | fdpcurrency | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ffee | 手续费 | numeric | 23 | 10 | √ | 0.0000000000 | 手续费 |
| 8 | ftargetentrustorg | 委托付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fdpexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 付款汇率 |
| 10 | flossamt | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 11 | fdpamt | 付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额 |
| 12 | fagreedrate | 兑换汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 兑换汇率 |
| 13 | ftargetlocalamount | 收款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额(本位币) |
| 14 | ftargetpayacctid | 付款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
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
| 2 | fautogenshare | 自动生成分摊单 | bpchar | 1 |  | √ | '0' | 自动生成分摊单 |
| 3 | ftaxshareway | 税额分摊方式 | bpchar | 1 |  | √ | '1' | 税额分摊方式,枚举: 1 :按分摊金额与税率计算 2 :按分摊金额比例计算 |
| 4 | fisbeforeshare | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 5 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 6 | fmonthrulestartdate | 开始月份 | timestamp | 0 |  |  | null | 开始月份 |
| 7 | fabovequota | 超额度 | varchar | 30 |  | √ | ' ' | 超额度,枚举: 1 :超额度 2 :未超额度 0 :- |
| 8 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 9 | fmeetlevel | fmeetlevel | varchar | 10 |  | √ | ' ' |  |
| 10 | fcityarea | 城市类别 | int8 | 64 |  | √ | 0 | [出差地域 er_triparea](../em_files/er_triparea.md) |
| 11 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 12 | fescortnum | 陪同人数 | int4 | 32 |  | √ | 0 | 陪同人数 |
| 13 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | [报销级别 er_reimburselevel](../em_files/er_reimburselevel.md) |
| 14 | fchangeinvoicedes | 换票说明 | varchar | 1000 |  | √ | ' ' | 换票说明 |
| 15 | fdaysnum | 住宿天数 | int4 | 32 |  | √ | 0 | 住宿天数 |
| 16 | fisstopreim | 止付 | bpchar | 1 |  | √ | '0' | 止付 |
| 17 | ftreatnum | 招待人数 | int4 | 32 |  | √ | 0 | 招待人数 |
| 18 | fischangeinvoice | 换发票 | bpchar | 1 |  | √ | '0' | 换发票 |
| 19 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 20 | fmonthruleenddate | 结束月份 | timestamp | 0 |  |  | null | 结束月份 |
| 21 | fmeetgrade | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 22 | fbizitem | 业务事项 | int8 | 64 |  | √ | 0 | [业务事项 er_standard_type](../em_files/er_standard_type.md) |
| 23 | fsharerule | 分摊规则 | varchar | 30 |  | √ | ' ' | 分摊规则,枚举: orgrule :按部门分摊 monthrule :按月分摊 yearrule :按年分摊 expenseitemrule :按费用项目分摊 |
| 24 | fsharemethod | 分摊方法 | varchar | 30 |  | √ | ' ' | 分摊方法,枚举: rate :比例分摊 avg :金额平均 amount :金额分摊 |
| 25 | fstopdescription | 止付说明 | varchar | 1000 |  | √ | ' ' | 止付说明 |
| 26 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | ' ' | 需要影像扫描,枚举: 1 :是 2 :否 |

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
| 4 | fwhentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fwhbillpayertype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 7 | forgiwhbalanceamount | 冲销余额 | numeric | 23 | 10 | √ | 0 | 冲销余额 |
| 8 | fwhcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fwhbalanceamount | 冲销余额(本位币) | numeric | 23 | 10 | √ | 0 | 冲销余额(本位币) |
| 10 | fwithholdingbillno | 预提单号 | varchar | 100 |  | √ | '0' | 预提单号 |
| 11 | fwhpayername | 申请人 | varchar | 200 |  | √ | ' ' | 申请人 |
| 12 | fwhsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型 |
| 13 | fwhbillpayerid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fwhentrycostcompanyid | 分录费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fwhcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fwhbursedcurramount | 冲销金额(本位币) | numeric | 23 | 10 | √ | 0 | 冲销金额(本位币) |
| 17 | fwhbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 18 | fwithholdingtype | 预提类型 | int8 | 64 |  | √ | 0 | [预提类型 er_withholdingtype](../em_files/er_withholdingtype.md) |
| 19 | fwhsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 20 | fwhentrycostdeptid | 分录费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fwhsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 22 | fwhbursedamount | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fwhexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 25 | fsourcewhitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_daily_withholding_fid |  | fid,fseq |
| 2 | pk_t_er_dailyreimwithholding |  | fentryid |
