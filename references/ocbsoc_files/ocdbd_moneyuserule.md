# 资金使用规则-ocdbd_moneyuserule

## 资金账户-多选基础资料表 t_ocdbd_accounttypes

- **表名称：** 资金账户-多选基础资料表
- **表名：** t_ocdbd_accounttypes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_accounttypes |  | fpkid |
| 2 | idx_ocdbd_accounttypes |  | fid,fbasedataid |

---

## 资金使用规则-多语言表 t_ocdbd_moneyuserule_l

- **表名称：** 资金使用规则-多语言表
- **表名：** t_ocdbd_moneyuserule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_moneyuserule_l |  | fpkid |
| 2 | idx_ocdbd_moneyuserulel_flid |  | fid,flocaleid |

---

## 特殊使用条件-子表 t_ocdbd_moneyuserule_e

- **表名称：** 特殊使用条件-子表
- **表名：** t_ocdbd_moneyuserule_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 条件类型 | bpchar | 1 |  | √ | '1' | 条件类型,枚举: 1 :按条件使用 0 :不允许使用 |
| 3 | famountrateentry | 使用比例 | numeric | 23 | 10 | √ | 0 | 使用比例 |
| 4 | forderchannelid | 渠道编码 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 5 | feffectivedate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | forderamountentry | 订单金额>= | numeric | 23 | 10 | √ | 0 | 订单金额>= |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fexpirationdate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 10 | fcustomerid | 客户ID | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_moneyuserule_e |  | fentryid |
| 2 | idx_ocdbd_moneyrulee_fid |  | fid |

---

## 资金使用规则-主表 t_ocdbd_moneyuserule

- **表名称：** 资金使用规则-主表
- **表名：** t_ocdbd_moneyuserule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | forderamountrate | 使用比例 | numeric | 23 | 10 | √ | 0 | 使用比例 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | forderamount | 订单金额>= | numeric | 23 | 10 | √ | 0 | 订单金额>= |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_moneyuserule |  | fid |
| 2 | idx_ocdbd_moneyuserule_num |  | fnumber |
