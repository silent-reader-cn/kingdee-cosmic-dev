# 利率-ifm_product

## 关联子实体-子表 t_ifm_product_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_product_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_product_lk |  | fpkid |

---

## 利率-多语言表 t_ifm_product_l

- **表名称：** 利率-多语言表
- **表名：** t_ifm_product_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcomment | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_product_l_id |  | fid |
| 2 | pk_t_ifm_product_l |  | fpkid |

---

## 单据体-多语言表 t_ifm_product_entry_l

- **表名称：** 单据体-多语言表
- **表名：** t_ifm_product_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcomment | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 2 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_product_entry_l_id |  | fentryid |
| 2 | pk_ifm_product_entry_l |  | fpkid |

---

## 单据体-子表 t_ifm_product_entry

- **表名称：** 单据体-子表
- **表名：** t_ifm_product_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbenchmark | 参考利率 | int8 | 64 |  | √ | 0 | 参考利率 tbd_referrate |
| 3 | ffloatrate | 浮动利率 | bpchar | 1 |  | √ | '0' | 浮动利率 |
| 4 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | finterestratedays | 利率转换天数 | varchar | 30 |  | √ | ' ' | 利率转换天数,枚举: Actual_360 :360 Actual_365 :365 |
| 6 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | finitdepositlimit | 起存限额 | numeric | 19 | 6 | √ | 0.000000 | 起存限额 |
| 9 | fconvertunit | 转移单位 | varchar | 30 |  | √ | ' ' | 转移单位,枚举: |
| 10 | fprice | 利率(%) | varchar | 30 |  | √ | ' ' | 利率(%) |
| 11 | ffloatdirection | 浮动方向 | varchar | 30 |  | √ | ' ' | 浮动方向,枚举: A :上浮 B :下浮 |
| 12 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 13 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | ffloatpoints | 浮动点数(bp) | int8 | 64 |  | √ | 0 | 浮动点数(bp) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fpricenum | 利率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 利率(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_product_entry_id |  | fentryid |
| 2 | pk_t_ifm_product_entry |  | fentryid |

---

## 利率-主表 t_ifm_product

- **表名称：** 利率-主表
- **表名：** t_ifm_product

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbenchmark | fbenchmark | int8 | 64 |  | √ | 0 |  |
| 3 | finterestratedays | 利率转换天数 | varchar | 30 |  | √ | ' ' | 利率转换天数,枚举: Actual_360 :360 Actual_365 :365 |
| 4 | freferrateid | 参考利率 | int8 | 64 |  | √ | 0 | 参考利率 tbd_referrate |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fprice | 利率(%) | varchar | 50 |  | √ | ' ' | 利率(%) |
| 7 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 12 | fproductterm | 产品期限 | varchar | 80 |  | √ | ' ' | 产品期限,枚举: - :活期 on :O/N day :1D week :1W twoWeek :2W threeWeek :3W month :1M twoMonth :2M season :3M fourMonth :4M fiveMonth :5M hyear :6M sevenMonth :7M eightMonth :8M nineMonth :9M tenMonth :10M elevenMonth :11M oneYear :1Y twoYear :2Y threeYear :3Y fourYear :4Y fiveYear :5Y |
| 13 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fproducttermid | fproducttermid | int8 | 64 |  | √ | 0 |  |
| 15 | fpricenum | 利率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 利率(%) |
| 16 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | ffloatrate | 浮动利率 | bpchar | 1 |  | √ | '0' | 浮动利率 |
| 18 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 19 | fcategory | 类别 | varchar | 30 |  | √ | ' ' | 类别,枚举: A :活期存款 B :协定存款 C :定期存款 D :通知存款 |
| 20 | fcomment | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 23 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | finitdepositlimit | 起存限额 | numeric | 19 | 6 | √ | 0.000000 | 起存限额 |
| 25 | fconvertunit | 转移单位 | varchar | 30 |  | √ | ' ' | 转移单位,枚举: 0.01 :0.01 1 :1 100 :100 10000 :10000 |
| 26 | fservicecategory | 金融服务项目 | varchar | 30 |  | √ | ' ' | 金融服务项目,枚举: A :存款 |
| 27 | ffloatdirection | 浮动方向 | varchar | 30 |  | √ | ' ' | 浮动方向,枚举: A :上浮 B :下浮 |
| 28 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | ffloatpoints | 浮动点数(bp) | int8 | 64 |  | √ | 0 | 浮动点数(bp) |
| 30 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 31 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_product_number |  | fnumber |
| 2 | pk_t_ifm_product |  | fid |
| 3 | idx_ifm_product_id |  | fnumber |
