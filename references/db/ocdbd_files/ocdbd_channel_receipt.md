# 渠道开票信息-ocdbd_channel_receipt

## 渠道开票信息-多语言表 t_ocdbd_chl_receipt_l

- **表名称：** 渠道开票信息-多语言表
- **表名：** t_ocdbd_chl_receipt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 抬头 | varchar | 100 |  | √ | ' ' | 抬头 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_chlreceiptl_fidlid |  | fid,flocaleid |
| 2 | pk_ocdbd_chl_receipt_l |  | fpkid |

---

## 渠道开票信息-主表 t_ocdbd_chl_receipt

- **表名称：** 渠道开票信息-主表
- **表名：** t_ocdbd_chl_receipt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | faddress | 地址 | varchar | 255 |  | √ | ' ' | 地址 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftel | 电话 | varchar | 80 |  | √ | ' ' | 电话 |
| 8 | fbankaccount | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 9 | fbankname | 开户银行 | varchar | 50 |  | √ | ' ' | 开户银行 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 税号 | varchar | 80 |  | √ | ' ' | 税号 |
| 17 | ftaxtype | 发票类型 | bpchar | 1 |  | √ | ' ' | 发票类型,枚举: 1 :普通发票 2 :专用发票 3 :电子发票 |
| 18 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_chl_receipt |  | fid |
| 2 | idx_ocdbd_chlreceipt_num |  | fnumber |
