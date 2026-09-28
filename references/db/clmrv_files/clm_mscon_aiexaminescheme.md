# 审查方案-clm_mscon_aiexaminescheme

## 审查方案-多语言表 t_mscon_aiexaminescheme_l

- **表名称：** 审查方案-多语言表
- **表名：** t_mscon_aiexaminescheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 155 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 770 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mscon_aiexaminescheme_l |  | fpkid |
| 2 | idx_mscon_aiexaminescheme_l_0 |  | fid,flocaleid |

---

## 审查方案-主表 t_mscon_aiexaminescheme

- **表名称：** 审查方案-主表
- **表名：** t_mscon_aiexaminescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fenableconditionjson_tag | 启用条件JSON_详情 | text | 0 |  |  | null | 启用条件JSON_详情 |
| 5 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fenablecondition | 启用条件 | varchar | 2000 |  | √ | ' ' | 启用条件 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fenableconditionjson | 启用条件JSON | varchar | 255 |  | √ | ' ' | 启用条件JSON |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fentityid | 单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mscon_aiexaminescheme_m0 |  | fmasterid |
| 2 | pk_mscon_aiexaminescheme |  | fid |

---

## 审查配置-子表 t_mscon_aiexamineentry

- **表名称：** 审查配置-子表
- **表名：** t_mscon_aiexamineentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexamineitemid | 审查项 | int8 | 64 |  | √ | 0 | [审查项 clm_mscon_examineitems](../clmrv_files/clm_mscon_examineitems.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fexaminerule | 审查规则 | varchar | 512 |  | √ | ' ' | 审查规则 |
| 4 | frisklevel | 风险等级 | varchar | 50 |  | √ | ' ' | 风险等级,枚举: A :高 B :中 C :低 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsearchrule | 检索规则 | varchar | 255 |  | √ | ' ' | 检索规则 |
| 8 | fkeyword | 关键字 | varchar | 255 |  | √ | ' ' | 关键字 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mscon_aiexamineentry_fk |  | fid |
| 2 | pk_mscon_aiexamineentry |  | fentryid |

---

## 审查配置-多语言表 t_mscon_aiexamineentry_l

- **表名称：** 审查配置-多语言表
- **表名：** t_mscon_aiexamineentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexaminerule | 审查规则 | varchar | 770 |  | √ | ' ' | 审查规则 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fsearchrule | 检索规则 | varchar | 399 |  | √ | ' ' | 检索规则 |
| 6 | fkeyword | 关键字 | varchar | 399 |  | √ | ' ' | 关键字 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mscon_aiexamineentry_l |  | fpkid |
| 2 | idx_mscon_aiexamineentry_l_0 |  | fentryid,flocaleid |
