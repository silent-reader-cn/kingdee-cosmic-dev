# 注册进度查询详情-adm_registerstatus

## 注册进度查询详情-分表 t_pur_regsupplier_a

- **表名称：** 注册进度查询详情-分表
- **表名：** t_pur_regsupplier_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fislistedco | fislistedco | bpchar | 1 |  | √ | ' ' |  |
| 3 | faddress | faddress | varchar | 255 |  | √ | ' ' |  |
| 4 | fregaddress | fregaddress | varchar | 255 |  | √ | ' ' |  |
| 5 | fexecuteresult | fexecuteresult | bpchar | 1 |  | √ | ' ' |  |
| 6 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 7 | fidcard | fidcard | varchar | 20 |  | √ | ' ' |  |
| 8 | fcfmdate | fcfmdate | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fpushsupplier | fpushsupplier | int8 | 64 |  | √ | 0 |  |
| 13 | fadvantage | fadvantage | varchar | 2000 |  | √ | ' ' |  |
| 14 | fstaffnum | fstaffnum | int8 | 64 |  | √ | 0 |  |
| 15 | frecruitno | frecruitno | varchar | 80 |  | √ | ' ' |  |
| 16 | fbizscope | fbizscope | varchar | 2000 |  | √ | ' ' |  |
| 17 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 18 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 19 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 20 | flisteddate | flisteddate | timestamp | 0 |  |  | null |  |
| 21 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 22 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 23 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 24 | fauditdate | 审批时间 | timestamp | 0 |  |  | null | 审批时间 |
| 25 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 26 | fcfmid | fcfmid | int8 | 64 |  | √ | 0 |  |
| 27 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | '5' |  |
| 28 | fcreditrate | fcreditrate | bpchar | 1 |  | √ | ' ' |  |
| 29 | fsimplename | fsimplename | varchar | 255 |  | √ | ' ' |  |
| 30 | flistedaddr | flistedaddr | varchar | 100 |  | √ | ' ' |  |
| 31 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 32 | fartificialperson | fartificialperson | varchar | 60 |  | √ | ' ' |  |
| 33 | flinkman | flinkman | varchar | 50 |  | √ | ' ' |  |
| 34 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 35 | fsummary | fsummary | varchar | 2000 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_regsupplier_a_pkey |  | fid |
| 2 | idx_pur_regsupplier_ftime |  | fcreatetime |

---

## 注册进度查询详情-多语言表 t_pur_regsupplier_l

- **表名称：** 注册进度查询详情-多语言表
- **表名：** t_pur_regsupplier_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | 企业名称 | varchar | 255 |  | √ | ' ' | 企业名称 |
| 4 | faddress | faddress | varchar | 255 |  | √ | ' ' |  |
| 5 | fregaddress | fregaddress | varchar | 255 |  | √ | ' ' |  |
| 6 | fsimplename | fsimplename | varchar | 255 |  | √ | ' ' |  |
| 7 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 8 | flinkman | flinkman | varchar | 255 |  | √ | ' ' |  |
| 9 | fartificialperson | fartificialperson | varchar | 60 |  | √ | ' ' |  |
| 10 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_regsupplier_l_fid |  | fid,flocaleid |
| 2 | t_pur_regsupplier_l_pkey |  | fpkid |
| 3 | idx_pur_regsupplier_fname |  | flocaleid,fname |

---

## 注册进度查询详情-主表 t_pur_regsupplier

