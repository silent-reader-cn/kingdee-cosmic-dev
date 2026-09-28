# 检修设备类型-mpdm_mrtype

## 检修设备类型-主表 t_mpdm_mrtype

- **表名称：** 检修设备类型-主表
- **表名：** t_mpdm_mrtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanufacturerid | 制造商 | int8 | 64 |  | √ | 0 | [制造商 mpdm_manufacturer](../mpdm_files/mpdm_manufacturer.md) |
| 3 | fmaxweight | 最大启动重量 | numeric | 23 | 10 | √ | 0 | 最大启动重量 |
| 4 | flength | 长 | numeric | 23 | 10 | √ | 0 | 长 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fwtunitid | 重量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fsource | 来源依据 | varchar | 255 |  | √ | ' ' | 来源依据 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fattachmentcount | fattachmentcount | int4 | 32 |  | √ | 0 |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fiswinlet | 翼尖小翼 | varchar | 5 |  | √ | ' ' | 翼尖小翼,枚举: 0 :N 1 :Y |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fmodelone | 型号L1 | varchar | 255 |  | √ | ' ' | 型号L1 |
| 19 | fmodeltrd | 型号L3 | varchar | 255 |  | √ | ' ' | 型号L3 |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | flightweight | 空载重量 | numeric | 23 | 10 | √ | 0 | 空载重量 |
| 24 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 25 | fbodytypeid | 机体分类 | int8 | 64 |  | √ | 0 | [机体类型 mpdm_bodytype](../mpdm_files/mpdm_bodytype.md) |
| 26 | fmodelmpdone | 型号L1-MPD | varchar | 255 |  | √ | ' ' | 型号L1-MPD |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fwide | 宽 | numeric | 23 | 10 | √ | 0 | 宽 |
| 29 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 30 | fmodeltwo | 型号L2 | varchar | 255 |  | √ | ' ' | 型号L2 |
| 31 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fheight | 高 | numeric | 23 | 10 | √ | 0 | 高 |
| 33 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 34 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fsizeunitid | 尺寸单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_mrtype_createorg |  | fcreateorgid |
| 2 | pk_mpdm_mrtype |  | fid |
| 3 | idx_mpdm_mrtype_fnumber |  | fnumber |
| 4 | idx_t_mpdm_mrtype_master |  | fmasterid |
| 5 | idx_mpdm_mrtype_fcreatetime |  | fcreatetime |

---

## 检修设备类型-多语言表 t_mpdm_mrtype_l

- **表名称：** 检修设备类型-多语言表
- **表名：** t_mpdm_mrtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |
| 6 | fsource | 来源依据 | varchar | 255 |  | √ | ' ' | 来源依据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_mrtypel_fid |  | fid,flocaleid |
| 2 | idx_mpdm_mrtypel_fname |  | fname |
| 3 | pk_mpdm_mrtype_l |  | fpkid |

---

## 检修设备类型-使用范围位图表 t_mpdm_mrtype_m

- **表名称：** 检修设备类型-使用范围位图表
- **表名：** t_mpdm_mrtype_m

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
| 1 | pk_t_mpdm_mrtype_m |  | forgid |

---

## 检修设备类型-使用范围表 t_mpdm_mrtype_u

- **表名称：** 检修设备类型-使用范围表
- **表名：** t_mpdm_mrtype_u

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
| 1 | idx_t_mpdm_mrtype_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_mrtype_u |  | fdataid,fuseorgid |
