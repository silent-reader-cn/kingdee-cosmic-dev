# 资产类别-fa_assetcategory

## 资产类别-使用范围表 t_fa_assetcategory_u

- **表名称：** 资产类别-使用范围表
- **表名：** t_fa_assetcategory_u

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
| 1 | t_fa_assetcategory_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_fa_assetcategory_u_uo |  | fuseorgid |

---

## 资产类别-使用范围位图表 t_fa_assetcategory_m

- **表名称：** 资产类别-使用范围位图表
- **表名：** t_fa_assetcategory_m

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
| 1 | pk_t_fa_assetcategory_m |  | forgid |

---

## 资产类别-多语言表 t_fa_assetcategory_l

- **表名称：** 资产类别-多语言表
- **表名：** t_fa_assetcategory_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 500 |  |  | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 500 |  |  | ' ' | 名称 |
| 4 | ffullname | 长名称 | varchar | 500 |  |  | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_assetcategory_l_pkey |  | fpkid |
| 2 | idx_fa_assetcategory_l |  | fid,flocaleid |

---

## 资产类别-主表 t_fa_assetcategory

- **表名称：** 资产类别-主表
- **表名：** t_fa_assetcategory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | fcardindexprefix | 卡片编码前缀 | varchar | 50 |  | √ | ' ' | 卡片编码前缀 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fremark | 备注 | varchar | 500 |  |  | ' ' | 备注 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | 名称 | varchar | 500 |  |  | ' ' | 名称 |
| 17 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | ffullname | 长名称 | varchar | 500 |  |  | ' ' | 长名称 |
| 20 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | flongnumber | 长编码 | varchar | 80 |  | √ | ' ' | 长编码 |
| 22 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 7 :私有 |
| 23 | fisdataasset | 数据资产 | bpchar | 1 |  | √ | '0' | 数据资产 |
| 24 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 25 | fenable | 使用状态 | varchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 27 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 28 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fa_assetcategory_createorg |  | fcreateorgid |
| 2 | idx_fa_asscat_fnumber |  | fnumber |
| 3 | t_fa_assetcategory_pkey |  | fid |
| 4 | idx_t_fa_assetcategory_master |  | fmasterid |
