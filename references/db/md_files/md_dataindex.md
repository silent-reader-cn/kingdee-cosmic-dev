# 指数数据-md_dataindex

## 指数数据-主表 t_md_dataindex

- **表名称：** 指数数据-主表
- **表名：** t_md_dataindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | favgprice | 均价 | numeric | 23 | 10 | √ | 0.0000000000 | 均价 |
| 6 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fmaxprice | 最高价 | numeric | 23 | 10 | √ | 0.0000000000 | 最高价 |
| 8 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | freferindexid | 指数代码 | int8 | 64 |  | √ | 0 | [指数定义 tbd_referindex](../fbd_files/tbd_referindex.md) |
| 13 | fbizdate | 报价时间 | timestamp | 0 |  |  | null | 报价时间 |
| 14 | ftimeprice | 具体时点价 | numeric | 23 | 10 | √ | 0.0000000000 | 具体时点价 |
| 15 | fendprice | 收盘价 | numeric | 23 | 10 | √ | 0.0000000000 | 收盘价 |
| 16 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 17 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源 |
| 18 | fminprice | 最低价 | numeric | 23 | 10 | √ | 0.0000000000 | 最低价 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fquotetype | 报价方式 | varchar | 30 |  | √ | ' ' | 报价方式,枚举: day :当日报价 time :时点报价 |
| 21 | fbeginprice | 开盘价 | numeric | 23 | 10 | √ | 0.0000000000 | 开盘价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_dataindex |  | fid |
| 2 | idx_tbd_dataindex |  | freferindexid,fbizdate |

---

## 指数数据-多语言表 t_md_dataindex_l

- **表名称：** 指数数据-多语言表
- **表名：** t_md_dataindex_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_dataindex_l |  | fpkid |
| 2 | idx_md_dataindxe_l_id |  | fid,flocaleid |
