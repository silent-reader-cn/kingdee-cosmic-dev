# 物料检修信息-mpdm_materialmtcinfo

## 物料检修信息-使用范围表 t_mpdm_materialmtcinfo_u

- **表名称：** 物料检修信息-使用范围表
- **表名：** t_mpdm_materialmtcinfo_u

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
| 1 | idx_t_mpdm_materialmtcinfo_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_materialmtcinfo_u |  | fdataid,fuseorgid |

---

## 物料检修信息-多语言表 t_mpdm_materialmtcinfo_l

- **表名称：** 物料检修信息-多语言表
- **表名：** t_mpdm_materialmtcinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_materialmtcinfo_l |  | fpkid |
| 2 | idx_mpdm_matefol_fid |  | fid,flocaleid |
| 3 | idx_mpdm_matefol_fname |  | fname |

---

## 物料检修信息-使用范围位图表 t_mpdm_materialmtcinfo_m

- **表名称：** 物料检修信息-使用范围位图表
- **表名：** t_mpdm_materialmtcinfo_m

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
| 1 | pk_t_mpdm_materialmtcinfo_m |  | forgid |

---

## 物料检修信息-主表 t_mpdm_materialmtcinfo

- **表名称：** 物料检修信息-主表
- **表名：** t_mpdm_materialmtcinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapmanufacturer | fapmanufacturer | int8 | 64 |  | √ | 0 |  |
| 3 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 4 | fmanufacturerid | 原产国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmarketvalue | fmarketvalue | numeric | 23 | 10 | √ | 0 |  |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fvlmodifttime | fvlmodifttime | timestamp | 0 |  |  | null |  |
| 10 | fmodeltwo1 | fmodeltwo1 | varchar | 255 |  | √ | ' ' |  |
| 11 | frecorddate | frecorddate | timestamp | 0 |  |  | null |  |
| 12 | fapmanufacturerid | 辅助动力制造商 | int8 | 64 |  | √ | 0 | [制造商 mpdm_manufacturer](../mpdm_files/mpdm_manufacturer.md) |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fbuilderid | fbuilderid | int8 | 64 |  | √ | 0 |  |
| 15 | fapmodifterid | fapmodifterid | int8 | 64 |  | √ | 0 |  |
| 16 | fmodeltrd | fmodeltrd | varchar | 255 |  | √ | ' ' |  |
| 17 | fegmodelone | 发动机型号L1 | varchar | 200 |  | √ | ' ' | 发动机型号L1 |
| 18 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 19 | fmtcmasterid | 物料检修信息内码 | int8 | 64 |  | √ | 0 | 物料检修信息内码 |
| 20 | fvadate | fvadate | timestamp | 0 |  |  | null |  |
| 21 | fmratypeid | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 22 | fapseq | 辅助动力序列号 | varchar | 255 |  | √ | ' ' | 辅助动力序列号 |
| 23 | fmodeltwo | fmodeltwo | varchar | 255 |  | √ | ' ' |  |
| 24 | fmodeltrd1 | fmodeltrd1 | varchar | 255 |  | √ | ' ' |  |
| 25 | fonmodifterid | fonmodifterid | int8 | 64 |  | √ | 0 |  |
| 26 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 31 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 32 | fchargeunitid | fchargeunitid | int8 | 64 |  | √ | 0 |  |
| 33 | foperattypeid | 运营类型 | int8 | 64 |  | √ | 0 | [运营类型 mpdm_operattype](../mpdm_files/mpdm_operattype.md) |
| 34 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 35 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 36 | ffirststdate | 首次运行日期 | timestamp | 0 |  |  | null | 首次运行日期 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fmasterid | 编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 39 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 40 | fapmodifttime | fapmodifttime | timestamp | 0 |  |  | null |  |
| 41 | fmodelone | 型号L1 | varchar | 255 |  | √ | ' ' | 型号L1 |
| 42 | fvlmodifterid | fvlmodifterid | int8 | 64 |  | √ | 0 |  |
| 43 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fmodelonempd | fmodelonempd | varchar | 255 |  | √ | ' ' |  |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fdeliverydate | 交付日期 | timestamp | 0 |  |  | null | 交付日期 |
| 48 | fenginetypeid | 发动机型号 | int8 | 64 |  | √ | 0 | [发动机型号 mpdm_enginetype](../mpdm_files/mpdm_enginetype.md) |
| 49 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 50 | fapmodel | 辅助动力型号 | varchar | 255 |  | √ | ' ' | 辅助动力型号 |
| 51 | fspecialconfigid | 特殊构型 | int8 | 64 |  | √ | 0 | [特殊构型 mpdm_specialconfig](../mpdm_files/mpdm_specialconfig.md) |
| 52 | fcabinconfigid | 客舱构型 | int8 | 64 |  | √ | 0 | [客舱构型 mpdm_cabinconfig](../mpdm_files/mpdm_cabinconfig.md) |
| 53 | fmodelone1 | fmodelone1 | varchar | 255 |  | √ | ' ' |  |
| 54 | fcheckboxfield | fcheckboxfield | int8 | 64 |  | √ | 0 |  |
| 55 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 56 | fonmodifttime | fonmodifttime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_matefo_fcreatetime |  | fcreatetime |
| 2 | pk_mpdm_materialmtcinfo |  | fid |
| 3 | idx_t_mpdm_materialmtcinfo_master |  | fmasterid |
| 4 | idx_mpdm_matefo_fnumber |  | fnumber |
| 5 | idx_t_mpdm_materialmtcinfo_createorg |  | fcreateorgid |

---

## 发动机信息-子表 t_mpdm_mtcengineentry

- **表名称：** 发动机信息-子表
- **表名：** t_mpdm_mtcengineentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fegcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fegcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fegmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fengineseq | 序列号 | varchar | 255 |  | √ | ' ' | 序列号 |
| 6 | flocation | 位置信息 | varchar | 255 |  | √ | ' ' | 位置信息 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fegmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_mtcery_fseq |  | fseq |
| 2 | pk_mpdm_mtcengineentry |  | fentryid |
| 3 | idx_mpdm_mtcery_fid |  | fid |
