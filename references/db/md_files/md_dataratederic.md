# 利率衍生品数据-md_dataratederic

## 利率衍生品数据-多语言表 t_md_dataratederic_l

- **表名称：** 利率衍生品数据-多语言表
- **表名：** t_md_dataratederic_l

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
| 1 | pk_t_md_dataratederic_l |  | fpkid |
| 2 | idx_md_dataratederic_l_id |  | fid |

---

## 利率衍生品数据-主表 t_md_dataratederic

- **表名称：** 利率衍生品数据-主表
- **表名：** t_md_dataratederic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fbuyprice | 买入价(%) | numeric | 23 | 10 | √ | 0 | 买入价(%) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fratedericativeid | 利率衍生品代码 | int8 | 64 |  | √ | 0 | [利率衍生品 tbd_ratederivative](../fbd_files/tbd_ratederivative.md) |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fmaxprice | 最高价(%) | numeric | 23 | 10 | √ | 0 | 最高价(%) |
| 9 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fsellprice | 卖出价(%) | numeric | 23 | 10 | √ | 0 | 卖出价(%) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fbizdate | 报价时间 | timestamp | 0 |  |  | null | 报价时间 |
| 15 | fendprice | 收盘价(%) | numeric | 23 | 10 | √ | 0 | 收盘价(%) |
| 16 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 17 | fminprice | 最低价(%) | numeric | 23 | 10 | √ | 0 | 最低价(%) |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fmiddleprice | 中间价(%) | numeric | 23 | 10 | √ | 0 | 中间价(%) |
| 20 | fbeginprice | 开盘价(%) | numeric | 23 | 10 | √ | 0 | 开盘价(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_dataratederic |  | fid |
| 2 | idx_md_dataratederic_n |  | fnumber |
