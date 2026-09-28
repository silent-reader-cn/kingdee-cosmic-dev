# 配置映射-plm_ipdsm_settingmap

## 配置映射-主表 t_plm_ipdsm_settingmap

- **表名称：** 配置映射-主表
- **表名：** t_plm_ipdsm_settingmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | fentitysettingkey | 实体配置 | varchar | 50 |  | √ | ' ' | 实体配置 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fattrsetting | 属性设置标识 | varchar | 50 |  | √ | ' ' | 属性设置标识 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fappid | 应用标识 | varchar | 50 |  | √ | ' ' | 应用标识 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fissupportversion | 是否支持版本 | bpchar | 1 |  | √ | '0' | 是否支持版本 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fbelonggroup | 分类 | varchar | 50 |  | √ | ' ' | 分类 |
| 16 | fentry | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 20 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [配置映射 plm_ipdsm_settingmap](../plmipdsm_files/plm_ipdsm_settingmap.md) |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 27 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 28 | fcombofield | 行业 | varchar | 50 |  | √ | ' ' | 行业,枚举: soft :软件行业 elec :机电行业 other :其他 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipdsm_settingmap |  | fid |
| 2 | idx_t_plm_ipdsm_settingmap_master |  | fmasterid |
| 3 | idx_plm_ipdsm_settingmap_m0 |  | fmasterid |
| 4 | idx_t_plm_ipdsm_settingmap_createorg |  | fcreateorgid |

---

## 配置映射-多语言表 t_plm_ipdsm_settingmap_l

- **表名称：** 配置映射-多语言表
- **表名：** t_plm_ipdsm_settingmap_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 80 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipdsm_settingmap_l |  | fpkid |
| 2 | idx_plm_ipdsm_settingmap_l_0 |  | fid,flocaleid |

---

## 配置映射-使用范围表 t_plm_ipdsm_settingmap_u

- **表名称：** 配置映射-使用范围表
- **表名：** t_plm_ipdsm_settingmap_u

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
| 1 | pk_t_plm_ipdsm_settingmap_u |  | fdataid,fuseorgid |
| 2 | idx_t_plm_ipdsm_settingmap_u_uo |  | fuseorgid |
