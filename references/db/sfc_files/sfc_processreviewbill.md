# 工序汇报单-sfc_processreviewbill

## 工序汇报明细-子表 t_sfc_reviewentry

- **表名称：** 工序汇报明细-子表
- **表名：** t_sfc_reviewentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freworksection | 返工来源工序段 | varchar | 1000 |  | √ | ' ' | 返工来源工序段 |
| 3 | frelationid | 代码生成id(关联id) | int8 | 64 |  | √ | 0 | 代码生成id(关联id) |
| 4 | ftransinrelationids | 转入工序relationid | varchar | 500 |  | √ | ' ' | 转入工序relationid |
| 5 | fworkentryf7 | 生产工单分录 | int8 | 64 |  | √ | 0 | [生产工单分录F7 sfc_mftorder_f7](../sfc_files/sfc_mftorder_f7.md) |
| 6 | fsequencetype | 序列类型 | bpchar | 1 |  | √ | ' ' | 序列类型,枚举: A :并行序列 B :返工序列 C :主干序列 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | ftracknoid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 10 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | frwsprocessno | frwsprocessno | int4 | 32 |  | √ | 0 |  |
| 12 | frewsreviewno | frewsreviewno | varchar | 80 |  | √ | ' ' |  |
| 13 | freporttype | freporttype | varchar | 10 |  | √ | ' ' |  |
| 14 | fsbilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 15 | fsendworkrowid | 派工行id | int8 | 64 |  | √ | 0 | 派工行id |
| 16 | freworklastprocess | 返工序列末序 | bpchar | 1 |  | √ | '0' | 返工序列末序 |
| 17 | fcorebillrow | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 18 | fcorebilltype | 核心单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 19 | fstockwastqty | fstockwastqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprocessunit | fprocessunit | int8 | 64 |  | √ | 0 |  |
| 21 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 22 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 23 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fmftorderno | 生产工单号(后台) | varchar | 80 |  | √ | ' ' | 生产工单号(后台) |
| 25 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 26 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 27 | fclassgroup | 班组 | int8 | 64 |  | √ | 0 | [班组 mpdm_classgroup](../mpdm_files/mpdm_classgroup.md) |
| 28 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 29 | freworksequence | 返工来源序列号 | int8 | 64 |  | √ | 0 | 返工来源序列号 |
| 30 | freworkqty | freworkqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fcorebillrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 33 | freworkmode | 返工方式 | bpchar | 1 |  | √ | ' ' | 返工方式,枚举: A :直接返工 B :返工序列 |
| 34 | fproplanid | 工序计划内码 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 35 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 36 | fupprocessid | 上工序id | varchar | 1000 |  | √ | ' ' | 上工序id |
| 37 | fworkwastqty | fworkwastqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fbizstatus | 生产工单业务状态 | bpchar | 1 |  | √ | ' ' | 生产工单业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 39 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 40 | fsumrepwastqty | fsumrepwastqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | fmaterielid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 42 | fplancompleteqty | fplancompleteqty | numeric | 23 | 10 | √ | 0 |  |
| 43 | fwastqty | fwastqty | numeric | 23 | 10 | √ | 0 |  |
| 44 | frewsreviewrowno | frewsreviewrowno | int4 | 32 |  | √ | 0 |  |
| 45 | fsecunitid | 产品辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 46 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 47 | fclasssystem | 班制 | int8 | 64 |  | √ | 0 | [班制 mpdm_classsystem](../mpdm_files/mpdm_classsystem.md) |
| 48 | fpickstatus | 生产工单领料状态 | bpchar | 1 |  | √ | ' ' | 生产工单领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 49 | fsbillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 50 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 51 | fpushreworkqty | fpushreworkqty | numeric | 23 | 10 | √ | 0 |  |
| 52 | fbackflishflag | 倒冲标识 | varchar | 10 |  | √ | ' ' | 倒冲标识,枚举: not :未倒冲 sucess :倒冲成功 part :部分倒冲 |
| 53 | fnextprocessid | 下工序id | varchar | 1000 |  | √ | ' ' | 下工序id |
| 54 | fproducttype | 产品类型 | varchar | 10 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 55 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 56 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 57 | fplanstatus | 生产工单计划状态 | bpchar | 1 |  | √ | ' ' | 生产工单计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 58 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 59 | fquaqyt | fquaqyt | numeric | 23 | 10 | √ | 0 |  |
| 60 | fsumrepquaqty | fsumrepquaqty | numeric | 23 | 10 | √ | 0 |  |
| 61 | fproplanbillid | 工序计划 | int8 | 64 |  | √ | 0 | 工序计划 sfc_processplanbill |
| 62 | fproplanno | 工序计划号 | varchar | 80 |  | √ | ' ' | 工序计划号 |
| 63 | fprocesscenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 64 | freworkprocesses | 返工来源工序 | int8 | 64 |  | √ | 0 | 返工来源工序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_reviewentry |  | fentryid |
| 2 | idx_sfc_reviewentry_id |  | fid |

