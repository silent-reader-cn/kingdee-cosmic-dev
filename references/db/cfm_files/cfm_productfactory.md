# 融资模型-cfm_productfactory

## 融资模型-分表 t_cfm_productfactory_e

- **表名称：** 融资模型-分表
- **表名：** t_cfm_productfactory_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fiscandefer | 允许展期 | bpchar | 1 |  | √ | '0' | 允许展期 |
| 3 | fdefermaxcount | 展期最大次数 | int4 | 32 |  | √ | 0 | 展期最大次数 |
| 4 | fgraceadjustrule | 宽限期节假日规则 | varchar | 30 |  | √ | ' ' | 宽限期节假日规则,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 5 | fintcalmethod | 利息计算方法 | varchar | 30 |  | √ | ' ' | 利息计算方法,枚举: totalcallint :积数计息法 onecallint :逐笔计息法（按日） periodcallint :逐笔计息法（按期） compcallint :余额复利法 |
| 6 | fpostpositiontype | 后置类型 | varchar | 30 |  | √ | ' ' | 后置类型,枚举: standard :标准后置 lookback :利率回溯 |
| 7 | fcapitalgracedays | 本金宽限天数 | int4 | 32 |  | √ | 0 | 本金宽限天数 |
| 8 | fgracecallintmode | 宽限期计息方式 | varchar | 30 |  | √ | ' ' | 宽限期计息方式,枚举: noint :宽限期不计息 int :按正常利率计息 |
| 9 | fissofrrate | SOFR类利率 | bpchar | 1 |  | √ | '0' | SOFR类利率 |
| 10 | flookbacktype | 利率回溯类型 | varchar | 30 |  | √ | ' ' | 利率回溯类型,枚举: noobserve :无观察期转换 observe :观察期转换 |
| 11 | fequaldealrule | fequaldealrule | varchar | 30 |  | √ | ' ' |  |
| 12 | frateresetcycle | 利率重置周期 | varchar | 30 |  | √ | ' ' | 利率重置周期,枚举: D :按天 W :按周 M :按月 |
| 13 | fiscallcompint | 复利计息 | bpchar | 1 |  | √ | '0' | 复利计息 |
| 14 | fintheadtailrule | 计息头尾规则 | varchar | 30 |  | √ | ' ' | 计息头尾规则,枚举: headnotail :算头不算尾 noheadtail :算尾不算头 headtail :算头又算尾 noheadnotail :头尾都不算 |
| 15 | fsettleintmode | 结息方式 | varchar | 30 |  | √ | ' ' | 结息方式,枚举: ykx :预扣息 lsbq :利随本清 gdpljx :固定频率结息 |
| 16 | fcompintadjustway | 复利利率浮动方式 | varchar | 30 |  | √ | ' ' | 复利利率浮动方式,枚举: nofloat :不浮动 valuefloat :按值浮动 percentfloat :按百分比浮动 |
| 17 | frateresetdays | 利率重置偏移（d） | int4 | 32 |  | √ | 0 | 利率重置偏移（d） |
| 18 | frateresetcycleday | 利率重置周期偏移 | int4 | 32 |  | √ | 0 | 利率重置周期偏移 |
| 19 | fiscanoverterm | 允许展期期限超过贷款期限 | bpchar | 1 |  | √ | '0' | 允许展期期限超过贷款期限 |
| 20 | fiscallint | 计息 | bpchar | 1 |  | √ | '0' | 计息 |
| 21 | fintgracedays | 利息宽限天数 | int4 | 32 |  | √ | 0 | 利息宽限天数 |
| 22 | fisprovision | 计提 | bpchar | 1 |  | √ | '0' | 计提 |
| 23 | fisgraceperiod | 有宽限期 | bpchar | 1 |  | √ | '0' | 有宽限期 |
| 24 | fcalcintway | 计息方式 | varchar | 30 |  | √ | 'forward' | 计息方式,枚举: forward :前瞻法 postposition :后顾后置法 |
| 25 | frepaymentmode | 还款方式 | varchar | 30 |  | √ | ' ' | 还款方式,枚举: bqhblsbq :到期还本，利随本清 dqhblsbq :定期还本，利随本清 bqhbdqhx :到期还本，定期还息 dqhbdqhx :定期还本，定期还息 debx :等额本息 debj :等额本金 dbdx :等本等息 zdyhk :自定义还款 |
| 26 | fbasis | 计息基准 | varchar | 30 |  | √ | ' ' | 计息基准,枚举: Actual_actual :Actual/actual SIA_30_360 :30/360(SIA) Actual_360 :Actual/360 Actual_365 :Actual/365 BMA_30_360 :30/360(BMA) ISDA_30_360 :30/360(ISDA) European_30_360 :30/360(European) Japanese_Actual_365 :Actual/365(Japanese) ICMA_Actual_actual :Actual/actual(ICMA) ICMA_Actual_360 :Actual/360(ICMA) ICMA_Actual_365 :Actual/365(ICMA) ICMA_30_360 :30/360E(ICMA) ISDA_Actual_365 :Actual/365(ISDA) BUS_252 :BUS/252 |
| 27 | floanexpireadjustrule | 贷款还款节假日规则 | varchar | 30 |  | √ | ' ' | 贷款还款节假日规则,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 28 | fintcapitalrule | 计息本金规则 | varchar | 30 |  | √ | ' ' | 计息本金规则,枚举: loanbal :贷款余额 Loanamt :放款金额 |
| 29 | frateadjustmethod | 利率重置方式 | varchar | 30 |  | √ | ' ' | 利率重置方式,枚举: deadline :即时重置 cycle :周期性重置 hand :手工重置 noadjust :不重置 |
| 30 | fisautooverdue | 自动转逾期 | bpchar | 1 |  | √ | '0' | 自动转逾期 |
| 31 | fisadjustfixrate | 固定利率可调整(old) | bpchar | 1 |  | √ | '0' | 固定利率可调整(old) |
| 32 | fintdateeffectrule | 计息日生效规则 | varchar | 30 |  | √ | ' ' | 计息日生效规则,枚举: contracteffectdate :合同生效日 iousintdate :借据起息日 loanissuedate :贷款发放日 |
| 33 | fratetype | 利率类型 | varchar | 30 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 34 | fintroundrule | 计息舍入规则 | varchar | 30 |  | √ | ' ' | 计息舍入规则,枚举: rounded :四舍五入 carry :无条件进位 give :无条件舍去 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_pro_e_s |  | fiscallint |
| 2 | pk_t_cfm_productfactory_e |  | fid |

