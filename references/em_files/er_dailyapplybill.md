# 费用申请单-er_dailyapplybill

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

## 费用明细-子表 t_er_dailyapplydetail

- **表名称：** 费用明细-子表
- **表名：** t_er_dailyapplydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 3 | ftreatway | 招待方式 | varchar | 10 |  | √ | ' ' | 招待方式,枚举: 1 :餐费 2 :酒店住宿 3 :酒水 4 :纪念品 |
| 4 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fgoodsnum | 酒水瓶数 | int4 | 32 |  | √ | 0 | 酒水瓶数 |
| 6 | forgiexpebalanceamount | 费用明细可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细可报销金额 |
| 7 | fotherstandarddesc | 酒水标准 | varchar | 255 |  | √ | ' ' | 酒水标准 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fpushedamount | 费用明细已借金额 | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细已借金额 |
| 10 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 11 | fcanloanamount | 费用明细可借金额 | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细可借金额 |
| 12 | fotherfeeamount | 酒水金额 | numeric | 23 | 10 | √ | 0 | 酒水金额 |
| 13 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 15 | fmeetlevel | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 16 | fcityarea | 城市类别 | int8 | 64 |  | √ | 0 | 出差地域 er_triparea |
| 17 | fisover | 超费用标准 | bpchar | 1 |  | √ | '0' | 超费用标准 |
| 18 | fexpwithholdingamount | 已预提金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额(本位币) |
| 19 | fotherstandamount | 酒水标准金额(页面不可见) | numeric | 23 | 10 | √ | 0 | 酒水标准金额(页面不可见) |
| 20 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 21 | fescortnum | 陪同人数 | int4 | 32 |  | √ | 0 | 陪同人数 |
| 22 | foverdesc | 超标说明(暂未支持) | varchar | 255 |  | √ | ' ' | 超标说明(暂未支持) |
| 23 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 24 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | 报销级别 er_reimburselevel |
| 25 | fcurrapplyamount | 申请金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(本位币) |
| 26 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 27 | fcanloancurramount | 费用明细可借金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细可借金额(本位币) |
| 28 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 29 | fdaysnum | 住宿天数 | int4 | 32 |  | √ | 0 | 住宿天数 |
| 30 | freimbursedamount | 费用明细已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细已报销金额 |
| 31 | fmeetitem | 会议事项 | varchar | 10 |  | √ | ' ' | 会议事项,枚举: 1 :伙食费 2 :酒店住宿 3 :交通费 4 :其他 |
| 32 | fpushedcurramount | 费用明细已借金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细已借金额(本位币) |
| 33 | ftreatnum | 招待人数 | int4 | 32 |  | √ | 0 | 招待人数 |
| 34 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 35 | fcontrolamt | 可申请金额 | numeric | 23 | 10 | √ | 0 | 可申请金额 |
| 36 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 37 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 38 | fexpebalanceamount | 费用明细可报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细可报销金额(本位币) |
| 39 | ffeestandid | 费用标准基础资料 | int8 | 64 |  | √ | 0 | 费用标准 er_standard |
| 40 | freimbursedcurramount | 费用明细已报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细已报销金额(本位币) |
| 41 | ffeestandardamt | 费用标准金额(页面不可见) | numeric | 23 | 10 | √ | 0 | 费用标准金额(页面不可见) |
| 42 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 43 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 44 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 45 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 46 | ffeestandarddesc | 费用标准 | varchar | 255 |  | √ | ' ' | 费用标准 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_applydetail_fseq |  | fid,fseq |
| 2 | t_er_dailyapplydetail_pkey |  | fdetailid |

---

## 费用申请单-主表 t_er_dailyapplybill

- **表名称：** 费用申请单-主表
- **表名：** t_er_dailyapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 4 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | floanedamount | 已借金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已借金额 |
| 6 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 8 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 11 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 12 | fapplierpositionstr | 职位文本 | varchar | 100 |  | √ | ' ' | 职位文本 |
| 13 | fisover | 是否超标（提交后有值） | bpchar | 1 |  | √ | '0' | 是否超标（提交后有值） |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 H :废弃 I :关闭 |
| 17 | fdaysnum | 住宿天数 | int4 | 32 |  | √ | 0 | 住宿天数 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 20 | ftreatnum | 招待人数 | int4 | 32 |  | √ | 0 | 招待人数 |
| 21 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 22 | fisenableinvoice | 是否启用发票云 | bpchar | 1 |  | √ | '0' | 是否启用发票云 |
| 23 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 24 | fmeetgrade | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 25 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 26 | fattachmentacount | fattachmentacount | int8 | 64 |  | √ | 0 |  |
| 27 | fbillcanloanamount | 可借金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可借金额 |
| 28 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 29 | fnextauditor | 下一步审核人 | varchar | 100 |  | √ | ' ' | 下一步审核人 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 32 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fbalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额 |
| 34 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 35 | ftel | 联系方式 | varchar | 30 |  | √ | ' ' | 联系方式 |
| 36 | fmeetlevel | fmeetlevel | varchar | 10 |  | √ | ' ' |  |
| 37 | fcityarea | 城市类别 | int8 | 64 |  | √ | 0 | 出差地域 er_triparea |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fstdreimbursetype | 申请类型 | varchar | 30 |  | √ | ' ' | 申请类型,枚举: otherexpenses :其他 meetting :会议费标准 entertainment :招待费标准 expense :费用报账 |
| 41 | fescortnum | 陪同人数 | int4 | 32 |  | √ | 0 | 陪同人数 |
| 42 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_loanbill :出差借款单 er_tripreimbursebill :差旅费报销单 er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_dailyreimbursebill :费用报销单 er_repaymentbill :还款单 |
| 43 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | 报销级别 er_reimburselevel |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 47 | fbizitem | 业务事项 | int8 | 64 |  | √ | 0 | 业务事项 er_standard_type |
| 48 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 49 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 50 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_dyappbill_fcreateor |  | fcreatorid |
| 2 | t_er_dailyapplybill_pkey |  | fid |
| 3 | idx_er_dyappbill_faper |  | fapplierid |
| 4 | idx_er_dyappbill_fbno |  | fbillno |
| 5 | idx_er_dyappbill_fbsta |  | fbillstatus |
| 6 | idx_er_dyappbill_fdate_no |  | fbizdate,fbillno |
| 7 | idx_er_dyappbill_fcompanyid |  | fcompanyid |

---

## 项目干系人-多选基础资料表 t_er_dailyapplyower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_dailyapplyower

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
| 1 | idx_er_dailyapplyuser |  | fbasedataid |
| 2 | pk_t_er_dailyapplyower |  | fpkid |
| 3 | idx_er_dailyapplybill |  | fid |

---

## 费用申请单-多语言表 t_er_dailyapplybill_l

- **表名称：** 费用申请单-多语言表
- **表名：** t_er_dailyapplybill_l

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
| 1 | idx_er_dayappbill_l_flcid |  | fid,flocaleid |
| 2 | t_er_dailyapplybill_l_pkey |  | fpkid |
