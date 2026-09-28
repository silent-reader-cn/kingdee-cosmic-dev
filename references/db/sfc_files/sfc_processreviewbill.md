# 工序汇报单-sfc_processreviewbill

## 单据体-子表 t_sfc_reviewentry

- **表名称：** 单据体-子表
- **表名：** t_sfc_reviewentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freworksection | 返工来源工序段 | varchar | 1000 |  | √ | ' ' | 返工来源工序段 |
| 3 | frelationid | 代码生成id(关联id) | int8 | 64 |  | √ | 0 | 代码生成id(关联id) |
| 4 | fsequencetype | 工序序列类型 | bpchar | 1 |  | √ | ' ' | 工序序列类型,枚举: A :并行序列 B :返工序列 C :主干序列 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | ftracknoid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 8 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | frwsprocessno | frwsprocessno | int4 | 32 |  | √ | 0 |  |
| 10 | frewsreviewno | frewsreviewno | varchar | 80 |  | √ | ' ' |  |
| 11 | freporttype | freporttype | varchar | 10 |  | √ | ' ' |  |
| 12 | fsbilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 13 | fcorebillrow | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 14 | fcorebilltype | 核心单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 15 | fstockwastqty | fstockwastqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | fprocessunit | fprocessunit | int8 | 64 |  | √ | 0 |  |
| 17 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 18 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 19 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 21 | fclassgroup | 班组 | int8 | 64 |  | √ | 0 | 班组 mpdm_classgroup |
| 22 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 23 | freworksequence | 返工来源序列号 | int8 | 64 |  | √ | 0 | 返工来源序列号 |
| 24 | freworkqty | freworkqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fcorebillrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 27 | fproplanid | 工序计划内码 | int8 | 64 |  | √ | 0 | 工序计划F7 sfc_processplan_f7 |
| 28 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 29 | fupprocessid | 上工序id | varchar | 1000 |  | √ | ' ' | 上工序id |
| 30 | fworkwastqty | fworkwastqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 32 | fsumrepwastqty | fsumrepwastqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fmaterielid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 34 | fplancompleteqty | fplancompleteqty | numeric | 23 | 10 | √ | 0 |  |
| 35 | fwastqty | fwastqty | numeric | 23 | 10 | √ | 0 |  |
| 36 | frewsreviewrowno | frewsreviewrowno | int4 | 32 |  | √ | 0 |  |
| 37 | fsecunitid | 产品辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 38 | fclasssystem | 班制 | int8 | 64 |  | √ | 0 | 班制 mpdm_classsystem |
| 39 | fsbillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 40 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 41 | fpushreworkqty | fpushreworkqty | numeric | 23 | 10 | √ | 0 |  |
| 42 | fnextprocessid | 下工序id | varchar | 1000 |  | √ | ' ' | 下工序id |
| 43 | fproducttype | 产品类型 | varchar | 10 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 44 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | 工序计划分录F7 sfc_processplanentry_f7 |
| 45 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 46 | fquaqyt | fquaqyt | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsumrepquaqty | fsumrepquaqty | numeric | 23 | 10 | √ | 0 |  |
| 48 | fproplanbillid | 工序计划 | int8 | 64 |  | √ | 0 | 工序计划 sfc_processplanbill |
| 49 | fproplanno | 工序计划号 | varchar | 80 |  | √ | ' ' | 工序计划号 |
| 50 | fprocesscenter | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心 sfc_workcenter |
| 51 | freworkprocesses | 返工来源工序 | int8 | 64 |  | √ | 0 | 返工来源工序 |

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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 设备 sfc_equipment |
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
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fworkshopid | 生产车间(隐藏) | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 10 | fprocessorg | 加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fprocessdepartid | 加工车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fpostdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 17 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

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
| 1 | fworkloadrate | 工作量比例 | numeric | 23 | 10 | √ | 1 | 工作量比例 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fuserid | 工号 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpercentage | 百分比 | numeric | 23 | 10 | √ | 0 | 百分比 |

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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
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

## 单据体-分表 t_sfc_reviewentry_r

