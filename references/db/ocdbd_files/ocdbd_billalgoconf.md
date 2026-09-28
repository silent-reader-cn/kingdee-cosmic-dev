# 渠道单据算法配置-ocdbd_billalgoconf

## 渠道单据算法配置-多语言表 t_ocdbd_billalgoconf_l

- **表名称：** 渠道单据算法配置-多语言表
- **表名：** t_ocdbd_billalgoconf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_billalgoconf_l |  | fpkid |
| 2 | idx_ocdbd_billalgoconf_l |  | fid,flocaleid |

---

## 校验器-多语言表 t_ocdbd_billalgovalidator_l

- **表名称：** 校验器-多语言表
- **表名：** t_ocdbd_billalgovalidator_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvalidatorname | 校验器名称 | varchar | 255 |  | √ | ' ' | 校验器名称 |
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
| 1 | idx_ocdbd_billalgovalidator_l |  | fentryid,flocaleid |
| 2 | pk_ocdbd_billalgovalidator_l |  | fpkid |

---

## 校验器-子表 t_ocdbd_billalgovalidator

- **表名称：** 校验器-子表
- **表名：** t_ocdbd_billalgovalidator

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisenable | 初始状态(预置) | bpchar | 1 |  | √ | '1' | 初始状态(预置),枚举: 1 :启用 0 :禁用 9 :下架 |
| 3 | fvalidatorplugin | 校验器插件 | varchar | 200 |  | √ | ' ' | 校验器插件 |
| 4 | fvalidatorname | 校验器名称 | varchar | 50 |  | √ | ' ' | 校验器名称 |
| 5 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fenabelcustom | 是否允许二开 | bpchar | 1 |  | √ | '1' | 是否允许二开 |
| 8 | foperation | 操作 | varchar | 80 |  | √ | ' ' | 操作,枚举: |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcustomisenable | 启用 | bpchar | 1 |  | √ | ' ' | 启用,枚举: 1 :启用 0 :禁用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_billalgovalidator |  | fid |
| 2 | pk_ocdbd_billalgovalidator |  | fentryid |

---

## 渠道单据算法配置-主表 t_ocdbd_billalgoconf

- **表名称：** 渠道单据算法配置-主表
- **表名：** t_ocdbd_billalgoconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fentityobj | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '1' | 是否系统预置 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_billalgoconf |  | fentityobj |
| 2 | pk_ocdbd_billalgoconf |  | fid |