---

## 设备-多选基础资料表 t_sfc_reviewequips

- **表名称：** 设备-多选基础资料表
- **表名：** t_sfc_reviewequips

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
| 1 | pk_t_sfc_reviewequips |  | fpkid |
| 2 | idx_sfc_requips_entryid |  | fentryid |

---

## 工序汇报单-主表 t_sfc_processreview

- **表名称：** 工序汇报单-主表
- **表名：** t_sfc_processreview

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fworkshopid | 生产车间(隐藏) | int8 | 64 |  | √ | 0 | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 10 | fprocessorg | 加工组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fprocessdepartid | 加工车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 14 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fpostdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 18 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_proreview_billno |  | fbillno |
| 2 | pk_t_sfc_processreview |  | fid |

---

## 人员信息-子表 t_sfc_processuser

- **表名称：** 人员信息-子表
- **表名：** t_sfc_processuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fuserid | 工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fchargeunitid | 计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fpercentage | 百分比 | numeric | 23 | 10 | √ | 0 | 百分比 |
| 5 | festimatedamount | 预计金额 | numeric | 23 | 10 | √ | 0 | 预计金额 |
| 6 | fworktimeprice | 工时单价 | numeric | 23 | 10 | √ | 0 | 工时单价 |
| 7 | fworkwastprice | 工废扣款单价 | numeric | 23 | 10 | √ | 0 | 工废扣款单价 |
| 8 | fworkloadrate | 工作量比例 | numeric | 23 | 10 | √ | 1 | 工作量比例 |
| 9 | fquaprice | 合格单价 | numeric | 23 | 10 | √ | 0 | 合格单价 |
| 10 | fchargefactor | 计件系数 | numeric | 23 | 10 | √ | 0 | 计件系数 |
| 11 | fworkwastamount | 工废扣款金额 | numeric | 23 | 10 | √ | 0 | 工废扣款金额 |
| 12 | fstockwastprice | 料废单价 | numeric | 23 | 10 | √ | 0 | 料废单价 |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_reviewu_entry |  | fentryid |
| 2 | pk_t_sfc_processuser |  | fdetailid |

---

## 操作人-多选基础资料表 t_sfc_operateuser

- **表名称：** 操作人-多选基础资料表
- **表名：** t_sfc_operateuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_operateuser_entryid |  | fentryid |
| 2 | pk_t_sfc_operateuser |  | fpkid |

---

## 工序汇报明细-分表 t_sfc_reviewentry_r

