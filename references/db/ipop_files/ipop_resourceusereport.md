# 资源用量报告-ipop_resourceusereport

## 单据体-子表 t_ipop_resusereportentry

- **表名称：** 单据体-子表
- **表名：** t_ipop_resusereportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuserate | 使用占比 | varchar | 50 |  | √ | ' ' | 使用占比 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fresname | 资源名称 | varchar | 50 |  | √ | ' ' | 资源名称 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcomparerate | 使用量/总量 | varchar | 50 |  | √ | ' ' | 使用量/总量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipop_resusereportentry |  | fentryid |
| 2 | idx_ipop_resusereportentry_id |  | fid |

---

## 资源用量报告-主表 t_ipop_resusereport

- **表名称：** 资源用量报告-主表
- **表名：** t_ipop_resusereport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fshowpublic | 显示公有云资源 | varchar | 1 |  | √ | '0' | 显示公有云资源 |
| 5 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipop_resusereport |  | fid |
| 2 | idx_ipop_resusereport_number |  | fnumber |
