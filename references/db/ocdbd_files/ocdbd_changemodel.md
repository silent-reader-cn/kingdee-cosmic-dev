# 渠道云变更模型-ocdbd_changemodel

## 插件实体-子表 t_ocdbd_changementry_p

- **表名称：** 插件实体-子表
- **表名：** t_ocdbd_changementry_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpluginenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 3 | fpluginjson | 插件JSON | varchar | 500 |  | √ | ' ' | 插件JSON |
| 4 | fclassname | 类名 | varchar | 200 |  | √ | ' ' | 类名 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fplugintype | 类型 | bpchar | 5 |  | √ | ' ' | 类型,枚举: 0 :Java插件 1 :JSript插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_changemep_fid |  | fid |
| 2 | pk_ocdbd_changementry_p |  | fentryid |

---

## 字段映射-子表 t_ocdbd_changementry_f

- **表名称：** 字段映射-子表
- **表名：** t_ocdbd_changementry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcefield | 源单字段标识 | varchar | 50 |  | √ | ' ' | 源单字段标识 |
| 3 | fsourcefieldname | 源单字段 | varchar | 80 |  | √ | ' ' | 源单字段 |
| 4 | fcandisplay | 可显示 | bpchar | 1 |  | √ | '0' | 可显示 |
| 5 | ftargetfieldname | 变更单字段 | varchar | 80 |  | √ | ' ' | 变更单字段 |
| 6 | fcanenable | 可变更 | bpchar | 1 |  | √ | '0' | 可变更 |
| 7 | fclearsourcefield | 清除 | varchar | 50 |  | √ | ' ' | 清除 |
| 8 | ftargetfield | 变更单字段标识 | varchar | 50 |  | √ | ' ' | 变更单字段标识 |
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
| 1 | idx_ocdbd_changemlfe_fid |  | fid |
| 2 | pk_ocdbd_changementry_f |  | fentryid |

---

## 渠道云变更模型-主表 t_ocdbd_changemodel

- **表名称：** 渠道云变更模型-主表
- **表名：** t_ocdbd_changemodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fupdatetype | 生效时机 | bpchar | 1 |  | √ | 'A' | 生效时机,枚举: A :手工生效 B :审核即生效 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsrcbillid | 源单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 8 | fxbillid | 变更单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_changemodel_xbill |  | fxbillid |
| 2 | pk_ocdbd_changemodel |  | fid |
| 3 | idx_ocdbd_changemodel_srcbill |  | fsrcbillid |
