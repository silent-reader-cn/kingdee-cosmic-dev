# 经营账簿-xkoac_operatingbook

## 经营账簿-多语言表 t_xkoac_operatingbook_l

- **表名称：** 经营账簿-多语言表
- **表名：** t_xkoac_operatingbook_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_operatingbook_l |  | fpkid |
| 2 | idx_xkoac_operatingbook_l |  | fid,flocaleid |

---

## 经营账簿-主表 t_xkoac_operatingbook

- **表名称：** 经营账簿-主表
- **表名：** t_xkoac_operatingbook

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fstartperiod | 启用期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | finitstatus | 是否结束初始化 | bpchar | 1 |  | √ | '0' | 是否结束初始化,枚举: 0 :未结束 1 :已结束 |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fcurperiod | 当前期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | forgstructureid | 经营组织架构 | int8 | 64 |  | √ | 0 | 经营组织架构 xkoac_orgsystemgroup |
| 15 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 19 | faccounttableid | 经营科目表 | int8 | 64 |  | √ | 0 | 经营科目表 xkoac_accounttable |
| 20 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 21 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | '5' |  |
| 22 | fperiodtypeid | 经营会计日历 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 23 | fdisableperson | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fvchbalance | fvchbalance | bpchar | 1 |  | √ | '0' |  |
| 25 | fenable | 禁用状态 | bpchar | 1 |  | √ | '1' | 禁用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 27 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 28 | fcurrencyid | 记账本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | faccountingpurpose | 经营流水账核算模式 | bpchar | 1 |  | √ | '1' | 经营流水账核算模式,枚举: 1 :经营损益模式 2 :资产负债模式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_operatingbook |  | fid |
| 2 | idx_xkoac_operatingbook |  | fnumber |
