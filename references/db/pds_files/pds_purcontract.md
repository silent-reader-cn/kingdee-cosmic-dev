# 采购合同-pds_purcontract

## 采购合同-主表 t_conm_purcontract

- **表名称：** 采购合同-主表
- **表名：** t_conm_purcontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmpmpaymethod | fmpmpaymethod | varchar | 5 |  | √ | ' ' |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 5 | fcancelstatus | fcancelstatus | varchar | 5 |  | √ | ' ' |  |
| 6 | fsplitschemeid | fsplitschemeid | int8 | 64 |  | √ | 0 |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | freviewstatus | freviewstatus | varchar | 5 |  | √ | ' ' |  |
| 9 | fterminatestatus | fterminatestatus | varchar | 5 |  | √ | ' ' |  |
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
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :采委会审批中 C :已经审核 D :采委会驳回 E :已发布 F :磋商中 G :供应商已确认 H :业务已确认 I :法务已确认 J :法务驳回 K :评审中 L :审核失败 M :已审核 N :机要人员已签章 O :供应商已签章 P :签章失败 Q :已终止 R :已关闭 S :已归档 T :归档失败 U :生成SAP合同 V :生成SAP合同失败 |
| 21 | fpayconditionid | fpayconditionid | int8 | 64 |  | √ | 0 |  |
| 22 | ftrdbillno | ftrdbillno | varchar | 50 |  | √ | ' ' |  |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | fbillcretype | fbillcretype | varchar | 5 |  | √ | '0' |  |
| 25 | fbiztimeend | fbiztimeend | timestamp | 0 |  |  | null |  |
| 26 | fbillname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 27 | ftypeid | ftypeid | int8 | 64 |  | √ | 0 |  |
| 28 | fdescountryid | fdescountryid | int8 | 64 |  | √ | 0 |  |
| 29 | fvalidstatus | fvalidstatus | varchar | 5 |  | √ | ' ' |  |
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
| 41 | fbiztime | fbiztime | timestamp | 0 |  |  | null |  |
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
