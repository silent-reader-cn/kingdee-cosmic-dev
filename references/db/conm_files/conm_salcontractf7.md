# 销售合同F7-conm_salcontractf7

## 销售合同F7-主表 t_conm_salcontract

- **表名称：** 销售合同F7-主表
- **表名：** t_conm_salcontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 4 | fcancelstatus | fcancelstatus | varchar | 5 |  | √ | ' ' |  |
| 5 | fsplitschemeid | fsplitschemeid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | freviewstatus | freviewstatus | varchar | 5 |  | √ | ' ' |  |
| 8 | fterminatestatus | 终止状态 | varchar | 5 |  | √ | ' ' | 终止状态,枚举: A :未终止 B :已终止 |
| 9 | ffreezerid | ffreezerid | int8 | 64 |  | √ | 0 |  |
| 10 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 11 | fvaliddate | fvaliddate | timestamp | 0 |  |  | null |  |
| 12 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 13 | fbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 14 | fversion | fversion | varchar | 30 |  | √ | '1' |  |
| 15 | fconfirmdate | fconfirmdate | timestamp | 0 |  |  | null |  |
| 16 | ftotalamountcn | ftotalamountcn | varchar | 50 |  | √ | ' ' |  |
| 17 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 18 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fmpmrecmethod | fmpmrecmethod | varchar | 50 |  | √ | ' ' |  |
| 21 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 22 | fbillcretype | fbillcretype | varchar | 5 |  | √ | '0' |  |
| 23 | fbiztimeend | fbiztimeend | timestamp | 0 |  |  | null |  |
| 24 | fbillname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 25 | ftypeid | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 26 | fdescountryid | fdescountryid | int8 | 64 |  | √ | 0 |  |
| 27 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 28 | fcanceldate | fcanceldate | timestamp | 0 |  |  | null |  |
| 29 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 30 | fpartaid | fpartaid | int8 | 64 |  | √ | 0 |  |
| 31 | fisonlist | fisonlist | bpchar | 1 |  | √ | '0' |  |
| 32 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 33 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 34 | fvaliderid | fvaliderid | int8 | 64 |  | √ | 0 |  |
| 35 | fiselecsignature | fiselecsignature | bpchar | 1 |  | √ | '0' |  |
| 36 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 37 | fconfirmstatus | fconfirmstatus | varchar | 5 |  | √ | ' ' |  |
| 38 | ftradetermid | ftradetermid | int8 | 64 |  | √ | 0 |  |
| 39 | fprojinvctrltype | fprojinvctrltype | varchar | 50 |  | √ | ' ' |  |
| 40 | fbiztime | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 41 | fchangestatus | fchangestatus | varchar | 5 |  | √ | ' ' |  |
| 42 | fdocumentid | fdocumentid | varchar | 50 |  | √ | ' ' |  |
| 43 | fcancelerid | fcancelerid | int8 | 64 |  | √ | 0 |  |
| 44 | fpricelistid | fpricelistid | int8 | 64 |  | √ | 0 |  |
| 45 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 46 | fsrccountryid | fsrccountryid | int8 | 64 |  | √ | 0 |  |
| 47 | ffilingstatus | ffilingstatus | varchar | 5 |  | √ | ' ' |  |
| 48 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 49 | fsignstatus | fsignstatus | varchar | 5 |  | √ | ' ' |  |
| 50 | frecconditionid | frecconditionid | int8 | 64 |  | √ | 0 |  |
| 51 | ffreezedate | ffreezedate | timestamp | 0 |  |  | null |  |
| 52 | funitsrctype | funitsrctype | varchar | 30 |  | √ | ' ' |  |
| 53 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 54 | fbizmode | fbizmode | varchar | 5 |  | √ | ' ' |  |
| 55 | fconmprop | fconmprop | varchar | 5 |  | √ | ' ' |  |
| 56 | ftotaltaxamountcn | ftotaltaxamountcn | varchar | 50 |  | √ | ' ' |  |
| 57 | fcomment | fcomment | varchar | 2000 |  |  | ' ' |  |
| 58 | fdesport | fdesport | varchar | 512 |  | √ | ' ' |  |
| 59 | freceiveaddressf7 | freceiveaddressf7 | int8 | 64 |  | √ | 0 |  |
| 60 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 61 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 62 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 63 | fsrcport | fsrcport | varchar | 512 |  | √ | ' ' |  |
| 64 | ftotalallamountcn | ftotalallamountcn | varchar | 50 |  | √ | ' ' |  |
| 65 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 66 | fclosestatus | fclosestatus | varchar | 5 |  | √ | ' ' |  |
| 67 | ffreezestatus | ffreezestatus | varchar | 5 |  | √ | ' ' |  |
| 68 | fpartbid | fpartbid | int8 | 64 |  | √ | 0 |  |
| 69 | fsubversion | fsubversion | varchar | 30 |  | √ | '1' |  |
| 70 | fconfirmerid | fconfirmerid | int8 | 64 |  | √ | 0 |  |
| 71 | ftemplateentryid | ftemplateentryid | int8 | 64 |  | √ | 0 |  |
| 72 | ftransportmodeid | ftransportmodeid | int8 | 64 |  | √ | 0 |  |
| 73 | finputamount | finputamount | bpchar | 1 |  | √ | '0' |  |
| 74 | fbiztimebegin | fbiztimebegin | timestamp | 0 |  |  | null |  |
| 75 | fcarrierid | fcarrierid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_salcontract_biztime |  | fbiztime |
| 2 | idx_conm_salcontract_billno |  | fbillno |
| 3 | idx_conm_salcontract_org |  | forgid,fbiztime,fbillno,fid |
| 4 | t_conm_salcontract_pkey |  | fid |

