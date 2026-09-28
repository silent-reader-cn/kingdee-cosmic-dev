# 研发费用明细-tdm_rdesd_expense

## 研发费用明细-多语言表 t_tdm_redesd_expense_l

- **表名称：** 研发费用明细-多语言表
- **表名：** t_tdm_redesd_expense_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_rdesd_expense |  | fid,flocaleid |
| 2 | pk_tdm_redesd_expense_l |  | fpkid |

---

## 研发费用明细-主表 t_tdm_redesd_expense

- **表名称：** 研发费用明细-主表
- **表名：** t_tdm_redesd_expense

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税务金额 | numeric | 23 | 10 | √ | 0 | 税务金额 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fbaseproject | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftype | 费用类型 | int8 | 64 |  | √ | 0 | 研发费用明细类型 tpo_rdesd_expense_type |
| 13 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: A :手工新增 B :模版引入 C :数据同步 |
| 16 | ftaxorgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fnumber | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 18 | faccountingamount | 会计金额 | numeric | 23 | 10 | √ | 0 | 会计金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_rdesd_expense_2 |  | ftype |
| 2 | pk_tdm_redesd_expense |  | fid |
| 3 | idx_tdm_rdesd_expense_1 |  | ftaxorgid |