- **表名称：** 单据体-分表
- **表名：** t_sfc_reviewentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frewsprocessno | 汇报.返工来源工序号 | int4 | 32 |  | √ | 0 | 汇报.返工来源工序号 |
| 3 | fstockwastbaseqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |
| 4 | ftobeinspectbaseqty | 待检基本数量 | numeric | 23 | 10 | √ | 0 | 待检基本数量 |
| 5 | fworkwastqty | 工废数 | numeric | 23 | 10 | √ | 0 | 工废数 |
| 6 | fwastbaseqty | 汇报.报废基本数量 | numeric | 23 | 10 | √ | 0 | 汇报.报废基本数量 |
| 7 | fsumrepwastqty | 汇报.累计汇报报废数量 | numeric | 23 | 10 | √ | 0 | 汇报.累计汇报报废数量 |
| 8 | fwastqty | 汇报.报废数量 | numeric | 23 | 10 | √ | 0 | 汇报.报废数量 |
| 9 | fplancompleteqty | 汇报.计划完成数量 | numeric | 23 | 10 | √ | 0 | 汇报.计划完成数量 |
| 10 | frewsreviewrowno | 汇报.返工来源汇报单行号 | int4 | 32 |  | √ | 0 | 汇报.返工来源汇报单行号 |
| 11 | fsumrepquaproqty | 汇报.累计汇报合格生产数量 | numeric | 23 | 10 | √ | 0 | 汇报.累计汇报合格生产数量 |
| 12 | fpushreworkproqty | 汇报.已返工生产数量 | numeric | 23 | 10 | √ | 0 | 汇报.已返工生产数量 |
| 13 | fbegintime | 实际开工时间 | timestamp | 0 |  |  | null | 实际开工时间 |
| 14 | ftobeinspectproqty | 待检生产数量 | numeric | 23 | 10 | √ | 0 | 待检生产数量 |
| 15 | frewsreviewno | 汇报.返工来源汇报单 | varchar | 80 |  | √ | ' ' | 汇报.返工来源汇报单 |
| 16 | fplancompleteproqty | 汇报.计划完成生产数量 | numeric | 23 | 10 | √ | 0 | 汇报.计划完成生产数量 |
| 17 | fworkwastbaseqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 18 | freporttype | 汇报类型 | varchar | 10 |  | √ | ' ' | 汇报类型,枚举: A :正常 B :返工 |
| 19 | fsumrepquabaseqty | 汇报.累计汇报合格基本数量 | numeric | 23 | 10 | √ | 0 | 汇报.累计汇报合格基本数量 |
| 20 | freworkdrawqty | 汇报.关联返工数量 | numeric | 23 | 10 | √ | 0 | 汇报.关联返工数量 |
| 21 | fstockwastqty | 料废数 | numeric | 23 | 10 | √ | 0 | 料废数 |
| 22 | fpushreworkqty | 汇报.已返工数量 | numeric | 23 | 10 | √ | 0 | 汇报.已返工数量 |
| 23 | fplancompletebaseqty | 汇报.计划完成基本数量 | numeric | 23 | 10 | √ | 0 | 汇报.计划完成基本数量 |
| 24 | fpushreworkbaseqty | 汇报.已返工基本数量 | numeric | 23 | 10 | √ | 0 | 汇报.已返工基本数量 |
| 25 | fsumrepwastproqty | 汇报.累计汇报报废生产数量 | numeric | 23 | 10 | √ | 0 | 汇报.累计汇报报废生产数量 |
| 26 | fqualbaseqyt | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 27 | freworkbaseqty | 待返工基本数量 | numeric | 23 | 10 | √ | 0 | 待返工基本数量 |
| 28 | fprocessunit | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 29 | ftobeinspectqty | 待检数 | numeric | 23 | 10 | √ | 0 | 待检数 |
| 30 | fcompletebaseqty | 完工基本数量 | numeric | 23 | 10 | √ | 0 | 完工基本数量 |
| 31 | fworkwastproqty | 工废生产数量 | numeric | 23 | 10 | √ | 0 | 工废生产数量 |
| 32 | freworkproqty | 待返工生产数量 | numeric | 23 | 10 | √ | 0 | 待返工生产数量 |
| 33 | fqualproqyt | 合格生产数量 | numeric | 23 | 10 | √ | 0 | 合格生产数量 |
| 34 | fstockwastproqty | 料废生产数量 | numeric | 23 | 10 | √ | 0 | 料废生产数量 |
| 35 | fsumrepwastbaseqty | 汇报.累计汇报报废基本数量 | numeric | 23 | 10 | √ | 0 | 汇报.累计汇报报废基本数量 |
| 36 | fcompleteproqty | 完工生产数量 | numeric | 23 | 10 | √ | 0 | 完工生产数量 |
| 37 | fcompleteqty | 完工数 | numeric | 23 | 10 | √ | 0 | 完工数 |
| 38 | freworkqty | 待返工数 | numeric | 23 | 10 | √ | 0 | 待返工数 |
| 39 | fquaqyt | 合格数 | numeric | 23 | 10 | √ | 0 | 合格数 |
| 40 | fsumrepquaqty | 汇报.累计汇报合格数量 | numeric | 23 | 10 | √ | 0 | 汇报.累计汇报合格数量 |
| 41 | fendtime | 实际完工时间 | timestamp | 0 |  |  | null | 实际完工时间 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 43 | fwastproqty | 汇报.报废生产数量 | numeric | 23 | 10 | √ | 0 | 汇报.报废生产数量 |

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

