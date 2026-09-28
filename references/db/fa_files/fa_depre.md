# 计提折旧-fa_depre

## 计提折旧-多语言表 t_fa_assetbook_l

- **表名称：** 计提折旧-多语言表
- **表名：** t_fa_assetbook_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_assetbook_l_pkey |  | fpkid |
| 2 | idx_fa_assetbook_l |  | fid,flocaleid |
| 3 | t_fa_assetbook_l_fid_flocaleid_key |  | fid,flocaleid |

---

## 计提折旧-主表 t_fa_assetbook

- **表名称：** 计提折旧-主表
- **表名：** t_fa_assetbook

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexchangetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | facctperiodtypeid | 会计日历 | int8 | 64 |  | √ | 0 | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 4 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdepresystemid | 资产政策 | int8 | 64 |  | √ | 0 | [资产政策 fa_depresystem](../fa_files/fa_depresystem.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdepreuse | 折旧用途 | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: B :未结束初始化 C :已结束初始化 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fpcstatus | 月结状态 | varchar | 50 |  | √ | 'INIT' | 月结状态,枚举: INIT : PC_ING :月结中 PC_ERR :月结失败 UPC_ING :反月结中 UPC_ERR :反月结失败 |
| 12 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 13 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 14 | fxkpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 15 | fcurrentperiodid | 当前期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 16 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fdepresystementryid | 折旧体系分录 | int8 | 64 |  | √ | 0 | [折旧体系分录 fa_depresystementry](../fa_files/fa_depresystementry.md) |
| 21 | fxkisenabled | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 22 | fenableperiodid | 启用期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 23 | fisgroupbook | fisgroupbook | bpchar | 1 |  | √ | '0' |  |
| 24 | fpcsubstatus | 月结子状态 | varchar | 50 |  | √ | 'INIT' | 月结子状态 |
| 25 | fctrlstrategy | fctrlstrategy | varchar | 10 |  | √ | ' ' |  |
| 26 | fismainbook | 主账簿 | bpchar | 1 |  | √ | '0' | 主账簿 |
| 27 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 30 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fa_assetbook_master |  | fmasterid |
| 2 | idx_t_fa_assetbook_createorg |  | fcreateorgid |
| 3 | t_fa_assetbook_pkey |  | fid |
| 4 | idx_fa_assboo_fnumber |  | fnumber |
