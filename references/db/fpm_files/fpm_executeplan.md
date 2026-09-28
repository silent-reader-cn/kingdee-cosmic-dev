# 计划执行记录（废弃）-fpm_executeplan

## 计划执行记录（废弃）-主表 t_fpm_executeplan

- **表名称：** 计划执行记录（废弃）-主表
- **表名：** t_fpm_executeplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecuteoperatorstatus | 执行操作状态 | varchar | 30 |  | √ | ' ' | 执行操作状态,枚举: A :初始 C :成功 B :失败 |
| 3 | fratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 4 | fdetailext1 | 自定义字段1 | varchar | 50 |  | √ | ' ' | 自定义字段1 |
| 5 | fcompanymem | 公司 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 6 | fdetailext4 | 自定义字段4 | varchar | 50 |  | √ | ' ' | 自定义字段4 |
| 7 | fdetailext5 | 自定义字段5 | varchar | 50 |  | √ | ' ' | 自定义字段5 |
| 8 | fbankcate | 银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 9 | fdetailext2 | 自定义字段2 | varchar | 50 |  | √ | ' ' | 自定义字段2 |
| 10 | fdetailext3 | 自定义字段3 | varchar | 50 |  | √ | ' ' | 自定义字段3 |
| 11 | fopusername | 对手方名称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fdetailext8 | 自定义字段8 | varchar | 50 |  | √ | ' ' | 自定义字段8 |
| 13 | fdetailext6 | 自定义字段6 | varchar | 50 |  | √ | ' ' | 自定义字段6 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | freportperiod | 编报期间 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 16 | fdetailext7 | 自定义字段7 | varchar | 50 |  | √ | ' ' | 自定义字段7 |
| 17 | fexecutedate | 执行日期 | timestamp | 0 |  |  | null | 执行日期 |
| 18 | frate | 折算汇率 | numeric | 23 | 10 | √ | 0 | 折算汇率 |
| 19 | fplandate | 计划日期 | timestamp | 0 |  |  | null | 计划日期 |
| 20 | freporttype | 编报类型 | int8 | 64 |  | √ | 0 | [编报类型设置（废弃） fpm_orgreporttype](../fpm_files/fpm_orgreporttype.md) |
| 21 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 22 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 23 | fsettletypemem | 结算方式 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 24 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcontractname | 合同名称 | varchar | 50 |  | √ | ' ' | 合同名称 |
| 26 | fdeleteflag | 删除标识 | bpchar | 1 |  | √ | '0' | 删除标识 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fbizbillid | 业务单据id | int8 | 64 |  | √ | 0 | 业务单据id |
| 29 | fplanexecuteop | 计划执行操作 | varchar | 50 |  | √ | ' ' | 计划执行操作,枚举: A :执行数写入 B :执行数删除 C :预占数写入 D :预占释放 E :预占记录删除 F :执行数释放 |
| 30 | freportorg | 编报主体 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 31 | fbodysys | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fcurrencymem | 币别 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 34 | fperiodmem | 明细期间 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 35 | frealamtbase | 执行额度币别基础资料 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 36 | forgmem | 编报组织 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fexectuefailreason | 失败原因 | varchar | 1000 |  | √ | ' ' | 失败原因 |
| 39 | fopusertype | 对手方类型 | varchar | 50 |  | √ | ' ' | 对手方类型,枚举: bos_org :业务单元 bos_user :职员 bd_customer :客户 bd_supplier :供应商 |
| 40 | fmatchedreportdataids | 匹配到的所有报表id | varchar | 1024 |  | √ | ' ' | 匹配到的所有报表id |
| 41 | foldexecuterecordnumber | 原执行记录编号 | varchar | 50 |  | √ | ' ' | 原执行记录编号 |
| 42 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fsubjectmem | 科目 | int8 | 64 |  | √ | 0 | [维度成员模板_计划科目（废弃） fpm_membersubject](../fpm_files/fpm_membersubject.md) |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | frealamt | 执行额度 | numeric | 23 | 10 | √ | 0 | 执行额度 |
| 46 | fcontractno | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 47 | fbusinesspartner | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 48 | fbillmatchrule | 单据匹配策略 | int8 | 64 |  | √ | 0 | [业务取数规则（废弃） fpm_matchrule](../fpm_files/fpm_matchrule.md) |
| 49 | freportdataid | 编制数据id | int8 | 64 |  | √ | 0 | 编制数据id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_execplan_currencymem |  | fcurrencymem |
| 2 | idx_execplan_bodysys |  | fbodysys |
| 3 | pk_t_fpm_executeplan |  | fid |
| 4 | idx_execplan_reportorg |  | freportorg |

---

## 单据体-子表 t_fpm_executeplan_bizinfo

- **表名称：** 单据体-子表
- **表名：** t_fpm_executeplan_bizinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizprop | 业务单据字段 | varchar | 50 |  | √ | ' ' | 业务单据字段 |
| 3 | fbizvalue | 业务单据字段值 | varchar | 2000 |  | √ | ' ' | 业务单据字段值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_executeplan_bizinfo |  | fentryid |
| 2 | idx_fpm_executeplan_bizinfo |  | fid |

---

## 计划执行记录（废弃）-分表 t_fpm_executeplan_e

- **表名称：** 计划执行记录（废弃）-分表
- **表名：** t_fpm_executeplan_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizorg | 业务责任主体 | varchar | 50 |  | √ | ' ' | 业务责任主体 |
| 3 | foriginalrecordid | 原记录id | int8 | 64 |  | √ | 0 | 原记录id |
| 4 | fbizbillamount | 业务金额 | numeric | 23 | 10 | √ | 0 | 业务金额 |
| 5 | fmatcheddimensions | 匹配维度 | varchar | 1024 |  | √ | ' ' | 匹配维度 |
| 6 | fbillbizetype | 业务单据类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fentrytypenumber | 分录字段标识 | varchar | 50 |  | √ | ' ' | 分录字段标识 |
| 8 | fexecuteinfo | 执行环节 | varchar | 50 |  | √ | ' ' | 执行环节 |
| 9 | fmatchdetailfields | 匹配明细字段 | varchar | 1024 |  | √ | ' ' | 匹配明细字段 |
| 10 | frelaterecordid | 关联记录id | int8 | 64 |  | √ | 0 | 关联记录id |
| 11 | faccuratematch | 是否精确匹配 | bpchar | 1 |  | √ | '0' | 是否精确匹配 |
| 12 | fbizbillcurrencytext | 业务单据币别 | varchar | 50 |  | √ | ' ' | 业务单据币别 |
| 13 | fentryid | 分录id | varchar | 50 |  | √ | ' ' | 分录id |
| 14 | fbizbillcode | 业务单据编码 | varchar | 50 |  | √ | ' ' | 业务单据编码 |
| 15 | fentrytypename | 分录字段名 | varchar | 50 |  | √ | ' ' | 分录字段名 |
| 16 | fbizbillcurrency | 业务单据币别基础资料 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_executeplan_e |  | fid |
| 2 | idx_fpm_executeplan_e |  | fentryid |
