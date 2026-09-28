# 风险定义-mpdm_riskdef

## 风险信息-多语言表 t_mpdm_riskdefentry_l

- **表名称：** 风险信息-多语言表
- **表名：** t_mpdm_riskdefentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | friskadvice | 风险应对建议 | varchar | 255 |  | √ | ' ' | 风险应对建议 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_riskdefentry_l |  | fpkid |
| 2 | idx_mpdm_riskdefentry_l_0 |  | fentryid,flocaleid |

---

## 风险定义-主表 t_mpdm_riskdef

- **表名称：** 风险定义-主表
- **表名：** t_mpdm_riskdef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 风险类别 | int8 | 64 |  | √ | 0 | [风险类别 mpdm_risktype](../mpdm_files/mpdm_risktype.md) |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fcardspecial | fcardspecial | int8 | 64 |  | √ | 0 |  |
| 5 | fchecklevel | 检修等级（废弃） | int8 | 64 |  | √ | 0 | [检修等级 mpdm_checklevel](../mpdm_files/mpdm_checklevel.md) |
| 6 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 7 | faudittime | faudittime | timestamp | 0 |  |  | null |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdisabletime | fdisabletime | timestamp | 0 |  |  | null |  |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fminlimitsymbol | 下限公式符号（废弃） | varchar | 50 |  | √ | ' ' | 下限公式符号（废弃）,枚举: A := B :> |
| 14 | fauditor | fauditor | int8 | 64 |  | √ | 0 |  |
| 15 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 16 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 17 | fdisabler | fdisabler | int8 | 64 |  | √ | 0 |  |
| 18 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 19 | fmaxlimitsymbol | 上限公式符号（废弃） | varchar | 50 |  | √ | ' ' | 上限公式符号（废弃）,枚举: A := C :< |
| 20 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 21 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fsuggestion | 风险对应建议（废弃） | varchar | 255 |  | √ | ' ' | 风险对应建议（废弃） |
| 25 | fenabler | fenabler | int8 | 64 |  | √ | 0 |  |
| 26 | fmaterialtype | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 27 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 28 | fenabletime | fenabletime | timestamp | 0 |  |  | null |  |
| 29 | fmaxlinitnum | 维修周期阈值上限（废弃） | numeric | 23 | 10 | √ | 0 | 维修周期阈值上限（废弃） |
| 30 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fminlinitnum | 维修周期阈值下限（废弃） | numeric | 23 | 10 | √ | 0 | 维修周期阈值下限（废弃） |
| 32 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 33 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |
| 34 | fcard | 工卡编码 | int8 | 64 |  | √ | 0 | [工卡 mpdm_mrocardroute](../mpdm_files/mpdm_mrocardroute.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_riskdef |  | fid |
| 2 | t_mpdm_riskdef_fnumber_idx |  | fnumber |
| 3 | idx_t_mpdm_riskdef_createorg |  | fcreateorgid |
| 4 | idx_t_mpdm_riskdef_master |  | fmasterid |

---

## 风险信息-子表 t_mpdm_riskdefentry

- **表名称：** 风险信息-子表
- **表名：** t_mpdm_riskdefentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flowerlimit | 维修周期阈值下限 | numeric | 23 | 10 | √ | 0 | 维修周期阈值下限 |
| 3 | frepairlevel | 检修等级 | int8 | 64 |  | √ | 0 | [检修等级 mpdm_checklevel](../mpdm_files/mpdm_checklevel.md) |
| 4 | fupperlimitsymbol | 上限公式符号 | varchar | 50 |  | √ | ' ' | 上限公式符号,枚举: A := B :< |
| 5 | friskadvice | 风险应对建议 | varchar | 255 |  | √ | ' ' | 风险应对建议 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fupperlimit | 维修周期阈值上限 | numeric | 23 | 10 | √ | 0 | 维修周期阈值上限 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | friskdeftype | friskdeftype | int8 | 64 |  | √ | 0 |  |
| 10 | flowerlimitsymbol | 下限公式符号 | varchar | 50 |  | √ | ' ' | 下限公式符号,枚举: A := C :> |
| 11 | friskdefdsc | friskdefdsc | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_riskdefentry_fk |  | fid |
| 2 | pk_mpdm_riskdefentry |  | fentryid |

---

## 风险定义-多语言表 t_mpdm_riskdef_l

- **表名称：** 风险定义-多语言表
- **表名：** t_mpdm_riskdef_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_riskdef_l |  | fpkid |
| 2 | idx_mpdm_riskdef_l_0 |  | fid,flocaleid |
