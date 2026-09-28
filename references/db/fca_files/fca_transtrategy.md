# 账户划拨策略-fca_transtrategy

## 账户划拨策略-多语言表 t_fca_transtrategy_l

- **表名称：** 账户划拨策略-多语言表
- **表名：** t_fca_transtrategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transtrategy_l_pkey |  | fpkid |
| 2 | idx_fca_transtrategy_l |  | fid,flocaleid |

---

## 账户划拨策略-主表 t_fca_transtrategy

- **表名称：** 账户划拨策略-主表
- **表名：** t_fca_transtrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransupscale | 上划比例(%) | numeric | 19 | 6 | √ | 0.000000 | 上划比例(%) |
| 3 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 4 | fminupamt | 最小上划金额 | numeric | 19 | 6 | √ | 0.000000 | 最小上划金额 |
| 5 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 6 | fstatus | 数据状态 | varchar | 80 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fistransup | 启用上划策略 | bpchar | 1 |  | √ | '0' | 启用上划策略 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsafetyamt | 留存金额 | numeric | 19 | 6 | √ | 0.000000 | 留存金额 |
| 11 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 14 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 17 | fupquotaamt | 上划定额 | numeric | 19 | 6 | √ | 0.000000 | 上划定额 |
| 18 | fsolidbal | 最小余额 | numeric | 19 | 6 | √ | 0.000000 | 最小余额 |
| 19 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fistransdown | 启用下拨策略 | bpchar | 1 |  | √ | '0' | 启用下拨策略 |
| 21 | fmindownamt | 最小下拨金额 | numeric | 19 | 6 | √ | 0.000000 | 最小下拨金额 |
| 22 | ftransint | 划拨取整基数 | varchar | 80 |  | √ | ' ' | 划拨取整基数,枚举: isnull :无 hundred :100 thousand :1,000 tenthousand :10,000 hunthousand :100,000 |
| 23 | fdownway | 下拨方式 | varchar | 80 |  | √ | ' ' | 下拨方式,枚举: isdownquota :定额 ispolish :补齐 |
| 24 | fenable | 使用状态 | varchar | 80 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 26 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fupway | 上划方式 | varchar | 80 |  | √ | ' ' | 上划方式,枚举: isfullamt :全额 isupquota :定额 isscale :按比例 issafety :留存 |
| 28 | fdownquotaamt | 下拨定额 | numeric | 19 | 6 | √ | 0.000000 | 下拨定额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transtrategy_pkey |  | fid |
| 2 | idx_fca_transtrategy |  | fnumber,fcurrencyid,fenable |
