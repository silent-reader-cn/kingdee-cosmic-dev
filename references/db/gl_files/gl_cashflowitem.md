# 现金流量项目-gl_cashflowitem

## 现金流量项目-使用范围表 t_gl_cashflowitem_u

- **表名称：** 现金流量项目-使用范围表
- **表名：** t_gl_cashflowitem_u

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
| 1 | t_gl_cashflowitem_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_gl_cashflowitem_u_uo |  | fuseorgid |

---

## 现金流量项目-多语言表 t_gl_cashflowitem_l

- **表名称：** 现金流量项目-多语言表
- **表名：** t_gl_cashflowitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_cashflowitem_l_pkey |  | fpkid |
| 2 | idx_gl_cashflowitem_l |  | fid,flocaleid |

---

## 现金流量项目-使用范围位图表 t_gl_cashflowitem_m

- **表名称：** 现金流量项目-使用范围位图表
- **表名：** t_gl_cashflowitem_m

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
| 1 | pk_t_gl_cashflowitem_m |  | forgid |

---

## 现金流量项目-主表 t_gl_cashflowitem

- **表名称：** 现金流量项目-主表
- **表名：** t_gl_cashflowitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fisdealactivity | 经营活动 | bpchar | 1 |  | √ | '0' | 经营活动 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 16 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [现金流量项目 gl_cashflowitem](../gl_files/gl_cashflowitem.md) |
| 17 | fisexchange | 汇率变动 | bpchar | 1 |  | √ | '0' | 汇率变动 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fisassist | 是否包含核算维度 | bpchar | 1 |  | √ | '0' | 是否包含核算维度 |
| 20 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 21 | flongnumber | 长编码 | varchar | 200 |  | √ | ' ' | 长编码 |
| 22 | fcashitemtbid | 现金流量项目表 | int8 | 64 |  | √ | 0 | [现金流量项目表 gl_cashflowitemtb](../gl_files/gl_cashflowitemtb.md) |
| 23 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '4' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 25 | fisprofit | 净利润 | bpchar | 1 |  | √ | '0' | 净利润 |
| 26 | ftype | 项目类别 | bpchar | 1 |  | √ | '0' | 项目类别,枚举: 1 :主表项目 3 :附表项目 |
| 27 | fisscheduleitem | 附表项目 | bpchar | 1 |  | √ | '0' | 附表项目 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fdirection | 现金流向 | bpchar | 1 |  | √ | '0' | 现金流向,枚举: b :流入流出 i :现金流入 o :现金流出 |
| 30 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 31 | fnotice | 现金流量通知单 | bpchar | 1 |  | √ | '0' | 现金流量通知单 |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gl_cashflowitem_master |  | fmasterid |
| 2 | idx_gl_cfi_createorg |  | fctrlstrategy,fcreateorgid |
| 3 | idx_gl_cfi_org |  | fctrlstrategy,forgid |
| 4 | idx_t_gl_cashflowitem_createorg |  | fcreateorgid |
| 5 | t_gl_cashflowitem_pkey |  | fid |
| 6 | idx_gl_cfi_masterid |  | fmasterid |
| 7 | idx_gl_cfi_num |  | fnumber |
| 8 | idx_gl_cfi_parent |  | fparentid |

---

## 核算维度-子表 t_gl_cashflowitemacttype

- **表名称：** 核算维度-子表
- **表名：** t_gl_cashflowitemacttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fasstypeid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 3 | fisdetail | 明细 | bpchar | 1 |  | √ | '0' | 明细 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fisrequire | 必录 | bpchar | 1 |  | √ | '0' | 必录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_cashflowitemacttype_pkey |  | fentryid |
| 2 | idx_gl_cashflowitemacttype |  | fid |
