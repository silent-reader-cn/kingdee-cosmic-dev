# 核销方案-msmod_scheme

## 核销方案-主表 t_msmod_scheme

- **表名称：** 核销方案-主表
- **表名：** t_msmod_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fdescribe | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fmatchruleid | 匹配规则 | int8 | 64 |  | √ | 0 | [匹配规则 msmod_matchrule](../mscommon_files/msmod_matchrule.md) |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fprecut | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 13 | fwriteofftype | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |
| 14 | fisunconditionmatch | 无条件匹配 | bpchar | 1 |  | √ | ' ' | 无条件匹配 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msmod_scheme_fnumber |  | fnumber |
| 2 | pk_t_msmod_scheme |  | fid |

---

## 排序规则-子表 t_msmod_smsortentry

- **表名称：** 排序规则-子表
- **表名：** t_msmod_smsortentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 3 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 4 | fsortbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [核销单据类型 msmod_billtype](../mscommon_files/msmod_billtype.md) |
| 5 | fsmsispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsorttype | 排序方式 | bpchar | 1 |  | √ | ' ' | 排序方式,枚举: 0 :升序 1 :降序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_smsortentry |  | fentryid |
| 2 | idx_smsort_fsortbilltypeid |  | fsortbilltypeid |
| 3 | idx_t_msmod_smsort_fid |  | fid |

---

## 核销方案-多语言表 t_msmod_scheme_l

- **表名称：** 核销方案-多语言表
- **表名：** t_msmod_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 512 |  | √ | ' ' | 名称 |
| 3 | fdescribe | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msmod_scheme_l_id |  | fid,flocaleid |
| 2 | pk_t_msmod_scheme_l |  | fpkid |

---

## 分摊面板-子表 t_msmod_schshareentity

- **表名称：** 分摊面板-子表
- **表名：** t_msmod_schshareentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffiltercondition_tag | 过滤条件有效值_详情 | text | 0 |  |  | null | 过滤条件有效值_详情 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fisabs | 取绝对值 | bpchar | 1 |  | √ | '0' | 取绝对值 |
| 5 | ffilterconditionview | 过滤条件 | varchar | 512 |  | √ | ' ' | 过滤条件 |
| 6 | fsharefield | 分摊标准字段 | varchar | 50 |  | √ | ' ' | 分摊标准字段 |
| 7 | ffilterconditiondesc | 过滤条件详情(JSON) | varchar | 255 |  | √ | ' ' | 过滤条件详情(JSON) |
| 8 | fseispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | ffilterconditiondesc_tag | 过滤条件详情(JSON)_详情 | text | 0 |  |  | null | 过滤条件详情(JSON)_详情 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ffiltercondition | 过滤条件有效值 | varchar | 255 |  | √ | ' ' | 过滤条件有效值 |
| 12 | fsharewfbilltypeid | 核销单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fsharefieldkey | 分摊标准字段Key | varchar | 50 |  | √ | ' ' | 分摊标准字段Key |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_schshareentity_fid |  | fid |
| 2 | pk_t_msmod_schshareentity |  | fentryid |
