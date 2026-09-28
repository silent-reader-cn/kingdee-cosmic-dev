# 工卡风险信息-mpdm_cardriskdef

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

## 工卡风险信息-主表 t_mpdm_riskdef

- **表名称：** 工卡风险信息-主表
- **表名：** t_mpdm_riskdef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcardspecial | fcardspecial | int8 | 64 |  | √ | 0 |  |
| 5 | fchecklevel | fchecklevel | int8 | 64 |  | √ | 0 |  |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fminlimitsymbol | fminlimitsymbol | varchar | 50 |  | √ | ' ' |  |
| 14 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmaterial | fmaterial | int8 | 64 |  | √ | 0 |  |
| 19 | fmaxlimitsymbol | fmaxlimitsymbol | varchar | 50 |  | √ | ' ' |  |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fsuggestion | fsuggestion | varchar | 255 |  | √ | ' ' |  |
| 25 | fenabler | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fmaterialtype | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 27 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 28 | fenabletime | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 29 | fmaxlinitnum | fmaxlinitnum | numeric | 23 | 10 | √ | 0 |  |
| 30 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fminlinitnum | fminlinitnum | numeric | 23 | 10 | √ | 0 |  |
| 32 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 33 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
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
| 9 | friskdeftype | 风险类别 | int8 | 64 |  | √ | 0 | [风险类别 mpdm_risktype](../mpdm_files/mpdm_risktype.md) |
| 10 | flowerlimitsymbol | 下限公式符号 | varchar | 50 |  | √ | ' ' | 下限公式符号,枚举: A := C :> |
| 11 | friskdefdsc | 风险描述 | varchar | 255 |  | √ | ' ' | 风险描述 |

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

## 工卡风险信息-使用范围位图表 t_mpdm_riskdef_m

- **表名称：** 工卡风险信息-使用范围位图表
- **表名：** t_mpdm_riskdef_m

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
| 1 | pk_t_mpdm_riskdef_m |  | forgid |

---

## 工卡风险信息-多语言表 t_mpdm_riskdef_l

- **表名称：** 工卡风险信息-多语言表
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

---

## 工卡风险信息-使用范围表 t_mpdm_riskdef_u

- **表名称：** 工卡风险信息-使用范围表
- **表名：** t_mpdm_riskdef_u

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
| 1 | idx_t_mpdm_riskdef_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_riskdef_u |  | fdataid,fuseorgid |
