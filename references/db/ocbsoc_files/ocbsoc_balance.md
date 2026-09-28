# 预收款余额-ocbsoc_balance

## 预收款余额-多语言表 t_ocbsoc_balance_l

- **表名称：** 预收款余额-多语言表
- **表名：** t_ocbsoc_balance_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_balance_l |  | fpkid |
| 2 | idx_ocbsoc_balancel_flid |  | fid,flocaleid |

---

## 预收款余额-主表 t_ocbsoc_balance

- **表名称：** 预收款余额-主表
- **表名：** t_ocbsoc_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foccupied | 订单预占余额 | numeric | 23 | 10 | √ | 0 | 订单预占余额 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fsalechannelid | 收款渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | forderchannelid | 付款渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 13 | fbalance | 预收款余额 | numeric | 23 | 10 | √ | 0 | 预收款余额 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fusable | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | fversion | 版本 | int8 | 64 |  | √ | 1 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_balance_sochl |  | fsalechannelid,forderchannelid |
| 2 | pk_ocbsoc_balance |  | fid |
