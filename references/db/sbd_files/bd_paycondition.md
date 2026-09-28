# 付款条件-bd_paycondition

## 分录明细-子表 t_bd_payconditionentry

- **表名称：** 分录明细-子表
- **表名：** t_bd_payconditionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemnameid | 款项名称 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 3 | frecratio | 累计收款比例(%) | numeric | 23 | 10 | √ | 0 | 累计收款比例(%) |
| 4 | fcomment | 描述 | varchar | 512 |  |  | ' ' | 描述 |
| 5 | fconfirmtypename | 到期日确定方式 | varchar | 80 |  | √ | ' ' | 到期日确定方式 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fconfirmtype | 到期日确定方式 | varchar | 5 |  | √ | ' ' | 到期日确定方式,枚举: A :交易日 B :某天后 C :月结 D :固定日 |
| 8 | famount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 9 | fconfirmtypedata | 到期日确定方式描述 | varchar | 2000 |  |  | ' ' | 到期日确定方式描述 |
| 10 | frate | 付款比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 付款比例(%) |
| 11 | fconfirmtypedesc | 到期日确定方式描述 | varchar | 512 |  |  | ' ' | 到期日确定方式描述 |
| 12 | fispre | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 13 | fcalculatetime | 到期日计算日期 | varchar | 5 |  | √ | ' ' | 到期日计算日期,枚举: |
| 14 | fpayratio | 累计付款比例(%) | numeric | 23 | 10 | √ | 0 | 累计付款比例(%) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_payconditionentry_pkey |  | fentryid |
| 2 | idx_bd_payconditionentry_fid |  | fid |

---

## 付款条件-多语言表 t_bd_paycondition_l

- **表名称：** 付款条件-多语言表
- **表名：** t_bd_paycondition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  |  | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_paycondition_l_pkey |  | fpkid |
| 2 | idx_bd_paycondition_l_fid |  | fid,flocaleid |

---

## 付款条件-主表 t_bd_paycondition

- **表名称：** 付款条件-主表
- **表名：** t_bd_paycondition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpaybill | 应付单 | bpchar | 1 |  | √ | '0' | 应付单 |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | fsplitscheme | 付款计划方案 | int8 | 64 |  | √ | 0 | [付款计划方案 ap_plansplit_scheme](../ap_files/ap_plansplit_scheme.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fdatecriterion | 到期日基准 | bpchar | 1 |  | √ | '0' | 到期日基准,枚举: 0 :次日起算 1 :当天起算 |
| 10 | fpayratiosetting | 付款比例设置 | varchar | 20 |  | √ | ' ' | 付款比例设置,枚举: ZDY :自定义 TBL :收支同步 |
| 11 | forderbill | 采购订单 | bpchar | 1 |  | √ | '0' | 采购订单 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 14 | fsettletype | 预付核销方式 | varchar | 5 |  | √ | ' ' | 预付核销方式,枚举: A :先到先用 B :按实际预付比例核销 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fdescription | 描述 | varchar | 512 |  |  | ' ' | 描述 |
| 18 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 19 | ftype | 付款方式 | varchar | 5 |  | √ | ' ' | 付款方式,枚举: A :按到期日 B :按采购订单 C :按采购物料 |
| 20 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 21 | flinkedpay | 联动付款 | bpchar | 1 |  | √ | '0' | 联动付款 |
| 22 | fmultipledays | 多到期日起算日期 | bpchar | 1 |  | √ | '0' | 多到期日起算日期 |
| 23 | fcalculatetime | 到期日计算日期 | varchar | 5 |  | √ | ' ' | 到期日计算日期,枚举: |
| 24 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fbasis | 付款设置依据 | varchar | 5 |  | √ | ' ' | 付款设置依据,枚举: A :按比例(%) B :按金额 |
| 26 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 27 | fpayref | 付款参考 | varchar | 20 |  | √ | ' ' | 付款参考,枚举: FKCK01 :项目收款 FKCK02 :阶段收款 FKCK03 :单个里程碑 FKCK04 :截止至固定里程碑 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_paycondition_pkey |  | fid |
| 2 | idx_bd_paycondition_fnumber |  | fnumber |
