# 预留方案-reserve_scheme

## 适用组织单据体-子表 t_reserve_schorg

- **表名称：** 适用组织单据体-子表
- **表名：** t_reserve_schorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisincludesuborg | 包含下级 | bpchar | 1 |  | √ | ' ' | 包含下级 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reserve_schorg_fid |  | fid |
| 2 | pk_t_reserve_schorg |  | fentryid |

---

## 预留方案-主表 t_reserve_scheme

- **表名称：** 预留方案-主表
- **表名：** t_reserve_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | f_number | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 4 | f_ctrl_strategy | f_ctrl_strategy | bpchar | 1 |  | √ | '1' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | f_result_plugin | 插件 | varchar | 512 |  | √ | ' ' | 插件 |
| 7 | f_req_filter_value | 值存储 | varchar | 2000 |  | √ | ' ' | 值存储 |
| 8 | fsupdiff | 供应不足处理方式 | varchar | 50 |  | √ | ' ' | 供应不足处理方式,枚举: A :供应不足不预留且不提示 B :尽量预留不提示 C :尽量预留且提示 D :供应不足不预留且提示操作失败 |
| 9 | f_remark | 描述 | varchar | 80 |  | √ | ' ' | 描述 |
| 10 | fschemetype | 预留方案用途 | varchar | 5 |  | √ | ' ' | 预留方案用途,枚举: 0 :手工预留 1 :自动预留 2 :预留下级工单 |
| 11 | f_is_sys_init | f_is_sys_init | bpchar | 1 |  | √ | '0' |  |
| 12 | f_result_handler | 整单结果处理 | bpchar | 1 |  | √ | '1' | 整单结果处理,枚举: 1 :尽量预留 2 :不足不预留 3 :整单同仓预留 4 :齐套同货主同仓 5 :仅执行插件 6 :齐套不足不预留 |
| 13 | fautoreserve | 自动预留 | bpchar | 1 |  | √ | '0' | 自动预留 |
| 14 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | f_data_status | 使用状态 | bpchar | 1 |  | √ | 'A' | 使用状态,枚举: A :可用 B :禁用 |
| 17 | f_require_bill | 需求单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | f_custom_result_plugin | 自定义处理插件 | bpchar | 1 |  | √ | '0' | 自定义处理插件 |
| 21 | f_name | 名称 | varchar | 510 |  | √ | ' ' | 名称 |
| 22 | f_create_org_id | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | f_auto_reserve | f_auto_reserve | bpchar | 1 |  | √ | '0' |  |
| 24 | freservetypeparam | 预留类型参数 | varchar | 5 |  | √ | '2' | 预留类型参数,枚举: 2 :物料预留类型 1 :强预留 0 :弱预留 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reserve_scheme_fnum |  | f_number |
| 2 | pk_reserve_scheme |  | fid |

---

## 单据体-子表 t_reserve_shemesupentry

- **表名称：** 单据体-子表
- **表名：** t_reserve_shemesupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | f_data_source_id | 预留数据源 | int8 | 64 |  | √ | 0 | [预留数据源（废弃） msmod_data_source](../mscommon_files/msmod_data_source.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reserve_shemesup_efid |  | fid |
| 2 | pk_t_reserve_shemesupentry |  | fentryid |

---

## 预留方案-多语言表 t_reserve_scheme_l

- **表名称：** 预留方案-多语言表
- **表名：** t_reserve_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | f_name | 名称 | varchar | 510 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_scheme_l |  | fpkid |
| 2 | idx_t_reserve_scheme_lid |  | fid,flocaleid |

---

## 预留策略信息-子表 t_reserve_shemestraentry

- **表名称：** 预留策略信息-子表
- **表名：** t_reserve_shemestraentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | f_strategy_seq | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | f_strategy_id | 预留策略 | int8 | 64 |  | √ | 0 | [预留策略 reserve_strategy](../msplan_files/reserve_strategy.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_shemestraentry |  | fentryid |
| 2 | idx_reserve_shemestraentry |  | fid |
