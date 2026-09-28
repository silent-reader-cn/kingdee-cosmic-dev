# 借贷市场利率-fbd_loanmarketrate

## 借贷市场利率-主表 t_fbd_lendingmarketrate

- **表名称：** 借贷市场利率-主表
- **表名：** t_fbd_lendingmarketrate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | frate | 利率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 利率(%) |
| 11 | flendingmarket | 借贷市场 | int8 | 64 |  | √ | 0 | 市场码表 fbd_lendingmarketcode |
| 12 | ftermcategory | 期限 | int8 | 64 |  | √ | 0 | 期限类别码表 fbd_termcategorycode |
| 13 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fpublishdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | inx_fbd_lendingmarket_number |  | flendingmarket |
| 2 | t_fbd_lendingmarketrate_pkey |  | fid |
| 3 | inx_fbd_lendingrate_enable |  | fenable |
| 4 | inx_fbd_termcategory_number |  | ftermcategory |

---

## 借贷市场利率-多语言表 t_fbd_lendingmarketrate_l

- **表名称：** 借贷市场利率-多语言表
- **表名：** t_fbd_lendingmarketrate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocleid | flocleid | varchar | 10 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 255 |  |  | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fbd_lendingmarketrate_l_pkey |  | fpkid |
| 2 | inx_fbd_lendingmarket_locleld |  | flocleid |
