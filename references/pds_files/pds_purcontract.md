# 采购合同-pds_purcontract

## 采购合同-主表 t_conm_purcontract

- **表名称：** 采购合同-主表
- **表名：** t_conm_purcontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 4 | fcancelstatus | fcancelstatus | varchar | 5 |  | √ | ' ' |  |
| 5 | fsplitschemeid | fsplitschemeid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | freviewstatus | freviewstatus | varchar | 5 |  | √ | ' ' |  |
| 8 | fterminatestatus | fterminatestatus | varchar | 5 |  | √ | ' ' |  |
| 9 | ffreezerid | ffreezerid | int8 | 64 |  | √ | 0 |  |
| 10 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 11 | fvaliddate | fvaliddate | timestamp | 0 |  |  | null |  |
| 12 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 13 | fbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 14 | fversion | fversion | varchar | 30 |  | √ | '1' |  |
| 15 | fconfirmdate | fconfirmdate | timestamp | 0 |  |  | null |  |
| 16 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 17 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 18 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :采委会审批中 C :已经审核 D :采委会驳回 E :已发布 F :磋商中 G :供应商已确认 H :业务已确认 I :法务已确认 J :法务驳回 K :评审中 L :审核失败 M :已审核 N :机要人员已签章 O :供应商已签章 P :签章失败 Q :已终止 R :已关闭 S :已归档 T :归档失败 U :生成SAP合同 V :生成SAP合同失败 |
| 19 | fpayconditionid | fpayconditionid | int8 | 64 |  | √ | 0 |  |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fbillcretype | fbillcretype | varchar | 5 |  | √ | '0' |  |
| 22 | fbiztimeend | fbiztimeend | timestamp | 0 |  |  | null |  |
| 23 | fbillname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 24 | ftypeid | ftypeid | int8 | 64 |  | √ | 0 |  |
| 25 | fvalidstatus | fvalidstatus | varchar | 5 |  | √ | ' ' |  |
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
| 36 | fbiztime | fbiztime | timestamp | 0 |  |  | null |  |
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
