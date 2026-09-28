# 报表数据源配置-scmc_report_conf

## 报表字段配置-子表 t_scmc_rpt_cf_cols

- **表名称：** 报表字段配置-子表
- **表名：** t_scmc_rpt_cf_cols

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilterfield | 关联过滤字段标识 | varchar | 30 |  | √ | ' ' | 关联过滤字段标识 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fisdisablegroup | 关闭多级分类汇总 | bpchar | 1 |  | √ | '0' | 关闭多级分类汇总 |
| 5 | fcaltype | 计算类型 | bpchar | 1 |  | √ | 'D' | 计算类型,枚举: A :维度 B :数值 C :参与运算 D :舍弃 |
| 6 | fisbillheadfield | 是否单据头字段 | bpchar | 1 |  | √ | '0' | 是否单据头字段 |
| 7 | fdefshow | 默认显示 | bpchar | 1 |  | √ | '0' | 默认显示 |
| 8 | fshowrefprop | 显示引用属性 | varchar | 255 |  | √ | ' ' | 显示引用属性 |
| 9 | fheadfieldtype | 单据头字段类型 | varchar | 50 |  | √ | ' ' | 单据头字段类型,枚举: 1 :候选健 2 :数值 |
| 10 | fissummary | 显示合计 | bpchar | 1 |  | √ | '0' | 显示合计 |
| 11 | fcolname | 字段名称（报表显示） | varchar | 150 |  | √ | ' ' | 字段名称（报表显示） |
| 12 | fisdisablesort | 关闭排序 | bpchar | 1 |  | √ | '0' | 关闭排序 |
| 13 | fshowprop | 显示属性 | bpchar | 1 |  | √ | '0' | 显示属性,枚举: 0 :自动处理 1 :名称 2 :编码 3 :名称+编码 4 :编码+名称 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | frepo_col | 字段标识 | varchar | 30 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_scmc_rpt_cf_cols_fid |  | fid |
| 2 | pk_t_scmc_rpt_cf_cols |  | fentryid |

---

## 报表数据源配置-多语言表 t_scmc_rpt_cf_l

- **表名称：** 报表数据源配置-多语言表
- **表名：** t_scmc_rpt_cf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 307 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_scmc_rpt_cf_l_id |  | fid,flocaleid |
| 2 | pk_t_scmc_rpt_cf_l |  | fpkid |

---

## 报表字段配置-多语言表 t_scmc_rpt_cf_cols_l

- **表名称：** 报表字段配置-多语言表
- **表名：** t_scmc_rpt_cf_cols_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcolname | 字段名称（报表显示） | varchar | 332 |  | √ | ' ' | 字段名称（报表显示） |
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
| 1 | idx_t_scmc_rpt_cf_cols_l_id |  | fentryid,flocaleid |
| 2 | pk_t_scmc_rpt_cf_cols_l |  | fpkid |

---

## 插件列表-子表 t_scmc_rpt_cf_plugin

- **表名称：** 插件列表-子表
- **表名：** t_scmc_rpt_cf_plugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpluginstatus | 插件状态 | bpchar | 1 |  | √ | '1' | 插件状态 |
| 3 | fpluginclass | 插件类 | varchar | 255 |  | √ | ' ' | 插件类 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fpluginname | 插件名称 | varchar | 150 |  | √ | ' ' | 插件名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scmc_rpt_cf_plugin |  | fentryid |
| 2 | idx_t_scmc_rpt_cf_plugin_id |  | fid |

---

## 报表数据源配置-主表 t_scmc_rpt_cf

- **表名称：** 报表数据源配置-主表
- **表名：** t_scmc_rpt_cf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | fenablesort | 启用排序 | bpchar | 1 |  | √ | '0' | 启用排序 |
| 4 | fprintandfdperm | 动态字段支持打印预览和字段权限 | bpchar | 1 |  | √ | '0' | 动态字段支持打印预览和字段权限 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | frepo | 字段库 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fstatus | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 1 :启用 0 :禁用 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | ftotalrowfloat | 总计行支持浮动显示 | bpchar | 1 |  | √ | '0' | 总计行支持浮动显示 |
| 10 | fsysdata | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | freqlimit | 最大并发请求数 | int8 | 64 |  | √ | '-1' | 最大并发请求数 |
| 13 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fapplylistdataperm | 单据列表数据权限 | bpchar | 1 |  | √ | '0' | 单据列表数据权限 |
| 15 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 16 | fenablegroup | 启用多级分类汇总 | bpchar | 1 |  | √ | '0' | 启用多级分类汇总 |
| 17 | ftimeout | 报表查询最大超时时间/分钟 | int4 | 32 |  | √ | 30 | 报表查询最大超时时间/分钟 |
| 18 | freport | 报表实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_scmc_rpt_cf_fnumber |  | fnumber |
| 2 | idx_t_scmc_rpt_cf_fmodifydate |  | fmodifydate |
| 3 | pk_t_scmc_rpt_cf |  | fid |
| 4 | idx_t_scmc_rpt_cf_freport |  | freport |

