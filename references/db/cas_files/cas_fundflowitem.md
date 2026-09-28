# 资金用途-cas_fundflowitem

## 资金用途-使用范围表 t_cas_fundflowitem_u

- **表名称：** 资金用途-使用范围表
- **表名：** t_cas_fundflowitem_u

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
| 1 | t_cas_fundflowitem_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_cas_fundflowitem_u_uo |  | fuseorgid |

---

## 资金用途-多语言表 t_cas_fundflowitem_l

- **表名称：** 资金用途-多语言表
- **表名：** t_cas_fundflowitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 1000 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 1000 |  |  | null | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_ffl_fpid |  | fid,flocaleid |
| 2 | t_cas_fundflowitem_l_pkey |  | fpkid |

---

## 资金用途-使用范围位图表 t_cas_fundflowitem_m

- **表名称：** 资金用途-使用范围位图表
- **表名：** t_cas_fundflowitem_m

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
| 1 | pk_t_cas_fundflowitem_m |  | forgid |

---

## 资金用途-主表 t_cas_fundflowitem

- **表名称：** 资金用途-主表
- **表名：** t_cas_fundflowitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fparentid | 上级资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | ffullname | ffullname | varchar | 256 |  | √ | ' ' |  |
| 19 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 20 | fproperty | 属性 | varchar | 5 |  | √ | ' ' | 属性,枚举: A :经营活动 B :投资活动 C :筹资活动 D :内部往来 E :其他 |
| 21 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 22 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 7 :私有 |
| 23 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 24 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 25 | fenable | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :禁用 1 :可用 |
| 26 | fdirection | 流向 | varchar | 5 |  | √ | ' ' | 流向,枚举: A :流入/流出 B :流入 C :流出 D :期初余额 E :期末余额 |
| 27 | fnumber | 编码 | varchar | 80 |  |  | ' ' | 编码 |
| 28 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cas_fundflowitem_createorg |  | fcreateorgid |
| 2 | idx_cas_ff_fnumber |  | fnumber |
| 3 | idx_t_cas_fundflowitem_master |  | fmasterid |
| 4 | t_cas_fundflowitem_pkey |  | fid |
