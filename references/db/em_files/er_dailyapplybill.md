# 费用申请单-er_dailyapplybill

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

## 费用明细-子表 t_er_dailyapplydetail

- **表名称：** 费用明细-子表
- **表名：** t_er_dailyapplydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 3 | fentrycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fgoodsnum | 酒水瓶数 | int4 | 32 |  | √ | 0 | 酒水瓶数 |
| 5 | forgiexpebalanceamount | 费用明细可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细可报销金额 |
| 6 | fwineway | 酒水来源 | varchar | 10 |  | √ | ' ' | 酒水来源,枚举: 1 :内部领用 2 :自行购买 3 :无酒水 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fpushedamount | 费用明细已借金额 | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细已借金额 |
| 9 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 10 | ffeequotetype | 换算方式(标准) | bpchar | 1 |  | √ | '0' | 换算方式(标准),枚举: 0 :直接汇率 1 :间接汇率 |
| 11 | fotherfeeamount | 酒水金额 | numeric | 23 | 10 | √ | 0 | 酒水金额 |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 13 | fisover | 超费用标准 | bpchar | 1 |  | √ | '0' | 超费用标准 |
| 14 | fcurotherfeeamount | 酒水金额 | numeric | 23 | 10 | √ | 0 | 酒水金额 |
| 15 | fotherstandamount | 酒水标准金额(页面不可见) | numeric | 23 | 10 | √ | 0 | 酒水标准金额(页面不可见) |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | foverdesc | 超标说明(暂未支持) | varchar | 255 |  | √ | ' ' | 超标说明(暂未支持) |
| 18 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 19 | fcurrapplyamount | 申请金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(本位币) |
| 20 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 21 | fcanloancurramount | 费用明细可借金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细可借金额(本位币) |
| 22 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 23 | fdaysnum | 住宿天数 | int4 | 32 |  | √ | 0 | 住宿天数 |
| 24 | fmeetitem | 会议事项 | varchar | 10 |  | √ | ' ' | 会议事项,枚举: 1 :伙食费 2 :酒店住宿 3 :交通费 4 :其他 |
| 25 | fpushedcurramount | 费用明细已借金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细已借金额(本位币) |
| 26 | ftreatnum | 招待人数 | int4 | 32 |  | √ | 0 | 招待人数 |
| 27 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 28 | fcontrolamt | 可申请金额 | numeric | 23 | 10 | √ | 0 | 可申请金额 |
| 29 | fcurothercontrolamt | 酒水可报金额 | numeric | 23 | 10 | √ | 0 | 酒水可报金额 |
| 30 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 31 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 32 | ffeestandid | 费用标准基础资料 | int8 | 64 |  | √ | 0 | [费用标准 er_standard](../em_files/er_standard.md) |
| 33 | ffeestandardamt | 费用标准金额(页面不可见) | numeric | 23 | 10 | √ | 0 | 费用标准金额(页面不可见) |
| 34 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 35 | ftreatway | 招待方式 | varchar | 10 |  | √ | ' ' | 招待方式,枚举: 1 :餐费 2 :酒店住宿 3 :酒水 4 :纪念品 |
| 36 | fotherstandarddesc | 酒水标准 | varchar | 255 |  | √ | ' ' | 酒水标准 |
| 37 | fcanloanamount | 费用明细可借金额 | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细可借金额 |
| 38 | fredml | 红酒（毫升） | int4 | 32 |  | √ | 0 | 红酒（毫升） |
| 39 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fmeetlevel | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 41 | fcityarea | 城市类别 | int8 | 64 |  | √ | 0 | [出差地域 er_triparea](../em_files/er_triparea.md) |
| 42 | fwhiteml | 白酒（毫升） | int4 | 32 |  | √ | 0 | 白酒（毫升） |
| 43 | fothercontrolamt | 酒水可报金额 | numeric | 23 | 10 | √ | 0 | 酒水可报金额 |
| 44 | fexpwithholdingamount | 已预提金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额(本位币) |
| 45 | fescortnum | 陪同人数 | int4 | 32 |  | √ | 0 | 陪同人数 |
| 46 | ffeecurrency | 币种(标准) | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 47 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | [报销级别 er_reimburselevel](../em_files/er_reimburselevel.md) |
| 48 | ffeeexchangerate | 汇率(标准) | numeric | 23 | 10 | √ | 0 | 汇率(标准) |
| 49 | freimbursedamount | 费用明细已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细已报销金额 |
| 50 | fexpebalanceamount | 费用明细可报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细可报销金额(本位币) |
| 51 | fcurcontrolamt | 可申请金额 | numeric | 23 | 10 | √ | 0 | 可申请金额 |
| 52 | freimbursedcurramount | 费用明细已报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 费用明细已报销金额(本位币) |
| 53 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 54 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 55 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 56 | ffeestandarddesc | 费用标准 | varchar | 255 |  | √ | ' ' | 费用标准 |

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
| 3 | finvokeinvoicecloud | 与发票云交互 | bpchar | 1 |  | √ | '0' | 与发票云交互 |
| 4 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | floanedamount | 已借金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已借金额 |
| 6 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fhasvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 8 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 11 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 12 | fapplierpositionstr | 职位文本 | varchar | 100 |  | √ | ' ' | 职位文本 |
| 13 | fisover | 超费用标准（提交后有值） | bpchar | 1 |  | √ | '0' | 超费用标准（提交后有值） |
| 14 | fneeduploadinvoice | 有待上传的纸票/附件 | bpchar | 1 |  | √ | '0' | 有待上传的纸票/附件 |
| 15 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 H :废弃 I :关闭 |
| 19 | fdaysnum | 住宿天数 | int4 | 32 |  | √ | 0 | 住宿天数 |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 22 | ftreatnum | 招待人数 | int4 | 32 |  | √ | 0 | 招待人数 |
| 23 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 24 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 25 | fisenableinvoice | 启用发票云 | bpchar | 1 |  | √ | '0' | 启用发票云 |
| 26 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 27 | fmeetgrade | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 28 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 29 | fattachmentacount | fattachmentacount | int8 | 64 |  | √ | 0 |  |
| 30 | fbillcanloanamount | 可借金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可借金额 |
| 31 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 32 | fnextauditor | 下一步审核人 | varchar | 100 |  | √ | ' ' | 下一步审核人 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 35 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fbalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额 |
| 37 | fisoverbudget | 超预算 | bpchar | 1 |  | √ | '0' | 超预算 |
| 38 | ftel | 联系方式 | varchar | 30 |  | √ | ' ' | 联系方式 |
| 39 | fmeetlevel | fmeetlevel | varchar | 10 |  | √ | ' ' |  |
| 40 | fcityarea | 城市类别 | int8 | 64 |  | √ | 0 | [出差地域 er_triparea](../em_files/er_triparea.md) |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fstdreimbursetype | 申请类型 | varchar | 30 |  | √ | ' ' | 申请类型,枚举: otherexpenses :其他 meetting :会议费标准 entertainment :招待费标准 expense :费用报账 |
| 44 | fescortnum | 陪同人数 | int4 | 32 |  | √ | 0 | 陪同人数 |
| 45 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_loanbill :出差借款单 er_tripreimbursebill :差旅费报销单 er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_dailyreimbursebill :费用报销单 er_repaymentbill :还款单 |
| 46 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | [报销级别 er_reimburselevel](../em_files/er_reimburselevel.md) |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 49 | fiscurrency | 多币种 | bpchar | 1 |  | √ | '0' | 多币种 |
| 50 | fbizitem | 业务事项 | int8 | 64 |  | √ | 0 | [业务事项 er_standard_type](../em_files/er_standard_type.md) |
| 51 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 52 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 53 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | [业务分类 er_projecttype](../em_files/er_projecttype.md) |
| 54 | fcurrencyid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