---

## 关联数据源实体-子表 t_scmc_rpt_cf_joindata

- **表名称：** 关联数据源实体-子表
- **表名：** t_scmc_rpt_cf_joindata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjoindatafs_tag | 数据块过滤设置_详情 | text | 0 |  |  | null | 数据块过滤设置_详情 |
| 3 | fjoinblockdesc | 数据描述 | varchar | 50 |  | √ | ' ' | 数据描述 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fjoinblockstatus | 数据块状态 | bpchar | 1 |  | √ | '1' | 数据块状态 |
| 6 | fjoindatafs | 数据块过滤设置 | varchar | 1 |  | √ | ' ' | 数据块过滤设置 |
| 7 | fjoinentity | 关联实体配置 | int8 | 64 |  | √ | 0 | [报表关联实体配置 scmc_rpt_joinentity](../mscommon_files/scmc_rpt_joinentity.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rpt_cf_joindata_id |  | fid |
| 2 | pk_t_scmc_rpt_cf_joindata |  | fentryid |

---

## 插件列表-多语言表 t_scmc_rpt_cf_plugin_l

- **表名称：** 插件列表-多语言表
- **表名：** t_scmc_rpt_cf_plugin_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fpluginname | 插件名称 | varchar | 303 |  | √ | ' ' | 插件名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scmc_rpt_cf_plugin_l |  | fpkid |
| 2 | idx_t_scmc_rpt_cf_plugin_l_id |  | fentryid,flocaleid |

---

## 数据源实体-多语言表 t_scmc_rpt_cf_data_l

- **表名称：** 数据源实体-多语言表
- **表名：** t_scmc_rpt_cf_data_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fblockdesc | 数据描述 | varchar | 150 |  | √ | ' ' | 数据描述 |
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
| 1 | pk_t_scmc_rpt_cf_data_l |  | fpkid |
| 2 | idx_t_scmc_rpt_cf_data_l_id |  | fentryid,flocaleid |

---

## 数据源实体-子表 t_scmc_rpt_cf_data

- **表名称：** 数据源实体-子表
- **表名：** t_scmc_rpt_cf_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fblockstatus | 数据块状态 | bpchar | 1 |  | √ | '1' | 数据块状态 |
| 3 | fdatafs | 数据块过滤设置 | varchar | 1 |  | √ | ' ' | 数据块过滤设置 |
| 4 | fblockdesc | 数据描述 | varchar | 150 |  | √ | ' ' | 数据描述 |
| 5 | fcolmap | 字段映射 | varchar | 30 |  | √ | ' ' | [报表数据源字段映射 scmc_report_colmap](../mscommon_files/scmc_report_colmap.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdatafs_tag | 数据块过滤设置_详情 | text | 0 |  |  | null | 数据块过滤设置_详情 |
| 8 | fsrcentity | 实体对象 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fsrctype | 来源类型 | bpchar | 1 |  | √ | ' ' | 来源类型,枚举: A :实体 B :插件 C :数据块 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scmc_rpt_cf_data |  | fentryid |
| 2 | idx_t_scmc_rpt_cf_data_id |  | fid |

---

## 关联数据源实体-多语言表 t_scmc_rpt_cf_joindata_l

- **表名称：** 关联数据源实体-多语言表
- **表名：** t_scmc_rpt_cf_joindata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fjoinblockdesc | 数据描述 | varchar | 50 |  | √ | ' ' | 数据描述 |
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
| 1 | pk_t_scmc_rpt_cf_joindata_l |  | fpkid |
| 2 | idx_rpt_cf_joindata_l_id |  | fentryid,flocaleid |
