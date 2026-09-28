# 币种（演示）-isc_demo_currency

## 币种（演示）-多语言表 t_isc_demo_currency_l

- **表名称：** 币种（演示）-多语言表
- **表名：** t_isc_demo_currency_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_isc_demo_currency_l |  | fpkid |
| 2 | idx_isc_demo_currency_l_2 |  | fname |
| 3 | idx_isc_demo_currency_l_1 |  | fid,flocaleid |

---

## 币种（演示）-主表 t_isc_demo_currency

- **表名称：** 币种（演示）-主表
- **表名：** t_isc_demo_currency

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fformat | 显示格式 | varchar | 30 |  | √ | ' ' | 显示格式,枚举: 1 :货币符号+数值 2 :数值+货币符号 |
| 5 | fsortcode | 排序码 | varchar | 50 |  | √ | ' ' | 排序码 |
| 6 | fsoid | 来源对象ID | varchar | 50 |  | √ | ' ' | 来源对象ID |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fsign | 币种符号 | varchar | 50 |  | √ | ' ' | 币种符号 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fisshowsign | 显示货币符号 | bpchar | 1 |  | √ | '0' | 显示货币符号 |
| 11 | fssid | 来源系统ID | varchar | 50 |  | √ | ' ' | 来源系统ID |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fpriceprecision | 单价精度 | int8 | 64 |  | √ | 0 | 单价精度 |
| 15 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 16 | famtprecision | 金额精度 | int8 | 64 |  | √ | 0 | 金额精度 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 货币代码 | varchar | 30 |  | √ | ' ' | 货币代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_demo_currency_2 |  | fsoid,fssid |
| 2 | pk_isc_demo_currency |  | fid |
| 3 | idx_isc_demo_currency_1 |  | fnumber |
