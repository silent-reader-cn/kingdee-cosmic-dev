# 编报进度管理（废弃）-fpm_report_process

## 主维度分录-子表 t_fpm_reportdatamain

- **表名称：** 主维度分录-子表
- **表名：** t_fpm_reportdatamain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountunit | 金额单位 | varchar | 50 |  | √ | ' ' | 金额单位,枚举: |
| 3 | fsourceid | 数据来源id | varchar | 255 |  | √ | ' ' | 数据来源id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcompanymemid | 公司成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 6 | fsourceid_tag | 数据来源id_详情 | text | 0 |  |  | null | 数据来源id_详情 |
| 7 | feffectflag | 生效状态 | bpchar | 1 |  | √ | '0' | 生效状态 |
| 8 | freportperiod | 编报期间 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 9 | fsettletypememid | 结算方式成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 10 | fsubjectmemid | 科目成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 11 | forigindatarow | 原始表行号 | int4 | 32 |  | √ | 0 | 原始表行号 |
| 12 | forgplanamt | 原始计划数 | numeric | 23 | 10 | √ | 0 | 原始计划数 |
| 13 | fplanamt | 计划数 | numeric | 23 | 10 | √ | 0 | 计划数 |
| 14 | fversion | 版本号 | int4 | 32 |  | √ | 0 | 版本号 |
| 15 | fplanreferenceamt | 计划参考值 | numeric | 23 | 10 | √ | 0 | 计划参考值 |
| 16 | fcurrencymemid | 币别成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 17 | fmaintable | 主表标识 | bpchar | 1 |  | √ | '0' | 主表标识 |
| 18 | fperiodmemid | 明细期间成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 19 | frealamt | 实际数 | numeric | 23 | 10 | √ | 0 | 实际数 |
| 20 | forgmemid | 编报组织成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 21 | fextmem3id | 预留成员3 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 22 | forigindatacol | 原始表列号 | int4 | 32 |  | √ | 0 | 原始表列号 |
| 23 | fextmem1id | 预留成员1 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 24 | fextmem2id | 预留成员2 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 25 | fsystemid | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | flockamt | 预占数 | numeric | 23 | 10 | √ | 0 | 预占数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_reportdatamain |  | fid |
| 2 | pk_t_fpm_reportdatamain |  | fentryid |

---

## 期间列表-多选基础资料表 t_fpm_report_period

- **表名称：** 期间列表-多选基础资料表
- **表名：** t_fpm_report_period

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fpm_report_period |  | fid |
| 2 | pk_t_fpm_report_period |  | fpkid |

---

## 明细字段分录-子表 t_fpm_reportdatadetail

- **表名称：** 明细字段分录-子表
- **表名：** t_fpm_reportdatadetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fbankaccountid | 本方账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 4 | fdetailext1 | 自定义字段1 | varchar | 255 |  | √ | ' ' | 自定义字段1 |
| 5 | fopuserid | 对手方名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 6 | fdetailext4 | 自定义字段4 | varchar | 255 |  | √ | ' ' | 自定义字段4 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcontractname | 合同名称 | varchar | 255 |  | √ | ' ' | 合同名称 |
| 9 | fdetailext5 | 自定义字段5 | varchar | 255 |  | √ | ' ' | 自定义字段5 |
| 10 | fdetailext2 | 自定义字段2 | varchar | 255 |  | √ | ' ' | 自定义字段2 |
| 11 | fdetailext3 | 自定义字段3 | varchar | 255 |  | √ | ' ' | 自定义字段3 |
| 12 | fdetailext8 | 自定义字段8 | varchar | 255 |  | √ | ' ' | 自定义字段8 |
| 13 | fmaindimdataid | 主维度数据ID | int8 | 64 |  | √ | 0 | 主维度数据ID |
| 14 | fcontractno | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 15 | fdetailext6 | 自定义字段6 | varchar | 255 |  | √ | ' ' | 自定义字段6 |
| 16 | fbankcateid | 银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 17 | fdetailext7 | 自定义字段7 | varchar | 255 |  | √ | ' ' | 自定义字段7 |
| 18 | fbusinesspartner | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 19 | fplandate | 计划日期 | timestamp | 0 |  |  | null | 计划日期 |
| 20 | fopusertype | 对手方类型 | varchar | 100 |  | √ | ' ' | 对手方类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :业务单元 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_reportdatadetail |  | fentryid |
| 2 | idx_fpm_reportdatadetail |  | fid |

---

## 编报进度管理（废弃）-主表 t_fpm_report

- **表名称：** 编报进度管理（废弃）-主表
- **表名：** t_fpm_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | ftemplatebakid | 资金计划模板备份表 | int8 | 64 |  | √ | 0 | [资金计划模板备份表（废弃） fpm_template_bak](../fpm_files/fpm_template_bak.md) |
| 4 | freferenceperiod | 参考期间 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 5 | finformant | 填报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fattachinfo | 关联附件信息 | int8 | 64 |  | √ | 0 | [报表附件（废弃） fpm_reportattachment](../fpm_files/fpm_reportattachment.md) |
| 7 | fdeclaredeadline | 申报截止时间 | timestamp | 0 |  |  | null | 申报截止时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdeclarestartdate | 申报开始日期 | timestamp | 0 |  |  | null | 申报开始日期 |
| 10 | freportperiod | 编报期间 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 11 | frollnum | 滚动期数 | int4 | 32 |  | √ | 0 | 滚动期数 |
| 12 | fchangestatus | 调整状态 | varchar | 50 |  | √ | 'unchange' | 调整状态,枚举: unchange :计划未调整 changing :计划调整中 changed :计划已调整 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | 报表名称 | varchar | 50 |  | √ | ' ' | 报表名称 |
| 17 | fparenttemplateid | 资金计划父模板 | int8 | 64 |  | √ | 0 | [资金计划模板（废弃） fpm_template](../fpm_files/fpm_template.md) |
| 18 | ftemplateid | 资金计划模板 | int8 | 64 |  | √ | 0 | [资金计划模板（废弃） fpm_template](../fpm_files/fpm_template.md) |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 23 | fplanstatus | 计划状态 | varchar | 30 |  | √ | ' ' | 计划状态,枚举: A :未生效 B :已生效 |
| 24 | finitflag | 初始化标识 | bpchar | 1 |  | √ | '0' | 初始化标识 |
| 25 | fexchangeratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 26 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 27 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 28 | freportorg | 编报主体 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 29 | fbodysys | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fcurrprocessor | 当前处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_report |  | fbillno |
| 2 | idx_reportperiod |  | freportperiod |
| 3 | idx_reportorg |  | freportorg |
| 4 | pk_t_fpm_report |  | fid |

---

## 编报进度管理（废弃）-多语言表 t_fpm_report_l

- **表名称：** 编报进度管理（废弃）-多语言表
- **表名：** t_fpm_report_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_report_l |  | fpkid |
| 2 | idx_fpm_report_l |  | fid |

---

## 币别范围-多选基础资料表 t_fpm_report_currency

- **表名称：** 币别范围-多选基础资料表
- **表名：** t_fpm_report_currency

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_report_currency |  | fpkid |
| 2 | pk_fpm_report_currency_fid |  | fid |