- **表名称：** 工序汇报明细-分表
- **表名：** t_sfc_reviewentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frewsprocessno | 汇报.返工来源工序号 | int4 | 32 |  | √ | 0 | 汇报.返工来源工序号 |
| 3 | fdamageproqty | 损耗生产数量 | numeric | 23 | 10 | √ | 0 | 损耗生产数量 |
| 4 | fstockwastbaseqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |
| 5 | fbegintime | 实际开工时间 | timestamp | 0 |  |  | null | 实际开工时间 |
| 6 | frewsreviewno | 汇报.返工来源汇报单 | varchar | 80 |  | √ | ' ' | 汇报.返工来源汇报单 |
| 7 | fplancompleteproqty | 汇报.计划完成生产数量 | numeric | 23 | 10 | √ | 0 | 汇报.计划完成生产数量 |
| 8 | fworkwastbaseqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 9 | freporttype | 汇报类型 | varchar | 10 |  | √ | ' ' | 汇报类型,枚举: A :正常 B :返工 |
| 10 | freworkdrawqty | 汇报.关联返工数量 | numeric | 23 | 10 | √ | 0 | 汇报.关联返工数量 |
| 11 | fstockwastqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 12 | fpushreworkbaseqty | 汇报.已返工基本数量 | numeric | 23 | 10 | √ | 0 | 汇报.已返工基本数量 |
| 13 | fsumrepwastproqty | 汇报.累计汇报报废生产数量 | numeric | 23 | 10 | √ | 0 | 汇报.累计汇报报废生产数量 |
| 14 | fprocessunit | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fworkwastproqty | 工废生产数量 | numeric | 23 | 10 | √ | 0 | 工废生产数量 |
| 16 | fqualproqyt | 合格生产数量 | numeric | 23 | 10 | √ | 0 | 合格生产数量 |
| 17 | fstockwastproqty | 料废生产数量 | numeric | 23 | 10 | √ | 0 | 料废生产数量 |
| 18 | fsumrepwastbaseqty | 汇报.累计汇报报废基本数量 | numeric | 23 | 10 | √ | 0 | 汇报.累计汇报报废基本数量 |
| 19 | fsampledestorybaseqty | 样本破坏基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏基本数量 |
| 20 | fenddifbegin | 实际完工时间-实际开工时间 | int8 | 64 |  | √ | 0 | 实际完工时间-实际开工时间 |
| 21 | freworkqty | 待返工数量 | numeric | 23 | 10 | √ | 0 | 待返工数量 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 23 | ftobeinspectbaseqty | 待检基本数量 | numeric | 23 | 10 | √ | 0 | 待检基本数量 |
| 24 | fworkwastqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 25 | fwastbaseqty | 汇报.报废基本数量 | numeric | 23 | 10 | √ | 0 | 汇报.报废基本数量 |
| 26 | fsumrepwastqty | 汇报.累计汇报报废数量 | numeric | 23 | 10 | √ | 0 | 汇报.累计汇报报废数量 |
| 27 | fsampledestoryproqty | 样本破坏生产数量 | numeric | 23 | 10 | √ | 0 | 样本破坏生产数量 |
| 28 | fwastqty | 汇报.报废数量 | numeric | 23 | 10 | √ | 0 | 汇报.报废数量 |
| 29 | fplancompleteqty | 汇报.计划完成数量 | numeric | 23 | 10 | √ | 0 | 汇报.计划完成数量 |
| 30 | frewsreviewrowno | 汇报.返工来源汇报单行号 | int4 | 32 |  | √ | 0 | 汇报.返工来源汇报单行号 |
| 31 | fsumrepquaproqty | 汇报.累计汇报合格生产数量 | numeric | 23 | 10 | √ | 0 | 汇报.累计汇报合格生产数量 |
| 32 | fdamagebaseqty | 损耗基本数量 | numeric | 23 | 10 | √ | 0 | 损耗基本数量 |
| 33 | fpushreworkproqty | 汇报.已返工生产数量 | numeric | 23 | 10 | √ | 0 | 汇报.已返工生产数量 |
| 34 | ftobeinspectproqty | 待检生产数量 | numeric | 23 | 10 | √ | 0 | 待检生产数量 |
| 35 | fsumrepquabaseqty | 汇报.累计汇报合格基本数量 | numeric | 23 | 10 | √ | 0 | 汇报.累计汇报合格基本数量 |
| 36 | fmanudate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 37 | fpushreworkqty | 汇报.已返工数量 | numeric | 23 | 10 | √ | 0 | 汇报.已返工数量 |
| 38 | fplancompletebaseqty | 汇报.计划完成基本数量 | numeric | 23 | 10 | √ | 0 | 汇报.计划完成基本数量 |
| 39 | fqualbaseqyt | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 40 | freworkbaseqty | 待返工基本数量 | numeric | 23 | 10 | √ | 0 | 待返工基本数量 |
| 41 | ftobeinspectqty | 待检数量 | numeric | 23 | 10 | √ | 0 | 待检数量 |
| 42 | fcompletebaseqty | 完工基本数量 | numeric | 23 | 10 | √ | 0 | 完工基本数量 |
| 43 | freworkproqty | 待返工生产数量 | numeric | 23 | 10 | √ | 0 | 待返工生产数量 |
| 44 | fsampledestoryqty | 样本破坏数量 | numeric | 23 | 10 | √ | 0 | 样本破坏数量 |
| 45 | fcompleteproqty | 完工生产数量 | numeric | 23 | 10 | √ | 0 | 完工生产数量 |
| 46 | fcompleteqty | 完工数量 | numeric | 23 | 10 | √ | 0 | 完工数量 |
| 47 | fquaqyt | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 48 | fsumrepquaqty | 汇报.累计汇报合格数量 | numeric | 23 | 10 | √ | 0 | 汇报.累计汇报合格数量 |
| 49 | fdamageqty | 损耗数量 | numeric | 23 | 10 | √ | 0 | 损耗数量 |
| 50 | fendtime | 实际完工时间 | timestamp | 0 |  |  | null | 实际完工时间 |
| 51 | fwastproqty | 汇报.报废生产数量 | numeric | 23 | 10 | √ | 0 | 汇报.报废生产数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_reviewentry_r_id |  | fid |
| 2 | pk_t_sfc_reviewentry_r |  | fentryid |

