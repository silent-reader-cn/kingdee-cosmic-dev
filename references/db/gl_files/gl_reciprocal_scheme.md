# 往来核销方案-gl_reciprocal_scheme

## 往来核销方案-使用范围位图表 t_gl_reci_scheme_m

- **表名称：** 往来核销方案-使用范围位图表
- **表名：** t_gl_reci_scheme_m

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
| 1 | pk_t_gl_reci_scheme_m |  | forgid |

---

## 往来核销方案-多语言表 t_gl_reci_scheme_l

- **表名称：** 往来核销方案-多语言表
- **表名：** t_gl_reci_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_reci_scheme_l |  | fid,flocaleid |
| 2 | t_gl_reci_scheme_l_pkey |  | fpkid |

---

## 往来核销方案-使用范围表 t_gl_reci_scheme_u

- **表名称：** 往来核销方案-使用范围表
- **表名：** t_gl_reci_scheme_u

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
| 1 | t_gl_reci_scheme_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_gl_reci_scheme_u_uo |  | fuseorgid |

---

## 币种-多选基础资料表 t_gl_reciprocal_currency

- **表名称：** 币种-多选基础资料表
- **表名：** t_gl_reciprocal_currency

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_reciprocal_currency |  | fid |
| 2 | t_gl_reciprocal_currency_pkey |  | fpkid |

---

## 科目-多选基础资料表 t_gl_reciprocal_account

- **表名称：** 科目-多选基础资料表
- **表名：** t_gl_reciprocal_account

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
| 1 | idx_gl_reciprocal_account |  | fid |
| 2 | t_gl_reciprocal_account_pkey |  | fpkid |

---

## 往来核销方案-主表 t_gl_reci_scheme

- **表名称：** 往来核销方案-主表
- **表名：** t_gl_reci_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fequalamountpriority | 金额相等优先核销 | bpchar | 1 |  | √ | '1' | 金额相等优先核销 |
| 3 | fuseorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | freverordersamedire | 按倒序进行同向冲销 | bpchar | 1 |  | √ | ' ' | 按倒序进行同向冲销 |
| 6 | fnoverifibusinoempty | 业务编号为空不允许核销 | bpchar | 1 |  | √ | ' ' | 业务编号为空不允许核销 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmoneyequacanverfi | 金额相等才能核销 | bpchar | 1 |  | √ | ' ' | 金额相等才能核销 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fverifidiffbusino | 业务编号不相同允许核销 | bpchar | 1 |  | √ | ' ' | 业务编号不相同允许核销 |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fverifiorder | 核销顺序 | bpchar | 1 |  | √ | ' ' | 核销顺序,枚举: 0 :业务日期+业务编号 1 :业务编号+业务日期 |
| 21 | fvoucherfilter | 凭证过滤 | varchar | 512 |  | √ | ' ' | 凭证过滤 |
| 22 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 23 | fiscopy | 是否复制 | bpchar | 1 |  | √ | '0' | 是否复制 |
| 24 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fvoucherfilterjson | 凭证过滤JSON | varchar | 2000 |  |  | ' ' | 凭证过滤JSON |
| 26 | fexcluunpostvoucher | 已过账凭证才能核销 | bpchar | 1 |  | √ | ' ' | 已过账凭证才能核销 |
| 27 | faccounttypeid | faccounttypeid | int8 | 64 |  | √ | 0 |  |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 30 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_reci_scheme_fnumber |  | fnumber |
| 2 | t_gl_reci_scheme_pkey |  | fid |
| 3 | idx_t_gl_reci_scheme_master |  | fmasterid |
| 4 | idx_t_gl_reci_scheme_createorg |  | fcreateorgid |
