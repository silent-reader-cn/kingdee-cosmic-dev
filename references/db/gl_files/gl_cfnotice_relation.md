# 现金流量通知单勾稽关系-gl_cfnotice_relation

## 单据体-子表 t_gl_cfnotice_oplogentry

- **表名称：** 单据体-子表
- **表名：** t_gl_cfnotice_oplogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fopvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fopvchentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_cfnotice_oplogentry |  | fentryid |
| 2 | idx_gl_cfoplogentry_fid |  | fid |
| 3 | idx_gl_cfoplogentry_fvchid |  | fopvoucherid |
| 4 | idx_gl_cfoplogentry_fvcheid |  | fopvchentryid |

---

## 现金流量通知单勾稽关系-主表 t_gl_cfnotice_relation

- **表名称：** 现金流量通知单勾稽关系-主表
- **表名：** t_gl_cfnotice_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | floccheck | 是否本位币勾稽 | bpchar | 1 |  | √ | '0' | 是否本位币勾稽 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_cfnotice_relation |  | floccheck |
| 2 | pk_t_gl_cfnotice_relation |  | fid |

---

## 单据体-子表 t_gl_cfnotice_logentry

- **表名称：** 单据体-子表
- **表名：** t_gl_cfnotice_logentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 3 | fvchentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_cflogentry_fvchentryid |  | fvchentryid |
| 2 | idx_gl_cflogentry_fvchid |  | fvoucherid |
| 3 | pk_t_gl_cfnotice_logentry |  | fentryid |
| 4 | idx_gl_cflogentry_fid |  | fid |
