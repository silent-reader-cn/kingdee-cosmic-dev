# 单据按钮隐藏配置-dhc_buttonvisible_conf

## 单据按钮隐藏配置-主表 t_dhc_btnconf

- **表名称：** 单据按钮隐藏配置-主表
- **表名：** t_dhc_btnconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fislist | 列表 | bpchar | 1 |  | √ | '0' | 列表 |
| 3 | fformid | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dhc_btn_formid |  | fformid |
| 2 | pk_t_dhc_btnconf |  | fid |

---

## 单据体-子表 t_dhc_btn_entry

- **表名称：** 单据体-子表
- **表名：** t_dhc_btn_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fbuttonid | 按钮标识 | varchar | 50 |  | √ | ' ' | 按钮标识 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dhc_btn_entry |  | fentryid |
| 2 | idx_dhc_btnentry_btnid |  | fbuttonid |
| 3 | idx_dhc_btnentry_id |  | fid |
