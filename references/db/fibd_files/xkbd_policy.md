# 会计政策-xkbd_policy

## 资产政策信息-子表 t_xkbd_policydepentry

- **表名称：** 资产政策信息-子表
- **表名：** t_xkbd_policydepentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdepremethodid | 折旧方法 | int8 | 64 |  | √ | 0 | [折旧方法 fa_depremethod](../fa_files/fa_depremethod.md) |
| 3 | fdepreeffect | 变动影响 | varchar | 50 |  | √ | ' ' | 变动影响,枚举: NEXT :影响下期 CUR :影响当期 |
| 4 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 5 | fuseyear | 预计使用年限/预计总工作量 | numeric | 19 | 6 | √ | 0 | 预计使用年限/预计总工作量 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdeprelimit | 一次性折旧限额 | numeric | 19 | 6 | √ | 0 | 一次性折旧限额 |
| 8 | fdepreconventionid | fdepreconventionid | int8 | 64 |  | √ | 0 |  |
| 9 | fdecpolicyid | 减值政策 | varchar | 50 |  | √ | ' ' | 减值政策,枚举: 1 :不减值 2 :减值可转回（限额：累计减值） 4 :减值可转回（限额：账面价值） 3 :减值不可转回 |
| 10 | fdepretime | 计提时点 | varchar | 50 |  | √ | ' ' | 计提时点,枚举: CLEAR :次月 NEW :当月 NEXT_DAY :次日 NEW_AND_CLEAR :当日 NEXT_YEAR :次年 THIS_YEAR :当年 FIRST_YEAR_CONVEN :首年常规 NEW_CLEAR :新增和清理当期均提折旧 |
| 11 | fusedatedepre | 新增和清理当期按天计算折旧 | bpchar | 1 |  | √ | '0' | 新增和清理当期按天计算折旧 |
| 12 | fdeprepolicyid | fdeprepolicyid | int8 | 64 |  | √ | 0 |  |
| 13 | fnetresidualvalrate | 净残值率(%) | numeric | 19 | 6 | √ | 0 | 净残值率(%) |
| 14 | fnodepre | 不提折旧 | bpchar | 1 |  | √ | '0' | 不提折旧 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fisallowdeduction | fisallowdeduction | bpchar | 1 |  | √ | '0' |  |

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
| 2 | fremark | 描述 | varchar | 500 |  |  | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 500 |  |  | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbd_policy_l |  | fpkid |
| 2 | idx_xkbd_policy_flocaleid |  | fid,flocaleid |

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
| 8 | fisrevaluate | 允许重估 | bpchar | 1 |  | √ | '0' | 允许重估 |
| 9 | fispreset | fispreset | bpchar | 1 |  | √ | '0' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 15 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 16 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 17 | fissyspreset | 预置数据 | bpchar | 1 |  | √ | '0' | 预置数据 |
| 18 | fdepreuseid | 折旧用途内码 | int8 | 64 |  | √ | 0 | 折旧用途内码 |
| 19 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 20 | fremark | 描述 | varchar | 500 |  |  | ' ' | 描述 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fname | 名称 | varchar | 500 |  |  | ' ' | 名称 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fmultifactoryaccount | 多工厂核算 | bpchar | 1 |  | √ | '0' | 多工厂核算 |
| 25 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 26 | fcalbycostelement | 启用分项结转 | bpchar | 1 |  | √ | '0' | 启用分项结转 |
| 27 | frevaluationruleid | 重估规则 | int8 | 64 |  | √ | 0 | [重估规则 fa_revaluationrule](../fa_files/fa_revaluationrule.md) |
| 28 | fctrlstrategy | fctrlstrategy | varchar | 30 |  | √ | '5' |  |
| 29 | fcalpolicyid | 核算政策内码 | int8 | 64 |  | √ | 0 | 核算政策内码 |
| 30 | fperiodtypeid | 会计日历 | int8 | 64 |  | √ | 0 | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 31 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 33 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 34 | fenableabroadpolicy | 适用会计准则 | varchar | 10 |  | √ | 'NO' | 适用会计准则,枚举: NO :中国/国际会计准则 VN :越南会计准则 Thailand :泰国会计准则 |
| 35 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 36 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

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
