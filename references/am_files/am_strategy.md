# 账户管理策略-am_strategy

## 账户管理策略-多语言表 t_am_strategy_l

- **表名称：** 账户管理策略-多语言表
- **表名：** t_am_strategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 256 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_am_strategy_l_pkey |  | fpkid |
| 2 | idx_am_straregy_l |  | fname |

---

## 账户管理策略-主表 t_am_strategy

- **表名称：** 账户管理策略-主表
- **表名：** t_am_strategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissubmit | 提交 | bpchar | 1 |  | √ | '0' | 提交 |
| 3 | fisallowover | 允许透支 | bpchar | 1 |  | √ | '0' | 允许透支 |
| 4 | fisballimit | 开启账户留存限额 | bpchar | 1 |  | √ | '0' | 开启账户留存限额 |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fisoverstrgy | 透支策略 | bpchar | 1 |  | √ | '0' | 透支策略 |
| 7 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 8 | fsinglelimit | 单笔限额 | numeric | 19 | 6 | √ | 0.000000 | 单笔限额 |
| 9 | fstatus | 数据状态 | varchar | 80 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fispay | 付款 | bpchar | 1 |  | √ | '0' | 付款 |
| 13 | fisinneraudit | 审核 | bpchar | 1 |  | √ | '0' | 审核 |
| 14 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fisinnerpay | 付款 | bpchar | 1 |  | √ | '0' | 付款 |
| 16 | finvolstrgy | 涉及策略 | varchar | 80 |  | √ | ' ' | 涉及策略,枚举: 1 :透支 2 :限额 |
| 17 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 19 | fisinnerstrategy | 是否内部账户策略 | bpchar | 1 |  | √ | '0' | 是否内部账户策略 |
| 20 | fminiacctlimit | 最低留存金额 | numeric | 19 | 6 | √ | 0.000000 | 最低留存金额 |
| 21 | fcomment | 备注 | varchar | 256 |  | √ | ' ' | 备注 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | foveramt | 透支额度 | numeric | 19 | 6 | √ | 0.000000 | 透支额度 |
| 24 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 25 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fisinnersave | 保存 | bpchar | 1 |  | √ | '0' | 保存 |
| 27 | fisoverworn | 透支提醒 | bpchar | 1 |  | √ | '0' | 透支提醒 |
| 28 | fisinnersubmit | 提交 | bpchar | 1 |  | √ | '0' | 提交 |
| 29 | fispaylimit | 开启账户支付限额 | bpchar | 1 |  | √ | '0' | 开启账户支付限额 |
| 30 | fenable | 使用状态 | varchar | 80 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 32 | fopenstrgy | 策略启用 | varchar | 80 |  | √ | ' ' | 策略启用 |
| 33 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 34 | fislimitstrgy | 限额策略 | bpchar | 1 |  | √ | '0' | 限额策略 |
| 35 | fdailylimit | 日限额 | numeric | 19 | 6 | √ | 0.000000 | 日限额 |
| 36 | fmonthlylimit | 月限额 | numeric | 19 | 6 | √ | 0.000000 | 月限额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_am_strategy_pkey |  | fid |
| 2 | idx_am_straregy |  | fnumber,fcurrencyid |
