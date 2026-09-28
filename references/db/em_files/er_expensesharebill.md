# 费用分摊单-er_expensesharebill

## 关联子实体-子表 t_er_expensesharewait_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_expensesharewait_lk

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
| 1 | t_er_expensesharewait_lk_pkey |  | fpkid |
| 2 | idx_er_sharewait_lk_fdetailid |  | fdetailid |

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

## 关联子实体-子表 t_er_expensesharebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_expensesharebill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | stableid | stableid | int8 | 64 |  | √ | 0 |  |
| 3 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
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
| 1 | t_er_expensesharebill_lk_pkey |  | fpkid |
| 2 | idx_er_sharebill_lk_fid |  | fid |

---

## 分摊明细-子表 t_er_expensesharerule

- **表名称：** 分摊明细-子表
- **表名：** t_er_expensesharerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 3 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 5 | fsharecurrency | 分摊币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 8 | fsharewaitseq | 待摊行号 | int4 | 32 |  | √ | 0 | 待摊行号 |
| 9 | fshareamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |
| 10 | fentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 11 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fshareappamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 13 | fentryexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 14 | fsharewaitid | 待摊明细id | int8 | 64 |  | √ | 0 | 待摊明细id |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fsharerate | 本次分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 本次分摊比例（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_expensesharerule_pkey |  | fdetailid |
| 2 | idx_er_expensesharerule_fseq |  | fid,fseq |

---

## 费用分摊单-多语言表 t_er_expensesharebill_l

- **表名称：** 费用分摊单-多语言表
- **表名：** t_er_expensesharebill_l

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
| 1 | t_er_expensesharebill_l_pkey |  | fpkid |
| 2 | idx_share_l_id |  | fid,flocaleid |

---

## 摊销明细-子表 t_er_expensesharedetail

- **表名称：** 摊销明细-子表
- **表名：** t_er_expensesharedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 3 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 4 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 6 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 7 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 10 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '1' | 是否抵扣 |
| 11 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 12 | fentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 13 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 14 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 16 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
| 17 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | '1' | 专票 |
| 18 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 19 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额（本位币） |
| 20 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | '0' | 发票类型,枚举: 0 :空 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 |
| 21 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 22 | ftaxclasscodeid | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 23 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 24 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |
| 25 | fitemfrom | 来源 | varchar | 2 |  | √ | '0' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 4 :分录导入 |
| 26 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 27 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 28 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 29 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 30 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 31 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 32 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 33 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 34 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 35 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 36 | flkwaitentryid | 待摊明细id | varchar | 200 |  | √ | ' ' | 待摊明细id |
| 37 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 38 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 39 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_expensesharedetail_fseq |  | fid,fseq |
| 2 | t_er_expensesharedetail_pkey |  | fdetailid |

---

## 费用分摊单-主表 t_er_expensesharebill

- **表名称：** 费用分摊单-主表
- **表名：** t_er_expensesharebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 4 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 5 | ftel | 联系方式 | varchar | 100 |  | √ | ' ' | 联系方式 |
| 6 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 9 | fsharecompanyid | 费用承担公司(分摊后) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 13 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fapplierpositionstr | fapplierpositionstr | varchar | 100 |  | √ | ' ' |  |
| 16 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 17 | fsharestatus | 分摊状态 | varchar | 30 |  | √ | ' ' | 分摊状态,枚举: A :分摊前 B :分摊中 C :分摊后 D :重新分摊 |
| 18 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fshareruleenddate | 结束月份 | timestamp | 0 |  |  | null | 结束月份 |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_expensesharebill :费用分摊单 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 26 | fwaitamount | 待分摊总金额 | numeric | 23 | 10 | √ | 0.0000000000 | 待分摊总金额 |
| 27 | fwaitapproveamount | 待分摊核定总金额 | numeric | 23 | 10 | √ | 0.0000000000 | 待分摊核定总金额 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 30 | fisenableinvoice | 是否启用发票云 | bpchar | 1 |  | √ | '0' | 是否启用发票云 |
| 31 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fimagenumber | 影像编号 | varchar | 255 |  | √ | ' ' | 影像编号 |
| 33 | fsharerule | 分摊规则 | varchar | 30 |  | √ | ' ' | 分摊规则,枚举: orgrule :按部门分摊 monthrule :按月分摊 yearrule :按年分摊 expenseitemrule :按费用项目分摊 |
| 34 | fsharemethod | 分摊方法 | varchar | 30 |  | √ | ' ' | 分摊方法,枚举: rate :比例分摊 avg :金额平均 amount :金额分摊 |
| 35 | fsumsharerate | 本次分摊比例合计 | numeric | 23 | 10 | √ | 0.0000000000 | 本次分摊比例合计 |
| 36 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 37 | fsharerulestartdate | 开始月份 | timestamp | 0 |  |  | null | 开始月份 |
| 38 | fshareway | 分摊方式 | bpchar | 1 |  | √ | 'B' | 分摊方式,枚举: A :事前分摊 B :事后分摊 |
| 39 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 40 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 43 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_share_fapplierid |  | fapplierid |
| 2 | idx_er_share_fbillno |  | fbillno |
| 3 | idx_er_share_fcreatorid |  | fcreatorid |
| 4 | idx_er_share_fbizdate_fbillno |  | fbizdate,fbillno |
| 5 | idx_er_share_fbillstatus |  | fbillstatus |
| 6 | t_er_expensesharebill_pkey |  | fid |
| 7 | idx_er_share_fcompanyid |  | fcompanyid |

