# 额度申请单-er_reimctlapplybill

## 额度申请单-多语言表 t_er_reimctlapplybill_l

- **表名称：** 额度申请单-多语言表
- **表名：** t_er_reimctlapplybill_l

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
| 1 | pk_t_er_reimctlapplybill_l |  | fpkid |
| 2 | idx_er_ctlapplybill_l_flcid |  | fid,flocaleid |

---

## 额度申请单-主表 t_er_reimctlapplybill

- **表名称：** 额度申请单-主表
- **表名：** t_er_reimctlapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | ftotalamount | 年总额度 | numeric | 23 | 10 | √ | 0.0000000000 | 年总额度 |
| 4 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | floanedamount | 已借金额 | numeric | 23 | 10 | √ | 0 | 已借金额 |
| 6 | fcostdeptid | 费用承担部门（废弃） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fseptemberamount | 9月 | numeric | 23 | 10 | √ | 0.0000000000 | 9月 |
| 8 | fquarter2 | 2季度 | numeric | 23 | 10 | √ | 0.0000000000 | 2季度 |
| 9 | fquarter3 | 3季度 | numeric | 23 | 10 | √ | 0.0000000000 | 3季度 |
| 10 | fquarter4 | 4季度 | numeric | 23 | 10 | √ | 0.0000000000 | 4季度 |
| 11 | fjulyamount | 7月 | numeric | 23 | 10 | √ | 0.0000000000 | 7月 |
| 12 | fquarter1 | 1季度 | numeric | 23 | 10 | √ | 0.0000000000 | 1季度 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | faugustamount | 8月 | numeric | 23 | 10 | √ | 0.0000000000 | 8月 |
| 15 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 16 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 17 | fapplierpositionstr | 职位文本 | varchar | 100 |  | √ | ' ' | 职位文本 |
| 18 | fmayamount | 5月 | numeric | 23 | 10 | √ | 0.0000000000 | 5月 |
| 19 | fjanuaryamount | 1月 | numeric | 23 | 10 | √ | 0.0000000000 | 1月 |
| 20 | fdecemberamount | 12月 | numeric | 23 | 10 | √ | 0.0000000000 | 12月 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fjuneamount | 6月 | numeric | 23 | 10 | √ | 0.0000000000 | 6月 |
| 23 | fstdbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 24 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0 | 已预提金额 |
| 25 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 H :废弃 I :关闭 |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 28 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 29 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 30 | fattachmentacount | fattachmentacount | int8 | 64 |  | √ | 0 |  |
| 31 | fbillcanloanamount | 可借金额 | numeric | 23 | 10 | √ | 0 | 可借金额 |
| 32 | foctoberamount | 10月 | numeric | 23 | 10 | √ | 0.0000000000 | 10月 |
| 33 | famounttype | 额度类型 | bpchar | 1 |  | √ | '1' | 额度类型,枚举: 1 :个人额度 2 :部门额度 |
| 34 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 35 | fnextauditor | 下一步审核人 | varchar | 100 |  | √ | ' ' | 下一步审核人 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fbalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 39 | fnovemberamount | 11月 | numeric | 23 | 10 | √ | 0.0000000000 | 11月 |
| 40 | ftel | 联系方式 | varchar | 30 |  | √ | ' ' | 联系方式 |
| 41 | ffebruaryamount | 2月 | numeric | 23 | 10 | √ | 0.0000000000 | 2月 |
| 42 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 44 | fcostcompanyid | 费用承担公司（废弃） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_reimctlapplybill :额度申请单 |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | freimbursecontrolcomany | 额度控制公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 48 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 49 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 50 | fcurrency | 本币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 51 | fduedate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 52 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 53 | femployee | 职员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 54 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 55 | fmarchamount | 3月 | numeric | 23 | 10 | √ | 0.0000000000 | 3月 |
| 56 | faprilamount | 4月 | numeric | 23 | 10 | √ | 0.0000000000 | 4月 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_reimctlapplybill |  | fid |
| 2 | idx_er_ctlapply_fcompanyid |  | fcompanyid |
| 3 | idx_er_ctlapply_fcreatorid |  | fcreatorid |
| 4 | idx_er_ctlapply_bizdate_billno |  | fbillno,fbizdate |
| 5 | idx_er_ctlapply_fbillstatus |  | fbillstatus |
| 6 | idx_er_ctlapply_fapplierid |  | fapplierid |

---

## 申请明细-子表 t_er_applydetail

