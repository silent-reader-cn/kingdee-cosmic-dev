# 日均消耗统计方案-invp_dailyavgcomsumption

## 日均消耗统计方案-使用范围表 t_invp_dailycomsumption_u

- **表名称：** 日均消耗统计方案-使用范围表
- **表名：** t_invp_dailycomsumption_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_dailycomsumption_u |  | fdataid,fuseorgid |
| 2 | idx_t_invp_dailycomsumption_u_uo |  | fuseorgid |

---

## 统计周期-子表 t_invp_dailyconsumestats

- **表名称：** 统计周期-子表
- **表名：** t_invp_dailyconsumestats

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenddate | 结束天数 | int8 | 64 |  | √ | 0 | 结束天数 |
| 3 | fbegindate | 开始天数 | int8 | 64 |  | √ | 0 | 开始天数 |
| 4 | fselectrule | fselectrule | varchar | 200 |  | √ | ' ' |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ffactor | 权数 | numeric | 23 | 2 | √ | 0 | 权数 |
| 7 | fselectruleformula_tag | fselectruleformula_tag | text | 0 |  |  | null |  |
| 8 | fbasedatetype | 基准类型 | varchar | 50 |  | √ | ' ' | 基准类型,枚举: A :运算日期 B :N年同期 |
| 9 | fselectruleformula | fselectruleformula | varchar | 512 |  | √ | ' ' |  |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fdateselector | N年前 | int8 | 64 |  | √ | 0 | N年前 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_dailyconsumestats |  | fentryid |
| 2 | idx_invp_dailyconsumestats_fid |  | fid |

---

## 日均消耗统计方案-多语言表 t_invp_dailycomsumption_l

- **表名称：** 日均消耗统计方案-多语言表
- **表名：** t_invp_dailycomsumption_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_dailycomsumption_l |  | fid,flocaleid |
| 2 | pk_invp_dailycomsumption_l |  | fpkid |

---

## 异常波动数据过滤-子表 t_invp_dailyconsumefilter

- **表名称：** 异常波动数据过滤-子表
- **表名：** t_invp_dailyconsumefilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprerulejson_tag | 前置条件（json）_详情 | text | 0 |  |  | null | 前置条件（json）_详情 |
| 3 | foverpercent | 高于均值百分比 | numeric | 23 | 4 | √ | 0 | 高于均值百分比 |
| 4 | fprerulejson | 前置条件（json） | varchar | 512 |  | √ | ' ' | 前置条件（json） |
| 5 | fprerule | 前置条件 | varchar | 512 |  | √ | ' ' | 前置条件 |
| 6 | fpreruleformula_tag | 前置条件（表达式）_详情 | text | 0 |  |  | null | 前置条件（表达式）_详情 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | funderpercent | 低于均值百分比 | numeric | 23 | 4 | √ | 0 | 低于均值百分比 |
| 9 | fsrcentity | fsrcentity | varchar | 36 |  | √ | ' ' |  |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fpreruleformula | 前置条件（表达式） | varchar | 512 |  | √ | ' ' | 前置条件（表达式） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_dailyconsumefilter_fid |  | fid |
| 2 | pk_invp_dailyconsumefilter |  | fentryid |

---

## 日均消耗统计方案-主表 t_invp_dailycomsumption

- **表名称：** 日均消耗统计方案-主表
- **表名：** t_invp_dailycomsumption

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpluginclass | 插件 | varchar | 200 |  | √ | ' ' | 插件 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | finvlevelfield | 日均消耗量字段 | varchar | 50 |  | √ | ' ' | 日均消耗量字段 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | finvlevel | finvlevel | int8 | 64 |  | √ | 0 |  |
| 11 | fadjustfactor | 调整系数 | numeric | 23 | 2 | √ | 0 | 调整系数 |
| 12 | fplangroupid | 计划组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fupdatetype | 日均消耗记录更新方式 | varchar | 50 |  | √ | ' ' | 日均消耗记录更新方式,枚举: A :追加 B :覆盖 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fmatchdimension | 匹配维度映射 | int8 | 64 |  | √ | 0 | 匹配映射配置 invp_matchmapping_config |
| 21 | fselectrulejson | 取数条件（json） | varchar | 512 |  | √ | ' ' | 取数条件（json） |
| 22 | fplannerid | 计划员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fmainplantype | 计划类型 | varchar | 10 |  | √ | ' ' | 计划类型,枚举: A :再订货点 B :最大最小 D :固定期间 |
| 25 | fselectrulejson_tag | 取数条件（json）_详情 | text | 0 |  |  | null | 取数条件（json）_详情 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fselectruleformula_tag | 取数条件（表达式）_详情 | text | 0 |  |  | null | 取数条件（表达式）_详情 |
| 28 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 29 | fconsumptionmodel | 日均消耗模型 | int8 | 64 |  | √ | 0 | 资源注册模型 invp_model_register |
| 30 | finvlevelfieldkey | 日均消耗量字段（标识） | varchar | 50 |  | √ | ' ' | 日均消耗量字段（标识） |
| 31 | fselectruleformula | 取数条件（表达式） | varchar | 512 |  | √ | ' ' | 取数条件（表达式） |
| 32 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 33 | fdimension | 库存水位维度 | int8 | 64 |  | √ | 0 | 库存水位维度 msplan_plan_dimension |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_dailycomsumption |  | fid |
| 2 | idx_invp_dailycomsumption_fnum |  | fnumber |
| 3 | idx_t_invp_dailycomsumption_createorg |  | fcreateorgid |
| 4 | idx_t_invp_dailycomsumption_master |  | fmasterid |

---

## 业务组织-多选基础资料表 t_invp_consschemeorg

- **表名称：** 业务组织-多选基础资料表
- **表名：** t_invp_consschemeorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_consscheme_org |  | fid |
| 2 | pk_t_invp_consschemeorg |  | fpkid |
