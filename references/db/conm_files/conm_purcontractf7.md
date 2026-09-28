# 采购合同F7-conm_purcontractf7

## 采购合同F7-分表 t_conm_purcontract_s

- **表名称：** 采购合同F7-分表
- **表名：** t_conm_purcontract_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddress | faddress | varchar | 512 |  |  | ' ' |  |
| 3 | fterminatorid | fterminatorid | int8 | 64 |  | √ | 0 |  |
| 4 | fproviderlinkmanid | fproviderlinkmanid | int8 | 64 |  | √ | 0 |  |
| 5 | fterminatedate | fterminatedate | timestamp | 0 |  |  | null |  |
| 6 | fcontpartiesid | fcontpartiesid | int8 | 64 |  | √ | 0 |  |
| 7 | fsigndate | fsigndate | timestamp | 0 |  |  | null |  |
| 8 | freviewdate | freviewdate | timestamp | 0 |  |  | null |  |
| 9 | fparty2nd | fparty2nd | varchar | 255 |  | √ | ' ' |  |
| 10 | fprovideraddress | fprovideraddress | varchar | 512 |  |  | ' ' |  |
| 11 | femail2nd | femail2nd | varchar | 100 |  | √ | ' ' |  |
| 12 | fphone2nd | fphone2nd | varchar | 255 |  |  | null |  |
| 13 | ffilingerid | ffilingerid | int8 | 64 |  | √ | 0 |  |
| 14 | finvoicesupplierid | finvoicesupplierid | int8 | 64 |  | √ | 0 |  |
| 15 | fframename | fframename | varchar | 100 |  | √ | ' ' |  |
| 16 | fcontactperson1st | fcontactperson1st | varchar | 60 |  | √ | ' ' |  |
| 17 | fframeversion | fframeversion | varchar | 30 |  | √ | ' ' |  |
| 18 | fframenum | fframenum | varchar | 80 |  | √ | ' ' |  |
| 19 | fprovidersupplierid | fprovidersupplierid | int8 | 64 |  | √ | 0 |  |
| 20 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 21 | freceivesupplierid | freceivesupplierid | int8 | 64 |  | √ | 0 |  |
| 22 | fpartcid | fpartcid | int8 | 64 |  | √ | 0 |  |
| 23 | fsignerid | fsignerid | int8 | 64 |  | √ | 0 |  |
| 24 | fparty1st | fparty1st | varchar | 255 |  | √ | ' ' |  |
| 25 | flinkmanid | flinkmanid | int8 | 64 |  | √ | 0 |  |
| 26 | fphone1st | fphone1st | varchar | 255 |  |  | null |  |
| 27 | ffilingdate | ffilingdate | timestamp | 0 |  |  | null |  |
| 28 | femail1st | femail1st | varchar | 100 |  | √ | ' ' |  |
| 29 | fcontactperson2nd | fcontactperson2nd | varchar | 60 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_purcontract_s |  | fsupplierid |
| 2 | t_conm_purcontract_s_pkey |  | fid |

---

## 采购合同F7-多语言表 t_conm_purcontract_l

- **表名称：** 采购合同F7-多语言表
- **表名：** t_conm_purcontract_l

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
| 1 | idx_conm_purcontract_l_name |  | fbillname,fid |
| 2 | idx_conm_purcontract_l |  | fid,flocaleid |
| 3 | t_conm_purcontract_l_pkey |  | fpkid |

---

## 采购合同F7-主表 t_conm_purcontract

