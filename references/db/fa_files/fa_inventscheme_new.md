# 盘点方案-fa_inventscheme_new

## 拆分规则详情-子表 t_fa_invent_taskrule

- **表名称：** 拆分规则详情-子表
- **表名：** t_fa_invent_taskrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsplitfieldvalue | 拆分依据字段值 | varchar | 2000 |  |  | ' ' | 拆分依据字段值 |
| 2 | finventperson | 盘点负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fentrystatus | 任务状态 | bpchar | 1 |  | √ | 'A' | 任务状态,枚举: A :未下达 B :已下达 C :已生成 Z :未保存 |
| 4 | finventschemeid | 盘点方案ID | int8 | 64 |  | √ | 0 | 盘点方案ID |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_invent_taskrule_pkey |  | fdetailid |
| 2 | idx_fa_invent_taskrule |  | fentryid |

---

## 盘点范围单据体-多语言表 t_fa_inventschemeentry_l

- **表名称：** 盘点范围单据体-多语言表
- **表名：** t_fa_inventschemeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 2 | fname | 任务名称 | varchar | 100 |  | √ | ' ' | 任务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_inventschemeentry_l_pkey |  | fpkid |
| 2 | idx_fa_inventschemeentry_l |  | fentryid,flocaleid |

---

## 盘点范围单据体-子表 t_fa_inventschemeentry

- **表名称：** 盘点范围单据体-子表
- **表名：** t_fa_inventschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | 任务名称 | varchar | 100 |  | √ | ' ' | 任务名称 |
| 4 | fqtytypevalue | 盘点数量默认值 | varchar | 10 |  | √ | '0' | 盘点数量默认值,枚举: 0 :0 1 :账存数量 |
| 5 | fchargepersonid | 盘点负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | finventorymode | 盘点模式 | varchar | 200 |  | √ | ' ' | 盘点模式,枚举: assetamount :资产数量 headuseperson :使用人 headusedept :使用部门 storeplace :存放地点 |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | ffiltercondition_tag | 盘点范围过滤条件_详情 | text | 0 |  |  | ' ' | 盘点范围过滤条件_详情 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fstatus | 任务状态 | bpchar | 1 |  | √ | 'A' | 任务状态,枚举: A :未下达 B :已下达 C :已生成 Z :未保存 |
| 12 | finventschemeentryid | finventschemeentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fassetunitid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | ffinaccountdate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 15 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 16 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 17 | ftaskrule | 任务拆分规则 | varchar | 50 |  | √ | ' ' | 任务拆分规则 |
| 18 | fenable | fenable | bpchar | 1 |  | √ | '1' |  |
| 19 | fnumber | 任务编码 | varchar | 50 |  | √ | ' ' | 任务编码 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | ffiltercondition | 盘点范围过滤条件 | varchar | 512 |  | √ | ' ' | 盘点范围过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_inventschemeentry_fid |  | fid |
| 2 | t_fa_inventschemeentry_pkey |  | fentryid |

---

## 盘点方案-主表 t_fa_inventscheme

- **表名称：** 盘点方案-主表
- **表名：** t_fa_inventscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmigsrc | 是否迁移 | int4 | 32 |  | √ | 0 | 是否迁移 |
| 10 | fbillstate | 单据状态(弃用) | bpchar | 1 |  | √ | '0' | 单据状态(弃用),枚举: A :进行中 C :已关闭 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '1' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 1 :逐级分配 6 :管控范围内共享 |
| 13 | fstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 20 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_inventscheme_fbillno |  | fnumber |
| 2 | idx_t_fa_inventscheme_createorg |  | fcreateorgid |
| 3 | t_fa_inventscheme_pkey |  | fid |
| 4 | idx_t_fa_inventscheme_master |  | fmasterid |

---

## 盘点方案-使用范围位图表 t_fa_inventscheme_m

- **表名称：** 盘点方案-使用范围位图表
- **表名：** t_fa_inventscheme_m

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
| 1 | pk_t_fa_inventscheme_m |  | forgid |

---

## 盘点方案-多语言表 t_fa_inventscheme_l

- **表名称：** 盘点方案-多语言表
- **表名：** t_fa_inventscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_inventscheme_l_fid |  | fid |
| 2 | t_fa_inventscheme_l_pkey |  | fpkid |

---

## 盘点方案-使用范围表 t_fa_inventscheme_u

- **表名称：** 盘点方案-使用范围表
- **表名：** t_fa_inventscheme_u

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
| 1 | pk_t_fa_inventscheme_u |  | fdataid,fuseorgid |
| 2 | idx_t_fa_inventscheme_u_uo |  | fuseorgid |

---

## 拆分依据-子表 t_fa_invent_splitfield

- **表名称：** 拆分依据-子表
- **表名：** t_fa_invent_splitfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fsplitfield | 依据字段 | varchar | 50 |  | √ | ' ' | 依据字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_invent_splitfield_pkey |  | fdetailid |
| 2 | idx_fa_invent_splitfield |  | fentryid |
