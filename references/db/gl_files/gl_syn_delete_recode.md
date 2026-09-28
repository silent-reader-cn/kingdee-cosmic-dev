# 凭证中间表删除记录-gl_syn_delete_recode

## 单据体-子表 t_gl_syn_recode_entry

- **表名称：** 单据体-子表
- **表名：** t_gl_syn_recode_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmidid | 中间表id | varchar | 50 |  | √ | ' ' | 中间表id |
| 3 | fmidbillno | 中间表凭证号 | varchar | 50 |  | √ | ' ' | 中间表凭证号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_syn_recode_entry |  | fentryid |
| 2 | idx_gl_synrecode_entry |  | fid |

---

## 凭证中间表删除记录-主表 t_gl_syn_deleterecode

- **表名称：** 凭证中间表删除记录-主表
- **表名：** t_gl_syn_deleterecode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdtime | 删除时间 | varchar | 50 |  | √ | ' ' | 删除时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_syn_deleterecode |  | fid |
| 2 | idx_gl_syn_deleterecode |  | fdtime |
