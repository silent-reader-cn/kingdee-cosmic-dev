# 计件工作量-sfc_pieceworkload

## 关联子实体-子表 t_sfc_pieceworkentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_pieceworkentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_pieceworkentry_lk |  | fpkid |
| 2 | idx_sfc_pieceworkentry_lk_fk |  | fentryid |

---

## 关联子实体-子表 t_sfc_piecework_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_piecework_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_piecework_lk |  | fpkid |
| 2 | idx_sfc_piecework_lk_fk |  | fid |

---

## 工作量明细单据体-子表 t_sfc_pieceworkentry

- **表名称：** 工作量明细单据体-子表
- **表名：** t_sfc_pieceworkentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproplanid | 工序计划内码 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 3 | fjobtype | 作业类型 | bpchar | 1 |  | √ | ' ' | 作业类型,枚举: A :团队作业 B :个人作业 |
| 4 | fworkunitid | 工作量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fteamfactor | 团队计件系数 | numeric | 23 | 10 | √ | 0 | 团队计件系数 |
| 6 | fsumauditamount | 总核准金额 | numeric | 23 | 10 | √ | 0 | 总核准金额 |
| 7 | fpieceworktype | 计件工作量类型 | bpchar | 1 |  | √ | ' ' | 计件工作量类型,枚举: A :产品数量 B :活动工时 |
| 8 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 9 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 10 | fworkwastqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fsbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 13 | fsource | 来源 | bpchar | 1 |  | √ | ' ' | 来源,枚举: A :工序汇报单 B :手工 C :辅助任务汇报 |
| 14 | fquaqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 15 | fcorebilltypeid | 核心单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 16 | fsbillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 17 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 18 | fcorebillrow | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 19 | fbaseunitid | 物料基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fstockwastqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 21 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 22 | fsumpieceamount | 总预计金额 | numeric | 23 | 10 | √ | 0 | 总预计金额 |
| 23 | fcorebillnumber | 核心单据编号 | varchar | 100 |  | √ | ' ' | 核心单据编号 |
| 24 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 25 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 26 | fsourcebillnumber | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 27 | fteamid | 团队 | int8 | 64 |  | √ | 0 | [制造团队 mpdm_mftteam](../mpdm_files/mpdm_mftteam.md) |
| 28 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 29 | fpieceworktime | 计件工时 | numeric | 23 | 10 | √ | 0 | 计件工时 |
| 30 | fadaptationscenario | 适配场景 | bpchar | 1 |  | √ | ' ' | 适配场景,枚举: A :工序汇报单 B :辅助任务汇报 |
| 31 | fproplanbillid | 工序计划号 | int8 | 64 |  | √ | 0 | 工序计划 sfc_processplanbill |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fprocesscenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 34 | fcorebillrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_pieceworkentry |  | fentryid |
| 2 | idx_sfc_pieceworkentry_fid |  | fid |

---

## 关联子实体-子表 t_sfc_pieceworkuser_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_pieceworkuser_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_pieceworkuser_lk_fk |  | fdetailid |
| 2 | pk_sfc_pieceworkuser_lk |  | fpkid |

---

## 操作员子单据体-子表 t_sfc_pieceworkuser

- **表名称：** 操作员子单据体-子表
- **表名：** t_sfc_pieceworkuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fauditamount | 核准金额 | numeric | 23 | 10 | √ | 0 | 核准金额 |
| 3 | fuserid | 工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fchargeunitid | 计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fpercentage | 百分比 | numeric | 23 | 10 | √ | 0 | 百分比 |
| 6 | festimatedamount | 预计金额 | numeric | 23 | 10 | √ | 0 | 预计金额 |
| 7 | fworktimeprice | 工时单价 | numeric | 23 | 10 | √ | 0 | 工时单价 |
| 8 | fworkwastprice | 工废扣款单价 | numeric | 23 | 10 | √ | 0 | 工废扣款单价 |
| 9 | fworkloadrate | 工作量比例 | numeric | 23 | 10 | √ | 1 | 工作量比例 |
| 10 | fquaprice | 合格单价 | numeric | 23 | 10 | √ | 0 | 合格单价 |
| 11 | fchargefactor | 计件系数 | numeric | 23 | 10 | √ | 0 | 计件系数 |
| 12 | fworkwastamount | 工废扣款金额 | numeric | 23 | 10 | √ | 0 | 工废扣款金额 |
| 13 | fstockwastprice | 料废单价 | numeric | 23 | 10 | √ | 0 | 料废单价 |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_pieceuser_entry |  | fentryid |
| 2 | pk_sfc_pieceworkuser |  | fdetailid |

---

## 计件工作量-主表 t_sfc_piecework

- **表名称：** 计件工作量-主表
- **表名：** t_sfc_piecework

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 加工组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fcalculatedsalary | 已核算工资 | bpchar | 1 |  | √ | '0' | 已核算工资 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdepartid | 加工车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 12 | fproductorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_piecework_billno |  | fbillno |
| 2 | pk_sfc_piecework |  | fid |

---

## 计件工作量-关联追踪表 t_sfc_piecework_tc

- **表名称：** 计件工作量-关联追踪表
- **表名：** t_sfc_piecework_tc

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
| 1 | pk_sfc_piecework_tc |  | fid |
| 2 | idx_sfc_piecework_tc_tid |  | ftid |
| 3 | idx_sfc_piecework_tc_tbill |  | ftbillid |

---

## 计件工作量-反写记录表 t_sfc_piecework_wb

- **表名称：** 计件工作量-反写记录表
- **表名：** t_sfc_piecework_wb

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
| 1 | pk_sfc_piecework_wb |  | fentryid |
| 2 | idx_sfc_piecework_wb_fk |  | fid |
