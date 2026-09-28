# 尾差规则-xkbotp_taildiff

## 尾差规则-多语言表 t_xkbotp_taildiff_l

- **表名称：** 尾差规则-多语言表
- **表名：** t_xkbotp_taildiff_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_taildiff_l_localeid |  | fid,flocaleid |
| 2 | pk_t_xkbotp_taildiff_l |  | fpkid |

---

## 转换规则设置单据体-子表 t_xkbotp_taildiff_rules

- **表名称：** 转换规则设置单据体-子表
- **表名：** t_xkbotp_taildiff_rules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconvertruleid | 标识 | varchar | 36 |  | √ | ' ' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbotp_taildiff_rules |  | fentryid |
| 2 | idx_taildiff_rules_fid |  | fid,fseq |
| 3 | idx_taildiff_rules_rid |  | fconvertruleid |

---

## 尾查字段和条件设置单据体-子表 t_xkbotp_taildiff_field

- **表名称：** 尾查字段和条件设置单据体-子表
- **表名：** t_xkbotp_taildiff_field

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmulbasefactor | 基本条件类型 | varchar | 100 |  | √ | ' ' | 基本条件类型,枚举: unit_price :单价 exchange_rate :汇率 tax_tate :税率 discount_rate :折扣率 customer_factor :自定义 |
| 3 | fsourcefactorfield | 源单条件字段 | varchar | 50 |  | √ | ' ' | 源单条件字段,枚举: |
| 4 | ftargettailfield | 目标单尾差调整字段 | varchar | 50 |  | √ | ' ' | 目标单尾差调整字段,枚举: |
| 5 | fsourcetailfield | 源单尾差匹配字段 | varchar | 50 |  | √ | ' ' | 源单尾差匹配字段,枚举: |
| 6 | fisnegativebusiness | 负向业务 | bpchar | 1 |  | √ | '0' | 负向业务 |
| 7 | ftargetfactorfield | 目标单条件字段 | varchar | 50 |  | √ | ' ' | 目标单条件字段,枚举: |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fadjustrange | 允许调整范围 | numeric | 23 | 10 | √ | 0 | 允许调整范围 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbotp_taildiff_field |  | fentryid |
| 2 | idx_taildiff_field_fid |  | fid,fseq |

---

## 基本条件设置单据体-子表 t_xkbotp_taildiff_factor

- **表名称：** 基本条件设置单据体-子表
- **表名：** t_xkbotp_taildiff_factor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasefactortype | 基本条件类型 | varchar | 50 |  | √ | ' ' | 基本条件类型,枚举: unit_price :单价 exchange_rate :汇率 tax_tate :税率 discount_rate :折扣率 customer_factor :自定义字段 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftargetbasefactorfield | 目标单基本条件字段 | varchar | 50 |  | √ | ' ' | 目标单基本条件字段,枚举: |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsourcebasefactorfield | 源单基本条件字段 | varchar | 50 |  | √ | ' ' | 源单基本条件字段,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbotp_taildiff_factor |  | fentryid |
| 2 | idx_taildiff_factor_fid |  | fid,fseq |

---

## 尾差规则-主表 t_xkbotp_taildiff

- **表名称：** 尾差规则-主表
- **表名：** t_xkbotp_taildiff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmarkkey | 尾差调整标识字段 | varchar | 50 |  | √ | ' ' | 尾差调整标识字段,枚举: |
| 8 | frecordkey | 尾差调整日志字段 | varchar | 50 |  | √ | ' ' | 尾差调整日志字段,枚举: |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fissystem | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 12 | fexecevent | 尾差执行事件 | varchar | 50 |  | √ | ' ' | 尾差执行事件,枚举: afterBizRule :afterBizRule afterConvert :afterConvert |
| 13 | fenable | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态,枚举: 0 :未启用 1 :启用 |
| 14 | fnumber | 标识 | varchar | 30 |  | √ | ' ' | 标识 |
| 15 | fsourceentitynumber | 源单 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | ftargetentitynumber | 目标单 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fversion | 版本号 | int8 | 64 |  | √ | 0 | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | iidx_xkbotp_taildiff_trg |  | ftargetentitynumber |
| 2 | pk_xkbotp_taildiff |  | fid |
| 3 | iidx_xkbotp_taildiff_src |  | fsourceentitynumber |