---

## 融资模型-多语言表 t_cfm_productfactory_l

- **表名称：** 融资模型-多语言表
- **表名：** t_cfm_productfactory_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模型名称 | varchar | 80 |  | √ | ' ' | 模型名称 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdescription | 模型描述 | varchar | 255 |  | √ | ' ' | 模型描述 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_productfactory_l |  | fid,flocaleid |
| 2 | pk_t_cfm_productfactory_l |  | fpkid |

---

## 融资模型-主表 t_cfm_productfactory

- **表名称：** 融资模型-主表
- **表名：** t_cfm_productfactory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fassureway | fassureway | varchar | 80 |  | √ | ' ' |  |
| 3 | fistradefininfo | 贸融信息 | bpchar | 1 |  | √ | '0' | 贸融信息 |
| 4 | fisloancommit | 合同占用授信 | bpchar | 1 |  | √ | '0' | 合同占用授信 |
| 5 | fiscycleloan | 循环贷款 | bpchar | 1 |  | √ | '0' | 循环贷款 |
| 6 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 7 | fislkbizprop | 关联业务信息 | bpchar | 1 |  | √ | '0' | 关联业务信息 |
| 8 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fbiztype | 业务分类 | varchar | 30 |  | √ | ' ' | 业务分类,枚举: loan :普通贷款 entrust :委托贷款 ec :企业往来 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fiscreditlimit | 控制授信额度 | bpchar | 1 |  | √ | '0' | 控制授信额度 |
| 14 | fisfinancingplan | fisfinancingplan | bpchar | 1 |  | √ | '0' |  |
| 15 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fisprojectinfo | 项目信息 | bpchar | 1 |  | √ | '0' | 项目信息 |
| 17 | fcurrencyrule | 币别规则 | varchar | 30 |  | √ | ' ' | 币别规则,枚举: nocurrency :不分币别 foreigncurrency :按外币 basecurrency :按本币 assigncurrency :指定币别 |
| 18 | frateresetadjustrule | 利率重置日节假日规则 | varchar | 80 |  | √ | 'no_adjust' | 利率重置日节假日规则,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 19 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fname | 模型名称 | varchar | 80 |  | √ | ' ' | 模型名称 |
| 21 | ffinproductid | 融资品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fisissueinfo | fisissueinfo | bpchar | 1 |  | √ | '0' |  |
| 24 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 25 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | floanreturninfo | 统借统还信息 | bpchar | 1 |  | √ | '0' | 统借统还信息 |
| 27 | fdescription | 模型描述 | varchar | 255 |  | √ | ' ' | 模型描述 |
| 28 | ftermtype | 期限类型 | varchar | 30 |  | √ | ' ' | 期限类型,枚举: short :短期 long :长期 nolimit :不限 |
| 29 | fisrepayplan | 按还款计划还款 | bpchar | 1 |  | √ | '0' | 按还款计划还款 |
| 30 | fisscminfo | 供应链信息 | bpchar | 1 |  | √ | '0' | 供应链信息 |
| 31 | fcreditortype | 债权/债务人类型 | varchar | 30 |  | √ | ' ' | 债权/债务人类型,枚举: bank :银行 finorg :非银金融机构 innerunit :内部单位 custom :客商 other :其他 |
| 32 | fenable | 产品状态 | varchar | 30 |  | √ | ' ' | 产品状态,枚举: 0 :禁用 1 :可用 |
| 33 | fnumber | 模型代码 | varchar | 80 |  | √ | ' ' | 模型代码 |
| 34 | fdrawway | 提款次数 | varchar | 30 |  | √ | ' ' | 提款次数,枚举: once :一次性 stage :分期 |
| 35 | fisslinfo | 银团信息 | bpchar | 1 |  | √ | '0' | 银团信息 |
| 36 | fpayintadjustrule | 付息日节假日规则 | varchar | 80 |  | √ | 'no_adjust' | 付息日节假日规则,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 37 | fbilltype | fbilltype | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_pro_n |  | fnumber,fstatus |
| 2 | pk_cfm_productfactory |  | fid |

---

## 指定币别-多选基础资料表 t_cfm_productfactory_c

- **表名称：** 指定币别-多选基础资料表
- **表名：** t_cfm_productfactory_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_productfactory_c_id |  | fid |
| 2 | pk_cfm_productfactory_c |  | fpkid |
