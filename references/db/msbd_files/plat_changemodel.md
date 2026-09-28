# 变更模型-plat_changemodel

## 字段映射-子表 t_plat_changemodelfe

- **表名称：** 字段映射-子表
- **表名：** t_plat_changemodelfe

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcefield | 源单字段 | varchar | 255 |  | √ | ' ' | 源单字段 |
| 3 | fcandisplay | 可显示 | bpchar | 1 |  | √ | '0' | 可显示 |
| 4 | fsourcefieldname | 源单字段 | varchar | 255 |  | √ | ' ' | 源单字段 |
| 5 | ftargetfieldname | 变更单字段 | varchar | 255 |  | √ | ' ' | 变更单字段 |
| 6 | fcanenable | 可变更 | bpchar | 1 |  | √ | '0' | 可变更 |
| 7 | fclearsourcefield | 清除 | varchar | 50 |  | √ | ' ' | 清除 |
| 8 | ftargetfield | 变更单字段 | varchar | 255 |  | √ | ' ' | 变更单字段 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcanwriteback | 可反写 | bpchar | 1 |  | √ | '0' | 可反写 |
| 12 | fcanlog | 记录日志 | bpchar | 1 |  | √ | '0' | 记录日志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plat_changemodelfe_fid |  | fid |
| 2 | pk_t_plat_changemodelfe |  | fentryid |

---

## 单据类型映射分录-子表 t_plat_changemodelbe

- **表名称：** 单据类型映射分录-子表
- **表名：** t_plat_changemodelbe

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fxbilltypeid | 变更单单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 3 | fpushtype | 下推类型 | varchar | 5 |  | √ | 'A' | 下推类型,枚举: A :仅指定类型 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsrcbilltypeid | 源单单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plat_changemodelbe_fid |  | fid |
| 2 | pk_t_plat_changemodelbe |  | fentryid |

---

## 校验条件实体-子表 t_plat_changemodelve

- **表名称：** 校验条件实体-子表
- **表名：** t_plat_changemodelve

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fvalidconditionjson_tag | 反写条件json_详情 | text | 0 |  |  | null | 反写条件json_详情 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fvalidconditionjson | 反写条件json | varchar | 512 |  |  | null | 反写条件json |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plat_changemodelve |  | fentryid |
| 2 | idx_plat_changemodelve_fid |  | fid |

---

## 插件实体-子表 t_plat_changemodelpe

- **表名称：** 插件实体-子表
- **表名：** t_plat_changemodelpe

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpluginenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 3 | fpluginjson | 插件JSON | varchar | 500 |  |  | ' ' | 插件JSON |
| 4 | fclassname | 类名 | varchar | 200 |  |  | ' ' | 类名 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fplugintype | 类型 | varchar | 5 |  | √ | ' ' | 类型,枚举: 0 :Java插件 1 :JSript插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plat_changemodelpe |  | fentryid |
| 2 | idx_plat_changemodelpe_fid |  | fid |

---

## 变更模型-主表 t_plat_changemodel

- **表名称：** 变更模型-主表
- **表名：** t_plat_changemodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 4 | fcustomparameter_tag | 详情 | text | 0 |  |  | null | 详情 |
| 5 | fhidepropkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | fupdatetype | 生效时机 | varchar | 5 |  | √ | ' ' | 生效时机,枚举: auto :审核即生效 man :手工生效 |
| 7 | fsrcbillid | 源单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fisnotupdateversion | 不更新版本号 | bpchar | 1 |  | √ | '0' | 不更新版本号 |
| 10 | fhideentrykey | 单据体标识 | varchar | 50 |  | √ | ' ' | 单据体标识 |
| 11 | fxbilllogid | 变更日志实体 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fareaconditionjson_tag | 数据范围条件json_详情 | text | 0 |  |  | null | 数据范围条件json_详情 |
| 13 | fvalidoptype | 校验时机 | varchar | 50 |  | √ | 'bizvalid' | 校验时机,枚举: submit :提交 audit :审核 bizvalid :生效 |
| 14 | fxbillid | 变更单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fcustomparameter |  | varchar | 512 |  |  | null |  |
| 17 | fhiderow | 默认不显示未变更的明细行 | bpchar | 1 |  | √ | '0' | 默认不显示未变更的明细行 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fareaconditionjson | 数据范围条件json | varchar | 512 |  |  | null | 数据范围条件json |
| 20 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 21 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 22 | fareaconditiondesc | 条件描述 | varchar | 2000 |  |  | null | 条件描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plat_changemodel_srcbill |  | fsrcbillid |
| 2 | pk_t_plat_changemodel |  | fid |
| 3 | idx_plat_changemodel_xbill |  | fxbillid |

---

## 变更模型-多语言表 t_plat_changemodel_l

- **表名称：** 变更模型-多语言表
- **表名：** t_plat_changemodel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fareaconditiondesc | 条件描述 | varchar | 2000 |  |  | null | 条件描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plat_changemodel_l |  | fpkid |
| 2 | idx_plat_changemodel_l_fid |  | fid,flocaleid |
| 3 | idx_plat_changemodel_l_fname |  | fname,fid |