---

## 工序汇报明细-分表 t_sfc_reviewentry_a

- **表名称：** 工序汇报明细-分表
- **表名：** t_sfc_reviewentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispal | 单据体.准备活动人工 | bpchar | 1 |  | √ | '0' | 单据体.准备活动人工 |
| 3 | fwamreportqty | 单据体.加工活动机器实际工时 | numeric | 23 | 10 | √ | 0 | 单据体.加工活动机器实际工时 |
| 4 | fpamreportqty | 单据体.准备活动机器实际工时 | numeric | 23 | 10 | √ | 0 | 单据体.准备活动机器实际工时 |
| 5 | fispam | 单据体.准备活动机器 | bpchar | 1 |  | √ | '0' | 单据体.准备活动机器 |
| 6 | fproplanentryid_ac | 工序计划分录_活动 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 7 | fpalreportqty7 | 单据体.其他活动一人工实际工时 | numeric | 23 | 10 | √ | 0 | 单据体.其他活动一人工实际工时 |
| 8 | frmresource | 准备活动机器*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 9 | fraresource | 准备活动人工*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 10 | fpamunit | 单据体.准备活动机器单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fomresource | 其他活动一机器*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 12 | foaresource | 其他活动一人工*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 13 | ftmresource | 其他活动二机器*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 14 | fpalunit | 单据体.准备活动人工单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fwalreportqty | 单据体.加工活动人工实际工时 | numeric | 23 | 10 | √ | 0 | 单据体.加工活动人工实际工时 |
| 16 | fiswal | 单据体.加工活动人工 | bpchar | 1 |  | √ | '0' | 单据体.加工活动人工 |
| 17 | fiswam | 单据体.加工活动机器 | bpchar | 1 |  | √ | '0' | 单据体.加工活动机器 |
| 18 | fpamreportqty8 | 单据体.其他活动二人工实际工时 | numeric | 23 | 10 | √ | 0 | 单据体.其他活动二人工实际工时 |
| 19 | ftaresource | 其他活动二人工*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 20 | funitfield8 | 单据体.其他活动二人工单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fpamreportqty4 | 单据体.其他活动二机器实际工时 | numeric | 23 | 10 | √ | 0 | 单据体.其他活动二机器实际工时 |
| 22 | funitfield3 | 单据体.其他活动一机器单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fpamreportqty3 | 单据体.其他活动一机器实际工时 | numeric | 23 | 10 | √ | 0 | 单据体.其他活动一机器实际工时 |
| 24 | fwalunit | 单据体.加工活动人工单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fpalreportqty | 单据体.准备活动人工实际工时 | numeric | 23 | 10 | √ | 0 | 单据体.准备活动人工实际工时 |
| 26 | funitfield7 | 单据体.其他活动一人工单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | funitfield4 | 单据体.其他活动二机器单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fispal4 | 单据体.其他活动二机器 | bpchar | 1 |  | √ | '0' | 单据体.其他活动二机器 |
| 29 | fiscomeup14 | 其他活动二机器是否来自上游 | bpchar | 1 |  | √ | '0' | 其他活动二机器是否来自上游 |
| 30 | fispal3 | 单据体.其他活动一机器 | bpchar | 1 |  | √ | '0' | 单据体.其他活动一机器 |
| 31 | fiscomeup3 | 加工人工是否来自上游 | bpchar | 1 |  | √ | '0' | 加工人工是否来自上游 |
| 32 | fwamunit | 单据体.加工活动机器单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | fiscomeup4 | 加工机器是否来自上游 | bpchar | 1 |  | √ | '0' | 加工机器是否来自上游 |
| 34 | fiscomeup13 | 其他活动一机器是否来自上游 | bpchar | 1 |  | √ | '0' | 其他活动一机器是否来自上游 |
| 35 | fiscomeup1 | 准备人工是否来自上游 | bpchar | 1 |  | √ | '0' | 准备人工是否来自上游 |
| 36 | fispal8 | 单据体.其他活动二人工 | bpchar | 1 |  | √ | '0' | 单据体.其他活动二人工 |
| 37 | fiscomeup18 | 其他活动二人工是否来自上游 | bpchar | 1 |  | √ | '0' | 其他活动二人工是否来自上游 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | fiscomeup2 | 准备机器是否来自上游 | bpchar | 1 |  | √ | '0' | 准备机器是否来自上游 |
| 40 | fispal7 | 单据体.其他活动一人工 | bpchar | 1 |  | √ | '0' | 单据体.其他活动一人工 |
| 41 | fpmresource | 加工活动机器*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 42 | fiscomeup17 | 其他活动一人工是否来自上游 | bpchar | 1 |  | √ | '0' | 其他活动一人工是否来自上游 |
| 43 | fparesource | 加工活动人工*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_reviewentry_a_id |  | fid |
| 2 | pk_t_sfc_reviewentry_a |  | fentryid |

