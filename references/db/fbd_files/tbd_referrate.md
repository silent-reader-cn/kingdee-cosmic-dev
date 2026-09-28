# 参考利率表-tbd_referrate

## 参考利率表-主表 t_tbd_referrate

- **表名称：** 参考利率表-主表
- **表名：** t_tbd_referrate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fterm | 期限 | varchar | 80 |  | √ | ' ' | 期限,枚举: day :1D sevenDay :7D week :1W twoWeek :2W threeWeek :3W month :1M twoMonth :2M season :3M fourMonth :4M fiveMonth :5M hyear :6M sevenMonth :7M eightMonth :8M nineMonth :9M tenMonth :10M elevenMonth :11M oneYear :1Y twoYear :2Y threeYear :3Y fourYear :4Y fiveYear :5Y moreThanFiveYear :5Y+ |
| 4 | fmarketid | 利率类型 | int8 | 64 |  | √ | 0 | [市场码表 fbd_lendingmarketcode](../fbd_files/fbd_lendingmarketcode.md) |
| 5 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | foffset | foffset | int8 | 64 |  | √ | 0 |  |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fissuezoneid | fissuezoneid | int8 | 64 |  | √ | 0 |  |
| 15 | fissuetime | fissuetime | int8 | 64 |  | √ | 0 |  |
| 16 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 17 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | freferrate | 参考利率名称 | varchar | 80 |  | √ | ' ' | 参考利率名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tbd_referrate |  | fnumber,fcurrencyid,fissuetime,fterm |
| 2 | pk_t_tbd_referrate |  | fid |

---

## 参考利率表-多语言表 t_tbd_referrate_l

- **表名称：** 参考利率表-多语言表
- **表名：** t_tbd_referrate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tbd_indxe_l_id |  | fid,flocaleid |
| 2 | pk_t_tbd_referrate_l |  | fpkid |
