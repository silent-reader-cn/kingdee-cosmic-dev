# 科目现金流量映射关系-gl_presetcashflowitem

## 科目现金流量映射关系-主表 t_gl_presetcashflowitem

- **表名称：** 科目现金流量映射关系-主表
- **表名：** t_gl_presetcashflowitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 现金流量项目 | int8 | 64 |  | √ | 0 | [现金流量项目 gl_cashflowitem](../gl_files/gl_cashflowitem.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 8 | fcashitemtbid | 现金流量项目表 | int8 | 64 |  | √ | 0 | [现金流量项目表 gl_cashflowitemtb](../gl_files/gl_cashflowitemtb.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | fstatus | varchar | 30 |  | √ | ' ' |  |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 17 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gl_presetcashflowitem_master |  | fmasterid |
| 2 | t_gl_presetcashflowitem_pkey |  | fid |
| 3 | idx_gl_persetitem |  | fcreateorgid,faccounttableid,fgroupid |
| 4 | idx_t_gl_presetcashflowitem_createorg |  | fcreateorgid |

---

## 科目现金流量映射关系-多语言表 t_gl_presetcashflowitem_l

- **表名称：** 科目现金流量映射关系-多语言表
- **表名：** t_gl_presetcashflowitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_presetcashflowitem_l_pkey |  | fpkid |
| 2 | idx_gl_presetcashflow_l |  | fid,flocaleid |

---

## 科目现金流量映射关系-使用范围位图表 t_gl_presetcashflowitem_m

- **表名称：** 科目现金流量映射关系-使用范围位图表
- **表名：** t_gl_presetcashflowitem_m

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
| 1 | pk_t_gl_presetcashflowitem_m |  | forgid |

---

## 科目现金流量映射关系-使用范围表 t_gl_presetcashflowitem_u

- **表名称：** 科目现金流量映射关系-使用范围表
- **表名：** t_gl_presetcashflowitem_u

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
| 1 | t_gl_presetcashflowitem_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_gl_presetcashflowitem_u_uo |  | fuseorgid |

---

## 贷方科目-多选基础资料表 t_gl_itemcreditacct

- **表名称：** 贷方科目-多选基础资料表
- **表名：** t_gl_itemcreditacct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_itemcreditacct_pkey |  | fpkid |
| 2 | idx_gl_itemcreditacct_fbid |  | fbasedataid |
| 3 | idx_gl_itemcreditacct_fid |  | fid |

---

## 单据体-子表 t_gl_presetcfentry

- **表名称：** 单据体-子表
- **表名：** t_gl_presetcfentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 3 | fdc | 发生额方向 | varchar | 2 |  | √ | ' ' | 发生额方向,枚举: 1 :借方 -1 :贷方 |
| 4 | fk_bj73_textfield | 收支核算维度分类 | varchar | 50 |  | √ | ' ' | 收支核算维度分类 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_presetcfentry_pkey |  | fentryid |
| 2 | idx_gl_presetcfentry |  | fid,faccountid,fassgrpid |

---

## 借方科目-多选基础资料表 t_gl_itemdebitacct

- **表名称：** 借方科目-多选基础资料表
- **表名：** t_gl_itemdebitacct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_itemdebitacct_pkey |  | fpkid |
| 2 | idx_gl_itemdebitacct_fbid |  | fbasedataid |
| 3 | idx_gl_itemdebitacct_fid |  | fid |
