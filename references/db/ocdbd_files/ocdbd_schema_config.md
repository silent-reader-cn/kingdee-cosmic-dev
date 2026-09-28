# 详情配置-ocdbd_schema_config

## 详情配置-多语言表 t_ocdbd_schemacfg_l

- **表名称：** 详情配置-多语言表
- **表名：** t_ocdbd_schemacfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_schemacfg_l |  | fpkid |
| 2 | idx_ocdbd_schemacfg_l |  | fid,flocaleid |

---

## 表达式规则配置-子表 t_ocdbd_schemacfg_ent

- **表名称：** 表达式规则配置-子表
- **表名：** t_ocdbd_schemacfg_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispass | 通过 | bpchar | 1 |  | √ | ' ' | 通过 |
| 3 | fresultdesc | 结果描述 | varchar | 2000 |  | √ | ' ' | 结果描述 |
| 4 | fexpression | 表达式 | text | 0 |  |  | ' ' | 表达式 |
| 5 | fexpressiontag | 表达式(存储) | text | 0 |  |  | ' ' | 表达式(存储) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_schemacfg_ent |  | fentryid |
| 2 | idx_ocdbd_schemacfg_ent |  | fid |

---

## 详情配置-主表 t_ocdbd_schemacfg

- **表名称：** 详情配置-主表
- **表名：** t_ocdbd_schemacfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstartconditionexp | 启动条件(后台字段) | text | 0 |  |  | ' ' | 启动条件(后台字段) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcomment | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbill | 单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fschemeid | 智能审单方案 | int8 | 64 |  | √ | 0 | [智能审单方案 ocdbd_scheme](../ocdbd_files/ocdbd_scheme.md) |
| 9 | fcfgtype | 配置方式 | varchar | 10 |  | √ | ' ' | 配置方式,枚举: exp :表达式 plugin :插件 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fstartcondition | 启动条件 | varchar | 2000 |  | √ | ' ' | 启动条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_schemacfg |  | fschemeid |
| 2 | pk_ocdbd_schemacfg |  | fid |