---

## 工序汇报明细-分表 t_sfc_reviewentry_e

- **表名称：** 工序汇报明细-分表
- **表名：** t_sfc_reviewentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbadreturnbaseqty | 完工.待返工退库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.待返工退库基本数量 |
| 3 | fbadpushinbaseqty | 完工.关联待返工入库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.关联待返工入库基本数量 |
| 4 | fbadpushinproqty | 完工.关联待返工入库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.关联待返工入库生产数量 |
| 5 | fscrappushinproqty | 完工.关联报废品入库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.关联报废品入库生产数量 |
| 6 | fqualifiedinqty | 完工.合格品入库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.合格品入库生产数量 |
| 7 | fscrappushinbaseqty | 完工.关联报废品入库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.关联报废品入库基本数量 |
| 8 | freturnbaseqty | 完工.退库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.退库基本数量 |
| 9 | fscrapreturnbaseqty | 完工.报废品退库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.报废品退库基本数量 |
| 10 | fpushinproqty | 完工.关联入库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.关联入库生产数量 |
| 11 | finwarehouseorg | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | freturnproqty | 完工.退库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.退库生产数量 |
| 13 | fbadquabaseinqty | 完工.待返工入库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.待返工入库基本数量 |
| 14 | fcompleteinqty | 完工.入库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.入库生产数量 |
| 15 | fquareturnbaseqyt | 完工.合格品退库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.合格品退库基本数量 |
| 16 | fscrapreturnproqty | 完工.报废品退库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.报废品退库生产数量 |
| 17 | fquabaseinqyt | 完工.合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.合格品入库基本数量 |
| 18 | fbadqualifyinqty | 完工.待返工入库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.待返工入库生产数量 |
| 19 | fscrinwainqty | 完工.报废品入库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.报废品入库生产数量 |
| 20 | fquareturnproqyt | 完工.合格品退库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.合格品退库生产数量 |
| 21 | fquapushinbaseqyt | 完工.关联合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.关联合格品入库基本数量 |
| 22 | fpushinbaseqty | 完工.关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.关联入库基本数量 |
| 23 | fquapushinproqyt | 完工.关联合格品入库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.关联合格品入库生产数量 |
| 24 | fmaterialinvid | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 25 | fscrinwabaseinqty | 完工.报废品入库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.报废品入库基本数量 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 27 | fbadreturnproqty | 完工.待返工退库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.待返工退库生产数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_reviewentry_e |  | fentryid |
| 2 | idx_sfc_reviewentry_e_id |  | fid |

