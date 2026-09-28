# 计划调整（废弃）-fpm_reportplan_adjust

## 主维度分录-子表 t_fpm_chgreportdatamain

- **表名称：** 主维度分录-子表
- **表名：** t_fpm_chgreportdatamain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountunit | 金额单位 | varchar | 50 |  | √ | ' ' | 金额单位,枚举: |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcompanymemid | 公司成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 5 | feffectflag | 生效状态 | bpchar | 1 |  | √ | '0' | 生效状态 |
| 6 | freportperiod | 编报期间 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 7 | fsettletypememid | 结算方式成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 8 | fsubjectmemid | 科目成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 9 | forigindatarow | 原始表行号 | int4 | 32 |  | √ | 0 | 原始表行号 |
| 10 | fplanamt | 调整前计划额度 | numeric | 23 | 10 | √ | 0 | 调整前计划额度 |
| 11 | fcurrentadjustamt | 本次调整额度 | numeric | 23 | 10 | √ | 0 | 本次调整额度 |
| 12 | fcurrencymemid | 币别成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 13 | fmaintable | 主表标识 | bpchar | 1 |  | √ | '0' | 主表标识 |
| 14 | fperiodmemid | 明细期间成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 15 | frealamt | 已执行额度 | numeric | 23 | 10 | √ | 0 | 已执行额度 |
| 16 | forgmemid | 编报组织成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 17 | fbodysysid | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 18 | fextmem3id | 预留成员3 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 19 | forigindatacol | 原始表列号 | int4 | 32 |  | √ | 0 | 原始表列号 |
| 20 | foriginalreportid | 原报表id | int8 | 64 |  | √ | 0 | 原报表id |
| 21 | fadjustedplanamt | 调整后计划额度 | numeric | 23 | 10 | √ | 0 | 调整后计划额度 |
| 22 | foriginalreportdataid | 原编制数据id | int8 | 64 |  | √ | 0 | 原编制数据id |
| 23 | fextmem1id | 预留成员1 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 24 | fextmem2id | 预留成员2 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | foriginalplanamt | 原始计划额度 | numeric | 23 | 10 | √ | 0 | 原始计划额度 |
| 27 | flockamt | 预占用额度 | numeric | 23 | 10 | √ | 0 | 预占用额度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_chgreportdatamain |  | fentryid |
| 2 | idx_fpm_chgreportdatamain |  | fid |

---

## 额度调整信息分录-子表 t_fpm_adjustamtinfo

- **表名称：** 额度调整信息分录-子表
- **表名：** t_fpm_adjustamtinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustompage1 | 自定义页面维1 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 3 | fadjustsumamtin | 流入科目调整总额 | numeric | 23 | 10 | √ | 0 | 流入科目调整总额 |
| 4 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 5 | fcustompage2 | 自定义页面维2 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 6 | famtunit | 金额单位 | varchar | 50 |  | √ | ' ' | 金额单位,枚举: one :元 thousand :千元 ten_thousand :万元 million :百万元 hundred_million :亿元 |
| 7 | fadjustsumamtout | 流出科目调整总额 | numeric | 23 | 10 | √ | 0 | 流出科目调整总额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fadjustsumamtbal | 余额科目调整总额 | numeric | 23 | 10 | √ | 0 | 余额科目调整总额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_adjustamtinfo |  | fid |
| 2 | pk_t_fpm_adjustamtinfo |  | fentryid |

---

## 计划调整（废弃）-主表 t_fpm_reportplan_adjust

- **表名称：** 计划调整（废弃）-主表
- **表名：** t_fpm_reportplan_adjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | freportperiodid | 编报期间 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 4 | famountunit | 金额单位： | varchar | 50 |  | √ | ' ' | 金额单位：,枚举: one :元 thousand :千元 ten_thousand :万元 million :百万元 hundred_million :亿元 fromparent :沿用主表 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbodysysid | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | freporttypeid | 编报类型 | int8 | 64 |  | √ | 0 | [编报类型设置（废弃） fpm_orgreporttype](../fpm_files/fpm_orgreporttype.md) |
| 12 | fadjustreason | 调整原因 | varchar | 255 |  | √ | ' ' | 调整原因 |
| 13 | foriginalreportids | 原报表id | varchar | 2000 |  | √ | ' ' | 原报表id |
| 14 | fcreatorid | 制单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | freportorgid | 编报主体 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |
| 16 | fadjusttype | 调整类型 | varchar | 50 |  | √ | ' ' | 调整类型,枚举: AMOUNT_WITHIN :额度内调剂 AMOUNT_ADDITIONAL :额度追加 |
| 17 | fpagedimensiontype1 | 页面维1维度类型 | varchar | 30 |  | √ | ' ' | 页面维1维度类型 |
| 18 | fpagedimensiontype2 | 页面维2维度类型 | varchar | 30 |  | √ | ' ' | 页面维2维度类型 |
| 19 | fmainreportid | 主表id | int8 | 64 |  | √ | 0 | 主表id |
| 20 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_adjust_reportperiod |  | freportperiodid |
| 2 | pk_t_fpm_reportplan_adjust |  | fid |
| 3 | idx_adjust_reportorg |  | freportorgid |
| 4 | idx_fpm_reporadjust |  | fbillno |

---

## 明细字段分录-子表 t_fpm_chgreportdatadetail

- **表名称：** 明细字段分录-子表
- **表名：** t_fpm_chgreportdatadetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fdetailext1 | 自定义字段1 | varchar | 255 |  | √ | ' ' | 自定义字段1 |
| 4 | fdetailext4 | 自定义字段4 | varchar | 255 |  | √ | ' ' | 自定义字段4 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcontractname | 合同名称 | varchar | 255 |  | √ | ' ' | 合同名称 |
| 7 | fdetailext5 | 自定义字段5 | varchar | 255 |  | √ | ' ' | 自定义字段5 |
| 8 | fbankcate | 银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 9 | fbankaccount | 本方账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 10 | fdetailext2 | 自定义字段2 | varchar | 255 |  | √ | ' ' | 自定义字段2 |
| 11 | fdetailext3 | 自定义字段3 | varchar | 255 |  | √ | ' ' | 自定义字段3 |
| 12 | fopusername | 对手方名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 13 | fdetailext8 | 自定义字段8 | varchar | 255 |  | √ | ' ' | 自定义字段8 |
| 14 | fmaindimdataid | 主维度数据id | int8 | 64 |  | √ | 0 | 主维度数据id |
| 15 | fcontractno | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 16 | fdetailext6 | 自定义字段6 | varchar | 255 |  | √ | ' ' | 自定义字段6 |
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
| 1 | pk_t_fpm_chgreportdatadetail |  | fentryid |
| 2 | idx_fpm_chgreportdatadetail |  | fid |
