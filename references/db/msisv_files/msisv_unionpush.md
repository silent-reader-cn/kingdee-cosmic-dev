# 联合下推-msisv_unionpush

## 联合下推-主表 t_msisv_unionpush

- **表名称：** 联合下推-主表
- **表名：** t_msisv_unionpush

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmonitorobj | 监听对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fsrcbillfilterjson_tag | 来源单据过滤条件json_详情 | text | 0 |  |  | null | 来源单据过滤条件json_详情 |
| 4 | ftarbill | 目标单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | frelateobjfilterjson | 过滤条件json | varchar | 255 |  | √ | ' ' | 过滤条件json |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | ftarbillmainfield | 目标单据字段 | varchar | 50 |  | √ | ' ' | 目标单据字段 |
| 8 | fsrcbill | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fisinvorelateobj | 是否涉及关联对象 | bpchar | 1 |  | √ | '0' | 是否涉及关联对象 |
| 10 | frelateobjfilterjson_tag | 过滤条件json_详情 | text | 0 |  |  | null | 过滤条件json_详情 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbotpruleid | BOTP转换规则 | varchar | 50 |  | √ | ' ' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | frelateobjfilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | frelateobj | 关联对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 18 | frelateobjmainfield | 关联对象字段 | varchar | 50 |  | √ | ' ' | 关联对象字段 |
| 19 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | frelateobjmainfieldkey | 关联对象字段标识 | varchar | 50 |  | √ | ' ' | 关联对象字段标识 |
| 21 | ftarbillmainfieldkey | 目标单据字段标识 | varchar | 50 |  | √ | ' ' | 目标单据字段标识 |
| 22 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fsrcbillfilterjson | 来源单据过滤条件json | varchar | 255 |  | √ | ' ' | 来源单据过滤条件json |
| 25 | fsrcbillfilter | 来源单据过滤条件 | varchar | 255 |  | √ | ' ' | 来源单据过滤条件 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fsrcbillfilterformula | 来源单据过滤条件表达式 | varchar | 255 |  | √ | ' ' | 来源单据过滤条件表达式 |
| 28 | fsrcbillmainfieldkey | 来源单据字段标识 | varchar | 50 |  | √ | ' ' | 来源单据字段标识 |
| 29 | fsrcbillmainfield | 来源单据字段 | varchar | 50 |  | √ | ' ' | 来源单据字段 |
| 30 | fsrcbillfilterformula_tag | 来源单据过滤条件表达式_详情 | text | 0 |  |  | null | 来源单据过滤条件表达式_详情 |
| 31 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 33 | frelateobjfilterformula | 过滤条件表达式 | varchar | 255 |  | √ | ' ' | 过滤条件表达式 |
| 34 | frelateobjfilterformula_tag | 过滤条件表达式_详情 | text | 0 |  |  | null | 过滤条件表达式_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msisv_unionpush |  | fid |
| 2 | idx_msisv_unionpush_num |  | fnumber |

---

## 与来源单据的匹配关系-子表 t_msisv_pumatchentry

- **表名称：** 与来源单据的匹配关系-子表
- **表名：** t_msisv_pumatchentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillmatchfield | 来源单据字段 | varchar | 50 |  | √ | ' ' | 来源单据字段 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | frelateobjmatchfieldkey | 关联对象字段标识 | varchar | 50 |  | √ | ' ' | 关联对象字段标识 |
| 6 | frelateobjmatchfield | 关联对象字段 | varchar | 50 |  | √ | ' ' | 关联对象字段 |
| 7 | fsrcbillmatchfieldkey | 来源单据字段标识 | varchar | 50 |  | √ | ' ' | 来源单据字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msisv_pumatchentry |  | fentryid |
| 2 | idx_msisv_pumatchentry_id |  | fid |

---

## 下推后执行目标单的操作-子表 t_msisv_puoperateentry

- **表名称：** 下推后执行目标单的操作-子表
- **表名：** t_msisv_puoperateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | foperation | 操作 | varchar | 50 |  | √ | ' ' | 操作,枚举: |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msisv_puoperateentry |  | fentryid |
| 2 | idx_msisv_puoperateentry_id |  | fid |

---

## 对目标单据赋值-子表 t_msisv_puassignentry

- **表名称：** 对目标单据赋值-子表
- **表名：** t_msisv_puassignentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelateobjassignfield | 关联对象字段 | varchar | 50 |  | √ | ' ' | 关联对象字段 |
| 3 | fisnegate | 取反 | bpchar | 1 |  | √ | '0' | 取反 |
| 4 | ftarbillassignfield | 目标单据字段 | varchar | 50 |  | √ | ' ' | 目标单据字段 |
| 5 | ftarbillassignfieldkey | 目标单据字段标识 | varchar | 50 |  | √ | ' ' | 目标单据字段标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fassignmethod | 赋值方式 | bpchar | 1 |  | √ | 'A' | 赋值方式,枚举: A :覆盖 B :累加 C :累减 D :按比例拆分 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | frelateobjassignfieldkey | 关联对象字段标识 | varchar | 50 |  | √ | ' ' | 关联对象字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msisv_puassignentry_id |  | fid |
| 2 | pk_t_msisv_puassignentry |  | fentryid |

---

## 联合下推-多语言表 t_msisv_unionpush_l

- **表名称：** 联合下推-多语言表
- **表名：** t_msisv_unionpush_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msisv_unionpush_l |  | fpkid |
| 2 | idx_msisv_unionpush_l_id |  | fid,flocaleid |
