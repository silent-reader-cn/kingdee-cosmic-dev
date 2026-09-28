# 收款条件-bd_reccondition

## 收款条件-主表 t_bd_reccondition

- **表名称：** 收款条件-主表
- **表名：** t_bd_reccondition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fsettletype | 预收核销方式 | varchar | 5 |  | √ | ' ' | 预收核销方式,枚举: A :先到先用 B :按实际预收比例核销 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fpaybill | fpaybill | bpchar | 1 |  | √ | '0' |  |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fsplitscheme | 收款计划方案 | int8 | 64 |  | √ | 0 | 收款计划方案 ar_plansplit_scheme |
| 10 | fdescription | 描述 | varchar | 512 |  |  | ' ' | 描述 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | foverrecrate | 预收允超比例(%) | numeric | 23 | 2 | √ | 0 | 预收允超比例(%) |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | ftype | 收款方式 | varchar | 5 |  | √ | ' ' | 收款方式,枚举: A :按到期日 B :按销售订单 C :按销售物料 |
| 17 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 18 | fcalculatetime | 到期日计算日期 | varchar | 5 |  | √ | ' ' | 到期日计算日期,枚举: A :销售订单日期 B :销售出库日期 C :应收单日期 |
| 19 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fbasis | 收款设置依据 | varchar | 5 |  | √ | ' ' | 收款设置依据,枚举: A :按比例(%) B :按金额 |
| 21 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 22 | forderbill | forderbill | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_reccondition_pkey |  | fid |
| 2 | idx_bd_reccondition_fnumber |  | fnumber |

---

## 收款条件-多语言表 t_bd_reccondition_l

- **表名称：** 收款条件-多语言表
- **表名：** t_bd_reccondition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fdescription | 描述 | varchar | 512 |  |  | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_reccondition_l_pkey |  | fpkid |
| 2 | idx_bd_reccondition_l_fid |  | fid,flocaleid |

---

## 分录明细-子表 t_bd_recconditionentry

- **表名称：** 分录明细-子表
- **表名：** t_bd_recconditionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliverybyprepaid | 按实际预收控制发货 | bpchar | 1 |  | √ | '0' | 按实际预收控制发货 |
| 3 | fitemnameid | 款项名称 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 4 | fcomment | 描述 | varchar | 512 |  |  | ' ' | 描述 |
| 5 | fcontrolsend | 控制环节 | varchar | 50 |  | √ | ' ' | 控制环节,枚举: delivernotice :发货通知 salout :销售出库 mftorder :生产工单 |
| 6 | fconfirmtypename | 到期日确定方式 | varchar | 80 |  | √ | ' ' | 到期日确定方式 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fconfirmtype | 到期日确定方式 | varchar | 5 |  | √ | ' ' | 到期日确定方式,枚举: A :交易日 B :某天后 C :月结 D :固定时点 |
| 9 | famount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 10 | fconfirmtypedata | 到期日确定方式描述 | varchar | 512 |  |  | ' ' | 到期日确定方式描述 |
| 11 | frate | 收款比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 收款比例(%) |
| 12 | fconfirmtypedesc | 到期日确定方式描述 | varchar | 255 |  |  | ' ' | 到期日确定方式描述 |
| 13 | fispre | 是否预收 | bpchar | 1 |  | √ | '0' | 是否预收 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_recconditionentry_fid |  | fid |
| 2 | t_bd_recconditionentry_pkey |  | fentryid |