---

## 销售合同F7-分表 t_conm_salcontract_c

- **表名称：** 销售合同F7-分表
- **表名：** t_conm_salcontract_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fterminatorid | fterminatorid | int8 | 64 |  | √ | 0 |  |
| 3 | fterminatedate | fterminatedate | timestamp | 0 |  |  | null |  |
| 4 | fcontpartiesid | fcontpartiesid | int8 | 64 |  | √ | 0 |  |
| 5 | fsigndate | fsigndate | timestamp | 0 |  |  | null |  |
| 6 | freclinkmanid | freclinkmanid | int8 | 64 |  | √ | 0 |  |
| 7 | freviewdate | freviewdate | timestamp | 0 |  |  | null |  |
| 8 | fparty2nd | fparty2nd | varchar | 255 |  | √ | ' ' |  |
| 9 | femail2nd | femail2nd | varchar | 100 |  | √ | ' ' |  |
| 10 | fphone2nd | fphone2nd | varchar | 255 |  |  | null |  |
| 11 | ffilingerid | ffilingerid | int8 | 64 |  | √ | 0 |  |
| 12 | fpayingcustomerid | fpayingcustomerid | int8 | 64 |  | √ | 0 |  |
| 13 | freccustomerid | freccustomerid | int8 | 64 |  | √ | 0 |  |
| 14 | fframename | fframename | varchar | 100 |  | √ | ' ' |  |
| 15 | fcontactperson1st | fcontactperson1st | varchar | 60 |  | √ | ' ' |  |
| 16 | fframeversion | fframeversion | varchar | 30 |  | √ | ' ' |  |
| 17 | fframenum | fframenum | varchar | 80 |  | √ | ' ' |  |
| 18 | fpartcid | fpartcid | int8 | 64 |  | √ | 0 |  |
| 19 | fsignerid | fsignerid | int8 | 64 |  | √ | 0 |  |
| 20 | fparty1st | fparty1st | varchar | 255 |  | √ | ' ' |  |
| 21 | fsettlecustomerid | fsettlecustomerid | int8 | 64 |  | √ | 0 |  |
| 22 | fphone1st | fphone1st | varchar | 255 |  |  | null |  |
| 23 | ffilingdate | ffilingdate | timestamp | 0 |  |  | null |  |
| 24 | femail1st | femail1st | varchar | 100 |  | √ | ' ' |  |
| 25 | fcontactperson2nd | fcontactperson2nd | varchar | 60 |  | √ | ' ' |  |
| 26 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 27 | freceiveaddress | freceiveaddress | varchar | 512 |  |  | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_salcontract_c_pkey |  | fid |
| 2 | idx_conm_salcontract_c |  | fcustomerid |

---

## 销售合同F7-多语言表 t_conm_salcontract_l

- **表名称：** 销售合同F7-多语言表
- **表名：** t_conm_salcontract_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | fcomment | varchar | 2000 |  |  | ' ' |  |
| 3 | fdesport | fdesport | varchar | 512 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fsrcport | fsrcport | varchar | 512 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fbillname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_salcontract_l_pkey |  | fpkid |
| 2 | idx_conm_salcontract_l_name |  | fbillname,fid |
| 3 | idx_conm_salcontract_l |  | fid,flocaleid |
