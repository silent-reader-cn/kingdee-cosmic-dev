# 商品定义-tbd_goodsdefined

## 商品定义-多语言表 t_tbd_goodsdefined_l

- **表名称：** 商品定义-多语言表
- **表名：** t_tbd_goodsdefined_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
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
| 1 | pk_t_tbd_goodsdefined_l |  | fpkid |
| 2 | idx_tbd_goodsdefined_l_id |  | fid |

---

## 商品定义-主表 t_tbd_goodsdefined

- **表名称：** 商品定义-主表
- **表名：** t_tbd_goodsdefined

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpublishtime | 发布时间 | int4 | 32 |  | √ | '-1' | 发布时间 |
| 6 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ftype | 类别 | varchar | 30 |  | √ | ' ' | 类别,枚举: metal :金属 energy :能源 chemical :化工 steel :钢材 farmproduct :农产品 |
| 12 | ftimezoneid | 发布时区 | int8 | 64 |  | √ | 0 | 时区 inte_timezone |
| 13 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 14 | fnumber | 商品代码 | varchar | 80 |  | √ | ' ' | 商品代码 |
| 15 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tbd_goodsdefined_n |  | fnumber |
| 2 | pk_t_tbd_goodsdefined |  | fid |
