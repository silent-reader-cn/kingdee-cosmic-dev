# 缴费明细-tnd_paymanage

## 缴费明细-主表 t_src_project

- **表名称：** 缴费明细-主表
- **表名：** t_src_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanschemeid | fplanschemeid | int8 | 64 |  | √ | 0 |  |
| 3 | freplydate | freplydate | timestamp | 0 |  |  | null |  |
| 4 | faptschemeid | faptschemeid | int8 | 64 |  | √ | 0 |  |
| 5 | fanswerdate | fanswerdate | timestamp | 0 |  |  | null |  |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 8 | fsrctypeid | fsrctypeid | int8 | 64 |  | √ | 0 |  |
| 9 | fpentitykey | fpentitykey | varchar | 50 |  | √ | ' ' |  |
| 10 | ffeewayid | ffeewayid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayenddate | fpayenddate | timestamp | 0 |  |  | null |  |
| 12 | forigin | forigin | varchar | 30 |  | √ | ' ' |  |
| 13 | fscoretype | fscoretype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 15 | fisbyproject | fisbyproject | bpchar | 1 |  | √ | '0' |  |
| 16 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 17 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 19 | fratio_oth | fratio_oth | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 21 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 22 | ftodotask | ftodotask | varchar | 255 |  | √ | ' ' |  |
| 23 | falterqty | falterqty | int8 | 64 |  | √ | 0 |  |
| 24 | fbidcount | fbidcount | int4 | 32 |  | √ | 0 |  |
| 25 | fwinerqty | fwinerqty | int8 | 64 |  | √ | 0 |  |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | ftecschemeid | ftecschemeid | int8 | 64 |  | √ | 0 |  |
| 28 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 29 | fnodename | fnodename | varchar | 50 |  | √ | ' ' |  |
| 30 | fscoremethod | fscoremethod | bpchar | 1 |  | √ | ' ' |  |
| 31 | fsendtendertime | fsendtendertime | timestamp | 0 |  |  | null |  |
| 32 | fstopbiddate | fstopbiddate | timestamp | 0 |  |  | null |  |
| 33 | fruleassess | fruleassess | bpchar | 1 |  | √ | ' ' |  |
| 34 | fratio_syn | fratio_syn | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 36 | ffeeitemid | ffeeitemid | int8 | 64 |  | √ | 0 |  |
| 37 | fbiderqty | fbiderqty | int8 | 64 |  | √ | 0 |  |
| 38 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 39 | fisautoopen | fisautoopen | bpchar | 1 |  | √ | '0' |  |
| 40 | fisviepublish | fisviepublish | bpchar | 1 |  | √ | '0' |  |
| 41 | ftieredtype | ftieredtype | bpchar | 1 |  | √ | '1' |  |
| 42 | fdecidedate | fdecidedate | timestamp | 0 |  |  | null |  |
| 43 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 44 | fwinruleid | fwinruleid | int8 | 64 |  | √ | 0 |  |
| 45 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 46 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsystype | fsystype | bpchar | 1 |  | √ | '1' |  |
| 48 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 49 | fsurplusamount | fsurplusamount | numeric | 23 | 10 | √ | 0 |  |
| 50 | fsupopentype | fsupopentype | bpchar | 1 |  | √ | '1' |  |
| 51 | fopentype | fopentype | bpchar | 1 |  | √ | ' ' |  |
| 52 | fclosetask | fclosetask | varchar | 255 |  | √ | ' ' |  |
| 53 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 54 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 55 | fismultipackage | fismultipackage | bpchar | 1 |  | √ | '0' |  |
| 56 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 57 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 58 | fopenstatus | fopenstatus | bpchar | 1 |  | √ | '1' |  |
| 59 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 60 | ftaxtype | ftaxtype | varchar | 30 |  | √ | ' ' |  |
| 61 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 62 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 63 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 64 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 65 | fisbypackage | fisbypackage | bpchar | 1 |  | √ | '0' |  |
| 66 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 67 | fentitykey | fentitykey | varchar | 50 |  | √ | ' ' |  |
| 68 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 69 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 70 | fratio_biz | fratio_biz | numeric | 23 | 10 | √ | 0 |  |
| 71 | fratio_tec | fratio_tec | numeric | 23 | 10 | √ | 0 |  |
| 72 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 73 | fisbypackage_apt | fisbypackage_apt | bpchar | 1 |  | √ | '0' |  |
| 74 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 75 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 76 | fextfilterid | fextfilterid | int8 | 64 |  | √ | 0 |  |
| 77 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 78 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 79 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 80 | fratiotype | fratiotype | bpchar | 1 |  | √ | '1' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_sourceid |  | fsourceid |
| 2 | pk_src_project |  | fid |
| 3 | idx_src_project_parentid |  | fparentid |
| 4 | idx_src_project_sourceclassid |  | fsourceclassid |
| 5 | idx_src_project_status |  | fopenstatus |
| 6 | idx_src_project_type |  | fsrctypeid |

