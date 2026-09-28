# 细分市场-plm_prm_market

## 细分市场-主表 t_plm_prm_market

- **表名称：** 细分市场-主表
- **表名：** t_plm_prm_market

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsmstandards | 细分市场标准 | varchar | 50 |  | √ | ' ' | 细分市场标准 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmarketdesc | 细分市场描述 | varchar | 255 |  | √ | ' ' | 细分市场描述 |
| 10 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmarketbudget | 市场规模预测 | varchar | 50 |  | √ | ' ' | 市场规模预测 |
| 16 | fgeoscope | 地理范围 | varchar | 50 |  | √ | ' ' | 地理范围 |
| 17 | fcustomerprofile | 目标客户画像 | varchar | 50 |  | √ | ' ' | 目标客户画像 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fmarketdesc_tag | 细分市场描述_详情 | text | 0 |  |  | null | 细分市场描述_详情 |
| 21 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_prm_market_master |  | fmasterid |
| 2 | idx_plm_prm_market_m0 |  | fmasterid |
| 3 | idx_t_plm_prm_market_createorg |  | fcreateorgid |
| 4 | pk_plm_prm_market |  | fid |

---

## 细分市场-多语言表 t_plm_prm_market_l

- **表名称：** 细分市场-多语言表
- **表名：** t_plm_prm_market_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmarketbudget | 市场规模预测 | varchar | 80 |  | √ | ' ' | 市场规模预测 |
| 4 | fsmstandards | 细分市场标准 | varchar | 80 |  | √ | ' ' | 细分市场标准 |
| 5 | fcustomerprofile | 目标客户画像 | varchar | 80 |  | √ | ' ' | 目标客户画像 |
| 6 | fgeoscope | 地理范围 | varchar | 80 |  | √ | ' ' | 地理范围 |
| 7 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 8 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_prm_market_l_0 |  | fid,flocaleid |
| 2 | pk_plm_prm_market_l |  | fpkid |

---

## 细分市场-使用范围表 t_plm_prm_market_u

- **表名称：** 细分市场-使用范围表
- **表名：** t_plm_prm_market_u

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
| 1 | idx_t_plm_prm_market_u_uo |  | fuseorgid |
| 2 | pk_t_plm_prm_market_u |  | fdataid,fuseorgid |
