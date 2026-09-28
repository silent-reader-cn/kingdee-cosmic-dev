# 立项单-er_applyprojectbill

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

## 分摊明细-子表 t_er_applyprojectrule

- **表名称：** 分摊明细-子表
- **表名：** t_er_applyprojectrule

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
| 1 | pk_t_er_applyprojectrule |  | fdetailid |
| 2 | idx_t_er_applyprorl_fseq |  | fentryid,fseq |

---

## 立项单-主表 t_er_applyprojectbill

- **表名称：** 立项单-主表
- **表名：** t_er_applyprojectbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fwltype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 4 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | floanedamount | 已预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预付金额 |
| 6 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 8 | fisbeforeshare | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fprojectnamedesc | 立项名称 | varchar | 255 |  | √ | ' ' | 立项名称 |
| 11 | fapplierpositionstr | 职位文本 | varchar | 100 |  | √ | ' ' | 职位文本 |
| 12 | fdetailtype | 立项类型 | varchar | 50 |  | √ | 'biztype_applybill' | 立项类型,枚举: biztype_applybill :立项申请 biztype_changebill :立项变更 biztype_sharebill :立项分摊 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 15 | fstdbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 16 | fischange | fischange | bpchar | 1 |  | √ | '0' |  |
| 17 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 H :废弃 I :关闭 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fdescription | 说明 | varchar | 1000 |  | √ | ' ' | 说明 |
| 21 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 22 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 23 | fsharerule | 分摊规则 | varchar | 50 |  | √ | 'monthrule' | 分摊规则,枚举: monthrule :按月分摊 yearrule :按年分摊 orgrule :按部门分摊 |
| 24 | fbillcanloanamount | 可预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可预付金额 |
| 25 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 26 | fchangetimes | 变更次数 | int4 | 32 |  | √ | 0 | 变更次数 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fbalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额 |
| 30 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 31 | ftel | 联系方式 | varchar | 30 |  | √ | ' ' | 联系方式 |
| 32 | fisshared | 是否分摊 | bpchar | 1 |  | √ | '0' | 是否分摊 |
| 33 | fwlunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 34 | fchangetype | 变更类型 | bpchar | 1 |  | √ | '0' | 变更类型,枚举: A :不限 B :调增 C :调减 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fusedamount | 已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额 |
| 37 | fisimport | 是否导入 | bpchar | 1 |  | √ | '0' | 是否导入 |
| 38 | fchangeamount | 累计变更金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更金额 |
| 39 | fcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_applyprojectbill :立项单 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | ffiperiod | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 44 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 45 | facapproveamount | 变更后核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定金额 |
| 46 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | fsharemethod | 分摊方法 | varchar | 50 |  | √ | 'rate' | 分摊方法,枚举: rate :比例分摊 avg :金额平均 amount :金额分摊 |
| 48 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 49 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | 业务分类 er_projecttype |
| 50 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 51 | fbilltype | fbilltype | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_applyprojectbill |  | fid |
| 2 | idx_er_applyproject_faper |  | fapplierid |
| 3 | idx_er_applyproject_fbno |  | fbillno |
| 4 | idx_er_applyproject_fcompanyid |  | fcompanyid |
| 5 | idx_er_applyproject_fcreateor |  | fcreatorid |
| 6 | idx_er_applyproject_fbsta |  | fbillstatus |
| 7 | idx_er_applyproject_fdate_no |  | fbizdate,fbillno |

---

## 立项明细-子表 t_er_applyprojectentry

- **表名称：** 立项明细-子表
- **表名：** t_er_applyprojectentry

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
| 11 | faccurprice | 变更后核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定不含税金额（本位币） |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 13 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额（本位币） |
| 14 | fsourcebillno | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |
| 15 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 16 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 17 | fcurrapplyamount | 申请金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(本位币) |
| 18 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 19 | fcanloancurramount | 可预付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 可预付金额(本位币) |
| 20 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: er_applyprojectbill :立项单 |
| 22 | fentryproducttype | 产品类别 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 23 | facexpeapprovecurramount | 变更后核定金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定金额(本位币) |
| 24 | fpushedcurramount | 已预付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已预付金额(本位币) |
| 25 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 26 | fexpeapprovecurramount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额(本位币) |
| 27 | fentryapplyprojectamount | 立项金额 | numeric | 23 | 10 | √ | 0.0000000000 | 立项金额 |
| 28 | fentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 29 | fentryremark | 说明 | varchar | 500 |  | √ | ' ' | 说明 |
| 30 | fentrychangeamount | 累计变更金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更金额(本位币) |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 33 | fentrywltype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 34 | fentrywlunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 35 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 36 | fcanloanamount | 可预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可预付金额 |
| 37 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 38 | fentrycostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fexpwithholdingamount | 已预提金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额(本位币) |
| 40 | fchangecurprice | 累计变更核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更核定不含税金额（本位币） |
| 41 | fitemfrom | 分录来源 | bpchar | 1 |  | √ | '0' | 分录来源,枚举: 0 :手工添加 5 :关联生成 |
| 42 | fentrychangeableamount | 可变更金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可变更金额 |
| 43 | freimbursedamount | 已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额 |
| 44 | facorientryamount | 变更后不含税 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后不含税 |
| 45 | fchangetaxamount | 累计变更税额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更税额 |
| 46 | fchangeprice | 累计变更核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更核定不含税金额 |
| 47 | factaxamount | 变更后税额 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后税额 |
| 48 | fexpebalanceamount | 可报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额(本位币) |
| 49 | fentryorichangeamount | 累计变更金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更金额 |
| 50 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 51 | fchangeorientryamount | 累计变更不含税 | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更不含税 |
| 52 | freimbursedcurramount | 已报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额(本位币) |
| 53 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 54 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 55 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_applyprojectentry |  | fentryid |
| 2 | idx_er_applyprojectentry_fseq |  | fid,fseq |

