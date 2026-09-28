# 组件方案配置-fpy_match_relation_conf

## 适用组织-子表 tk_fpy_match_config_org

- **表名称：** 适用组织-子表
- **表名：** tk_fpy_match_config_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fk_fpy_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_match_config_org |  | fentryid |

---

## 自动组件规则-子表 tk_fpy_match_config_item

- **表名称：** 自动组件规则-子表
- **表名：** tk_fpy_match_config_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_fpy_ruleconfig | 关联规则 | varchar | 1024 |  | √ | ' ' | 关联规则 |
| 3 | fk_fpy_ruletype | 关系类型 | varchar | 50 |  | √ | ' ' | 关系类型,枚举: 1 :1对1 2 :1对多 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fk_fpy_srccondition | 来源单据适用条件 | varchar | 1024 |  | √ | ' ' | 来源单据适用条件 |
| 6 | fk_fpy_rulename | 规则项名称 | varchar | 200 |  | √ | ' ' | 规则项名称 |
| 7 | fk_fpy_targetcond_val | 目标单据适用条件值 | varchar | 255 |  | √ | ' ' | 目标单据适用条件值 |
| 8 | fk_fpy_srccond_val_tag | 来源单据适用条件值_详情 | text | 0 |  |  | null | 来源单据适用条件值_详情 |
| 9 | fk_fpy_targetcondition | 目标单据适用条件 | varchar | 1024 |  | √ | ' ' | 目标单据适用条件 |
| 10 | fk_fpy_ruleconfigval | 关联方案值 | varchar | 255 |  | √ | ' ' | 关联方案值 |
| 11 | fk_fpy_ruleconfigval_tag | 关联方案值_详情 | text | 0 |  |  | null | 关联方案值_详情 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fk_fpy_srccond_val | 来源单据适用条件值 | varchar | 255 |  | √ | ' ' | 来源单据适用条件值 |
| 14 | fk_fpy_targetcond_val_tag | 目标单据适用条件值_详情 | text | 0 |  |  | null | 目标单据适用条件值_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_match_config_item |  | fentryid |

---

## 组件方案配置-主表 tk_fpy_match_relate_conf

- **表名称：** 组件方案配置-主表
- **表名：** tk_fpy_match_relate_conf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fk_fpy_interorg | 允许跨组织组件 | bpchar | 1 |  | √ | '0' | 允许跨组织组件 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fk_fpy_business_target | 目标单据类型 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fk_fpy_business_source | 来源单据类型 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 |
| 10 | fk_fpy_relation_entity | 关联实体 | varchar | 50 |  | √ | ' ' | 关联实体 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 15 | fk_eafc_arcorg | 创建人组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_match_relate_conf |  | fid |

---

## 组件方案配置-多语言表 tk_fpy_match_relate_conf_l

- **表名称：** 组件方案配置-多语言表
- **表名：** tk_fpy_match_relate_conf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_match_relate_conf_l |  | fpkid |