- **表名称：** 采购合同F7-主表
- **表名：** t_conm_purcontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmpmpaymethod | fmpmpaymethod | varchar | 5 |  | √ | ' ' |  |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 5 | fcancelstatus | fcancelstatus | varchar | 5 |  | √ | ' ' |  |
| 6 | fsplitschemeid | fsplitschemeid | int8 | 64 |  | √ | 0 |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | freviewstatus | freviewstatus | varchar | 5 |  | √ | ' ' |  |
| 9 | fterminatestatus | 终止状态 | varchar | 5 |  | √ | ' ' | 终止状态,枚举: A :未终止 B :已终止 |
| 10 | ffreezerid | ffreezerid | int8 | 64 |  | √ | 0 |  |
| 11 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 12 | fvaliddate | fvaliddate | timestamp | 0 |  |  | null |  |
| 13 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 15 | fversion | fversion | varchar | 30 |  | √ | '1' |  |
| 16 | fconfirmdate | fconfirmdate | timestamp | 0 |  |  | null |  |
| 17 | ftotalamountcn | ftotalamountcn | varchar | 50 |  | √ | ' ' |  |
| 18 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 19 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fpayconditionid | fpayconditionid | int8 | 64 |  | √ | 0 |  |
| 22 | ftrdbillno | ftrdbillno | varchar | 50 |  | √ | ' ' |  |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | fbillcretype | fbillcretype | varchar | 5 |  | √ | '0' |  |
| 25 | fbiztimeend | fbiztimeend | timestamp | 0 |  |  | null |  |
| 26 | fbillname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 27 | ftypeid | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 28 | fdescountryid | fdescountryid | int8 | 64 |  | √ | 0 |  |
| 29 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 30 | fcanceldate | fcanceldate | timestamp | 0 |  |  | null |  |
| 31 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 32 | fpartaid | fpartaid | int8 | 64 |  | √ | 0 |  |
| 33 | fisonlist | fisonlist | bpchar | 1 |  | √ | '0' |  |
| 34 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 35 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 36 | fvaliderid | fvaliderid | int8 | 64 |  | √ | 0 |  |
| 37 | fiselecsignature | fiselecsignature | bpchar | 1 |  | √ | '0' |  |
| 38 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 39 | fconfirmstatus | fconfirmstatus | varchar | 5 |  | √ | ' ' |  |
| 40 | ftradetermid | ftradetermid | int8 | 64 |  | √ | 0 |  |
| 41 | fbiztime | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 42 | fchangestatus | fchangestatus | varchar | 5 |  | √ | ' ' |  |
| 43 | fdocumentid | fdocumentid | varchar | 50 |  | √ | ' ' |  |
| 44 | fcancelerid | fcancelerid | int8 | 64 |  | √ | 0 |  |
| 45 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 46 | fsrccountryid | fsrccountryid | int8 | 64 |  | √ | 0 |  |
| 47 | ffilingstatus | ffilingstatus | varchar | 5 |  | √ | ' ' |  |
| 48 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 49 | fsignstatus | fsignstatus | varchar | 5 |  | √ | ' ' |  |
| 50 | ffreezedate | ffreezedate | timestamp | 0 |  |  | null |  |
| 51 | funitsrctype | funitsrctype | varchar | 30 |  | √ | ' ' |  |
| 52 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 53 | fbizmode | fbizmode | varchar | 5 |  | √ | ' ' |  |
| 54 | fconmprop | fconmprop | varchar | 5 |  | √ | ' ' |  |
| 55 | ftotaltaxamountcn | ftotaltaxamountcn | varchar | 50 |  | √ | ' ' |  |
| 56 | fcomment | fcomment | varchar | 2000 |  |  | ' ' |  |
| 57 | fdesport | fdesport | varchar | 512 |  | √ | ' ' |  |
| 58 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 59 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 60 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 61 | fsrcport | fsrcport | varchar | 512 |  | √ | ' ' |  |
| 62 | ftotalallamountcn | ftotalallamountcn | varchar | 50 |  | √ | ' ' |  |
| 63 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 64 | fclosestatus | fclosestatus | varchar | 5 |  | √ | ' ' |  |
| 65 | ffreezestatus | ffreezestatus | varchar | 5 |  | √ | ' ' |  |
| 66 | fpartbid | fpartbid | int8 | 64 |  | √ | 0 |  |
| 67 | fsubversion | fsubversion | varchar | 30 |  | √ | '1' |  |
| 68 | fconfirmerid | fconfirmerid | int8 | 64 |  | √ | 0 |  |
| 69 | ftemplateentryid | ftemplateentryid | int8 | 64 |  | √ | 0 |  |
| 70 | ftransportmodeid | ftransportmodeid | int8 | 64 |  | √ | 0 |  |
| 71 | finputamount | finputamount | bpchar | 1 |  | √ | '0' |  |
| 72 | fbiztimebegin | fbiztimebegin | timestamp | 0 |  |  | null |  |
| 73 | ftaxinprice | ftaxinprice | bpchar | 1 |  | √ | '0' |  |
| 74 | fcarrierid | fcarrierid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_purcontract_pkey |  | fid |
| 2 | idx_conm_purcontract_biztime |  | fbiztime |
| 3 | idx_conm_purcontract_org |  | forgid,fbiztime,fbillno,fid |
| 4 | idx_conm_purcontract_billno |  | fbillno |