---

## 工序汇报明细-分表 t_sfc_reviewentry_i

- **表名称：** 工序汇报明细-分表
- **表名：** t_sfc_reviewentry_i

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjobtype | 作业类型 | bpchar | 1 |  | √ | ' ' | 作业类型,枚举: A :团队作业 B :个人作业 |
| 3 | fteamfactor | 团队计件系数 | numeric | 23 | 10 | √ | 0 | 团队计件系数 |
| 4 | fwalfixedworkqty | 单据体.准备活动人工定额工时 | numeric | 23 | 10 | √ | 0 | 单据体.准备活动人工定额工时 |
| 5 | fwamfixedworkqty | 单据体.准备活动机器定额工时 | numeric | 23 | 10 | √ | 0 | 单据体.准备活动机器定额工时 |
| 6 | fonemacworkhours | 单据体.其他活动一机器实际工时(秒) | numeric | 23 | 10 | √ | 0 | 单据体.其他活动一机器实际工时(秒) |
| 7 | finspectqty | 检验数量 | numeric | 23 | 10 | √ | 0 | 检验数量 |
| 8 | fpieceworktype | 计件工作量类型 | bpchar | 1 |  | √ | ' ' | 计件工作量类型,枚举: A :产品数量 B :活动工时 |
| 9 | fonelabworkhours | 单据体.其他活动一人工实际工时(秒) | numeric | 23 | 10 | √ | 0 | 单据体.其他活动一人工实际工时(秒) |
| 10 | fpamfixedworkqty | 单据体.加工活动机器定额工时 | numeric | 23 | 10 | √ | 0 | 单据体.加工活动机器定额工时 |
| 11 | fpalfixedworkqty | 单据体.加工活动人工定额工时 | numeric | 23 | 10 | √ | 0 | 单据体.加工活动人工定额工时 |
| 12 | flinkinspectqty | 关联检验数量 | numeric | 23 | 10 | √ | 0 | 关联检验数量 |
| 13 | flinkinproqty | 关联检验生产数量 | numeric | 23 | 10 | √ | 0 | 关联检验生产数量 |
| 14 | fprocmacworkhours | 单据体.加工活动机器实际工时(秒) | numeric | 23 | 10 | √ | 0 | 单据体.加工活动机器实际工时(秒) |
| 15 | fproclabworkhours | 单据体.加工活动人工实际工时(秒) | numeric | 23 | 10 | √ | 0 | 单据体.加工活动人工实际工时(秒) |
| 16 | finspectplan | 检验方案(废弃) | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 17 | finspectplanrowid | 检验方案分录id | int8 | 64 |  | √ | 0 | 检验方案分录id |
| 18 | flinkinbaseqty | 关联检验基本数量 | numeric | 23 | 10 | √ | 0 | 关联检验基本数量 |
| 19 | finspectproqty | 检验生产数量 | numeric | 23 | 10 | √ | 0 | 检验生产数量 |
| 20 | fproinspect | 工序检验 | bpchar | 1 |  | √ | '0' | 工序检验 |
| 21 | finspectbaseqty | 检验基本数量 | numeric | 23 | 10 | √ | 0 | 检验基本数量 |
| 22 | fsumpieceamount | 总预计金额 | numeric | 23 | 10 | √ | 0 | 总预计金额 |
| 23 | finspectschemeid | 检验方案编码 | int8 | 64 |  | √ | 0 | [检验方案 qcbd_inspectpro](../qcbd_files/qcbd_inspectpro.md) |
| 24 | finspectcompletedate | 期望检验完成日期 | timestamp | 0 |  |  | null | 期望检验完成日期 |
| 25 | ftalfixedworkqty | 单据体.其他活动二人工定额工时 | numeric | 23 | 10 | √ | 0 | 单据体.其他活动二人工定额工时 |
| 26 | ftwolabworkhours | 单据体.其他活动二人工实际工时(秒) | numeric | 23 | 10 | √ | 0 | 单据体.其他活动二人工实际工时(秒) |
| 27 | foamfixedworkqty | 单据体.其他活动一机器定额工时 | numeric | 23 | 10 | √ | 0 | 单据体.其他活动一机器定额工时 |
| 28 | fteamid | 团队 | int8 | 64 |  | √ | 0 | [制造团队 mpdm_mftteam](../mpdm_files/mpdm_mftteam.md) |
| 29 | foalfixedworkqty | 单据体.其他活动一人工定额工时 | numeric | 23 | 10 | √ | 0 | 单据体.其他活动一人工定额工时 |
| 30 | fprepmacworkhours | 单据体.准备活动机器实际工时(秒) | numeric | 23 | 10 | √ | 0 | 单据体.准备活动机器实际工时(秒) |
| 31 | ftwomacworkhours | 单据体.其他活动二机器实际工时(秒) | numeric | 23 | 10 | √ | 0 | 单据体.其他活动二机器实际工时(秒) |
| 32 | finspectuserid | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | ftamfixedworkqty | 单据体.其他活动二机器定额工时 | numeric | 23 | 10 | √ | 0 | 单据体.其他活动二机器定额工时 |
| 34 | ffirstinspect | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 35 | finspectdepid | 质检部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fisurgent | 加急 | bpchar | 1 |  | √ | '0' | 加急 |
| 37 | finspectorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | fhaspushpiece | 已下推计件工作量 | bpchar | 1 |  | √ | '0' | 已下推计件工作量 |
| 40 | fpreplabworkhours | 单据体.准备活动人工实际工时(秒) | numeric | 23 | 10 | √ | 0 | 单据体.准备活动人工实际工时(秒) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_reviewentry_i |  | fentryid |
| 2 | idx_sfc_reviewentry_i_id |  | fid |

