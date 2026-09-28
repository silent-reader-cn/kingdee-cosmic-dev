# 关联项类型集成配置-plm_ipdsm_fc_model

## 关联项类型集成配置-主表 t_plmpm_deliverablemodel

- **表名称：** 关联项类型集成配置-主表
- **表名：** t_plmpm_deliverablemodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | fintegrationtype | 集成类型 | varchar | 50 |  | √ | ' ' | 集成类型,枚举: A :第三方 B :金蝶云苍穹 |
| 4 | ftrdapp | 第三方应用 | int8 | 64 |  | √ | 0 | [集成应用配置 plm_pm_trd](../plmipdsm_files/plm_pm_trd.md) |
| 5 | forgfield | forgfield | int8 | 64 |  | √ | 0 |  |
| 6 | fdatasourceid | fdatasourceid | int8 | 64 |  | √ | 0 |  |
| 7 | fisitem | 是否工作项 | bpchar | 1 |  | √ | '0' | 是否工作项 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fdataprocessor | 值处理器 | varchar | 200 |  | √ | ' ' | 值处理器 |
| 11 | fdatastatus | fdatastatus | int8 | 64 |  | √ | 0 |  |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fpreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 15 | faffiliatedbill | 所属单据 | varchar | 36 |  | √ | ' ' | [业务对象列表_可多选 bos_flydb_objlist](../superquery_files/bos_flydb_objlist.md) |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 18 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [关联项类型集成配置 plm_ipdsm_fc_model](../plmipdsm_files/plm_ipdsm_fc_model.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flongnumber | 长编码 | varchar | 300 |  | √ | ' ' | 长编码 |
| 21 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 22 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fdatasource | fdatasource | varchar | 50 |  | √ | ' ' |  |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fdatatype | fdatatype | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmpm_deliverablemodel |  | fid |
| 2 | idx_plmpm_deliverablemodel_m0 |  | fmasterid |

---

## 关联项类型集成配置-多语言表 t_plmpm_deliverablemodel_l

- **表名称：** 关联项类型集成配置-多语言表
- **表名：** t_plmpm_deliverablemodel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 100 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmpm_deliverablemodel_l |  | fpkid |
| 2 | idx_plmpm_deliverablemodel_l_0 |  | fid,flocaleid |

---

## 关联状态-多选基础资料表 t_plm_pm_mappingstatus

- **表名称：** 关联状态-多选基础资料表
- **表名：** t_plm_pm_mappingstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [交付物状态配置 plm_pm_deliverable_status](../plmpm_files/plm_pm_deliverable_status.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_pm_mappingstatus |  | fpkid |
| 2 | idx_plm_pm_mappingstatus_fk |  | fid |

---

## 转换映射-子表 t_deliverable_model_map

- **表名称：** 转换映射-子表
- **表名：** t_deliverable_model_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsourcefield | 实例属性 | varchar | 200 |  | √ | ' ' | 实例属性 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fitemfield | 工作项属性 | varchar | 50 |  | √ | ' ' | 工作项属性,枚举: |
| 4 | ftargetfield | 关联项列表属性 | varchar | 50 |  | √ | ' ' | 关联项列表属性,枚举: |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmultilang | 是否多语言 | bpchar | 1 |  | √ | '0' | 是否多语言 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_deliverable_model_map_fk |  | fid |
| 2 | pk_deliverable_model_map |  | fentryid |

---

## 配置参数-子表 t_deliverable_model_param

- **表名称：** 配置参数-子表
- **表名：** t_deliverable_model_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue | 参数值 | varchar | 200 |  | √ | ' ' | 参数值 |
| 3 | fparam | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_deliverable_model_param |  | fentryid |
| 2 | idx_deliverable_model_param_fk |  | fid |
