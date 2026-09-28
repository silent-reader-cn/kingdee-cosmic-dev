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
| 7 | fidcard | 统一社会信用代码 | varchar | 20 |  | √ | ' ' | 统一社会信用代码 |
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

## 注册进度查询详情-分表 t_pur_regsupplier_c

- **表名称：** 注册进度查询详情-分表
- **表名：** t_pur_regsupplier_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flastyear | flastyear | varchar | 255 |  | √ | ' ' |  |
| 3 | ftechniciannum | ftechniciannum | numeric | 19 |  | √ | 0 |  |
| 4 | ftyear | ftyear | varchar | 255 |  | √ | ' ' |  |
| 5 | fmanagementstaff | fmanagementstaff | numeric | 19 |  | √ | 0 |  |
| 6 | ftaxregistredads | ftaxregistredads | varchar | 255 |  | √ | ' ' |  |
| 7 | fenterprisetype | fenterprisetype | bpchar | 1 |  | √ | ' ' |  |
| 8 | fcertifiapplyid | fcertifiapplyid | int8 | 64 |  | √ | 0 |  |
| 9 | fissuerfiid | fissuerfiid | varchar | 80 |  | √ | ' ' |  |
| 10 | fmanagecur | fmanagecur | int8 | 64 |  | √ | 0 |  |
| 11 | fstandcapacity | fstandcapacity | bpchar | 1 |  | √ | ' ' |  |
| 12 | fqualitystaffnum | fqualitystaffnum | numeric | 19 |  | √ | 0 |  |
| 13 | fdunsnumber | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 14 | fbeforeyear | fbeforeyear | varchar | 255 |  | √ | ' ' |  |
| 15 | fdesigncapacity | fdesigncapacity | bpchar | 1 |  | √ | ' ' |  |
| 16 | fsupnameen | fsupnameen | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_regsupplier_c |  | fissuerfiid |
| 2 | idxcer_t_pur_regsupplier_c |  | fcertifiapplyid |
| 3 | pk_t_pur_regsupplier_c |  | fid |

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
| 10 | fphone | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 11 | fname | 企业名称 | varchar | 255 |  | √ | ' ' | 企业名称 |
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
| 24 | flinkman | 用户 | varchar | 255 |  | √ | ' ' | 用户 |
| 25 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 26 | fcentralpurtype | fcentralpurtype | bpchar | 1 |  | √ | ' ' |  |
| 27 | fareacodeid | fareacodeid | int8 | 64 |  | √ | 0 |  |
| 28 | fregaddress | fregaddress | varchar | 255 |  | √ | ' ' |  |
| 29 | fsocietycreditcode | 统一社会信用代码 | varchar | 60 |  | √ | ' ' | 统一社会信用代码 |
| 30 | forgcode | forgcode | varchar | 60 |  | √ | ' ' |  |
| 31 | ftaxkind | ftaxkind | bpchar | 1 |  | √ | ' ' |  |
| 32 | fsupplierstatus | fsupplierstatus | int8 | 64 |  | √ | 0 |  |
| 33 | fnewemail | fnewemail | varchar | 50 |  | √ | ' ' |  |
| 34 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :填写资料 B :提交审批 C :注册通过 D :注册驳回 E :资审通过 F :资审驳回 G :现场通过 H :现场驳回 I :样品通过 J :样品驳回 K :物料通过 L :物料驳回 Z :正式供应商 M :生效驳回 |
| 35 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 36 | fregtype | fregtype | bpchar | 1 |  | √ | ' ' |  |
| 37 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 38 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 39 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 40 | fpost | fpost | varchar | 10 |  | √ | ' ' |  |
| 41 | ffax | ffax | varchar | 50 |  | √ | ' ' |  |
| 42 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 43 | fregsuptplid | fregsuptplid | int8 | 64 |  | √ | 0 |  |
| 44 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 45 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 46 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 47 | fcurrid | fcurrid | int8 | 64 |  | √ | 0 |  |
| 48 | finvoicetypeid | finvoicetypeid | int8 | 64 |  | √ | 0 |  |
| 49 | ftaxclass | ftaxclass | bpchar | 1 |  | √ | ' ' |  |
| 50 | ftarsupplierstatus | ftarsupplierstatus | bpchar | 1 |  | √ | 'A' |  |
| 51 | fcountryid | fcountryid | int8 | 64 |  | √ | 0 |  |
| 52 | fauditstatus1 | fauditstatus1 | bpchar | 1 |  | √ | ' ' |  |
| 53 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 54 | fauditstatus2 | fauditstatus2 | bpchar | 1 |  | √ | ' ' |  |
| 55 | fauditstatus3 | fauditstatus3 | bpchar | 1 |  | √ | ' ' |  |
| 56 | fregcapital | fregcapital | numeric | 19 | 6 | √ | 0.000000 |  |
| 57 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 58 | fauditstatus4 | fauditstatus4 | bpchar | 1 |  | √ | ' ' |  |
| 59 | fregdate | fregdate | timestamp | 0 |  |  | null |  |
| 60 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 61 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 62 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | ' ' |  |
| 63 | fnewphone | fnewphone | varchar | 50 |  | √ | ' ' |  |
| 64 | ftype | ftype | bpchar | 1 |  | √ | ' ' |  |
| 65 | findustryid | findustryid | int8 | 64 |  | √ | 0 |  |
| 66 | fsimplename | fsimplename | varchar | 255 |  | √ | ' ' |  |
| 67 | furl | furl | varchar | 100 |  | √ | ' ' |  |
| 68 | ftoexam | ftoexam | bpchar | 1 |  | √ | '1' |  |
| 69 | fdeductible | fdeductible | bpchar | 1 |  | √ | ' ' |  |
| 70 | ftxregisterno | ftxregisterno | varchar | 60 |  | √ | ' ' |  |
| 71 | fenterprisespros | fenterprisespros | bpchar | 1 |  | √ | '0' |  |

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
