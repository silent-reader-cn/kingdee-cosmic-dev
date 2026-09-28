# 辅助任务汇报-mpdm_assistreport

## 人员-子表 t_mpdm_assistreport_e_d

- **表名称：** 人员-子表
- **表名：** t_mpdm_assistreport_e_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fchargeunitid | 计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | festimatedamount | 预计金额 | numeric | 23 | 10 | √ | 0 | 预计金额 |
| 4 | fworktimeprice | 工时单价 | numeric | 23 | 10 | √ | 0 | 工时单价 |
| 5 | fworkwastprice | 工废扣款单价 | numeric | 23 | 10 | √ | 0 | 工废扣款单价 |
| 6 | fworkratio | 工作量比例 | numeric | 23 | 10 | √ | 0 | 工作量比例 |
| 7 | fquaprice | 合格单价 | numeric | 23 | 10 | √ | 0 | 合格单价 |
| 8 | fchargefactor | 计件系数 | numeric | 23 | 10 | √ | 0 | 计件系数 |
| 9 | fworkwastamount | 工废扣款金额 | numeric | 23 | 10 | √ | 0 | 工废扣款金额 |
| 10 | fpersonid | 工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fstockwastprice | 料废单价 | numeric | 23 | 10 | √ | 0 | 料废单价 |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fproportion | 百分比 | numeric | 23 | 10 | √ | 0 | 百分比 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_assistreport_e_d |  | fdetailid |
| 2 | idx_mpdm_assistreport_e_d |  | fentryid |

---

## 汇报明细-多语言表 t_mpdm_assistreport_e_l

- **表名称：** 汇报明细-多语言表
- **表名：** t_mpdm_assistreport_e_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcomment | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 2 | ftaskdesc | 任务说明 | varchar | 2000 |  | √ | ' ' | 任务说明 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_assistreport_e_l_id |  | fentryid,flocaleid |
| 2 | pk_mpdm_assistreport_e_l |  | fpkid |

---

## 汇报明细-子表 t_mpdm_assistreport_e

- **表名称：** 汇报明细-子表
- **表名：** t_mpdm_assistreport_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fteamfactor | 团队计件系数 | numeric | 23 | 10 | √ | 0 | 团队计件系数 |
| 3 | fmanualtime | 人工工时 | numeric | 23 | 10 | √ | 0 | 人工工时 |
| 4 | fpieceworktype | 计件工作量类型 | bpchar | 1 |  | √ | ' ' | 计件工作量类型,枚举: A :产品数量 B :活动工时 |
| 5 | ftaskrowno | 任务行号 | int4 | 32 |  | √ | 0 | 任务行号 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 7 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | [辅助任务类型 mpdm_assisttasktype](../mpdm_files/mpdm_assisttasktype.md) |
| 8 | fhaspiecerange | 启用计件 | bpchar | 1 |  | √ | '0' | 启用计件 |
| 9 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 10 | fworkwastqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fsbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 13 | fsource | 来源 | bpchar | 1 |  | √ | ' ' | 来源,枚举: A :辅助任务 B :手工 |
| 14 | fbegintime | 实际开工时间 | timestamp | 0 |  |  | null | 实际开工时间 |
| 15 | fquaqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 16 | fcorebilltypeid | 核心单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 17 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 18 | fcomplete | 完工 | bpchar | 1 |  | √ | '0' | 完工 |
| 19 | fprotimeunitid | 工时单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fsbillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 21 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 22 | fcorebillrow | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 23 | fstockwastqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 24 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 25 | fassisttaskentryid | 辅助任务分录 | int8 | 64 |  | √ | 0 | [辅助任务分录F7 mpdm_assisttaskentry_f7](../mpdm_files/mpdm_assisttaskentry_f7.md) |
| 26 | fcomment | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 27 | ftaskdesc | 任务说明 | varchar | 2000 |  | √ | ' ' | 任务说明 |
| 28 | fnormprocessid | 标准工序 | int8 | 64 |  | √ | 0 | [标准工序 mpdm_normprocess](../mpdm_files/mpdm_normprocess.md) |
| 29 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 30 | fsumpieceamount | 总预计金额 | numeric | 23 | 10 | √ | 0 | 总预计金额 |
| 31 | fassisttaskid | 辅助任务F7 | int8 | 64 |  | √ | 0 | [辅助任务F7 mpdm_assisttask_f7](../mpdm_files/mpdm_assisttask_f7.md) |
| 32 | funitid | 物料单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | fassisttaskbillid | 辅助任务 | int8 | 64 |  | √ | 0 | 辅助任务 mpdm_assisttask |
| 34 | fcorebillnumber | 核心单据编号 | varchar | 100 |  | √ | ' ' | 核心单据编号 |
| 35 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 36 | fsourcebillnumber | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 37 | fproduceteamid | 团队 | int8 | 64 |  | √ | 0 | [制造团队 mpdm_mftteam](../mpdm_files/mpdm_mftteam.md) |
| 38 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 39 | fmachinetime | 机器工时 | numeric | 23 | 10 | √ | 0 | 机器工时 |
| 40 | fendtime | 实际完工时间 | timestamp | 0 |  |  | null | 实际完工时间 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | fcorebillrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 43 | fhaspushpiece | 已生成计件工作量 | bpchar | 1 |  | √ | '0' | 已生成计件工作量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_assistreport_e_fid |  | fid |
| 2 | pk_mpdm_assistreport_e |  | fentryid |

