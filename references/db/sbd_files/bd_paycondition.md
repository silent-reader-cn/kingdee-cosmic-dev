# 付款条件-bd_paycondition

## 分录明细-子表 t_bd_payconditionentry

- **表名称：** 分录明细-子表
- **表名：** t_bd_payconditionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemnameid | 款项名称 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 3 | frate | 付款比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 付款比例(%) |
| 4 | fcomment | 描述 | varchar | 512 |  |  | ' ' | 描述 |
| 5 | fconfirmtypedesc | 到期日确定方式描述 | varchar | 512 |  |  | ' ' | 到期日确定方式描述 |
| 6 | fconfirmtypename | 到期日确定方式 | varchar | 80 |  | √ | ' ' | 到期日确定方式 |
| 7 | fispre | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fconfirmtype | 到期日确定方式 | varchar | 5 |  | √ | ' ' | 到期日确定方式,枚举: A :交易日 B :某天后 C :月结 D :固定时点 |
| 10 | famount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fconfirmtypedata | 到期日确定方式描述 | varchar | 512 |  |  | ' ' | 到期日确定方式描述 |

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
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
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
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fsettletype | 预付核销方式 | varchar | 5 |  | √ | ' ' | 预付核销方式,枚举: A :先到先用 B :按实际预付比例核销 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fpaybill | 应付单 | bpchar | 1 |  | √ | '0' | 应付单 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fsplitscheme | 付款计划方案 | int8 | 64 |  | √ | 0 | 付款计划方案 ap_plansplit_scheme |
| 10 | fdescription | 描述 | varchar | 512 |  |  | ' ' | 描述 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftype | 付款方式 | varchar | 5 |  | √ | ' ' | 付款方式,枚举: A :按到期日 B :按采购订单 C :按采购物料 |
| 16 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 17 | fcalculatetime | 到期日计算日期 | varchar | 5 |  | √ | ' ' | 到期日计算日期,枚举: A :采购订单日期 B :收料通知单日期 C :采购入库日期 D :应付单日期 |
| 18 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fbasis | 付款设置依据 | varchar | 5 |  | √ | ' ' | 付款设置依据,枚举: A :按比例(%) B :按金额 |
| 20 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 21 | forderbill | 采购订单 | bpchar | 1 |  | √ | '0' | 采购订单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_paycondition_pkey |  | fid |
| 2 | idx_bd_paycondition_fnumber |  | fnumber |
