# 市场码表-fbd_lendingmarketcode

## 市场码表-多语言表 t_fbd_lendingmarketcode_l

- **表名称：** 市场码表-多语言表
- **表名：** t_fbd_lendingmarketcode_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 显示名称 | varchar | 80 |  | √ | ' ' | 显示名称 |
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
| 1 | t_fbd_lendingmarketcode_l_pkey |  | fpkid |
| 2 | inx_fbd_lendingcode_l_locleld |  | flocleid |

---

## 市场码表-主表 t_fbd_lendingmarketcode

- **表名称：** 市场码表-主表
- **表名：** t_fbd_lendingmarketcode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 显示名称 | varchar | 80 |  | √ | ' ' | 显示名称 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | ftype | 类别 | varchar | 30 |  | √ | ' ' | 类别,枚举: 贷款市场 :贷款市场 银行间同业市场 :银行间同业市场 other :其他 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态基本信息 | varchar | 30 |  | √ | ' ' | 使用状态基本信息,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 代码 | varchar | 30 |  | √ | ' ' | 代码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fbd_lendingmarketcode_pkey |  | fid |
| 2 | inx_lengdingcode_ftype |  | ftype |
