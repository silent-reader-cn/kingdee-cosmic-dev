# 报表附注-tdm_finance_attachment

## 附件-附件表 t_tdm_finance_file

- **表名称：** 附件-附件表
- **表名：** t_tdm_finance_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_finance_file |  | fid |
| 2 | pk_tdm_finance_file |  | fpkid |

---

## 报表附注-主表 t_tdm_finance_attachment

- **表名称：** 报表附注-主表
- **表名：** t_tdm_finance_attachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpeirod | 报表期间 | timestamp | 0 |  |  | null | 报表期间 |
| 3 | faccountbookstype | 账簿类型 | varchar | 50 |  | √ | ' ' | 账簿类型 |
| 4 | fsbbid | 申报表ID | varchar | 50 |  | √ | ' ' | 申报表ID |
| 5 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tctb_template_type |
| 6 | forg | 编制组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_finance_attachment |  | fid |
| 2 | idx_tdm_finance_attachment |  | forg |
