# 指数定义-tbd_referindex

## 指数定义-多语言表 t_tbd_referindex_l

- **表名称：** 指数定义-多语言表
- **表名：** t_tbd_referindex_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 指数名称 | varchar | 80 |  | √ | ' ' | 指数名称 |
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
| 1 | idx_tbd_referindxe_l_id |  | fid,flocaleid |
| 2 | pk_t_tbd_referindex_l |  | fpkid |

---

## 指数定义-主表 t_tbd_referindex

- **表名称：** 指数定义-主表
- **表名：** t_tbd_referindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 指数名称 | varchar | 80 |  | √ | ' ' | 指数名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | ftype | 资产类别 | varchar | 30 |  | √ | ' ' | 资产类别,枚举: stock :股票 bond :债券 fund :基金 futures :期货 commodity :商品 |
| 11 | fissuezoneid | 发布时区 | int8 | 64 |  | √ | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 12 | fissuetime | 发布时间 | int8 | 64 |  | √ | 0 | 发布时间 |
| 13 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 14 | fnumber | 指数代码 | varchar | 30 |  | √ | ' ' | 指数代码 |
| 15 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tbd_referindex |  | fid |
| 2 | idx_tbd_referindex |  | fnumber |
