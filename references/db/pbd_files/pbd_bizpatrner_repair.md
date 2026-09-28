# 商务伙伴检查及修复-pbd_bizpatrner_repair

## 单据体-子表 t_pbd_bizpartnerrepair

- **表名称：** 单据体-子表
- **表名：** t_pbd_bizpartnerrepair

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuppliername | srm供应商字段名 | varchar | 50 |  | √ | ' ' | srm供应商字段名 |
| 3 | fbdsuppliername | 主数据供应商字段名 | varchar | 50 |  | √ | ' ' | 主数据供应商字段名 |
| 4 | fbizpartnername | 商务伙伴字段名 | varchar | 50 |  | √ | ' ' | 商务伙伴字段名 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbillentityid | 单据对象 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_bizprepair_fid |  | fid |
| 2 | pk_t_pbd_bizpartnerrepair |  | fentryid |

---

## 商务伙伴检查及修复-主表 t_pbd_bizpartnerrepair_h

- **表名称：** 商务伙伴检查及修复-主表
- **表名：** t_pbd_bizpartnerrepair_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_bizpartnerrepair_h |  | fid |
| 2 | idx_pbd_bizrepair_name |  | fname |
