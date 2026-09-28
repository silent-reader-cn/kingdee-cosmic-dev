# 业财对账方案-frm_reconciliation_scheme

## 科目-多选基础资料表 t_ai_recon_scheme_acct

- **表名称：** 科目-多选基础资料表
- **表名：** t_ai_recon_scheme_acct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_recon_scheme_acct_pkey |  | fpkid |
| 2 | idx_t_ai_recon_scheme_acct |  | fentryid |

---

## 适用账簿-多选基础资料表 t_ai_recon_scheme_books

- **表名称：** 适用账簿-多选基础资料表
- **表名：** t_ai_recon_scheme_books

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_reconsch_books_fid |  | fid |
| 2 | pk_ai_recon_scheme_books |  | fpkid |

---

## 对账类型-多选基础资料表 t_ai_recon_scheme_amtype2

- **表名称：** 对账类型-多选基础资料表
- **表名：** t_ai_recon_scheme_amtype2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | '0' | [对账类型 frm_amouttype_layout](../frm_files/frm_amouttype_layout.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_recon_scheme_amtype2_pkey |  | fpkid |
| 2 | idx_ai_recon_scheme_amtype2 |  | fid |

---

## 业财对账方案-多语言表 t_ai_recon_scheme_l

- **表名称：** 业财对账方案-多语言表
- **表名：** t_ai_recon_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_recon_scheme_l_pkey |  | fpkid |
| 2 | idx_ai_recon_scheme_l |  | fid,flocaleid |

---

## 对账设置-子表 t_ai_recon_tab3entry

- **表名称：** 对账设置-子表
- **表名：** t_ai_recon_tab3entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctfdc | 余额方向 | varchar | 30 |  | √ | '1' | 余额方向,枚举: 1 :借 -1 :贷 |
| 3 | fmulassist2info | 核算维度（存储） | varchar | 2000 |  |  | ' ' | 核算维度（存储） |
| 4 | fmulassist2infodesc | 核算维度 | varchar | 2000 |  |  | ' ' | 核算维度 |
| 5 | facctacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | freportparamdesc | 报表参数设置 | varchar | 255 |  |  | ' ' | 报表参数设置 |
| 8 | fglassistbizinfo | 核算维度对应业务维度（存储） | varchar | 2000 |  | √ | ' ' | 核算维度对应业务维度（存储） |
| 9 | fbizassist | 业务维度范围 | varchar | 2000 |  |  | ' ' | 业务维度范围 |
| 10 | freportparam | 报表参数设置（存储） | varchar | 1000 |  |  | ' ' | 报表参数设置（存储） |
| 11 | fentryamounttype | 对账取值类型 | bpchar | 1 |  | √ | '3' | 对账取值类型,枚举: 3 :本期增加+本期减少+余额 2 :本期增加+本期减少 0 :本期增加 1 :本期减少 |
| 12 | fbizdatarule | 业务取数规则 | int8 | 64 |  | √ | 0 | [业务取数规则 frm_recdatarule](../frm_files/frm_recdatarule.md) |
| 13 | fbizassistinfo_tag | 对账维度（存储）_详情 | text | 0 |  |  | ' ' | 对账维度（存储）_详情 |
| 14 | fglassistbizinfodesc | 核算维度对应业务维度 | varchar | 500 |  | √ | ' ' | 核算维度对应业务维度 |
| 15 | fignoreempty | 忽略维度空值 | bpchar | 1 |  | √ | '0' | 忽略维度空值 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fbizassistinfo | 对账维度（存储） | varchar | 2000 |  |  | ' ' | 对账维度（存储） |
| 18 | fmulassist2info_tag | 核算维度（存储）_详情 | text | 0 |  |  | ' ' | 核算维度（存储）_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ai_recon_tab3entry |  | fentryid |
| 2 | idx_ai_recon_tab3entry |  | fid |

---

## 业财对账方案-使用范围位图表 t_ai_recon_scheme_m

- **表名称：** 业财对账方案-使用范围位图表
- **表名：** t_ai_recon_scheme_m

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
| 1 | pk_t_ai_recon_scheme_m |  | forgid |

---

## 业财对账方案-主表 t_ai_recon_scheme

- **表名称：** 业财对账方案-主表
- **表名：** t_ai_recon_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmulcurrencytype | 对账币别 | varchar | 100 |  | √ | ',1,' | 对账币别,枚举: 1 :原币 2 :本位币 |
| 3 | fuseorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | faccounttable | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 6 | fbooktype | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 7 | fdataruleid | fdataruleid | int8 | 64 |  | √ | 0 |  |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fpreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fcloseparam | 对账平衡才允许结账 | bpchar | 1 |  | √ | '0' | 对账平衡才允许结账,枚举: 0 :不检查 1 :业务系统 2 :总账 3 :业务系统+总账 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fbizapp | 业务系统 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 21 | freconciliactionconfig | freconciliactionconfig | int8 | 64 |  | √ | 0 |  |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fctrlstrategy | 控制策略 | varchar | 36 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fpresetnumber | 预置对账方案编码 | varchar | 80 |  | √ | ' ' | 预置对账方案编码 |
| 25 | fbalancebasis | 平衡依据 | bpchar | 1 |  | √ | 5 | 平衡依据,枚举: 0 :借方 1 :贷方 2 :借方+贷方 3 :期初余额 4 :期末余额 5 :全部 |
| 26 | fisbak | 是否备份 | bpchar | 1 |  | √ | '0' | 是否备份 |
| 27 | freconamounttype | 对账取值类型 | bpchar | 1 |  | √ | 3 | 对账取值类型,枚举: 3 :本期增加+本期减少+余额 2 :本期增加+本期减少 0 :本期增加 1 :本期减少 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 30 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ai_recon_scheme_master |  | fmasterid |
| 2 | t_ai_recon_scheme_pkey |  | fid |
| 3 | idx_t_ai_recon_scheme_createorg |  | fcreateorgid |
| 4 | idx_ai_recon_scheme |  | fcreateorgid,fbizapp |

---

## 业财对账方案-使用范围表 t_ai_recon_scheme_u

- **表名称：** 业财对账方案-使用范围表
- **表名：** t_ai_recon_scheme_u

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
| 1 | idx_t_ai_recon_scheme_u_uo |  | fuseorgid |
| 2 | t_ai_recon_scheme_u_pkey |  | fdataid,fuseorgid |
