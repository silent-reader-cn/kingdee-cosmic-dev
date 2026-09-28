# 单据归档规则（旧）-bos_cbs_archi_config_old

## 单据体-子表 t_cbs_archi_config_refbd

- **表名称：** 单据体-子表
- **表名：** t_cbs_archi_config_refbd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustom | fcustom | bpchar | 1 |  | √ | '0' |  |
| 3 | fbdname | 基础资料名称 | varchar | 50 |  | √ | ' ' | 基础资料名称 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fbd | fbd | varchar | 50 |  | √ | ' ' |  |
| 6 | ftimeattr | ftimeattr | varchar | 50 |  | √ | ' ' |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fbdnumber | 基础资料编码 | varchar | 50 |  | √ | ' ' | 基础资料编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_config_refbd_fk |  | fid |
| 2 | pk_cbs_archi_config_refbd |  | fentryid |

---

## 单据归档规则（旧）-多语言表 t_cbs_archi_config_l

- **表名称：** 单据归档规则（旧）-多语言表
- **表名：** t_cbs_archi_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_config_l |  | fid,flocaleid |
| 2 | pk_cbs_archi_config_l |  | fpkid |

---

## 单据归档规则（旧）-主表 t_cbs_archi_config

- **表名称：** 单据归档规则（旧）-主表
- **表名：** t_cbs_archi_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 归档库 | int8 | 64 |  | √ | 0 | [归档库管理 bos_cbs_archi_database](../cbs_files/bos_cbs_archi_database.md) |
| 5 | ffiltertype | 条件类型 | varchar | 50 |  | √ | ' ' | 条件类型,枚举: bill :单据 es :ElasticSearch custom :自定义 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fentitynumber | 归档单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | ftarget_type | ftarget_type | varchar | 50 |  | √ | ' ' |  |
| 9 | fmovingtype | 转储或清除 | bpchar | 1 |  | √ | ' ' | 转储或清除,枚举: 0 :归档转储 1 :归档清除 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | farchiveplugin | 插件路径 | varchar | 2000 |  | √ | ' ' | 插件路径 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fbillsetid | fbillsetid | int8 | 64 |  | √ | 0 |  |
| 14 | fconditiondesc | fconditiondesc | varchar | 2000 |  | √ | ' ' |  |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fconditiontype | 注册方式 | bpchar | 1 |  | √ | ' ' | 注册方式,枚举: 0 :单据注册 1 :实体插件注册 2 :表插件注册 |
| 18 | fpreset | fpreset | bpchar | 1 |  | √ | '0' |  |
| 19 | fsyncbasedata | 同步同库基础资料 | bpchar | 1 |  | √ | ' ' | 同步同库基础资料 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 21 | fcondition | 归档条件 | text | 0 |  |  | null | 归档条件 |
| 22 | fregion | fregion | varchar | 50 |  | √ | ' ' |  |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_config |  | fid |
| 2 | idx_cbs_archi_config |  | fnumber |
