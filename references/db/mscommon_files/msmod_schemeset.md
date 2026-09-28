# 流程核销配置-msmod_schemeset

## 核销单据-子表 t_msmod_scheme_billentry

- **表名称：** 核销单据-子表
- **表名：** t_msmod_scheme_billentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffiltercondition_tag | 过滤条件有效值_详情 | text | 0 |  |  | null | 过滤条件有效值_详情 |
| 3 | fwriteoffop | 核销 | varchar | 30 |  | √ | ' ' | 核销 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcfiltercondition_tag | 追加过滤条件有效值_详情 | text | 0 |  |  | null | 追加过滤条件有效值_详情 |
| 6 | ffilterconditiondesc | 过滤条件详情(JSON) | varchar | 255 |  | √ | ' ' | 过滤条件详情(JSON) |
| 7 | fcwriteoffbillfilter | 追加条件过滤 | varchar | 512 |  | √ | ' ' | 追加条件过滤 |
| 8 | frewriteoffop | 反核销 | varchar | 30 |  | √ | ' ' | 反核销 |
| 9 | frewriteoffopname | 反核销 | varchar | 50 |  | √ | ' ' | 反核销 |
| 10 | fwriteoffbillfilter | 条件过滤 | varchar | 255 |  | √ | ' ' | 条件过滤 |
| 11 | fsbispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 12 | fwriteoffbill | 核销单据 | int8 | 64 |  | √ | 0 | [核销单据类型 msmod_billtype](../mscommon_files/msmod_billtype.md) |
| 13 | fissync | 同步调用 | bpchar | 1 |  | √ | '0' | 同步调用 |
| 14 | ffilterconditiondesc_tag | 过滤条件详情(JSON)_详情 | text | 0 |  |  | null | 过滤条件详情(JSON)_详情 |
| 15 | fcfilterconditiondesc | 过滤条件详情(JSON) | varchar | 255 |  | √ | ' ' | 过滤条件详情(JSON) |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | ffiltercondition | 过滤条件有效值 | varchar | 255 |  | √ | ' ' | 过滤条件有效值 |
| 18 | fwriteoffopname | 核销 | varchar | 50 |  | √ | ' ' | 核销 |
| 19 | fcfiltercondition | 追加过滤条件有效值 | varchar | 255 |  | √ | ' ' | 追加过滤条件有效值 |
| 20 | fcfilterconditiondesc_tag | 过滤条件详情(JSON)_详情 | text | 0 |  |  | null | 过滤条件详情(JSON)_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_scheme_billentry |  | fentryid |
| 2 | idx_t_msmod_scheme_bill_fid |  | fid |

---

## 核销顺序（废弃）-子表 t_msmod_scheme_sortentry

- **表名称：** 核销顺序（废弃）-子表
- **表名：** t_msmod_scheme_sortentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funilateral | 单边核销 | bpchar | 1 |  | √ | ' ' | 单边核销 |
| 3 | frbpriority | 红蓝单优先核销 | bpchar | 1 |  | √ | ' ' | 红蓝单优先核销 |
| 4 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 5 | fequalsfirst | 数值相等优先核销 | bpchar | 1 |  | √ | ' ' | 数值相等优先核销 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fonlyequals | 数值相等核销 | bpchar | 1 |  | √ | ' ' | 数值相等核销 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fwriteoffscheme | 自动核销方案 | int8 | 64 |  | √ | 0 | [核销方案 msmod_scheme](../mscommon_files/msmod_scheme.md) |
| 10 | fwhole | 完全核销 | bpchar | 1 |  | √ | ' ' | 完全核销 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scheme_sortentry_fid |  | fid |
| 2 | pk_t_msmod_scheme_sortentry |  | fentryid |

---

## 流程核销配置-多语言表 t_msmod_schemeset_l

- **表名称：** 流程核销配置-多语言表
- **表名：** t_msmod_schemeset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 512 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msmod_schemeset_l_id |  | fid,flocaleid |
| 2 | pk_t_msmod_schemeset_l |  | fpkid |

---

## 流程核销配置-主表 t_msmod_schemeset

- **表名称：** 流程核销配置-主表
- **表名：** t_msmod_schemeset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 10 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fwriteofftypeid | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_schemeset |  | fid |
| 2 | idx_t_msmod_schemeset_fnumber |  | fnumber |

---

## 核销顺序-子表 t_msmod_sch_sortsubentry

- **表名称：** 核销顺序-子表
- **表名：** t_msmod_sch_sortsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsub_wf_scheme | 流程核销方案 | int8 | 64 |  | √ | 0 | [核销方案 msmod_scheme](../mscommon_files/msmod_scheme.md) |
| 2 | fsub_unilateral | 单边核销 | bpchar | 1 |  | √ | ' ' | 单边核销 |
| 3 | fsub_equalsfirst | 数量/金额相等优先 | bpchar | 1 |  | √ | ' ' | 数量/金额相等优先 |
| 4 | fsub_whole | 完全核销 | bpchar | 1 |  | √ | ' ' | 完全核销 |
| 5 | fsub_rbpriority | 红蓝单优先核销 | bpchar | 1 |  | √ | ' ' | 红蓝单优先核销 |
| 6 | fsub_onlyequals | 数量/金额相等 | bpchar | 1 |  | √ | ' ' | 数量/金额相等 |
| 7 | fseispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fsub_priority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_sch_sortsubentry |  | fdetailid |
| 2 | idx_sch_sortsubentry_fentryid |  | fentryid |
