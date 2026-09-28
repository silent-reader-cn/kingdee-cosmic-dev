# 报表项-rdem_report_item

## 报表项-多语言表 t_rdem_report_item_l

- **表名称：** 报表项-多语言表
- **表名：** t_rdem_report_item_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 多维组合名称 | varchar | 390 |  | √ | ' ' | 多维组合名称 |
| 3 | flongname | 多维组合长名称 | varchar | 2000 |  | √ | ' ' | 多维组合长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_report_item_l_0 |  | fid,flocaleid |
| 2 | pk_rdem_report_item_l |  | fpkid |

---

## 报表项-主表 t_rdem_report_item

- **表名称：** 报表项-主表
- **表名：** t_rdem_report_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 多维组合名称 | varchar | 256 |  | √ | ' ' | 多维组合名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | frowid | 行维成员 | int8 | 64 |  | √ | 0 | [行维成员管理 rdem_row_member](../rdem_files/rdem_row_member.md) |
| 6 | flongname | 多维组合长名称 | varchar | 2000 |  | √ | ' ' | 多维组合长名称 |
| 7 | fmodelid | 体系 | int8 | 64 |  | √ | 0 | [体系管理 rdem_model](../rdem_files/rdem_model.md) |
| 8 | ffcolumnid | 列维成员 | int8 | 64 |  | √ | 0 | [列维成员管理 rdem_col_member](../rdem_files/rdem_col_member.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 多维组合标识 | varchar | 128 |  | √ | ' ' | 多维组合标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_report_item_m0 |  | fmasterid |
| 2 | pk_rdem_report_item |  | fid |
