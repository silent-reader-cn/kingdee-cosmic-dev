# 重算流水明细-ccm_recalculatedetail

## 重算流水明细-主表 t_ccm_recalculatedetail

- **表名称：** 重算流水明细-主表
- **表名：** t_ccm_recalculatedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farchiveid | 关联档案ID | int8 | 64 |  | √ | 0 | 关联档案ID |
| 3 | fdimensionid | 维度 | int8 | 64 |  | √ | 0 | 信控维度 ccm_dimension |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fop | 单据操作 | varchar | 30 |  | √ | ' ' | 单据操作 |
| 6 | fschemeid | 信控方案 | int8 | 64 |  | √ | 0 | （废弃）信控方案 ccm_scheme |
| 7 | foriginalamount | 原始数额 | numeric | 23 | 10 | √ | 0 | 原始数额 |
| 8 | famount | 数额 | numeric | 23 | 10 | √ | 0 | 数额 |
| 9 | froleid0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 维度成员值0 |
| 10 | fmainbillid | 主业务单据ID | int8 | 64 |  | √ | 0 | 主业务单据ID |
| 11 | froleid2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 维度成员值2 |
| 12 | froleid1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 维度成员值1 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | froleid3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 维度成员值3 |
| 15 | fchecktypeid | 信用控制形式 | int8 | 64 |  | √ | 0 | （废弃）信用控制形式 ccm_checktype |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | foriginalunitid | 原始单位 | int8 | 64 |  | √ | 0 | 原始单位 |
| 19 | funitid | 折算单位 | int8 | 64 |  | √ | 0 | 折算单位 |
| 20 | froletype2 | 维度成员类型2 | varchar | 80 |  | √ | ' ' | 维度成员类型2 |
| 21 | fentitykey | 实体标识 | varchar | 30 |  | √ | ' ' | 实体标识 |
| 22 | froletype3 | 维度成员类型3 | varchar | 80 |  | √ | ' ' | 维度成员类型3 |
| 23 | fconversionrate | 换算率 | numeric | 23 | 10 | √ | 0 | 换算率 |
| 24 | fentrykey | 分录标识 | varchar | 30 |  | √ | ' ' | 分录标识 |
| 25 | froletype0 | 维度成员类型0 | varchar | 80 |  | √ | ' ' | 维度成员类型0 |
| 26 | froletype1 | 维度成员类型1 | varchar | 80 |  | √ | ' ' | 维度成员类型1 |
| 27 | fmainentitykey | 主业务单据标识 | varchar | 30 |  | √ | ' ' | 主业务单据标识 |
| 28 | fdimensionvalue | 维度值 | varchar | 255 |  | √ | ' ' | 维度值 |
| 29 | faction | 信用操作 | varchar | 30 |  | √ | ' ' | 信用操作,枚举: UPDATE :更新 INIT :初始化 RECALCULATE :重算 ADJUST :额度调整 |
| 30 | fquotatype | 额度类型 | varchar | 30 |  | √ | ' ' | 额度类型,枚举: amount :金额 qty :数量 days :天数 privilegeamt :特批总额 privilegeday :特批天数 |
| 31 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 32 | fdirection | 信用方向 | varchar | 30 |  | √ | ' ' | 信用方向,枚举: REDUCE :占用 INCREASE :返还 |
| 33 | frecrecordid | 重算记录ID | int8 | 64 |  | √ | 0 | 重算记录ID |
| 34 | fentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccm_recalculatedetail |  | fid |
| 2 | idx_ccm_recalculatedetail_rec |  | fschemeid,frecrecordid,fdimensionvalue |