---

## 关联子实体-子表 t_sfc_reviewentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_reviewentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | freworkqty_old | 待返工数量_原始携带值 | numeric | 23 | 10 |  | null | 待返工数量_原始携带值 |
| 2 | fwamreportqty_old | 单据体.加工活动机器实际工时_原始携带值 | numeric | 23 | 10 |  | null | 单据体.加工活动机器实际工时_原始携带值 |
| 3 | fwamreportqty | 单据体.加工活动机器实际工时_确认携带值 | numeric | 23 | 10 |  | null | 单据体.加工活动机器实际工时_确认携带值 |
| 4 | fpamreportqty | 单据体.准备活动机器实际工时_确认携带值 | numeric | 23 | 10 |  | null | 单据体.准备活动机器实际工时_确认携带值 |
| 5 | fpushreworkqty_old | fpushreworkqty_old | numeric | 23 | 10 |  | null |  |
| 6 | fworkwastqty | fworkwastqty | numeric | 23 | 10 |  | null |  |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fsumrepwastqty | fsumrepwastqty | numeric | 23 | 10 |  | null |  |
| 9 | fplancompleteqty | fplancompleteqty | numeric | 23 | 10 |  | null |  |
| 10 | fworkwastqty_old | fworkwastqty_old | numeric | 23 | 10 |  | null |  |
| 11 | fsumrepquaqty_old | fsumrepquaqty_old | numeric | 23 | 10 |  | null |  |
| 12 | fplancompleteqty_old | fplancompleteqty_old | numeric | 23 | 10 |  | null |  |
| 13 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 14 | fwalreportqty | 单据体.加工活动人工实际工时_确认携带值 | numeric | 23 | 10 |  | null | 单据体.加工活动人工实际工时_确认携带值 |
| 15 | fstockwastqty | fstockwastqty | numeric | 23 | 10 |  | null |  |
| 16 | fwalreportqty_old | 单据体.加工活动人工实际工时_原始携带值 | numeric | 23 | 10 |  | null | 单据体.加工活动人工实际工时_原始携带值 |
| 17 | fpushreworkqty | fpushreworkqty | numeric | 23 | 10 |  | null |  |
| 18 | freworkbaseqty | 待返工基本数量_确认携带值 | numeric | 23 | 10 |  | null | 待返工基本数量_确认携带值 |
| 19 | fpamreportqty_old | 单据体.准备活动机器实际工时_原始携带值 | numeric | 23 | 10 |  | null | 单据体.准备活动机器实际工时_原始携带值 |
| 20 | fpalreportqty_old | 单据体.准备活动人工实际工时_原始携带值 | numeric | 23 | 10 |  | null | 单据体.准备活动人工实际工时_原始携带值 |
| 21 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 22 | fstockwastqty_old | fstockwastqty_old | numeric | 23 | 10 |  | null |  |
| 23 | fpalreportqty | 单据体.准备活动人工实际工时_确认携带值 | numeric | 23 | 10 |  | null | 单据体.准备活动人工实际工时_确认携带值 |
| 24 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 25 | fquaqyt_old | fquaqyt_old | numeric | 23 | 10 |  | null |  |
| 26 | freworkbaseqty_old | 待返工基本数量_原始携带值 | numeric | 23 | 10 |  | null | 待返工基本数量_原始携带值 |
| 27 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 28 | freworkqty | 待返工数量_确认携带值 | numeric | 23 | 10 |  | null | 待返工数量_确认携带值 |
| 29 | fquaqyt | fquaqyt | numeric | 23 | 10 |  | null |  |
| 30 | fsumrepquaqty | fsumrepquaqty | numeric | 23 | 10 |  | null |  |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 32 | fsumrepwastqty_old | fsumrepwastqty_old | numeric | 23 | 10 |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_reviewentry_lk |  | fpkid |
| 2 | idx_sfc_reviewentry_lk_fk |  | fentryid |

---

## 工序汇报单-反写记录表 t_sfc_processreview_wb

- **表名称：** 工序汇报单-反写记录表
- **表名：** t_sfc_processreview_wb

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
| 1 | pk_sfc_processreview_wb |  | fentryid |
| 2 | idx_sfc_processreview_wb_fk |  | fid |

---

## 工序汇报单-关联追踪表 t_sfc_processreview_tc

- **表名称：** 工序汇报单-关联追踪表
- **表名：** t_sfc_processreview_tc

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
| 1 | idx_sfc_processreview_tc_tbill |  | ftbillid |
| 2 | pk_sfc_processreview_tc |  | fid |
| 3 | idx_sfc_processreview_tc_tid |  | ftid |
