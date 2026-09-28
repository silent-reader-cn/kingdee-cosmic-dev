# 税金采集-tctsa_tax_collections

## 税金采集-主表 t_tctsa_tax_collections

- **表名称：** 税金采集-主表
- **表名：** t_tctsa_tax_collections

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fyysr | 应税收入 | numeric | 23 | 10 |  | 0 | 应税收入 |
| 4 | fjmse | 减免税额 | numeric | 23 | 10 |  | 0 | 减免税额 |
| 5 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :手工新增 1 :模板引入 |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 10 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 |  | 0 | 本期应补（退）税额 |
| 11 | forg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_tax_collections |  | forg,ftaxtype,fskssqq,fskssqz |
| 2 | pk_tctsa_tax_collections |  | fid |
