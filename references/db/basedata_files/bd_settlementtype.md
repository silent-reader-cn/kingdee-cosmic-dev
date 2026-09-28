# 结算方式-bd_settlementtype

## 结算方式-主表 t_bd_settlementtype

- **表名称：** 结算方式-主表
- **表名：** t_bd_settlementtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fisagencypersonpay | 并笔入账 | bpchar | 1 |  |  | null | 并笔入账 |
| 3 | fpaymentchannel | 限定支付渠道 | varchar | 50 |  | √ | ' ' | 限定支付渠道,枚举: |
| 4 | forgid | forgid | int8 | 64 |  |  | null |  |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fispersonpay | 对私支付 | bpchar | 1 |  |  | null | 对私支付 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 11 | fislinkpay | 联动支付 | bpchar | 1 |  | √ | '0' | 联动支付 |
| 12 | fsettlementtype | 类别 | varchar | 30 |  |  | null | 类别,枚举: 0 :现金 1 :支票 2 :本票 3 :汇兑 4 :票汇 5 :商业承兑汇票 6 :银行承兑汇票 7 :信用证到单/交单 14 :虚拟结算 16 :信用证开立 |
| 13 | fissystem | fissystem | bpchar | 1 |  |  | null |  |
| 14 | fbillopetype | 票据行为 | varchar | 50 |  | √ | ' ' | 票据行为,枚举: recpay :收票/出票 endorse :背书转让 |
| 15 | fpaythroughbe | 银企直联支付 | bpchar | 1 |  |  | null | 银企直联支付 |
| 16 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 17 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fdisablerid | 禁用人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 22 | fdpaymentchannel | 默认支付渠道 | varchar | 50 |  | √ | ' ' | 默认支付渠道,枚举: |
| 23 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 24 | fenable | 使用状态 | bpchar | 1 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fexchangetype | 金融机构类别 | varchar | 50 |  | √ | '0' | 金融机构类别,枚举: 0 :银行 1 :结算中心 2 :第三方支付机构 |
| 26 | fnumber | 编码 | varchar | 80 |  |  | null | 编码 |
| 27 | fisdefault | 默认 | bpchar | 1 |  |  | null | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_settltype_number |  | fnumber |
| 2 | t_bd_settlementtype_pkey |  | fid |

---

## 结算方式-多语言表 t_bd_settlementtype_l

- **表名称：** 结算方式-多语言表
- **表名：** t_bd_settlementtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fname | 名称 | varchar | 255 |  |  | null | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_settlementtype_l_pkey |  | fpkid |
| 2 | idx_t_bd_settltype_l_fid |  | fid,flocaleid |
