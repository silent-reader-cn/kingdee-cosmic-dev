# 费用标准-er_standard

## 关联标准-多选基础资料表 t_er_relatedstandard

- **表名称：** 关联标准-多选基础资料表
- **表名：** t_er_relatedstandard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 费用标准 er_standard |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_relatedstandard |  | fpkid |
| 2 | idx_er_relatedstandard_seq |  | fid |

---

## 费用标准-主表 t_er_fee_standard

- **表名称：** 费用标准-主表
- **表名：** t_er_fee_standard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fctlnumber | 报销频率 | int4 | 32 |  | √ | 0 | 报销频率 |
| 3 | ftreatway | 招待方式 | varchar | 10 |  | √ | ' ' | 招待方式,枚举: 1 :餐费 2 :酒店住宿 3 :酒水 4 :纪念品 |
| 4 | fstardardtype | 业务事项 | int8 | 64 |  | √ | 0 | 业务事项 er_standard_type |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | factualreimexpense | 实报实销 | bpchar | 1 |  | √ | '0' | 实报实销 |
| 13 | fcostcompany | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | ftreattypebill | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fotherstandamount | 酒水标准（元/次） | numeric | 23 | 10 | √ | 0 | 酒水标准（元/次） |
| 18 | fcity | 城市类别 | varchar | 36 |  | √ | ' ' | 出差地域 er_triparea |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | 报销级别 er_reimburselevel |
| 21 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | ftreatgrade | ftreatgrade | varchar | 20 |  | √ | ' ' |  |
| 25 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 26 | fmeetitem | 会议事项 | varchar | 10 |  | √ | ' ' | 会议事项,枚举: 1 :伙食费 2 :酒店住宿 3 :交通费 4 :其他 |
| 27 | fmeettypebill | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 28 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 29 | fcityareabill | 城市类别 | int8 | 64 |  | √ | 0 | 出差地域 er_triparea |
| 30 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | fmeetgrade | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 32 | fctlperiod | 控制周期 | varchar | 10 |  | √ | ' ' | 控制周期,枚举: week :周 month :月 season :季 year :年 |
| 33 | fotherstand | 酒水标准 | bpchar | 1 |  | √ | '0' | 酒水标准 |
| 34 | fcalcexpr | 计算公式 | varchar | 512 |  | √ | ' ' | 计算公式,枚举: feestandardamt * ( treatnum + escortnum) :标准金额*(分录.招待人数 + 分录.陪同人数) feestandardamt * goodsnum :标准金额* 酒水瓶数 feestandardamt * daysnum * treatnum :标准金额*分录.住宿天数（或分录.会议天数）*分录.招待人数(或分录.参会人数) feestandardamt * treatnum :标准金额*分录.招待人数 feestandardamt :标准金额 feestandardamt * ( treatnum_bill + escortnum_bill) :标准金额*(招待人数 + 陪同人数) feestandardamt * daysnum_bill * treatnum_bill :标准金额*住宿天数（或会议天数）*招待人数(或参会人数) feestandardamt * treatnum_bill :标准金额*招待人数 |
| 35 | fstandardamount | 标准（元/次） | numeric | 23 | 10 | √ | 0 | 标准（元/次） |
| 36 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 37 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 39 | fsummarycontrol | 汇总控制 | bpchar | 1 |  | √ | '0' | 汇总控制 |
| 40 | fmeetgradebill | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 41 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 42 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 43 | fdimension | 业务维度 | varchar | 512 |  | √ | ' ' | 业务维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_fee_standard |  | fid |
| 2 | idx_t_er_fee_standard_master |  | fmasterid |
| 3 | idx_fee_standard_createorg |  | fcreateorgid |
| 4 | idx_t_er_fee_standard_createorg |  | fcreateorgid |

---

## 费用标准-使用范围表 t_er_fee_standard_u

- **表名称：** 费用标准-使用范围表
- **表名：** t_er_fee_standard_u

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
| 1 | idx_t_er_fee_standard_u_uo |  | fuseorgid |
| 2 | pk_t_er_fee_standard_u |  | fdataid,fuseorgid |

---

## 费用标准-多语言表 t_er_fee_standard_l

- **表名称：** 费用标准-多语言表
- **表名：** t_er_fee_standard_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_fee_standard_l_0 |  | fid,flocaleid |
| 2 | pk_t_er_fee_standard_l |  | fpkid |
