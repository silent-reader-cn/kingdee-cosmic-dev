# 外汇市场牌价-fbd_foreignmarkerate

## 外汇市场牌价-多语言表 t_fbd_foreignmarkerate_l

- **表名称：** 外汇市场牌价-多语言表
- **表名：** t_fbd_foreignmarkerate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fbd_foreignmarkerate_l_pkey |  | fpkid |
| 2 | idx_formarate_l_fname |  | fname |

---

## 外汇市场牌价-主表 t_fbd_foreignmarkerate

- **表名称：** 外汇市场牌价-主表
- **表名：** t_fbd_foreignmarkerate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forganization | 机构 | varchar | 30 |  | √ | ' ' | 机构,枚举: bd_bankcgsetting :银行类别 bd_finorginfo :合作金融机构 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftargetcurrencyamount_c | 目标货币数量 | varchar | 50 |  | √ | ' ' | 目标货币数量,枚举: 1 :1 100 :100 10000 :10000 |
| 5 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fconvertprice | 折算价 | numeric | 23 | 10 | √ | 0.0000000000 | 折算价 |
| 8 | freleasedate | 发布日期 | timestamp | 0 |  |  | null | 发布日期 |
| 9 | fbuyingprice | 买入价 | numeric | 23 | 10 | √ | 0.0000000000 | 买入价 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ftargetcurrency | 目标货币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fdeadline | 期限 | int8 | 64 |  | √ | 0 | 期限类别码表 fbd_termcategorycode |
| 16 | fenable | 使用状态 | varchar | 30 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | ftargetcurrencyamount | ftargetcurrencyamount | int8 | 64 |  | √ | 0 |  |
| 18 | fratesources | 牌价来源 | int8 | 64 |  | √ | 0 | 银行类别 bd_bankcgsetting |
| 19 | foriginalcurrency | 原币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fmiddleprice | 中间价 | numeric | 23 | 10 | √ | 0.0000000000 | 中间价 |
| 22 | fsellingprice | 卖出价 | numeric | 23 | 10 | √ | 0.0000000000 | 卖出价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fbd_foreignmarkerate_pkey |  | fid |
| 2 | idx_formarate_fratesources |  | fratesources |
