# 多角贸易日志-sbs_multiorgpursalelog

## 多角贸易日志-主表 t_sbs_multiorgpursalelog

- **表名称：** 多角贸易日志-主表
- **表名：** t_sbs_multiorgpursalelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatebillno | 操作单据编号 | varchar | 50 |  | √ | ' ' | 操作单据编号 |
| 3 | foperatebill | 操作单据名称 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | foperator | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | foperatetype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: 0 :审核 1 :删除多组织单据 2 :生成多组织单据 |
| 7 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 8 | foperatebillname | 操作单据名称 | varchar | 50 |  | √ | ' ' | 操作单据名称 |
| 9 | foperatestatus | 操作状态 | varchar | 50 |  | √ | ' ' | 操作状态,枚举: 0 :成功 1 :失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_multiorgpursalelog |  | foperatebillno |
| 2 | pk_sbs_multiorgpursalelog |  | fid |

---

## 单据体-子表 t_sbs_multiorgpslogentry

- **表名称：** 单据体-子表
- **表名：** t_sbs_multiorgpslogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstep | 步骤 | int4 | 32 |  | √ | 0 | 步骤 |
| 3 | fbillformid | 单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbillformname | 单据名称 | varchar | 50 |  | √ | ' ' | 单据名称 |
| 7 | fdescription | 详细信息 | varchar | 2000 |  | √ | ' ' | 详细信息 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sbs_multiorgpslogentry |  | fentryid |
| 2 | idx_sbs_multiorgpslogentry |  | fid |
