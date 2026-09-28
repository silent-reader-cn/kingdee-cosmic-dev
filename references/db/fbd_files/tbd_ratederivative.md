# 利率衍生品-tbd_ratederivative

## 利率衍生品-多语言表 t_tbd_ratedericative_l

- **表名称：** 利率衍生品-多语言表
- **表名：** t_tbd_ratedericative_l

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
| 1 | pk_t_tbd_ratedericative_l |  | fpkid |
| 2 | idx_tbd_ratedericative_l_id |  | fid |

---

## 利率衍生品-主表 t_tbd_ratedericative

- **表名称：** 利率衍生品-主表
- **表名：** t_tbd_ratedericative

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffra | FRA（num-num） | varchar | 30 |  | √ | ' ' | FRA（num-num） |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fterm | 期限 | varchar | 30 |  | √ | ' ' | 期限,枚举: day :1D week :1W twoWeek :2W threeWeek :3W month :1M twoMonth :2M season :3M fourMonth :4M fiveMonth :5M hyear :6M sevenMonth :7M eightMonth :8M nineMonth :9M tenMonth :10M elevenMonth :11M oneYear :1Y twoYear :2Y threeYear :3Y fourYear :4Y fiveYear :5Y |
| 6 | fcontract | 合约 | varchar | 30 |  | √ | ' ' | 合约 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fpublishtime | 发布时间 | int4 | 32 |  | √ | '-1' | 发布时间 |
| 9 | freferrateid | 参考利率编码 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: forward :利率远期 futures :利率期货 swap :利率互换 |
| 15 | ftimezoneid | 发布时区 | int8 | 64 |  | √ | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 16 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 17 | fnumber | 利率衍生品代码 | varchar | 80 |  | √ | ' ' | 利率衍生品代码 |
| 18 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tbd_ratedericative |  | fid |
| 2 | idx_tbd_ratedericative_n |  | fnumber |
