# 会计政策-xkbd_policy

## 资产政策信息-子表 t_xkbd_policydepentry

- **表名称：** 资产政策信息-子表
- **表名：** t_xkbd_policydepentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdepremethodid | 折旧方法 | int8 | 64 |  | √ | 0 | 折旧方法 fa_depremethod |
| 3 | fdepreeffect | 变动影响 | varchar | 50 |  | √ | ' ' | 变动影响,枚举: NEXT :影响下期 CUR :影响当期 |
| 4 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 5 | fuseyear | 预计使用年限/预计总工作量 | int4 | 32 |  | √ | 0 | 预计使用年限/预计总工作量 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdeprelimit | 一次性折旧限额 | numeric | 19 | 6 | √ | 0 | 一次性折旧限额 |
| 8 | fdepreconventionid | fdepreconventionid | int8 | 64 |  | √ | 0 |  |
| 9 | fdecpolicyid | 减值政策 | varchar | 50 |  | √ | ' ' | 减值政策,枚举: 1 :不减值 2 :减值，可转回（限额：累计减值） 4 :减值，可转回（限额：账面价值） 3 :减值，不可转回 |
| 10 | fdepretime | 计提时点 | varchar | 50 |  | √ | ' ' | 计提时点,枚举: CLEAR :次月 NEW :当月 NEXT_DAY :次日 NEW_AND_CLEAR :当日 NEXT_YEAR :次年 THIS_YEAR :当年 FIRST_YEAR_CONVEN :首年常规 |
| 11 | fdeprepolicyid | fdeprepolicyid | int8 | 64 |  | √ | 0 |  |
| 12 | fnetresidualvalrate | 净残值率(%) | numeric | 19 | 6 | √ | 0 | 净残值率(%) |
| 13 | fnodepre | 不提折旧 | bpchar | 1 |  | √ | '0' | 不提折旧 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fisallowdeduction | fisallowdeduction | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbd_policydepentry |  | fentryid |
| 2 | idx_xkbd_policyentry_fid |  | fid |

---

## 会计政策-多语言表 t_xkbd_policy_l

- **表名称：** 会计政策-多语言表
- **表名：** t_xkbd_policy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbd_policy_flocaleid |  | fid,flocaleid |
| 2 | pk_xkbd_policy_l |  | fpkid |

---

## 会计政策-主表 t_xkbd_policy

- **表名称：** 会计政策-主表
- **表名：** t_xkbd_policy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fforbiddenid | fforbiddenid | int8 | 64 |  | √ | 0 |  |
| 3 | fforbiddentime | fforbiddentime | timestamp | 0 |  |  | null |  |
| 4 | fsupporttaxamt | 存货核算支持含税金额 | bpchar | 1 |  | √ | '0' | 存货核算支持含税金额 |
| 5 | fcalbysubelement | 按成本子要素核算 | bpchar | 1 |  | √ | '0' | 按成本子要素核算 |
| 6 | fconvertmode | 汇率计算方式 | varchar | 5 |  | √ | ' ' | 汇率计算方式,枚举: A :直接汇率 B :间接汇率 |
| 7 | ffapolicyid | 资产政策内码 | int8 | 64 |  | √ | 0 | 资产政策内码 |
| 8 | fispreset | fispreset | bpchar | 1 |  | √ | '0' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 14 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 15 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 16 | fissyspreset | 预置数据 | bpchar | 1 |  | √ | '0' | 预置数据 |
| 17 | fdepreuseid | 折旧用途内码 | int8 | 64 |  | √ | 0 | 折旧用途内码 |
| 18 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 19 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 20 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fmultifactoryaccount | 多工厂核算 | bpchar | 1 |  | √ | '0' | 多工厂核算 |
| 24 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 25 | fcalbycostelement | 启用分项结转 | bpchar | 1 |  | √ | '0' | 启用分项结转 |
| 26 | fctrlstrategy | fctrlstrategy | varchar | 30 |  | √ | '5' |  |
| 27 | fcalpolicyid | 核算政策内码 | int8 | 64 |  | √ | 0 | 核算政策内码 |
| 28 | fperiodtypeid | 会计日历 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 29 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 31 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 32 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_xkbd_policy_master |  | fmasterid |
| 2 | pk_xkbd_policy |  | fid |
| 3 | idx_xkbd_policy_fnumber |  | fnumber |
| 4 | idx_t_xkbd_policy_createorg |  | fcreateorgid |
