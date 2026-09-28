# 立项单-er_applyprojectbill

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

## 分摊明细-子表 t_er_applyprojectrule

- **表名称：** 分摊明细-子表
- **表名：** t_er_applyprojectrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 2 | fshareremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 5 | fstdentrycostcenterrule | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fshareamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |
| 11 | fentrycostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 3 | fwltype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 4 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | floanedamount | 已预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预付金额 |
| 6 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fhasvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 8 | fisbeforeshare | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fprojectnamedesc | 立项名称 | varchar | 255 |  | √ | ' ' | 立项名称 |
| 11 | fapplierpositionstr | 职位文本 | varchar | 100 |  | √ | ' ' | 职位文本 |
| 12 | fneeduploadinvoice | 有待上传的纸票/附件 | bpchar | 1 |  | √ | '0' | 有待上传的纸票/附件 |
| 13 | fdetailtype | 立项类型 | varchar | 50 |  | √ | 'biztype_applybill' | 立项类型,枚举: biztype_applybill :立项申请 biztype_changebill :立项变更 biztype_sharebill :立项分摊 |
| 14 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 17 | fstdbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 18 | fischange | fischange | bpchar | 1 |  | √ | '0' |  |
| 19 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 H :废弃 I :关闭 |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fdescription | 说明 | varchar | 1000 |  | √ | ' ' | 说明 |
| 23 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 24 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 25 | fsharerule | 分摊规则 | varchar | 50 |  | √ | 'monthrule' | 分摊规则,枚举: monthrule :按月分摊 yearrule :按年分摊 orgrule :按部门分摊 |
| 26 | fbillcanloanamount | 可预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可预付金额 |
| 27 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 28 | fchangetimes | 变更次数 | int4 | 32 |  | √ | 0 | 变更次数 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fbalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额 |
| 32 | fisoverbudget | 超预算 | bpchar | 1 |  | √ | '0' | 超预算 |
| 33 | ftel | 联系方式 | varchar | 30 |  | √ | ' ' | 联系方式 |
| 34 | fisshared | 分摊 | bpchar | 1 |  | √ | '0' | 分摊 |
| 35 | fwlunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 36 | fchangetype | 变更类型 | bpchar | 1 |  | √ | '0' | 变更类型,枚举: A :不限 B :调增 C :调减 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fusedamount | 已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额 |
| 39 | fisimport | 导入 | bpchar | 1 |  | √ | '0' | 导入 |
| 40 | fchangeamount | 累计变更金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计变更金额 |
| 41 | fcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_applyprojectbill :立项单 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | ffiperiod | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 46 | fiscurrency | 多币种 | bpchar | 1 |  | √ | '0' | 多币种 |
| 47 | facapproveamount | 变更后核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定金额 |
| 48 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | fsharemethod | 分摊方法 | varchar | 50 |  | √ | 'rate' | 分摊方法,枚举: rate :比例分摊 avg :金额平均 amount :金额分摊 |
| 50 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 51 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | [业务分类 er_projecttype](../em_files/er_projecttype.md) |
| 52 | fcurrencyid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 53 | fbilltype | fbilltype | int8 | 64 |  | √ | 0 |  |

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
| 3 | fwithholdingtaxrate | 预扣税率 | numeric | 23 | 10 | √ | 0 | 预扣税率 |
| 4 | facprice | 变更后核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定不含税金额 |
| 5 | fentrycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 7 | forgiexpebalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额 |
| 8 | fsourceentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fpushedamount | 已预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预付金额 |
| 11 | facexpeapproveamount | 变更后核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定金额 |
| 12 | faccurprice | 变更后核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定不含税金额（本位币） |
| 13 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 14 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额（本位币） |
| 15 | fsourcebillno | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |
| 16 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 17 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 18 | fcurrapplyamount | 申请金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(本位币) |
| 19 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 20 | fcanloancurramount | 可预付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 可预付金额(本位币) |
| 21 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: er_applyprojectbill :立项单 |
| 23 | fentryproducttype | 产品类别 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 24 | facexpeapprovecurramount | 变更后核定金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 变更后核定金额(本位币) |
| 25 | fpushedcurramount | 已预付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已预付金额(本位币) |
| 26 | fapplyamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 27 | fexpeapprovecurramount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额(本位币) |
| 28 | fentryapplyprojectamount | 立项金额 | numeric | 23 | 10 | √ | 0.0000000000 | 立项金额 |
| 29 | fentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 30 | fentryremark | 说明 | varchar | 500 |  | √ | ' ' | 说明 |
| 31 | fentrychangeamount | (变更前)累计变更金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | (变更前)累计变更金额(本位币) |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 34 | fentrywltype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 35 | fentrywlunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 36 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 37 | fcanloanamount | 可预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可预付金额 |
| 38 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 39 | fentrycostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fcurwithholdingtaxamount | 预扣税额（本位币） | numeric | 23 | 10 | √ | 0 | 预扣税额（本位币） |
| 41 | fexpwithholdingamount | 已预提金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额(本位币) |
| 42 | fchangecurprice | (变更前)累计变更核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | (变更前)累计变更核定不含税金额（本位币） |
| 43 | fitemfrom | 分录来源 | bpchar | 1 |  | √ | '0' | 分录来源,枚举: 0 :手工添加 5 :关联生成 |
| 44 | fentrychangeableamount | 可变更金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可变更金额 |
| 45 | freimbursedamount | 已报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额 |
| 46 | facorientryamount | 变更后不含税 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后不含税 |
| 47 | fchangetaxamount | (变更前)累计变更税额 | numeric | 23 | 10 | √ | 0.0000000000 | (变更前)累计变更税额 |
| 48 | fchangeprice | (变更前)累计变更核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | (变更前)累计变更核定不含税金额 |
| 49 | factaxamount | 变更后税额 | numeric | 23 | 10 | √ | 0.0000000000 | 变更后税额 |
| 50 | fexpebalanceamount | 可报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额(本位币) |
| 51 | fentryorichangeamount | (变更前)累计变更金额 | numeric | 23 | 10 | √ | 0.0000000000 | (变更前)累计变更金额 |
| 52 | fwithholdingtaxamount | 预扣税额 | numeric | 23 | 10 | √ | 0 | 预扣税额 |
| 53 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 54 | fchangeorientryamount | (变更前)累计变更不含税 | numeric | 23 | 10 | √ | 0.0000000000 | (变更前)累计变更不含税 |
| 55 | freimbursedcurramount | 已报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已报销金额(本位币) |
| 56 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 57 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 58 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

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
| 2 | finvokeinvoicecloud | 与发票云交互 | bpchar | 1 |  | √ | '0' | 与发票云交互 |
| 3 | fcostimateamount | 暂估金额 | numeric | 23 | 10 | √ | 0 | 暂估金额 |
| 4 | fnonpayamount | 待付金额 | numeric | 23 | 10 | √ | 0 | 待付金额 |
| 5 | fcontractamount | 合同金额 | numeric | 23 | 10 | √ | 0 | 合同金额 |
| 6 | fpayamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 7 | fisenableinvoice | 启用发票云 | bpchar | 1 |  | √ | '0' | 启用发票云 |
| 8 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 9 | ftotalcurwhtaxamount | 预扣税合计（费用） | numeric | 23 | 10 | √ | 0 | 预扣税合计（费用） |
| 10 | favailableamount | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 11 | ftotalwhtaxamount | 预扣税原币合计（费用） | numeric | 23 | 10 | √ | 0 | 预扣税原币合计（费用） |
| 12 | fcancontractamount | 可用合同金额 | numeric | 23 | 10 | √ | 0 | 可用合同金额 |
| 13 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 14 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
| 4 | foriexpapplyprotaxamount | 立项税额 | numeric | 23 | 10 | √ | 0 | 立项税额 |
| 5 | fexpcancontractamount | 可用合同金额本位币 | numeric | 23 | 10 | √ | 0 | 可用合同金额本位币 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | foriexpcancontractamount | 可用合同金额 | numeric | 23 | 10 | √ | 0 | 可用合同金额 |

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
| 4 | fentrycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 6 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 9 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 10 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 11 | fentrycostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 13 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
| 14 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额（本位币） |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |
| 17 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 18 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 19 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 21 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fentryproducttype | 产品类别 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 23 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 24 | fentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 25 | flkwaitentryid | 待摊明细id | varchar | 200 |  | √ | ' ' | 待摊明细id |
| 26 | fissharepush | 已生成分摊单 | bpchar | 1 |  | √ | '0' | 已生成分摊单 |
| 27 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 29 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 30 | fentrywltype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |

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
