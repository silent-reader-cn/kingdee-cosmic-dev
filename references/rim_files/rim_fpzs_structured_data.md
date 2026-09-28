# 发票头结构化数据-rim_fpzs_structured_data

## 发票头结构化数据-主表 t_rim_structured_data

- **表名称：** 发票头结构化数据-主表
- **表名：** t_rim_structured_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | ftypes | 适用发票类型 | varchar | 255 |  | √ | ' ' | 适用发票类型,枚举: 1 :电子普通发票 2 :电子专用发票 3 :纸质普通发票 4 :纸质专用发票 5 :普通纸质卷票 7 :通用机打纸质发票 8 :出租车票 9 :火车/高铁票 10 :飞机行程单 11 :其他票 12 :机动车销售发票 13 :二手车销售发票 14 :定额发票 15 :通行费电子发票 16 :公路汽车票 17 :过路桥费发票 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车票退票凭证 25 :财政电子票据 26 :全电普票 27 :全电专票 |
| 10 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 11 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_structured_data_num |  | fnumber,fname |
| 2 | pk_t_rim_structured_data |  | fid |

---

## 发票头结构化数据-多语言表 t_rim_structured_data_l

- **表名称：** 发票头结构化数据-多语言表
- **表名：** t_rim_structured_data_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_structured_data_l |  | fpkid |
| 2 | idx_rim_structured_data_l_0 |  | fid,flocaleid |
