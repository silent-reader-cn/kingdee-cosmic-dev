# 信用重算日志-ccm_recalculaterecord

## 重算结果-子表 t_ccm_recalresultentry

- **表名称：** 重算结果-子表
- **表名：** t_ccm_recalresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | farchiveid | 信用档案ID | int8 | 64 |  | √ | 0 | 信用档案ID |
| 3 | fnewbalance | 重算后余额 | numeric | 23 | 10 | √ | 0 | 重算后余额 |
| 4 | forgscope | 控制组织范围 | varchar | 30 |  | √ | ' ' | 控制组织范围,枚举: GLOBAL :集团范围 SINGLE :业务组织范围 |
| 5 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | foldreducesum | 重算前占用 | numeric | 23 | 10 | √ | 0 | 重算前占用 |
| 8 | fquota | 信用额度(初始额度) | numeric | 23 | 10 | √ | 0 | 信用额度(初始额度) |
| 9 | foldbalance | 重算前余额 | numeric | 23 | 10 | √ | 0 | 重算前余额 |
| 10 | froleid0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 11 | froleid2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 12 | foldincreasesum | 重算前返还 | numeric | 23 | 10 | √ | 0 | 重算前返还 |
| 13 | froleid1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 14 | froleid3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 15 | fdimensionvalue | 维度取值 | varchar | 255 |  | √ | ' ' | 维度取值 |
| 16 | fscheme | 信控方案 | int8 | 64 |  | √ | 0 | [信用控制方案 ccm_schemes](../ccm_files/ccm_schemes.md) |
| 17 | fquotatype | 额度类型 | varchar | 30 |  | √ | ' ' | 额度类型,枚举: amount :信用额度 qty :信用数量 days :信用天数 overdueamt :逾期额度 |
| 18 | fnewincreasesum | 重算后返还 | numeric | 23 | 10 | √ | 0 | 重算后返还 |
| 19 | fnewreducesum | 重算后占用 | numeric | 23 | 10 | √ | 0 | 重算后占用 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_recalresultentry |  | fentryid |
| 2 | idx_ccm_recalretety_id |  | fid |

---

## 信用重算日志-主表 t_ccm_recalresult

- **表名称：** 信用重算日志-主表
- **表名：** t_ccm_recalresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frecalculatorid | 重算人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmessage | 重算结果 | varchar | 1024 |  | √ | ' ' | 重算结果 |
| 4 | frecaltype | 重算类型 | varchar | 30 |  | √ | ' ' | 重算类型,枚举: recal :重算 init :初始化 |
| 5 | fbegindate | 重算起始日期 | timestamp | 0 |  |  | null | 重算起始日期 |
| 6 | fdimensionid | 维度 | int8 | 64 |  | √ | 0 | [信控维度 ccm_dimension](../ccm_files/ccm_dimension.md) |
| 7 | froletype2 | 维度成员类型2 | varchar | 80 |  | √ | ' ' | 维度成员类型2,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_operator :业务员 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 8 | froletype3 | 维度成员类型3 | varchar | 80 |  | √ | ' ' | 维度成员类型3,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_operator :业务员 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 9 | frecalenddate | 重算完成时间 | timestamp | 0 |  |  | null | 重算完成时间 |
| 10 | froletype0 | 维度成员类型0 | varchar | 80 |  | √ | ' ' | 维度成员类型0,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_operator :业务员 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 11 | froletype1 | 维度成员类型1 | varchar | 80 |  | √ | ' ' | 维度成员类型1,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_operator :业务员 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 12 | finitdate | finitdate | timestamp | 0 |  |  | null |  |
| 13 | fsessionid | 重算线程ID | varchar | 100 |  | √ | ' ' | 重算线程ID |
| 14 | frecalstatus | 重算状态 | varchar | 20 |  | √ | ' ' | 重算状态,枚举: A :重算进行中 B :重算完成 C :重算失败 |
| 15 | fbillno | 重算记录号 | varchar | 80 |  | √ | ' ' | 重算记录号 |
| 16 | frecalculatedate | 重算时间 | timestamp | 0 |  |  | null | 重算时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_recalret_date |  | frecalculatedate |
| 2 | pk_ccm_recalresult |  | fid |

---

## 组织共享范围-多选基础资料表 t_ccm_recalresult_org

- **表名称：** 组织共享范围-多选基础资料表
- **表名：** t_ccm_recalresult_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_recalresult_org |  | fpkid |
| 2 | idx_ccm_recalresult_org |  | fentryid |
