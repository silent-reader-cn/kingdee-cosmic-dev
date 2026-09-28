# 高新技术收入明细-tdm_high_tech_income

## 高新技术收入明细-主表 t_tdm_high_tech_income

- **表名称：** 高新技术收入明细-主表
- **表名：** t_tdm_high_tech_income

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fyear | 年度 | timestamp | 0 |  |  | null | 年度 |
| 4 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: A :手工新增 B :模版引入 C :数据同步 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | ftaxorgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fproductgroup | 产品组 | varchar | 1000 |  | √ | ' ' | 产品组 |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 10 | fincometype | 收入类型 | varchar | 50 |  | √ | ' ' | 收入类型,枚举: A :产品（服务）收入 B :技术性收入 |
| 11 | fishightech | 是否高新 | bpchar | 1 |  | √ | '0' | 是否高新 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_highti_org |  | ftaxorgid |
| 2 | pk_tdm_high_tech_income |  | fid |
