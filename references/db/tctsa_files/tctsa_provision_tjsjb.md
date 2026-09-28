# 统计计提税金表-tctsa_provision_tjsjb

## 统计计提税金表-主表 t_tctsa_provision_tjsjb

- **表名称：** 统计计提税金表-主表
- **表名：** t_tctsa_provision_tjsjb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbooktype | 账簿类型 | varchar | 50 |  | √ | ' ' | 账簿类型,枚举: 0 :本地账簿 1 :集团账簿 |
| 3 | fcurrency | 计提币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fmetadataid | 元数据标识 | varchar | 200 |  | √ | ' ' | 元数据标识 |
| 5 | fskssqq | 计提期间起 | timestamp | 0 |  |  | null | 计提期间起 |
| 6 | fhsorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | forg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 9 | fskssqz | 计提期间止 | timestamp | 0 |  |  | null | 计提期间止 |
| 10 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 11 | fsbbid | 关联id | varchar | 50 |  | √ | ' ' | 关联id |
| 12 | fsjtotal | 税金合计 | numeric | 23 | 10 | √ | 0 | 税金合计 |
| 13 | fprovisionmatter | 计提事项 | int8 | 64 |  | √ | 0 | 计提事项 itp_proviston_item |
| 14 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_provisi_sbbid |  | fsbbid |
| 2 | pk_tctsa_provision_tjsjb |  | fid |

---

## 单据体-子表 t_tctsa_provisi_tjsjb_djt

- **表名称：** 单据体-子表
- **表名：** t_tctsa_provisi_tjsjb_djt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsm | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 3 | fbizdimensiontype | 业务维度 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 5 | fjtsj | 计提税金 | numeric | 23 | 10 | √ | 0 | 计提税金 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_provisi_tjsjb_djt |  | fentryid |
| 2 | idx_tctsa_provisi_tjsjb_djt_fk |  | fid |