---

## 辅助任务汇报-主表 t_mpdm_assistreport

- **表名称：** 辅助任务汇报-主表
- **表名：** t_mpdm_assistreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fapplyorgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fapplydepartid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 执行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fapplyconfirm | 申请部门已确认 | bpchar | 1 |  | √ | '0' | 申请部门已确认 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fexecutedepartid | 执行车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 14 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fpostdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_assistreport_billno |  | fbillno |
| 2 | pk_mpdm_assistreport |  | fid |

---

## 设备-多选基础资料表 t_mpdm_assistreport_eqp

- **表名称：** 设备-多选基础资料表
- **表名：** t_mpdm_assistreport_eqp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [设备 sfc_equipment](../mpdm_files/sfc_equipment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_assistreport_eqp |  | fpkid |
| 2 | idx_mpdm_report_eqp_fidbdid |  | fentryid,fbasedataid |

---

## 辅助任务汇报-反写记录表 t_mpdm_assistreport_wb

- **表名称：** 辅助任务汇报-反写记录表
- **表名：** t_mpdm_assistreport_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_assistreport_wb_fk |  | fid |
| 2 | pk_mpdm_assistreport_wb |  | fentryid |

---

## 关联子实体-子表 t_mpdm_assistreport_e_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpdm_assistreport_e_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmanualtime_old | 人工工时_原始携带值 | numeric | 23 | 10 |  | null | 人工工时_原始携带值 |
| 2 | fmanualtime | 人工工时_确认携带值 | numeric | 23 | 10 |  | null | 人工工时_确认携带值 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fworkwastqty | 工废数量_确认携带值 | numeric | 23 | 10 |  | null | 工废数量_确认携带值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fstockwastqty_old | 料废数量_原始携带值 | numeric | 23 | 10 |  | null | 料废数量_原始携带值 |
| 7 | fquaqty_old | 合格数量_原始携带值 | numeric | 23 | 10 |  | null | 合格数量_原始携带值 |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 9 | fworkwastqty_old | 工废数量_原始携带值 | numeric | 23 | 10 |  | null | 工废数量_原始携带值 |
| 10 | fmachinetime_old | 机器工时_原始携带值 | numeric | 23 | 10 |  | null | 机器工时_原始携带值 |
| 11 | fquaqty | 合格数量_确认携带值 | numeric | 23 | 10 |  | null | 合格数量_确认携带值 |
| 12 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 13 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 14 | fmachinetime | 机器工时_确认携带值 | numeric | 23 | 10 |  | null | 机器工时_确认携带值 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 16 | fstockwastqty | 料废数量_确认携带值 | numeric | 23 | 10 |  | null | 料废数量_确认携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_assistreport_e_lk_fk |  | fentryid |
| 2 | pk_mpdm_assistreport_e_lk |  | fpkid |

---

## 辅助任务汇报-关联追踪表 t_mpdm_assistreport_tc

- **表名称：** 辅助任务汇报-关联追踪表
- **表名：** t_mpdm_assistreport_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_assistreport_tc_tbill |  | ftbillid |
| 2 | pk_mpdm_assistreport_tc |  | fid |
| 3 | idx_mpdm_assistreport_tc_tid |  | ftid |
