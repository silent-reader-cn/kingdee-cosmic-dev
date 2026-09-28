# 信用流水明细-ccm_journaldetail

## 信用流水明细-主表 t_ccm_journaldetail

- **表名称：** 信用流水明细-主表
- **表名：** t_ccm_journaldetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farchiveid | 关联档案ID | int8 | 64 |  | √ | 0 | 关联档案ID |
| 3 | fsrcentryid | 上游单据分录ID | int8 | 64 |  | √ | 0 | 上游单据分录ID |
| 4 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 5 | fdimensionid | 维度 | int8 | 64 |  | √ | 0 | [信控维度 ccm_dimension](../ccm_files/ccm_dimension.md) |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fop | 单据操作 | varchar | 30 |  | √ | ' ' | 单据操作 |
| 8 | fschemeid | 信控方案 | int8 | 64 |  | √ | 0 | [信用控制方案 ccm_schemes](../ccm_files/ccm_schemes.md) |
| 9 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 10 | foriginalamount | 原始数额 | numeric | 23 | 10 | √ | 0 | 原始数额 |
| 11 | famount | 数额 | numeric | 23 | 10 | √ | 0 | 数额 |
| 12 | fsrcentrykey | 上游单据分录标识 | varchar | 80 |  | √ | ' ' | 上游单据分录标识 |
| 13 | froleid0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 维度成员值0 |
| 14 | fsrcbaseqty | 释放上游单据基本单位数量 | numeric | 23 | 10 | √ | 0 | 释放上游单据基本单位数量 |
| 15 | fmainbillid | 主业务单据ID | int8 | 64 |  | √ | 0 | 主业务单据ID |
| 16 | froleid2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 维度成员值2 |
| 17 | froleid1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 维度成员值1 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | froleid3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 维度成员值3 |
| 20 | fchecktypeid | 控制范围 | int8 | 64 |  | √ | 0 | [（废弃）信用控制形式 ccm_checktype](../ccm_files/ccm_checktype.md) |
| 21 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 22 | fmainbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 基本单位 |
| 23 | fsrcjournalid | 反向更新对应的更新的流水id | int8 | 64 |  | √ | 0 | 反向更新对应的更新的流水id |
| 24 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: recsettle :应收收款核销 recself :收款红蓝对冲 arself :应收红蓝对冲 artransfer :应收转销 arapsettle :应收冲应付 arwriteoff :应收红蓝冲销 baddebtloss :坏账损失 baddebtrecovery :坏账收回 recpaysettle :收款冲退款 arpaysettle :应收退款核销 arliqsettle :应收清理 aparsettle :应付冲应收 payrecsettle :付款冲退款 aprecsettle :应付退款核销 recclearing :收款清理 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | foriginalunitid | 原始单位 | int8 | 64 |  | √ | 0 | 原始单位 |
| 27 | funitid | 折算单位 | int8 | 64 |  | √ | 0 | 折算单位 |
| 28 | froletype2 | 维度成员类型2 | varchar | 80 |  | √ | ' ' | 维度成员类型2 |
| 29 | fentitykey | 实体标识 | varchar | 30 |  | √ | ' ' | 实体标识 |
| 30 | froletype3 | 维度成员类型3 | varchar | 80 |  | √ | ' ' | 维度成员类型3 |
| 31 | fconversionrate | 换算率 | numeric | 23 | 10 | √ | 0 | 换算率 |
| 32 | fentrykey | 分录标识 | varchar | 30 |  | √ | ' ' | 分录标识 |
| 33 | froletype0 | 维度成员类型0 | varchar | 80 |  | √ | ' ' | 维度成员类型0 |
| 34 | froletype1 | 维度成员类型1 | varchar | 80 |  | √ | ' ' | 维度成员类型1 |
| 35 | fjournaltype | 流水类型 | varchar | 80 |  | √ | ' ' | 流水类型,枚举: normal :普通 releasesrc :释放源单 |
| 36 | fmainentitykey | 主业务单据标识 | varchar | 30 |  | √ | ' ' | 主业务单据标识 |
| 37 | fdimensionvalue | 维度值 | varchar | 255 |  | √ | ' ' | 维度值 |
| 38 | faction | 信用操作 | varchar | 30 |  | √ | ' ' | 信用操作,枚举: UPDATE :更新 INIT :初始化 RECALCULATE :重算 ADJUST :额度调整 |
| 39 | fquotatype | 额度类型 | varchar | 30 |  | √ | ' ' | 额度类型,枚举: amount :金额 qty :数量 days :天数 privilegeamt :特批总额 privilegeday :特批天数 |
| 40 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 41 | fdirection | 信用方向 | varchar | 30 |  | √ | ' ' | 信用方向,枚举: REDUCE :扣减 INCREASE :返还 |
| 42 | fentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 43 | fmainbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 44 | fdtype | 流水可删除类型 | varchar | 30 |  | √ | 'N' | 流水可删除类型,枚举: N :正常流水 D :可删除流水 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_journaldetail |  | fid |
| 2 | idx_ccm_jourdetail_arc |  | farchiveid,fentryid |
| 3 | idx_ccm_jourdetail_bill |  | fmainentitykey,fmainbillid,fentryid |
