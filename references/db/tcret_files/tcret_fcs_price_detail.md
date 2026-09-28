# 从价计征房产税申报明细-tcret_fcs_price_detail

## 从价计征房产税申报明细-主表 t_tcret_fcs_price_detail

- **表名称：** 从价计征房产税申报明细-主表
- **表名：** t_tcret_fcs_price_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapanage | 属地管理名称 | varchar | 50 |  | √ | ' ' | 属地管理名称 |
| 3 | ftaxauthority | 主管税务机关 | varchar | 50 |  | √ | ' ' | 主管税务机关 |
| 4 | fassertvalue | 房产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 房产原值 |
| 5 | fdeclaremonth | 申报月份 | varchar | 50 |  | √ | ' ' | 申报月份 |
| 6 | ftaxrate | 计税比例 | numeric | 23 | 10 | √ | 0.0000000000 | 计税比例 |
| 7 | ftaxratio | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 8 | ftaxlimit | 纳税期限 | varchar | 30 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 year :按年申报 halfyear :半年申报 false :—— |
| 9 | fsourceid | 税源数据ID | int8 | 64 |  | √ | 0 | 税源数据ID |
| 10 | fcurrentpayable | 本期应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应纳税额 |
| 11 | fisshowfcsbyprice | 是否展示从价计征房产税 | bpchar | 1 |  | √ | ' ' | 是否展示从价计征房产税 |
| 12 | fissuitableforsmall | 是否适用增值税小规模纳税人减征政策 | varchar | 30 |  | √ | ' ' | 是否适用增值税小规模纳税人减征政策,枚举: 1 :是 0 :否 |
| 13 | fbuildingcode | 房产编号 | varchar | 50 |  | √ | ' ' | 房产编号 |
| 14 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 15 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 17 | frentalvalue | 其中出租房产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 其中出租房产原值 |
| 18 | frowno | 数据编号 | int8 | 64 |  | √ | 0 | 数据编号 |
| 19 | fcurrentjmamount | 本期减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期减免税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcret_fcs_price_detail_pkey |  | fid |
| 2 | idx_tcret_fcs_price_detail |  | fskssqq,fskssqz,forg |

---

## 单据体-子表 t_tcret_price_det_entry

- **表名称：** 单据体-子表
- **表名：** t_tcret_price_det_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 减免性质代码名称 | varchar | 100 |  | √ | ' ' | 减免性质代码名称 |
| 3 | fjmcodeid | 减免性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 4 | fjmamount | 减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税额 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | famount | 减免房产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 减免房产原值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcode | 减免性质代码文本 | varchar | 50 |  | √ | ' ' | 减免性质代码文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_price_det_entry_fk |  | fid |
| 2 | pk_tcret_price_det_entry |  | fentryid |
