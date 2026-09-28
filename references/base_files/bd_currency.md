# 币种-bd_currency

## 币种-主表 t_bd_currency

- **表名称：** 币种-主表
- **表名：** t_bd_currency

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flogo | LOGO | varchar | 255 |  | √ | ' ' | LOGO |
| 3 | fformat | 显示格式 | varchar | 255 |  | √ | ' ' | 显示格式,枚举: 1 :货币符号+数值 2 :数值+货币符号 |
| 4 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fisshowsign | 显示货币符号 | bpchar | 1 |  | √ | ' ' | 显示货币符号 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '1' | 是否系统预置 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fpositiveformat | fpositiveformat | varchar | 30 |  | √ | ' ' |  |
| 13 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fsortcode | 排序码 | varchar | 10 |  | √ | ' ' | 排序码 |
| 16 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 18 | fsign | 币种符号 | varchar | 20 |  | √ | ' ' | 币种符号 |
| 19 | fseparator | fseparator | varchar | 1 |  | √ | ' ' |  |
| 20 | fpriceprecision | 单价精度 | int8 | 64 |  | √ | 0 | 单价精度 |
| 21 | fnegativeformat | fnegativeformat | varchar | 30 |  | √ | ' ' |  |
| 22 | famtprecision | 金额精度 | int8 | 64 |  | √ | 0 | 金额精度 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 货币代码 | varchar | 80 |  | √ | ' ' | 货币代码 |
| 25 | fgroupformat | fgroupformat | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_currency_pkey |  | fid |
| 2 | idx_t_bd_currency_number |  | fnumber |

---

## 币种-多语言表 t_bd_currency_l

- **表名称：** 币种-多语言表
- **表名：** t_bd_currency_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_currency_l_fid |  | fid,flocaleid |
| 2 | t_bd_currency_l_pkey |  | fpkid |