---

## 立项单-分表 t_er_applyprojectbill_s

- **表名称：** 立项单-分表
- **表名：** t_er_applyprojectbill_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 3 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 4 | favailableamount | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 5 | fcostimateamount | 暂估金额 | numeric | 23 | 10 | √ | 0 | 暂估金额 |
| 6 | fcancontractamount | 可用合同金额 | numeric | 23 | 10 | √ | 0 | 可用合同金额 |
| 7 | fnonpayamount | 待付金额 | numeric | 23 | 10 | √ | 0 | 待付金额 |
| 8 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 9 | fcontractamount | 合同金额 | numeric | 23 | 10 | √ | 0 | 合同金额 |
| 10 | fpayamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 11 | fisenableinvoice | 是否启用发票云 | bpchar | 1 |  | √ | '0' | 是否启用发票云 |
| 12 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_applyprojectbill_s |  | fid |
| 2 | idx_er_applyprojectbill_s_fid |  | fcontractamount |

---

## 关联子实体-子表 t_er_applyprojectbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_applyprojectbill_lk

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
| 1 | pk_er_applyprojectbill_lk |  | fpkid |
| 2 | idx_er_applyproject_lk_fid |  | fid |

---

## 立项单-多语言表 t_er_applyprojectbill_l

- **表名称：** 立项单-多语言表
- **表名：** t_er_applyprojectbill_l

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
| 1 | idx_er_applyproject_l_flcid |  | fid,flocaleid |
| 2 | pk_er_applyprojectbill_l |  | fpkid |

---

## 项目干系人-多选基础资料表 t_er_applyprojectower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_applyprojectower

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
| 1 | idx_er_applyprojectower_fid |  | fid |
| 2 | pk_er_applyprojectower |  | fpkid |

---

## 关联子实体-子表 t_er_applyprojectentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_applyprojectentry_lk

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
| 1 | pk_er_applyprojectentry_lk |  | fpkid |
| 2 | idx_er_applyprojectet_lk_fetid |  | fentryid |

---

## 立项明细-分表 t_er_applyprojectentry_s

- **表名称：** 立项明细-分表
- **表名：** t_er_applyprojectentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpcontractamount | 合同金额（本位币） | numeric | 23 | 10 | √ | 0 | 合同金额（本位币） |
| 3 | foriexpcontractamount | 合同金额 | numeric | 23 | 10 | √ | 0 | 合同金额 |
| 4 | fexpcancontractamount | 可用金额（合同本位币） | numeric | 23 | 10 | √ | 0 | 可用金额（合同本位币） |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | foriexpcancontractamount | 可用金额（合同） | numeric | 23 | 10 | √ | 0 | 可用金额（合同） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_applyprojectentry_s |  | fentryid |
| 2 | idx_er_applyprojectentry_s_fid |  | foriexpcontractamount |

---

## 立项单-关联追踪表 t_er_applyprojectbill_tc

- **表名称：** 立项单-关联追踪表
- **表名：** t_er_applyprojectbill_tc

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
| 1 | pk_er_applyprojectbill_tc |  | fid |
| 2 | idx_er_applyprojectbill_tc_tbill |  | ftbillid |
| 3 | idx_er_applyprojectbill_tc_tid |  | ftid |
| 4 | idx_er_applyproject_tc_fsbld |  | fsbillid |
| 5 | idx_er_applyproject_tc_ftbld |  | ftbillid |

---

## 摊销明细-子表 t_er_applyprojectshared

- **表名称：** 摊销明细-子表
- **表名：** t_er_applyprojectshared

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
| 10 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 11 | fentrycostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 13 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
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
| 30 | fentrywltype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_applyprojectshared |  | fdetailid |
| 2 | idx_er_applyprosd_fseq |  | fid,fseq |

---

## 立项单-反写记录表 t_er_applyprojectbill_wb

- **表名称：** 立项单-反写记录表
- **表名：** t_er_applyprojectbill_wb

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
| 1 | idx_er_applyproject_wb_fid |  | fid |
| 2 | pk_er_applyprojectbill_wb |  | fentryid |