- **表名称：** 申请明细-子表
- **表名：** t_er_applydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 3 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fentryduedate | 有效期间.结束 | timestamp | 0 |  |  | null | 有效期间.结束 |
| 5 | forgiexpebalanceamount | 费用明细可报销金额 | numeric | 23 | 10 | √ | 0 | 费用明细可报销金额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcurrexpenseamount | 申请金额(本位币) | numeric | 23 | 10 | √ | 0 | 申请金额(本位币) |
| 8 | fpushedamount | 费用明细已借金额 | numeric | 23 | 10 | √ | 0 | 费用明细已借金额 |
| 9 | fentrycostcompany | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fcanloanamount | 费用明细可借金额 | numeric | 23 | 10 | √ | 0 | 费用明细可借金额 |
| 11 | fentryemployee | 职员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 13 | fentrycompany | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fexpwithholdingamount | 已预提金额(本位币) | numeric | 23 | 10 | √ | 0 | 已预提金额(本位币) |
| 15 | fentrycostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fstdproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 17 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 18 | fentryeffectivedate | 有效期间.开始 | timestamp | 0 |  |  | null | 有效期间.开始 |
| 19 | fcanloancurramount | 费用明细可借金额(本位币) | numeric | 23 | 10 | √ | 0 | 费用明细可借金额(本位币) |
| 20 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 21 | freimbursedamount | 费用明细已报销金额 | numeric | 23 | 10 | √ | 0 | 费用明细已报销金额 |
| 22 | fpushedcurramount | 费用明细已借金额(本位币) | numeric | 23 | 10 | √ | 0 | 费用明细已借金额(本位币) |
| 23 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0 | 核定金额（本位币） |
| 24 | fexpebalanceamount | 费用明细可报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 费用明细可报销金额(本位币) |
| 25 | fexpenseamount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 26 | freimbursedcurramount | 费用明细已报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 费用明细已报销金额(本位币) |
| 27 | fentryremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 30 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 31 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0 | 已预提金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ctlapplydetail_fseq |  | fid,fseq |
| 2 | pk_t_er_applydetail |  | fentryid |

---

## 额度明细-子表 t_er_reimctldetail

- **表名称：** 额度明细-子表
- **表名：** t_er_reimctldetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freimctltotalamount | 年总额度 | numeric | 23 | 10 | √ | 0.000000 | 年总额度 |
| 3 | freimctlemployee | 职员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | freimctlcompany | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | freimctlcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | freimctlmonth10 | 10月 | numeric | 23 | 10 | √ | 0.000000 | 10月 |
| 8 | freimctlmonth11 | 11月 | numeric | 23 | 10 | √ | 0.000000 | 11月 |
| 9 | freimctlmonth12 | 12月 | numeric | 23 | 10 | √ | 0.000000 | 12月 |
| 10 | freimctlmonth2 | 2月 | numeric | 23 | 10 | √ | 0.000000 | 2月 |
| 11 | freimctlmonth3 | 3月 | numeric | 23 | 10 | √ | 0.000000 | 3月 |
| 12 | freimctlmonth4 | 4月 | numeric | 23 | 10 | √ | 0.000000 | 4月 |
| 13 | freimctlexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 14 | freimctlmonth5 | 5月 | numeric | 23 | 10 | √ | 0.000000 | 5月 |
| 15 | freimctlmonth6 | 6月 | numeric | 23 | 10 | √ | 0.000000 | 6月 |
| 16 | freimctldatayear | 年度 | varchar | 4 |  | √ | ' ' | 年度,枚举: |
| 17 | freimctlmonth7 | 7月 | numeric | 23 | 10 | √ | 0.000000 | 7月 |
| 18 | freimctlmonth8 | 8月 | numeric | 23 | 10 | √ | 0.000000 | 8月 |
| 19 | freimctlmonth9 | 9月 | numeric | 23 | 10 | √ | 0.000000 | 9月 |
| 20 | freimctlquarter3 | 第三季度 | numeric | 23 | 10 | √ | 0 | 第三季度 |
| 21 | freimctlquarter2 | 第二季度 | numeric | 23 | 10 | √ | 0 | 第二季度 |
| 22 | freimctlquarter4 | 第四季度 | numeric | 23 | 10 | √ | 0 | 第四季度 |
| 23 | freimctlquarter1 | 第一季度 | numeric | 23 | 10 | √ | 0 | 第一季度 |
| 24 | freimctlremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 25 | freimctlcostcompany | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | freimctlmonth1 | 1月 | numeric | 23 | 10 | √ | 0.000000 | 1月 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_reimctldetail_fseq |  | fid,fseq |
| 2 | pk_t_er_reimctldetail |  | fentryid |