- **表名称：** 注册进度查询详情-主表
- **表名：** t_pur_regsupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | faddress | faddress | varchar | 255 |  | √ | ' ' |  |
| 4 | forgfield | forgfield | int8 | 64 |  |  | null |  |
| 5 | ftaxrate | ftaxrate | numeric | 19 | 6 | √ | 0.000000 |  |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 8 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 9 | fareacode | fareacode | varchar | 100 |  | √ | ' ' |  |
| 10 | fphone | 注册账号 | varchar | 50 |  | √ | ' ' | 注册账号 |
| 11 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 12 | femail | femail | varchar | 50 |  | √ | ' ' |  |
| 13 | fpaycondid | fpaycondid | int8 | 64 |  | √ | 0 |  |
| 14 | ftaxcode | ftaxcode | bpchar | 1 |  | √ | ' ' |  |
| 15 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 16 | ftelephone | ftelephone | varchar | 50 |  | √ | ' ' |  |
| 17 | fisquitregister | fisquitregister | bpchar | 1 |  | √ | '0' |  |
| 18 | finvoicetype | finvoicetype | bpchar | 1 |  | √ | ' ' |  |
| 19 | fcomplaintel | fcomplaintel | varchar | 50 |  | √ | ' ' |  |
| 20 | fenable | fenable | bpchar | 1 |  | √ | ' ' |  |
| 21 | fbizregisterno | fbizregisterno | varchar | 60 |  | √ | ' ' |  |
| 22 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |
| 23 | fartificialperson | fartificialperson | varchar | 60 |  | √ | ' ' |  |
| 24 | flinkman | 注册用户 | varchar | 255 |  | √ | ' ' | 注册用户 |
| 25 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 26 | fcentralpurtype | fcentralpurtype | bpchar | 1 |  | √ | ' ' |  |
| 27 | fareacodeid | fareacodeid | int8 | 64 |  | √ | 0 |  |
| 28 | fregaddress | fregaddress | varchar | 255 |  | √ | ' ' |  |
| 29 | fsocietycreditcode | 统一社会信用代码 | varchar | 60 |  | √ | ' ' | 统一社会信用代码 |
| 30 | forgcode | forgcode | varchar | 60 |  | √ | ' ' |  |
| 31 | ftaxkind | ftaxkind | bpchar | 1 |  | √ | ' ' |  |
| 32 | fsupplierstatus | fsupplierstatus | int8 | 64 |  | √ | 0 |  |
| 33 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :填写资料 B :提交审批 C :注册通过 D :注册驳回 E :资审通过 F :资审驳回 G :现场通过 H :现场驳回 I :样品通过 J :样品驳回 K :物料通过 L :物料驳回 Z :正式供应商 M :生效驳回 |
| 34 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 35 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 36 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 37 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 38 | fpost | fpost | varchar | 10 |  | √ | ' ' |  |
| 39 | ffax | ffax | varchar | 50 |  | √ | ' ' |  |
| 40 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 41 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 42 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 43 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 44 | fcurrid | fcurrid | int8 | 64 |  | √ | 0 |  |
| 45 | finvoicetypeid | finvoicetypeid | int8 | 64 |  | √ | 0 |  |
| 46 | ftaxclass | ftaxclass | bpchar | 1 |  | √ | ' ' |  |
| 47 | fcountryid | fcountryid | int8 | 64 |  | √ | 0 |  |
| 48 | fauditstatus1 | fauditstatus1 | bpchar | 1 |  | √ | ' ' |  |
| 49 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 50 | fauditstatus2 | fauditstatus2 | bpchar | 1 |  | √ | ' ' |  |
| 51 | fauditstatus3 | fauditstatus3 | bpchar | 1 |  | √ | ' ' |  |
| 52 | fregcapital | fregcapital | numeric | 19 | 6 | √ | 0.000000 |  |
| 53 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 54 | fauditstatus4 | fauditstatus4 | bpchar | 1 |  | √ | ' ' |  |
| 55 | fregdate | fregdate | timestamp | 0 |  |  | null |  |
| 56 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 57 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 58 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | ' ' |  |
| 59 | ftype | ftype | bpchar | 1 |  | √ | ' ' |  |
| 60 | findustryid | findustryid | int8 | 64 |  | √ | 0 |  |
| 61 | fsimplename | fsimplename | varchar | 255 |  | √ | ' ' |  |
| 62 | furl | furl | varchar | 100 |  | √ | ' ' |  |
| 63 | fdeductible | fdeductible | bpchar | 1 |  | √ | ' ' |  |
| 64 | ftxregisterno | ftxregisterno | varchar | 60 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_regsupplier_createorg |  | fcreateorgid |
| 2 | idx_pur_regsupplier_fnumber |  | fnumber |
| 3 | idx_pur_regsupplier_fphone |  | fphone |
| 4 | t_pur_regsupplier_pkey |  | fid |
| 5 | idx_t_pur_regsupplier_master |  | fmasterid |
