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
| 11 | fphone2nd | fphone2nd | varchar | 255 |  |  | null |  |
| 12 | ffilingerid | ffilingerid | int8 | 64 |  | √ | 0 |  |
| 13 | finvoicesupplierid | finvoicesupplierid | int8 | 64 |  | √ | 0 |  |
| 14 | fframename | fframename | varchar | 100 |  | √ | ' ' |  |
| 15 | fcontactperson1st | fcontactperson1st | varchar | 60 |  | √ | ' ' |  |
| 16 | fframeversion | fframeversion | varchar | 30 |  | √ | ' ' |  |
| 17 | fframenum | fframenum | varchar | 80 |  | √ | ' ' |  |
| 18 | fprovidersupplierid | fprovidersupplierid | int8 | 64 |  | √ | 0 |  |
| 19 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | freceivesupplierid | freceivesupplierid | int8 | 64 |  | √ | 0 |  |
| 21 | fpartcid | fpartcid | int8 | 64 |  | √ | 0 |  |
| 22 | fsignerid | fsignerid | int8 | 64 |  | √ | 0 |  |
| 23 | fparty1st | fparty1st | varchar | 255 |  | √ | ' ' |  |
| 24 | flinkmanid | flinkmanid | int8 | 64 |  | √ | 0 |  |
| 25 | fphone1st | fphone1st | varchar | 255 |  |  | null |  |
| 26 | ffilingdate | ffilingdate | timestamp | 0 |  |  | null |  |
| 27 | fcontactperson2nd | fcontactperson2nd | varchar | 60 |  | √ | ' ' |  |

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
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fbillname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |

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
| 2 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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
| 16 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 17 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 18 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fpayconditionid | fpayconditionid | int8 | 64 |  | √ | 0 |  |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fbillcretype | fbillcretype | varchar | 5 |  | √ | '0' |  |
| 22 | fbiztimeend | fbiztimeend | timestamp | 0 |  |  | null |  |
| 23 | fbillname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 24 | ftypeid | 合同类型 | int8 | 64 |  | √ | 0 | 合同类型 conm_type |
| 25 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 26 | fcanceldate | fcanceldate | timestamp | 0 |  |  | null |  |
| 27 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 28 | fpartaid | fpartaid | int8 | 64 |  | √ | 0 |  |
| 29 | fisonlist | fisonlist | bpchar | 1 |  | √ | '0' |  |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 31 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 32 | fvaliderid | fvaliderid | int8 | 64 |  | √ | 0 |  |
| 33 | fiselecsignature | fiselecsignature | bpchar | 1 |  | √ | '0' |  |
| 34 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 35 | fconfirmstatus | fconfirmstatus | varchar | 5 |  | √ | ' ' |  |
| 36 | fbiztime | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 37 | fchangestatus | fchangestatus | varchar | 5 |  | √ | ' ' |  |
| 38 | fdocumentid | fdocumentid | varchar | 50 |  | √ | ' ' |  |
| 39 | fcancelerid | fcancelerid | int8 | 64 |  | √ | 0 |  |
| 40 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 41 | ffilingstatus | ffilingstatus | varchar | 5 |  | √ | ' ' |  |
| 42 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 43 | fsignstatus | fsignstatus | varchar | 5 |  | √ | ' ' |  |
| 44 | ffreezedate | ffreezedate | timestamp | 0 |  |  | null |  |
| 45 | funitsrctype | funitsrctype | varchar | 30 |  | √ | ' ' |  |
| 46 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 47 | fbizmode | fbizmode | varchar | 5 |  | √ | ' ' |  |
| 48 | fconmprop | fconmprop | varchar | 5 |  | √ | ' ' |  |
| 49 | fcomment | fcomment | varchar | 2000 |  |  | ' ' |  |
| 50 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 51 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 52 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 53 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 54 | fclosestatus | fclosestatus | varchar | 5 |  | √ | ' ' |  |
| 55 | ffreezestatus | ffreezestatus | varchar | 5 |  | √ | ' ' |  |
| 56 | fpartbid | fpartbid | int8 | 64 |  | √ | 0 |  |
| 57 | fsubversion | fsubversion | varchar | 30 |  | √ | '1' |  |
| 58 | fconfirmerid | fconfirmerid | int8 | 64 |  | √ | 0 |  |
| 59 | ftemplateentryid | ftemplateentryid | int8 | 64 |  | √ | 0 |  |
| 60 | fbiztimebegin | fbiztimebegin | timestamp | 0 |  |  | null |  |
| 61 | ftaxinprice | ftaxinprice | bpchar | 1 |  | √ | '0' |  |

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
