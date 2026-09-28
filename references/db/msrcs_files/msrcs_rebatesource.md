# 返利计算数据源-msrcs_rebatesource

## 字段映射分录-多语言表 t_msrcs_rebatesource_e_l

- **表名称：** 字段映射分录-多语言表
- **表名：** t_msrcs_rebatesource_e_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcolname | 通用字段名称 | varchar | 100 |  | √ | ' ' | 通用字段名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_rebatesource_e_l |  | fentryid,flocaleid |
| 2 | pk_msrcs_rebatesource_e_l |  | fpkid |

---

## 返利计算数据源-主表 t_msrcs_rebatesource

- **表名称：** 返利计算数据源-主表
- **表名：** t_msrcs_rebatesource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fdatafilter | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsrcbillid | 主表来源单据 | varchar | 40 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | frebatemodelid | 返利计算模型 | varchar | 40 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebatesource |  | fid |
| 2 | idx_msrcs_rebatesource_num |  | fnumber |

---

## 字段映射分录-子表 t_msrcs_rebatesource_e

- **表名称：** 字段映射分录-子表
- **表名：** t_msrcs_rebatesource_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flinksourcefield6 | 关联字段6 | varchar | 100 |  | √ | ' ' | 关联字段6 |
| 3 | fcolid | 通用字段标识 | varchar | 50 |  | √ | ' ' | 通用字段标识 |
| 4 | flinksourcefield5 | 关联字段5 | varchar | 100 |  | √ | ' ' | 关联字段5 |
| 5 | flinksourcefield4 | 关联字段4 | varchar | 100 |  | √ | ' ' | 关联字段4 |
| 6 | flinksourcefield3 | 关联字段3 | varchar | 100 |  | √ | ' ' | 关联字段3 |
| 7 | flinksourcefield2 | 关联字段2 | varchar | 100 |  | √ | ' ' | 关联字段2 |
| 8 | flinksourcefield1 | 关联字段1 | varchar | 100 |  | √ | ' ' | 关联字段1 |
| 9 | flinksourcefield0 | 关联字段0 | varchar | 100 |  | √ | ' ' | 关联字段0 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fmodelpropid | 目标字段标识 | varchar | 80 |  | √ | ' ' | 目标字段标识 |
| 12 | fsrcpropname | 主表来源字段名称 | varchar | 80 |  | √ | ' ' | 主表来源字段名称 |
| 13 | flinksourcefield9 | 关联字段9 | varchar | 100 |  | √ | ' ' | 关联字段9 |
| 14 | flinksourcefield8 | 关联字段8 | varchar | 100 |  | √ | ' ' | 关联字段8 |
| 15 | flinksourcefield7 | 关联字段7 | varchar | 100 |  | √ | ' ' | 关联字段7 |
| 16 | fsrcpropid | 主表来源字段标识 | varchar | 80 |  | √ | ' ' | 主表来源字段标识 |
| 17 | fcolname | 通用字段名称 | varchar | 100 |  | √ | ' ' | 通用字段名称 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fmodelpropname | 目标字段名称 | varchar | 80 |  | √ | ' ' | 目标字段名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebatesource_e |  | fentryid |
| 2 | idx_msrcs_rebatesourcee_fid |  | fid |

---

## 返利计算数据源-多语言表 t_msrcs_rebatesource_l

- **表名称：** 返利计算数据源-多语言表
- **表名：** t_msrcs_rebatesource_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_rebatesourcel_flid |  | fid,flocaleid |
| 2 | pk_msrcs_rebatesource_l |  | fpkid |

---

## 单据体-子表 t_msrcs_rebatesourcelink

- **表名称：** 单据体-子表
- **表名：** t_msrcs_rebatesourcelink

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fintegerfield | 关联表对应的序号 | int4 | 32 |  | √ | 0 | 关联表对应的序号 |
| 3 | fdatafilter | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 4 | flinksourceid | 关联数据源 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | flinktype | 关联方式 | bpchar | 1 |  | √ | ' ' | 关联方式,枚举: A :关联 B :合并 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | flinkfieldsetting | 字段映射关系 | varchar | 2000 |  | √ | ' ' | 字段映射关系 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebatesourcelink |  | fentryid |
| 2 | idx_msrcs_rebatesourcelink |  | fid |
