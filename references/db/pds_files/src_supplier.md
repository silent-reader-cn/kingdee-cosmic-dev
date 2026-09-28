# 注册供应商-src_supplier

## 注册供应商-分表 t_pur_regsupplier_a

- **表名称：** 注册供应商-分表
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
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fpushsupplier | fpushsupplier | int8 | 64 |  | √ | 0 |  |
| 13 | fadvantage | fadvantage | varchar | 2000 |  | √ | ' ' |  |
| 14 | fstaffnum | fstaffnum | int8 | 64 |  | √ | 0 |  |
| 15 | frecruitno | frecruitno | varchar | 80 |  | √ | ' ' |  |
| 16 | fbizscope | fbizscope | varchar | 2000 |  | √ | ' ' |  |
| 17 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 18 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | flisteddate | flisteddate | timestamp | 0 |  |  | null |  |
| 21 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 24 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 25 | fauditopinion | fauditopinion | varchar | 255 |  | √ | ' ' |  |
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

## 注册供应商-使用范围表 t_pur_regsupplier_u

- **表名称：** 注册供应商-使用范围表
- **表名：** t_pur_regsupplier_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_regsupplier_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_pur_regsupplier_u_uo |  | fuseorgid |

---

## 注册供应商-使用范围位图表 t_pur_regsupplier_m

- **表名称：** 注册供应商-使用范围位图表
- **表名：** t_pur_regsupplier_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_regsupplier_m |  | forgid |

---

## 注册供应商-多语言表 t_pur_regsupplier_l

- **表名称：** 注册供应商-多语言表
- **表名：** t_pur_regsupplier_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
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

## 注册供应商-主表 t_pur_regsupplier

- **表名称：** 注册供应商-主表
- **表名：** t_pur_regsupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 供应商分组 | int8 | 64 |  | √ | 0 | [供应商分类 bd_suppliergroup](../basedata_files/bd_suppliergroup.md) |
| 3 | faddress | faddress | varchar | 255 |  | √ | ' ' |  |
| 4 | forgfield | forgfield | int8 | 64 |  |  | null |  |
| 5 | ftaxrate | ftaxrate | numeric | 19 | 6 | √ | 0.000000 |  |
| 6 | forgid | 审批组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 9 | fareacode | fareacode | varchar | 100 |  | √ | ' ' |  |
| 10 | fphone | fphone | varchar | 50 |  | √ | ' ' |  |
| 11 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 12 | femail | femail | varchar | 50 |  | √ | ' ' |  |
| 13 | fpaycondid | fpaycondid | int8 | 64 |  | √ | 0 |  |
| 14 | ftaxcode | ftaxcode | bpchar | 1 |  | √ | ' ' |  |
| 15 | fsupplierid | 正式供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 16 | ftelephone | ftelephone | varchar | 50 |  | √ | ' ' |  |
| 17 | fisquitregister | fisquitregister | bpchar | 1 |  | √ | '0' |  |
| 18 | finvoicetype | finvoicetype | bpchar | 1 |  | √ | ' ' |  |
| 19 | fcomplaintel | fcomplaintel | varchar | 50 |  | √ | ' ' |  |
| 20 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fbizregisterno | fbizregisterno | varchar | 60 |  | √ | ' ' |  |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fartificialperson | fartificialperson | varchar | 60 |  | √ | ' ' |  |
| 24 | flinkman | flinkman | varchar | 255 |  | √ | ' ' |  |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 26 | fcentralpurtype | fcentralpurtype | bpchar | 1 |  | √ | ' ' |  |
| 27 | fareacodeid | fareacodeid | int8 | 64 |  | √ | 0 |  |
| 28 | fregaddress | fregaddress | varchar | 255 |  | √ | ' ' |  |
| 29 | fsocietycreditcode | 统一社会信用代码 | varchar | 60 |  | √ | ' ' | 统一社会信用代码 |
| 30 | forgcode | forgcode | varchar | 60 |  | √ | ' ' |  |
| 31 | ftaxkind | ftaxkind | bpchar | 1 |  | √ | ' ' |  |
| 32 | fsupplierstatus | fsupplierstatus | int8 | 64 |  | √ | 0 |  |
| 33 | fnewemail | fnewemail | varchar | 50 |  | √ | ' ' |  |
| 34 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: C :注册通过 Z :正式供应商 |
| 35 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 36 | fregtype | fregtype | bpchar | 1 |  | √ | ' ' |  |
| 37 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 38 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 39 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 40 | fpost | fpost | varchar | 10 |  | √ | ' ' |  |
| 41 | ffax | ffax | varchar | 50 |  | √ | ' ' |  |
| 42 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 43 | fregsuptplid | fregsuptplid | int8 | 64 |  | √ | 0 |  |
| 44 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 45 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 57 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 58 | fauditstatus4 | fauditstatus4 | bpchar | 1 |  | √ | ' ' |  |
| 59 | fregdate | fregdate | timestamp | 0 |  |  | null |  |
| 60 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 61 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 62 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
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

---

## 联系人分录-子表 t_pur_regsuplink

- **表名称：** 联系人分录-子表
- **表名：** t_pur_regsuplink

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 联系人姓名 | varchar | 255 |  | √ | ' ' | 联系人姓名 |
| 3 | fphone | 联系人座机 | varchar | 50 |  | √ | ' ' | 联系人座机 |
| 4 | faddress | 联系地址 | varchar | 100 |  | √ | ' ' | 联系地址 |
| 5 | fgender | 性别 | bpchar | 1 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 |
| 6 | femail | 联系人邮箱 | varchar | 50 |  | √ | ' ' | 联系人邮箱 |
| 7 | fdept | 部门 | varchar | 50 |  | √ | ' ' | 部门 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fbizscopetype | fbizscopetype | bpchar | 1 |  | √ | ' ' |  |
| 11 | fmobile | 联系人手机 | varchar | 50 |  | √ | ' ' | 联系人手机 |
| 12 | fduty | 联系人职务 | varchar | 50 |  | √ | ' ' | 联系人职务 |
| 13 | fpost | 邮编 | varchar | 10 |  | √ | ' ' | 邮编 |
| 14 | ffax | 联系人传真 | varchar | 50 |  | √ | ' ' | 联系人传真 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fisdefault | 是否默认联系人 | bpchar | 1 |  | √ | ' ' | 是否默认联系人 |
| 17 | fbizscope | 负责业务 | varchar | 50 |  | √ | ' ' | 负责业务 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_regsuplink_fid_fseq |  | fid,fseq |
| 2 | t_pur_regsuplink_pkey |  | fentryid |
