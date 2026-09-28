# 签入反写规则-botp_wrlistcheckin

## 签入反写规则-分表 t_botp_writebackrule_s

- **表名称：** 签入反写规则-分表
- **表名：** t_botp_writebackrule_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fcuststatus | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态,枚举: 0 :草稿 1 :启用 2 :禁用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_botp_writebackrule_s |  | fcuststatus |
| 2 | t_botp_writebackrule_s_pkey |  | fid |

---

## 签入反写规则-多语言表 t_botp_writebackrule_l

- **表名称：** 签入反写规则-多语言表
- **表名：** t_botp_writebackrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdata | fdata | text | 0 |  |  | null |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_botp_writebackrule_l_pkey |  | fpkid |
| 2 | idx_botp_writebackrule_l_fid |  | fid |

---

## 签入反写规则-主表 t_botp_writebackrule

- **表名称：** 签入反写规则-主表
- **表名：** t_botp_writebackrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 标识 | varchar | 36 |  | √ | ' ' | 标识 |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fsubsysid | fsubsysid | int8 | 64 |  |  | null |  |
| 4 | fmodeltype | fmodeltype | varchar | 50 |  |  | null |  |
| 5 | fparentid | 父规则 | varchar | 36 |  |  | null | [反写规则 botp_writebackrule](../botp_files/botp_writebackrule.md) |
| 6 | fisv | 开发商 | varchar | 50 |  |  | null | 开发商 |
| 7 | finheritpath | finheritpath | varchar | 300 |  | √ | ' ' |  |
| 8 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fsysstatus | 出厂状态 | bpchar | 1 |  |  | '0' | 出厂状态,枚举: 0 :正常 1 :禁用 |
| 10 | fcreatedate | fcreatedate | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 11 | fmasterid | 原始规则 | varchar | 36 |  | √ | ' ' | [反写规则 botp_writebackrule](../botp_files/botp_writebackrule.md) |
| 12 | ftype | 扩展状态 | bpchar | 1 |  | √ | '0' | 扩展状态,枚举: 0 :原始规则 1 :派生规则 2 :扩展规则 |
| 13 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 14 | ftimestamp | ftimestamp | int8 | 64 |  |  | null |  |
| 15 | fdata | fdata | text | 0 |  |  | null |  |
| 16 | fistemplate | fistemplate | bpchar | 1 |  |  | '0' |  |
| 17 | fsourceentitynumber | 源单 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 18 | fversion | fversion | int8 | 64 |  | √ | 0 |  |
| 19 | ftargetentitynumber | 目标单 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 20 | fcuststatus | fcuststatus | bpchar | 1 |  |  | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_botp_writebackrule_pkey |  | fid |
| 2 | idx_botp_writebackrule_t |  | ftargetentitynumber |
| 3 | idx_botp_writebackrule_ms |  | fmasterid |
