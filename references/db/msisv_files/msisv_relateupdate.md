# 关联更新-msisv_relateupdate

## 对目标单据赋值-子表 t_msisv_upassignentry

- **表名称：** 对目标单据赋值-子表
- **表名：** t_msisv_upassignentry

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
| 1 | idx_msisv_upassignentry_id |  | fid |
| 2 | pk_t_msisv_upassignentry |  | fentryid |

---

## 关联更新-主表 t_msisv_relateupdate

- **表名称：** 关联更新-主表
- **表名：** t_msisv_relateupdate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmonitorobj | 监听对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | ftarbillfilter | 目标单据过滤条件 | varchar | 255 |  | √ | ' ' | 目标单据过滤条件 |
| 4 | ftarbill | 目标单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | frelateobjfilterjson | 过滤条件json | varchar | 255 |  | √ | ' ' | 过滤条件json |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | ftarbillmainfield | 目标单据字段 | varchar | 50 |  | √ | ' ' | 目标单据字段 |
| 8 | frelateobjfilterjson_tag | 过滤条件json_详情 | text | 0 |  |  | null | 过滤条件json_详情 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | frelateobjfilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | frelateobj | 关联对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | frelateobjmainfield | 关联对象字段 | varchar | 50 |  | √ | ' ' | 关联对象字段 |
| 16 | ftarbillfilterjson_tag | 目标单据过滤条件json_详情 | text | 0 |  |  | null | 目标单据过滤条件json_详情 |
| 17 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | frelateobjmainfieldkey | 关联对象字段标识 | varchar | 50 |  | √ | ' ' | 关联对象字段标识 |
| 19 | ftarbillmainfieldkey | 目标单据字段标识 | varchar | 50 |  | √ | ' ' | 目标单据字段标识 |
| 20 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | ftarbillfilterformula_tag | 目标单据过滤条件表达式_详情 | text | 0 |  |  | null | 目标单据过滤条件表达式_详情 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | ftarbillfilterformula | 目标单据过滤条件表达式 | varchar | 255 |  | √ | ' ' | 目标单据过滤条件表达式 |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 27 | ftarbillfilterjson | 目标单据过滤条件json | varchar | 255 |  | √ | ' ' | 目标单据过滤条件json |
| 28 | frelateobjfilterformula | 过滤条件表达式 | varchar | 255 |  | √ | ' ' | 过滤条件表达式 |
| 29 | frelateobjfilterformula_tag | 过滤条件表达式_详情 | text | 0 |  |  | null | 过滤条件表达式_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msisv_relateupdate |  | fid |
| 2 | idx_msisv_reupdate_num |  | fnumber |

---

## 与目标单据的匹配关系-子表 t_msisv_upmatchentry

- **表名称：** 与目标单据的匹配关系-子表
- **表名：** t_msisv_upmatchentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | ftarbillmatchfield | 目标单据字段 | varchar | 50 |  | √ | ' ' | 目标单据字段 |
| 4 | ftarbillmatchfieldkey | 目标单据字段标识 | varchar | 50 |  | √ | ' ' | 目标单据字段标识 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | frelateobjmatchfieldkey | 关联对象字段标识 | varchar | 50 |  | √ | ' ' | 关联对象字段标识 |
| 7 | frelateobjmatchfield | 关联对象字段 | varchar | 50 |  | √ | ' ' | 关联对象字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msisv_upmatchentry |  | fentryid |
| 2 | idx_msisv_upmatchentry_id |  | fid |

---

## 关联更新-多语言表 t_msisv_relateupdate_l

- **表名称：** 关联更新-多语言表
- **表名：** t_msisv_relateupdate_l

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
| 1 | idx_msisv_relateupdate_l_id |  | fid,flocaleid |
| 2 | pk_t_msisv_relateupdate_l |  | fpkid |

---

## 更新目标单后执行的操作-子表 t_msisv_upoperateentry

- **表名称：** 更新目标单后执行的操作-子表
- **表名：** t_msisv_upoperateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fcondition | 条件 | varchar | 255 |  | √ | ' ' | 条件 |
| 4 | fconditionjson | 条件json | varchar | 255 |  | √ | ' ' | 条件json |
| 5 | fconditionjson_tag | 条件json_详情 | text | 0 |  |  | null | 条件json_详情 |
| 6 | fconditionformula_tag | 条件表达式_详情 | text | 0 |  |  | null | 条件表达式_详情 |
| 7 | foperation | 操作 | varchar | 50 |  | √ | ' ' | 操作,枚举: |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fconditionformula | 条件表达式 | varchar | 255 |  | √ | ' ' | 条件表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msisv_upopentry_eid |  | fid,fentryid |
| 2 | pk_t_msisv_upoperateentry |  | fentryid |
