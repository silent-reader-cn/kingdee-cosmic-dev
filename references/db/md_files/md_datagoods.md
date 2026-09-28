# 商品数据-md_datagoods

## 商品数据-主表 t_md_datagoods

- **表名称：** 商品数据-主表
- **表名：** t_md_datagoods

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fgoodsid | 商品代码 | int8 | 64 |  | √ | 0 | [商品定义 tbd_goodsdefined](../fbd_files/tbd_goodsdefined.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmornprice | 早盘价 | numeric | 23 | 10 | √ | 0 | 早盘价 |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fmaxprice | 最高价 | numeric | 23 | 10 | √ | 0 | 最高价 |
| 9 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fbizdate | 报价时间 | timestamp | 0 |  |  | null | 报价时间 |
| 14 | fnoonprice | 午盘价 | numeric | 23 | 10 | √ | 0 | 午盘价 |
| 15 | fendprice | 收盘价 | numeric | 23 | 10 | √ | 0 | 收盘价 |
| 16 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 17 | fminprice | 最低价 | numeric | 23 | 10 | √ | 0 | 最低价 |
| 18 | fsettleprice | 结算价 | numeric | 23 | 10 | √ | 0 | 结算价 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fcurrencyid | 商品币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fbeginprice | 开盘价 | numeric | 23 | 10 | √ | 0 | 开盘价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_md_datagoods_n |  | fnumber |
| 2 | pk_t_md_datagoods |  | fid |

---

## 商品数据-多语言表 t_md_datagoods_l

- **表名称：** 商品数据-多语言表
- **表名：** t_md_datagoods_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
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
| 1 | idx_md_dataindex_l_id |  | fid,flocaleid |
| 2 | pk_t_md_datagoods_l |  | fpkid |
