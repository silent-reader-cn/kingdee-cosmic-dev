# 销售合同F7-conm_salcontractf7

## 销售合同F7-主表 t_conm_salcontract

- **表名称：** 销售合同F7-主表
- **表名：** t_conm_salcontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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
| 19 | fmpmrecmethod | fmpmrecmethod | varchar | 50 |  | √ | ' ' |  |
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
| 40 | fpricelistid | fpricelistid | int8 | 64 |  | √ | 0 |  |
| 41 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 42 | ffilingstatus | ffilingstatus | varchar | 5 |  | √ | ' ' |  |
| 43 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 44 | fsignstatus | fsignstatus | varchar | 5 |  | √ | ' ' |  |
| 45 | frecconditionid | frecconditionid | int8 | 64 |  | √ | 0 |  |
| 46 | ffreezedate | ffreezedate | timestamp | 0 |  |  | null |  |
| 47 | funitsrctype | funitsrctype | varchar | 30 |  | √ | ' ' |  |
| 48 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 49 | fbizmode | fbizmode | varchar | 5 |  | √ | ' ' |  |
| 50 | fconmprop | fconmprop | varchar | 5 |  | √ | ' ' |  |
| 51 | fcomment | fcomment | varchar | 2000 |  |  | ' ' |  |
| 52 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 53 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 54 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 55 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 56 | fclosestatus | fclosestatus | varchar | 5 |  | √ | ' ' |  |
| 57 | ffreezestatus | ffreezestatus | varchar | 5 |  | √ | ' ' |  |
| 58 | fpartbid | fpartbid | int8 | 64 |  | √ | 0 |  |
| 59 | fsubversion | fsubversion | varchar | 30 |  | √ | '1' |  |
| 60 | fconfirmerid | fconfirmerid | int8 | 64 |  | √ | 0 |  |
| 61 | ftemplateentryid | ftemplateentryid | int8 | 64 |  | √ | 0 |  |
| 62 | fbiztimebegin | fbiztimebegin | timestamp | 0 |  |  | null |  |

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
| 9 | fphone2nd | fphone2nd | varchar | 255 |  |  | null |  |
| 10 | ffilingerid | ffilingerid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayingcustomerid | fpayingcustomerid | int8 | 64 |  | √ | 0 |  |
| 12 | freccustomerid | freccustomerid | int8 | 64 |  | √ | 0 |  |
| 13 | fframename | fframename | varchar | 100 |  | √ | ' ' |  |
| 14 | fcontactperson1st | fcontactperson1st | varchar | 60 |  | √ | ' ' |  |
| 15 | fframeversion | fframeversion | varchar | 30 |  | √ | ' ' |  |
| 16 | fframenum | fframenum | varchar | 80 |  | √ | ' ' |  |
| 17 | fpartcid | fpartcid | int8 | 64 |  | √ | 0 |  |
| 18 | fsignerid | fsignerid | int8 | 64 |  | √ | 0 |  |
| 19 | fparty1st | fparty1st | varchar | 255 |  | √ | ' ' |  |
| 20 | fsettlecustomerid | fsettlecustomerid | int8 | 64 |  | √ | 0 |  |
| 21 | fphone1st | fphone1st | varchar | 255 |  |  | null |  |
| 22 | ffilingdate | ffilingdate | timestamp | 0 |  |  | null |  |
| 23 | fcontactperson2nd | fcontactperson2nd | varchar | 60 |  | √ | ' ' |  |
| 24 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 25 | freceiveaddress | freceiveaddress | varchar | 512 |  |  | ' ' |  |

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
| 1 | t_conm_salcontract_l_pkey |  | fpkid |
| 2 | idx_conm_salcontract_l_name |  | fbillname,fid |
| 3 | idx_conm_salcontract_l |  | fid,flocaleid |
