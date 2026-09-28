# 文化事业建设费申报信息-totf_whsyjsf_message

## 单据体-子表 t_totf_message_entry

- **表名称：** 单据体-子表
- **表名：** t_totf_message_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fzszm | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tysbsf_bizdef_entry |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_message_entry |  | fentryid |
| 2 | idx_totf_message_entry |  | fid |

---

## 文化事业建设费申报信息-主表 t_totf_whsyjsf_message

- **表名称：** 文化事业建设费申报信息-主表
- **表名：** t_totf_whsyjsf_message

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fskssqz | 费款所属期止 | timestamp | 0 |  |  | null | 费款所属期止 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsbbid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 5 | fskssqq | 费款所属期起 | timestamp | 0 |  |  | null | 费款所属期起 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_totf_message |  | fsbbid |
| 2 | pk_totf_whsyjsf_message |  | fid |