---

## 费用分摊单-关联追踪表 t_er_expensesharebill_tc

- **表名称：** 费用分摊单-关联追踪表
- **表名：** t_er_expensesharebill_tc

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
| 1 | idx_er_expensesharebill_tc_tid |  | ftid |
| 2 | idx_er_expensesharebill_tc_tbill |  | ftbillid |
| 3 | idx_er_sharebill_tc_fbillid |  | ftbillid |
| 4 | t_er_expensesharebill_tc_pkey |  | fid |

---

## 待摊明细-子表 t_er_expensesharewait

- **表名称：** 待摊明细-子表
- **表名：** t_er_expensesharewait

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 3 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 4 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 6 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 7 | fsourceentryid | 源单分录ID | varchar | 100 |  | √ | ' ' | 源单分录ID |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '1' | 是否抵扣 |
| 10 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 12 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
| 13 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | '1' | 专票 |
| 14 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额（本位币） |
| 15 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | '0' | 发票类型,枚举: 0 :空 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | ftaxclasscodeid | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 18 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 19 | fsourcebillno | 源单编号 | varchar | 100 |  | √ | ' ' | 源单编号 |
| 20 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 21 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 22 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 23 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 24 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | fthiscurprice | 本次待摊核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 本次待摊核定不含税金额（本位币） |
| 26 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 27 | fthistax | fthistax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 28 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 29 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 30 | fthisapprovenotax | 本次待摊核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次待摊核定不含税金额 |
| 31 | fthisapplyamount | 本次待摊申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次待摊申请金额 |
| 32 | fentrysharedamount | 已摊销金额（用于计算可摊比例） | numeric | 23 | 10 | √ | 0.0000000000 | 已摊销金额（用于计算可摊比例） |
| 33 | fsrcbilltype | 源单类型 | varchar | 100 |  | √ | ' ' | 源单类型,枚举: er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 er_tripreimbursebill :差旅报销单 |
| 34 | fthisapproveamount | 本次待摊核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次待摊核定金额 |
| 35 | fthisapprovecurramount | 本次待摊核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 本次待摊核定金额（本位币） |
| 36 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 37 | fthiscurrapplyamount | 本次待摊申请金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 本次待摊申请金额(本位币) |
| 38 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 39 | fentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 40 | fthisapporvetax | 本次待摊抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次待摊抵扣税额 |
| 41 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 42 | fentrythisshareamount | fentrythisshareamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 43 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 44 | fthisiteminoutamount | 本次待摊转出金额 | numeric | 23 | 10 | √ | 0 | 本次待摊转出金额 |
| 45 | fitemfrom | 来源 | varchar | 2 |  | √ | '0' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 4 :分录导入 |
| 46 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 47 | fthisapprovetax | 本次待摊核定税额 | numeric | 23 | 10 | √ | 0 | 本次待摊核定税额 |
| 48 | fthisnotax | 本次待摊不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次待摊不含税金额 |
| 49 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 50 | fsourcebillid | 源单id | varchar | 100 |  | √ | ' ' | 源单id |
| 51 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 52 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 53 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 54 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_expensesharewait_pkey |  | fdetailid |
| 2 | idx_er_expensesharewait_fseq |  | fid,fseq |

---

## 费用分摊单-反写记录表 t_er_expensesharebill_wb

- **表名称：** 费用分摊单-反写记录表
- **表名：** t_er_expensesharebill_wb

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
| 1 | t_er_expensesharebill_wb_pkey |  | fentryid |
| 2 | idx_er_sharebill_wb_fid |  | fid |
