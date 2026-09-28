# 会计政策-cal_bd_calpolicy

## 会计政策-主表 t_cal_calpolicy

- **表名称：** 会计政策-主表
- **表名：** t_cal_calpolicy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fforbiddenid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 6 | fforbiddentime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fsupporttaxamt | 存货核算支持含税金额 | bpchar | 1 |  | √ | '0' | 存货核算支持含税金额 |
| 9 | fcalbysubelement | 按成本子要素核算 | bpchar | 1 |  | √ | '0' | 按成本子要素核算 |
| 10 | fconvertmode | 汇率计算方式 | varchar | 5 |  | √ | ' ' | 汇率计算方式,枚举: A :直接汇率 B :间接汇率 |
| 11 | fremark_tag | fremark_tag | text | 0 |  |  | null |  |
| 12 | fmultifactoryaccount | 多工厂核算 | bpchar | 1 |  | √ | '0' | 多工厂核算 |
| 13 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 14 | fcalbycostelement | 启用分项结转 | bpchar | 1 |  | √ | '0' | 启用分项结转 |
| 15 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fperiodtypeid | 会计日历 | int8 | 64 |  | √ | 0 | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 21 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_calpolicy_number |  | fnumber |
| 2 | t_cal_calpolicy_pkey |  | fid |

---

## 会计政策-多语言表 t_cal_calpolicy_l

- **表名称：** 会计政策-多语言表
- **表名：** t_cal_calpolicy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_calpolicy_l_pkey |  | fpkid |
| 2 | idx_cal_policyl_id |  | fid,flocaleid |