---

## 凭证附件-附件表 t_src_paymententry_fj1

- **表名称：** 凭证附件-附件表
- **表名：** t_src_paymententry_fj1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_paymententry_fj1 |  | fpkid |
| 2 | idx_src_paymententry_fj1_bid |  | fbasedataid |
| 3 | idx_src_paymententry_fj1_eid |  | fentryid |

---

## 费用明细分录-子表 t_src_paymententry

- **表名称：** 费用明细分录-子表
- **表名：** t_src_paymententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpackfeeitemid | fpackfeeitemid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | ftransferdate | ftransferdate | timestamp | 0 |  |  | null |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fresult | fresult | bpchar | 1 |  | √ | ' ' |  |
| 7 | freturnopinion | freturnopinion | varchar | 100 |  | √ | ' ' |  |
| 8 | fcfmdate | fcfmdate | timestamp | 0 |  |  | null |  |
| 9 | ffeewayid | 收费方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | ftransferuserid | ftransferuserid | int8 | 64 |  | √ | 0 |  |
| 12 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 13 | fsurplustype | fsurplustype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fcarryoveropinion | fcarryoveropinion | varchar | 100 |  | √ | ' ' |  |
| 15 | fconfirmdate | fconfirmdate | timestamp | 0 |  |  | null |  |
| 16 | freturndate | freturndate | timestamp | 0 |  |  | null |  |
| 17 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 18 | fisfeeagent | fisfeeagent | bpchar | 1 |  | √ | '0' |  |
| 19 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 20 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 21 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 22 | fcarryoverdate | fcarryoverdate | timestamp | 0 |  |  | null |  |
| 23 | fusesurplus | fusesurplus | numeric | 23 | 10 | √ | 0 |  |
| 24 | frejectopinion | frejectopinion | varchar | 100 |  | √ | ' ' |  |
| 25 | ffeeitemid | 收费项 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 28 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | famount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 30 | fpayamount | 实收金额 | numeric | 23 | 10 | √ | 0 | 实收金额 |
| 31 | freturnuserid | freturnuserid | int8 | 64 |  | √ | 0 |  |
| 32 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 33 | fsurplusamount | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |
| 34 | fpresurplusamount | fpresurplusamount | numeric | 23 | 10 | √ | 0 |  |
| 35 | fpaystatus | 缴费状态 | bpchar | 1 |  | √ | ' ' | 缴费状态,枚举: A :待收款 B :已收款\|待确认 C :已收款\|已确认 D :已退还 E :已转结余 F :免交 |
| 36 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 37 | frejectdate | frejectdate | timestamp | 0 |  |  | null |  |
| 38 | ffeeamount | 收费金额 | numeric | 23 | 10 | √ | 0 | 收费金额 |
| 39 | fcarryoveruserid | fcarryoveruserid | int8 | 64 |  | √ | 0 |  |
| 40 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 41 | ftransferamount | ftransferamount | numeric | 23 | 10 | √ | 0 |  |
| 42 | fremark | 收款说明 | varchar | 100 |  | √ | ' ' | 收款说明 |
| 43 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 44 | fconfirmuserid | fconfirmuserid | int8 | 64 |  | √ | 0 |  |
| 45 | fusedate | fusedate | timestamp | 0 |  |  | null |  |
| 46 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 47 | fsurplusid | fsurplusid | int8 | 64 |  | √ | 0 |  |
| 48 | freturnamount | freturnamount | numeric | 23 | 10 | √ | 0 |  |
| 49 | fcarryoveramount | fcarryoveramount | numeric | 23 | 10 | √ | 0 |  |
| 50 | ftransferopinion | ftransferopinion | varchar | 100 |  | √ | ' ' |  |
| 51 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 52 | frejectuserid | frejectuserid | int8 | 64 |  | √ | 0 |  |
| 53 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 54 | fconfirmopinion | fconfirmopinion | varchar | 255 |  | √ | ' ' |  |
| 55 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 56 | fpaydate | 收款时间 | timestamp | 0 |  |  | null | 收款时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_paymententry_fct |  | fcreatetime |
| 2 | idx_src_paymententry_fpg |  | fpackageid |
| 3 | idx_src_paymententry_fid |  | fid |
| 4 | idx_src_paymententry_ftype |  | fsurplustype |
| 5 | idx_src_paymententry_fbillno |  | fbillno |
| 6 | pk_src_paymententry |  | fentryid |
| 7 | idx_src_paymententry_fsup |  | fsupplierid |
