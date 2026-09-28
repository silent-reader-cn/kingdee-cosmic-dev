# 工单关闭反写配置-mpdm_closeconfig

## 工单关闭反写配置-多语言表 t_mpdm_closeconfig_l

- **表名称：** 工单关闭反写配置-多语言表
- **表名：** t_mpdm_closeconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_closeconfig_l |  | fpkid |
| 2 | idx_mpdm_closeconfig_l |  | fid,flocaleid |

---

## 工单关闭反写配置-主表 t_mpdm_closeconfig

- **表名称：** 工单关闭反写配置-主表
- **表名：** t_mpdm_closeconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsourceentityid | 源实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_closeconfig |  | fid |

---

## 单据体-子表 t_mpdm_closeconfigentry

- **表名称：** 单据体-子表
- **表名：** t_mpdm_closeconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fsourcefieldname | 源单基本字段名称 | varchar | 50 |  | √ | ' ' | 源单基本字段名称 |
| 4 | fbaseunitname | 基本单位名称 | varchar | 50 |  | √ | ' ' | 基本单位名称 |
| 5 | fsourcefieldflag | 源单基本字段标识 | varchar | 50 |  | √ | ' ' | 源单基本字段标识 |
| 6 | fbizunitname | 业务单位字段名称 | varchar | 50 |  | √ | ' ' | 业务单位字段名称 |
| 7 | fbaseunitflag | 基本单位字段标识 | varchar | 50 |  | √ | ' ' | 基本单位字段标识 |
| 8 | fmaterialflag | 物料字段标识 | varchar | 50 |  | √ | ' ' | 物料字段标识 |
| 9 | fbizunitflag | 业务单位字段标识 | varchar | 50 |  | √ | ' ' | 业务单位字段标识 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fsourcebizfieldflag | 源单业务字段标识 | varchar | 50 |  | √ | ' ' | 源单业务字段标识 |
| 12 | fmaterialname | 物料字段名称 | varchar | 50 |  | √ | ' ' | 物料字段名称 |
| 13 | fsourcebizfieldname | 源单业务字段名称 | varchar | 50 |  | √ | ' ' | 源单业务字段名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_closeconfigentry |  | fid |
| 2 | pk_mpdm_closeconfigentry |  | fentryid |