## 单据体-分表 t_sfc_reviewentry_a

- **表名称：** 单据体-分表
- **表名：** t_sfc_reviewentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispal | 单据体.准备活动人工 | bpchar | 1 |  | √ | '0' | 单据体.准备活动人工 |
| 3 | fwamreportqty | 单据体.加工活动机器汇报数量 | numeric | 23 | 10 | √ | 0 | 单据体.加工活动机器汇报数量 |
| 4 | fpamreportqty | 单据体.准备活动机器活动汇报数量 | numeric | 23 | 10 | √ | 0 | 单据体.准备活动机器活动汇报数量 |
| 5 | fispam | 单据体.准备活动机器 | bpchar | 1 |  | √ | '0' | 单据体.准备活动机器 |
| 6 | fproplanentryid_ac | 工序计划分录_活动 | int8 | 64 |  | √ | 0 | 工序计划分录F7 sfc_processplanentry_f7 |
| 7 | fpalreportqty7 | 单据体.其他活动一人工汇报数量 | numeric | 23 | 10 | √ | 0 | 单据体.其他活动一人工汇报数量 |
| 8 | frmresource | 准备活动机器*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 9 | fraresource | 准备活动人工*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 10 | fpamunit | 单据体.准备活动机器单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fomresource | 其他活动一机器*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 12 | foaresource | 其他活动一人工*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 13 | ftmresource | 其他活动二机器*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 14 | fpalunit | 单据体.准备活动人工单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fwalreportqty | 单据体.加工活动人工汇报数量 | numeric | 23 | 10 | √ | 0 | 单据体.加工活动人工汇报数量 |
| 16 | fiswal | 单据体.加工活动人工 | bpchar | 1 |  | √ | '0' | 单据体.加工活动人工 |
| 17 | fiswam | 单据体.加工活动机器 | bpchar | 1 |  | √ | '0' | 单据体.加工活动机器 |
| 18 | fpamreportqty8 | 单据体.其他活动二人工汇报数量 | numeric | 23 | 10 | √ | 0 | 单据体.其他活动二人工汇报数量 |
| 19 | ftaresource | 其他活动二人工*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 20 | funitfield8 | 单据体.其他活动二人工单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fpamreportqty4 | 单据体.其他活动二机器汇报数量 | numeric | 23 | 10 | √ | 0 | 单据体.其他活动二机器汇报数量 |
| 22 | funitfield3 | 单据体.其他活动一机器单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fpamreportqty3 | 单据体.其他活动一机器汇报数量 | numeric | 23 | 10 | √ | 0 | 单据体.其他活动一机器汇报数量 |
| 24 | fwalunit | 单据体.加工活动人工单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fpalreportqty | 单据体.准备活动人工活动汇报数量 | numeric | 23 | 10 | √ | 0 | 单据体.准备活动人工活动汇报数量 |
| 26 | funitfield7 | 单据体.其他活动一人工单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | funitfield4 | 单据体.其他活动二机器单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fispal4 | 单据体.其他活动二机器 | bpchar | 1 |  | √ | '0' | 单据体.其他活动二机器 |
| 29 | fiscomeup14 | 其他活动二机器是否来自上游 | bpchar | 1 |  | √ | '0' | 其他活动二机器是否来自上游 |
| 30 | fispal3 | 单据体.其他活动一机器 | bpchar | 1 |  | √ | '0' | 单据体.其他活动一机器 |
| 31 | fiscomeup3 | 加工人工是否来自上游 | bpchar | 1 |  | √ | '0' | 加工人工是否来自上游 |
| 32 | fwamunit | 单据体.加工活动机器单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 33 | fiscomeup4 | 加工机器是否来自上游 | bpchar | 1 |  | √ | '0' | 加工机器是否来自上游 |
| 34 | fiscomeup13 | 其他活动一机器是否来自上游 | bpchar | 1 |  | √ | '0' | 其他活动一机器是否来自上游 |
| 35 | fiscomeup1 | 准备人工是否来自上游 | bpchar | 1 |  | √ | '0' | 准备人工是否来自上游 |
| 36 | fispal8 | 单据体.其他活动二人工 | bpchar | 1 |  | √ | '0' | 单据体.其他活动二人工 |
| 37 | fiscomeup18 | 其他活动二人工是否来自上游 | bpchar | 1 |  | √ | '0' | 其他活动二人工是否来自上游 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | fiscomeup2 | 准备机器是否来自上游 | bpchar | 1 |  | √ | '0' | 准备机器是否来自上游 |
| 40 | fispal7 | 单据体.其他活动一人工 | bpchar | 1 |  | √ | '0' | 单据体.其他活动一人工 |
| 41 | fpmresource | 加工活动机器*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 42 | fiscomeup17 | 其他活动一人工是否来自上游 | bpchar | 1 |  | √ | '0' | 其他活动一人工是否来自上游 |
| 43 | fparesource | 加工活动人工*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |

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

