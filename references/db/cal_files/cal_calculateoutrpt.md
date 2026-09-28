# 出库核算报告-cal_calculateoutrpt

## 出库核算报告-主表 t_cal_caloutrpt

- **表名称：** 出库核算报告-主表
- **表名：** t_cal_caloutrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcalstatus | 结转状态 | varchar | 5 |  | √ | ' ' | 结转状态,枚举: A :成功 B :失败 C :警告 |
| 3 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fcalorgid | 核算组织名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 cal_bd_caldimension](../cal_files/cal_bd_caldimension.md) |
| 7 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | [核算范围 cal_bd_calrange](../cal_files/cal_bd_calrange.md) |
| 8 | fdividebasisid | 划分依据 | int8 | 64 |  | √ | 0 | [划分依据 cal_bd_dividebasis](../cal_files/cal_bd_dividebasis.md) |
| 9 | flog | 日志 | varchar | 255 |  | √ | ' ' | 日志 |
| 10 | fcaldimensionvalue | 核算维度值 | varchar | 255 |  | √ | ' ' | 核算维度值 |
| 11 | foperationuserid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | faccounttype | 计价方法 | varchar | 5 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 G :先进先出法 C :即时移动平均法 E :即时先进先出法 |
| 13 | fnextseq | 下一序号 | int8 | 64 |  | √ | 0 | 下一序号 |
| 14 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 15 | fdividebasisvalue | 划分依据值 | varchar | 255 |  | √ | ' ' | 划分依据值 |
| 16 | fcaltime | 计算时间 | timestamp | 0 |  |  | null | 计算时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_caloutrpt_pkey |  | fid |
| 2 | idx_cal_caloutrpt_costacc |  | fcostaccountid |

---

## 单据体-子表 t_cal_caloutrptentry

- **表名称：** 单据体-子表
- **表名：** t_cal_caloutrptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutstr | 发出 | varchar | 500 |  | √ | ' ' | 发出 |
| 3 | fbalancestr | 结存 | varchar | 500 |  | √ | ' ' | 结存 |
| 4 | fbilltypenum | 业务单据类型编号 | varchar | 255 |  | √ | ' ' | 业务单据类型编号 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | finstr | 收入 | varchar | 500 |  | √ | ' ' | 收入 |
| 8 | fbillnumber | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 9 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 10 | fcostsource | 成本来源 | varchar | 50 |  | √ | ' ' | 成本来源,枚举: 2 :出库核算 31 :入库成本汇总维护 32 :出库成本汇总维护 33 :入库成本维护 34 :出库成本维护 35 :其他存货核算 351 :其他存货核算（权重和费用） 36 :委外入库成本维护 37 :零成本批量维护 4 :勾稽与费用分摊 7 :返工取价 8 :实际成本核算 A :成本记录创建 B :应付结算清单 |
| 11 | fbizdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 12 | fparententryid | 父分录id | int8 | 64 |  | √ | 0 | 父分录id |
| 13 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fbilltype | 单据类型 | varchar | 255 |  | √ | ' ' | 单据类型 |
| 16 | ffivouchernum | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 17 | fbizbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_caloutrptentry_pkey |  | fentryid |
| 2 | idx_cal_caloutrpte_id |  | fid |
