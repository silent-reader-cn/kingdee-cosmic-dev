# 关联交易内容-theme_transaction_content

## 关联交易内容-主表 t_theme_transaction_conte

- **表名称：** 关联交易内容-主表
- **表名：** t_theme_transaction_conte

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescribe | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 6 | fcontenttype | 内容类型 | varchar | 50 |  | √ | ' ' | 内容类型,枚举: 0 :关联采购 1 :关联销售 2 :资金拆借 3 :代收代付 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fprecut | 是否系统预制 | bpchar | 1 |  | √ | ' ' | 是否系统预制 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_transaction_conte |  | fid |
| 2 | theme_transaction_conte_name |  | fname |

---

## 关联交易内容-多语言表 t_theme_transaction_conte_l

- **表名称：** 关联交易内容-多语言表
- **表名：** t_theme_transaction_conte_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_transaction_conte_l |  | fpkid |
| 2 | idx_transaction_conte_lname |  | fname |