## 单据体-分表 t_sfc_reviewentry_e

- **表名称：** 单据体-分表
- **表名：** t_sfc_reviewentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fquabaseinqyt | 完工.合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.合格品入库基本数量 |
| 3 | fpushinbaseqty | 完工入库.下推入库基本数量 | numeric | 23 | 10 | √ | 0 | 完工入库.下推入库基本数量 |
| 4 | finwarehouseorg | 入库组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbadqualifyinqty | 完工.待返工入库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.待返工入库生产数量 |
| 6 | fscrinwainqty | 完工.报废品入库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.报废品入库生产数量 |
| 7 | fqualifiedinqty | 完工.合格品入库生产数量 | numeric | 23 | 10 | √ | 0 | 完工.合格品入库生产数量 |
| 8 | fscrinwabaseinqty | 完工.报废品入库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.报废品入库基本数量 |
| 9 | fbadquabaseinqty | 完工.待返工入库基本数量 | numeric | 23 | 10 | √ | 0 | 完工.待返工入库基本数量 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fcompleteinqty | 完工入库.完工入库生产数量 | numeric | 23 | 10 | √ | 0 | 完工入库.完工入库生产数量 |

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

## 单据体-分表 t_sfc_reviewentry_i

- **表名称：** 单据体-分表
- **表名：** t_sfc_reviewentry_i

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finspectqty | 检验数量 | numeric | 23 | 10 | √ | 0 | 检验数量 |
| 3 | fproinspect | 工序检验 | bpchar | 1 |  | √ | '0' | 工序检验 |
| 4 | finspectbaseqty | 检验基本数量 | numeric | 23 | 10 | √ | 0 | 检验基本数量 |
| 5 | flinkinspectqty | 关联检验数量 | numeric | 23 | 10 | √ | 0 | 关联检验数量 |
| 6 | flinkinproqty | 关联检验生产数量 | numeric | 23 | 10 | √ | 0 | 关联检验生产数量 |
| 7 | finspectuserid | 质检员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | finspectplan | 检验方案(废弃) | int8 | 64 |  | √ | 0 | 工作中心 sfc_workcenter |
| 9 | flinkinbaseqty | 关联检验基本数量 | numeric | 23 | 10 | √ | 0 | 关联检验基本数量 |
| 10 | finspectproqty | 检验生产数量 | numeric | 23 | 10 | √ | 0 | 检验生产数量 |
| 11 | finspectdepid | 质检部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | finspectorg | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

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
| 1 | freworkqty_old | 待返工数_原始携带值 | numeric | 23 | 10 |  | null | 待返工数_原始携带值 |
| 2 | fwamreportqty_old | 单据体.加工活动机器汇报数量_原始携带值 | numeric | 23 | 10 |  | null | 单据体.加工活动机器汇报数量_原始携带值 |
| 3 | fwamreportqty | 单据体.加工活动机器汇报数量_确认携带值 | numeric | 23 | 10 |  | null | 单据体.加工活动机器汇报数量_确认携带值 |
| 4 | fpamreportqty | 单据体.准备活动机器活动汇报数量_确认携带值 | numeric | 23 | 10 |  | null | 单据体.准备活动机器活动汇报数量_确认携带值 |
| 5 | fpushreworkqty_old | fpushreworkqty_old | numeric | 23 | 10 |  | null |  |
| 6 | fworkwastqty | fworkwastqty | numeric | 23 | 10 |  | null |  |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fsumrepwastqty | fsumrepwastqty | numeric | 23 | 10 |  | null |  |
| 9 | fplancompleteqty | fplancompleteqty | numeric | 23 | 10 |  | null |  |
| 10 | fworkwastqty_old | fworkwastqty_old | numeric | 23 | 10 |  | null |  |
| 11 | fsumrepquaqty_old | fsumrepquaqty_old | numeric | 23 | 10 |  | null |  |
| 12 | fplancompleteqty_old | fplancompleteqty_old | numeric | 23 | 10 |  | null |  |
| 13 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 14 | fwalreportqty | 单据体.加工活动人工汇报数量_确认携带值 | numeric | 23 | 10 |  | null | 单据体.加工活动人工汇报数量_确认携带值 |
| 15 | fstockwastqty | fstockwastqty | numeric | 23 | 10 |  | null |  |
| 16 | fwalreportqty_old | 单据体.加工活动人工汇报数量_原始携带值 | numeric | 23 | 10 |  | null | 单据体.加工活动人工汇报数量_原始携带值 |
| 17 | fpushreworkqty | fpushreworkqty | numeric | 23 | 10 |  | null |  |
| 18 | freworkbaseqty | 待返工基本数量_确认携带值 | numeric | 23 | 10 |  | null | 待返工基本数量_确认携带值 |
| 19 | fpamreportqty_old | 单据体.准备活动机器活动汇报数量_原始携带值 | numeric | 23 | 10 |  | null | 单据体.准备活动机器活动汇报数量_原始携带值 |
| 20 | fpalreportqty_old | 单据体.准备活动人工活动汇报数量_原始携带值 | numeric | 23 | 10 |  | null | 单据体.准备活动人工活动汇报数量_原始携带值 |
| 21 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 22 | fstockwastqty_old | fstockwastqty_old | numeric | 23 | 10 |  | null |  |
| 23 | fpalreportqty | 单据体.准备活动人工活动汇报数量_确认携带值 | numeric | 23 | 10 |  | null | 单据体.准备活动人工活动汇报数量_确认携带值 |
| 24 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 25 | fquaqyt_old | fquaqyt_old | numeric | 23 | 10 |  | null |  |
| 26 | freworkbaseqty_old | 待返工基本数量_原始携带值 | numeric | 23 | 10 |  | null | 待返工基本数量_原始携带值 |
| 27 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 28 | freworkqty | 待返工数_确认携带值 | numeric | 23 | 10 |  | null | 待返工数_确认携带值 |
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
