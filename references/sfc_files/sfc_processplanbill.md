# 工序计划-sfc_processplanbill

## 工序计划明细-子表 t_sfc_processplanentry

- **表名称：** 工序计划明细-子表
- **表名：** t_sfc_processplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freworksection | 返工来源工序段 | varchar | 1000 |  | √ | ' ' | 返工来源工序段 |
| 3 | frelationid | 代码生成id(关联id) | int8 | 64 |  | √ | 0 | 代码生成id(关联id) |
| 4 | fislastprocess | 末序 | bpchar | 1 |  | √ | '0' | 末序 |
| 5 | fprocessqty | 工序数量 | numeric | 23 | 10 | √ | 0 | 工序数量 |
| 6 | fprocesscontrolcode | 工序控制码 | int8 | 64 |  | √ | 0 | 工序控制码 mpdm_processcontrolcode |
| 7 | fsequencetype | 工序序列类型 | bpchar | 1 |  | √ | ' ' | 工序序列类型,枚举: A :并行序列 B :返工序列 C :主干序列 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | freportsbqty | freportsbqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | fprocessroutid | 工艺路线id | int8 | 64 |  | √ | 0 | 工艺路线 mpdm_sfcprocessroute |
| 11 | fbegintime | fbegintime | timestamp | 0 |  |  | null |  |
| 12 | fupprocesstype | 上工序类型 | varchar | 10 |  | √ | ' ' | 上工序类型,枚举: A :单个 B :多个 C :群组 |
| 13 | fisfirstprocess | 首序 | bpchar | 1 |  | √ | '0' | 首序 |
| 14 | flowerqty | flowerqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | fprocessdepartid | 加工车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | freworkplanqty | 返工计划数量 | numeric | 23 | 10 | √ | 0 | 返工计划数量 |
| 17 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 18 | ftobereworkedqty | ftobereworkedqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | fprocessinfocode | 工序编码 | varchar | 30 |  | √ | ' ' | 工序编码 |
| 20 | fprocessunit | 单据体.工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | freworkedqty | freworkedqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fhigherqty | fhigherqty | numeric | 23 | 10 | √ | 0 |  |
| 23 | fprocessorg | 加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fplanbegintime | 计划开工日期(可修改) | timestamp | 0 |  |  | null | 计划开工日期(可修改) |
| 25 | freworksequence | 返工来源序列号 | int8 | 64 |  | √ | 0 | 返工来源序列号 |
| 26 | fsumquaqyt | fsumquaqyt | numeric | 23 | 10 | √ | 0 |  |
| 27 | fplanendtime1 | 计划完工日期(上游带入不可改) | timestamp | 0 |  |  | null | 计划完工日期(上游带入不可改) |
| 28 | fpromethod | 加工类型 | varchar | 10 |  | √ | ' ' | 加工类型,枚举: 1 :厂内加工 2 :内协加工 3 :委外加工 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fsumstockwastqty | fsumstockwastqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | fprocesssequence | 序列号 | int8 | 64 |  | √ | 0 | 序列号 |
| 32 | fintoqty | fintoqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fbasebsqty | 基本批量 | numeric | 23 | 10 | √ | 0 | 基本批量 |
| 34 | fupprocessid | 上工序id | varchar | 1000 |  | √ | ' ' | 上工序id |
| 35 | freportmethod | 汇报控制 | varchar | 10 |  | √ | ' ' | 汇报控制,枚举: no :不汇报 must :必须汇报 |
| 36 | frevoveryqty | frevoveryqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fprocessinstructions | 工序说明 | varchar | 512 |  | √ | ' ' | 工序说明 |
| 38 | foutsourcedqty | foutsourcedqty | numeric | 23 | 10 | √ | 0 |  |
| 39 | fprocesscode | 工序 | int8 | 64 |  | √ | 0 | 标准工序 mpdm_normprocess |
| 40 | fsumworkwastqty | fsumworkwastqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | freportordercontrol | 汇报顺序控制 | bpchar | 1 |  | √ | ' ' | 汇报顺序控制,枚举: A :不控制 B :警告 C :严格控制 |
| 42 | fnextprocessid | 下工序id | varchar | 1000 |  | √ | ' ' | 下工序id |
| 43 | fcompleteqty | fcompleteqty | numeric | 23 | 10 | √ | 0 |  |
| 44 | fismilestone | 里程碑 | bpchar | 1 |  | √ | '0' | 里程碑 |
| 45 | fplanbegintime1 | 计划开工日期(上游带入不可改) | timestamp | 0 |  |  | null | 计划开工日期(上游带入不可改) |
| 46 | fprocesstatus | 工序状态 | varchar | 10 |  | √ | ' ' | 工序状态,枚举: A :计划 B :下达 C :开工 D :完工 |
| 47 | fplanendtime | 计划完工日期(可修改) | timestamp | 0 |  |  | null | 计划完工日期(可修改) |
| 48 | fismainprocess | 主工序 | bpchar | 1 |  | √ | '0' | 主工序 |
| 49 | fendtime | fendtime | timestamp | 0 |  |  | null |  |
| 50 | fprocesscenter | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心 sfc_workcenter |
| 51 | freworkprocesses | 返工来源工序 | int8 | 64 |  | √ | 0 | 返工来源工序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processplanentry |  | fentryid |
| 2 | idx_sfc_plane_id |  | fid |

---

## 关联子实体-子表 t_sfc_processplan_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_processplan_lk

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
| 1 | idx_sfc_processplan_lk_fk |  | fid |
| 2 | pk_sfc_processplan_lk |  | fpkid |

---

## 工序计划-主表 t_sfc_processplan

- **表名称：** 工序计划-主表
- **表名：** t_sfc_processplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprocessrout | 工艺路线 | int8 | 64 |  | √ | 0 | 工艺路线 mpdm_sfcprocessroute |
| 3 | fworkentryf7 | 生产工单分录 | int8 | 64 |  | √ | 0 | 生产工单分录F7 sfc_mftorder_f7 |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 6 | fworkshop | 生产车间(隐藏) | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 7 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 9 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fworkid | 工单id | int8 | 64 |  | √ | 0 | 工单id |
| 13 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fprojno | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 15 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 16 | fworkrowid | 工单行id | int8 | 64 |  | √ | 0 | 工单行id |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fworkn | 工单号 | varchar | 50 |  | √ | ' ' | 工单号 |
| 19 | fmaterial | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 20 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 21 | fcorebilltype | 核心单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 22 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 23 | fsourcebillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 24 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fsourcebilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 28 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 33 | fworkrown | 工单行号 | int4 | 32 |  | √ | 0 | 工单行号 |
| 34 | fsourcebillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 35 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 36 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | funit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 39 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 40 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_pplan_wid |  | fworkid |
| 2 | pk_t_sfc_processplan |  | fid |

---

## 工序计划-反写记录表 t_sfc_processplan_wb

- **表名称：** 工序计划-反写记录表
- **表名：** t_sfc_processplan_wb

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
| 1 | pk_sfc_processplan_wb |  | fentryid |
| 2 | idx_sfc_processplan_wb_fk |  | fid |

---

## 工序计划明细-分表 t_sfc_processplanentry_c

- **表名称：** 工序计划明细-分表
- **表名：** t_sfc_processplanentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fintoqty | 内协转入数量 | numeric | 23 | 10 | √ | 0 | 内协转入数量 |
| 3 | fsumworkwastbaseqty | 累计工废基本数量 | numeric | 23 | 10 | √ | 0 | 累计工废基本数量 |
| 4 | fsumcompleteqty | fsumcompleteqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | freportsbqty | 关联汇报数量 | numeric | 23 | 10 | √ | 0 | 关联汇报数量 |
| 6 | ftobereworkedbaseqty | 待返工基本数量 | numeric | 23 | 10 | √ | 0 | 待返工基本数量 |
| 7 | freportmethod | freportmethod | varchar | 10 |  | √ | ' ' |  |
| 8 | fsumcompletebaseqty | fsumcompletebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | fheadunitfactor | 生产单位换算系数 | int4 | 32 |  | √ | 0 | 生产单位换算系数 |
| 10 | fbegintime | 实际开工时间 | timestamp | 0 |  |  | null | 实际开工时间 |
| 11 | fsumworkwastproqty | 累计工废生产数量 | numeric | 23 | 10 | √ | 0 | 累计工废生产数量 |
| 12 | frevoveryqty | 委外接收数量 | numeric | 23 | 10 | √ | 0 | 委外接收数量 |
| 13 | ftobeinspectproqty | 待检生产数量 | numeric | 23 | 10 | √ | 0 | 待检生产数量 |
| 14 | foutsourcedqty | 委外发出数量 | numeric | 23 | 10 | √ | 0 | 委外发出数量 |
| 15 | flowerqty | 汇报下限 | numeric | 23 | 10 | √ | 0 | 汇报下限 |
| 16 | fsumquabaseqyt | 累计合格基本数量 | numeric | 23 | 10 | √ | 0 | 累计合格基本数量 |
| 17 | freworkdrawqty | 关联返工数量 | numeric | 23 | 10 | √ | 0 | 关联返工数量 |
| 18 | fouttoqty | 内协转出数量 | numeric | 23 | 10 | √ | 0 | 内协转出数量 |
| 19 | fsumworkwastqty | 累计工废数量 | numeric | 23 | 10 | √ | 0 | 累计工废数量 |
| 20 | ftobereworkedqty | 待返工数量 | numeric | 23 | 10 | √ | 0 | 待返工数量 |
| 21 | fsumstockwastproqty | 累计料废生产数量 | numeric | 23 | 10 | √ | 0 | 累计料废生产数量 |
| 22 | ftobereworkedproqty | 待返工生产数量 | numeric | 23 | 10 | √ | 0 | 待返工生产数量 |
| 23 | ftobeinspectqty | 待检数量 | numeric | 23 | 10 | √ | 0 | 待检数量 |
| 24 | fcompletebaseqty | 完工基本单位数量 | numeric | 23 | 10 | √ | 0 | 完工基本单位数量 |
| 25 | ftobeinsbaseqty | 待检基本单位数量 | numeric | 23 | 10 | √ | 0 | 待检基本单位数量 |
| 26 | foutsourcedsbqty | 关联委外发出数量 | numeric | 23 | 10 | √ | 0 | 关联委外发出数量 |
| 27 | fprounitfactor | 工序单位换算系数 | int4 | 32 |  | √ | 0 | 工序单位换算系数 |
| 28 | freworkedqty | 下推返工数量(废弃) | numeric | 23 | 10 | √ | 0 | 下推返工数量(废弃) |
| 29 | fhigherqty | 汇报上限 | numeric | 23 | 10 | √ | 0 | 汇报上限 |
| 30 | fsumstockwastbaseqty | 累计料废基本数量 | numeric | 23 | 10 | √ | 0 | 累计料废基本数量 |
| 31 | fcompleteproqty | 完工生产数量 | numeric | 23 | 10 | √ | 0 | 完工生产数量 |
| 32 | fcompleteqty | 完工数量 | numeric | 23 | 10 | √ | 0 | 完工数量 |
| 33 | ftransfersbqty | 转移选单数量 | numeric | 23 | 10 | √ | 0 | 转移选单数量 |
| 34 | fsumquaproqyt | 累计合格生产数量 | numeric | 23 | 10 | √ | 0 | 累计合格生产数量 |
| 35 | fsumquaqyt | 累计合格数量 | numeric | 23 | 10 | √ | 0 | 累计合格数量 |
| 36 | freportdownlimit | 汇报下限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报下限允差（%） |
| 37 | fendtime | 实际完工时间 | timestamp | 0 |  |  | null | 实际完工时间 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | fsumstockwastqty | 累计料废数量 | numeric | 23 | 10 | √ | 0 | 累计料废数量 |
| 40 | freportupperlimit | 汇报上限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报上限允差（%） |
| 41 | fyetreworkedqty | 已返工数量 | numeric | 23 | 10 | √ | 0 | 已返工数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processplanentry_c |  | fentryid |
| 2 | idx_sfc_plane_c_id |  | fid |

---

## 工序计划明细-分表 t_sfc_processplanentry_d

- **表名称：** 工序计划明细-分表
- **表名：** t_sfc_processplanentry_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpurchasegroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 3 | foutreworkproqty | 委外退回返工生产数量 | numeric | 23 | 10 | √ | 0 | 委外退回返工生产数量 |
| 4 | finreworkproqty | 内协退回返工生产数量 | numeric | 23 | 10 | √ | 0 | 内协退回返工生产数量 |
| 5 | foutsourcepriceandtax | 委外含税单价 | numeric | 23 | 10 | √ | 0 | 委外含税单价 |
| 6 | fworkwasteprice | 工废单价 | numeric | 23 | 10 | √ | 0 | 工废单价 |
| 7 | foutreworkqty | 委外退回返工数量 | numeric | 23 | 10 | √ | 0 | 委外退回返工数量 |
| 8 | finacceptqty | 内协接收数量 | numeric | 23 | 10 | √ | 0 | 内协接收数量 |
| 9 | fchargeunitid | 计价单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | finsendmenuqty | 关联内协发出数量 | numeric | 23 | 10 | √ | 0 | 关联内协发出数量 |
| 11 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | finreworkbaseqty | 内协退回返工基本数量 | numeric | 23 | 10 | √ | 0 | 内协退回返工基本数量 |
| 14 | fscrapwasteprice | 料废单价 | numeric | 23 | 10 | √ | 0 | 料废单价 |
| 15 | fworkwastepriceandtax | 工废含税单价 | numeric | 23 | 10 | √ | 0 | 工废含税单价 |
| 16 | foutreworkbaseqty | 委外退回返工基本数量 | numeric | 23 | 10 | √ | 0 | 委外退回返工基本数量 |
| 17 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 18 | finsendqty | 内协发出数量 | numeric | 23 | 10 | √ | 0 | 内协发出数量 |
| 19 | fscrapwastepriceandtax | 料废含税单价 | numeric | 23 | 10 | √ | 0 | 料废含税单价 |
| 20 | finreworkqty | 内协退回返工数量 | numeric | 23 | 10 | √ | 0 | 内协退回返工数量 |
| 21 | foutsourceprice | 委外单价 | numeric | 23 | 10 | √ | 0 | 委外单价 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 23 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processplanentry_d |  | fentryid |
| 2 | idx_sfc_plane_d_id |  | fid |

---

## 工序计划明细-分表 t_sfc_processplanentry_i

- **表名称：** 工序计划明细-分表
- **表名：** t_sfc_processplanentry_i

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finspectuserid | 质检员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fproinspect | 工序检验 | bpchar | 1 |  | √ | '0' | 工序检验 |
| 4 | finspectplan | 检验方案(废弃) | int8 | 64 |  | √ | 0 | 工作中心 sfc_workcenter |
| 5 | finspectdepid | 质检部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | finspectorg | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processplanentry_i |  | fentryid |
| 2 | idx_sfc_proplanentry_i_id |  | fid |

---

## 工序计划明细-分表 t_sfc_processplanentry_a

- **表名称：** 工序计划明细-分表
- **表名：** t_sfc_processplanentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispal | 准备活动人工 | bpchar | 1 |  | √ | '0' | 准备活动人工 |
| 3 | fraactivityreport | 准备活动人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 4 | fwamreportqty | 加工活动机器汇报数量 | numeric | 23 | 10 | √ | 0 | 加工活动机器汇报数量 |
| 5 | fsumwamplanqty | 加工活动机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 加工活动机器计划活动总量 |
| 6 | fpamreportqty | 准备活动机器活动汇报数量 | numeric | 23 | 10 | √ | 0 | 准备活动机器活动汇报数量 |
| 7 | fispam | 准备活动机器 | bpchar | 1 |  | √ | '0' | 准备活动机器 |
| 8 | frmactivityreport | 准备活动机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 9 | fpmpformulaid | 加工活动机器*计划活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 10 | frapformulaid | 准备活动人工*计划活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 11 | frmresource | 准备活动机器*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 12 | fwalplanqty | 加工活动人工基本数量 | numeric | 23 | 10 | √ | 0 | 加工活动人工基本数量 |
| 13 | fraresource | 准备活动人工*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 14 | frmpformulaid | 准备活动机器*计划活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 15 | fpamunit | 准备活动机器单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fpmactivityreport | 加工活动机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 17 | fwalreportqty | 加工活动人工汇报数量 | numeric | 23 | 10 | √ | 0 | 加工活动人工汇报数量 |
| 18 | fsumwalplanqty | 加工活动人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 加工活动人工计划活动总量 |
| 19 | fiswal | 加工活动人工 | bpchar | 1 |  | √ | '0' | 加工活动人工 |
| 20 | fiswam | 加工活动机器 | bpchar | 1 |  | √ | '0' | 加工活动机器 |
| 21 | fpalplanqty | 准备活动人工基本数量 | numeric | 23 | 10 | √ | 0 | 准备活动人工基本数量 |
| 22 | fpamplanqty | 准备活动机器基本数量 | numeric | 23 | 10 | √ | 0 | 准备活动机器基本数量 |
| 23 | funitfield | 准备活动人工单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fpalreportqty | 准备活动人工活动汇报数量 | numeric | 23 | 10 | √ | 0 | 准备活动人工活动汇报数量 |
| 25 | fwalunit | 加工活动人工单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | fpaactivityreport | 加工活动人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 27 | fpapformulaid | 加工活动人工*计划活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 28 | fwamplanqty | 加工活动机器基本数量 | numeric | 23 | 10 | √ | 0 | 加工活动机器基本数量 |
| 29 | fiscomeup3 | 加工人工默认 | bpchar | 1 |  | √ | '0' | 加工人工默认 |
| 30 | fwamunit | 加工活动机器单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | fiscomeup4 | 加工机器默认 | bpchar | 1 |  | √ | '0' | 加工机器默认 |
| 32 | fiscomeup1 | 准备人工默认 | bpchar | 1 |  | √ | '0' | 准备人工默认 |
| 33 | fsumpamplanqty | 准备活动机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 准备活动机器计划活动总量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fiscomeup2 | 准备机器默认 | bpchar | 1 |  | √ | '0' | 准备机器默认 |
| 36 | fsumpalplanqty | 准备活动人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 准备活动人工计划活动总量 |
| 37 | fpmresource | 加工活动机器*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 38 | fparesource | 加工活动人工*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_plane_a_id |  | fid |
| 2 | pk_sfc_processplanentry_a |  | fentryid |

---

## 工序计划明细-分表 t_sfc_processplanentry_b

- **表名称：** 工序计划明细-分表
- **表名：** t_sfc_processplanentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpalreportqty7 | 其他活动一人工汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动一人工汇报数量 |
| 3 | fomresource | 其他活动一机器*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 4 | fpalplanqty8 | 其他活动二人工基本数量 | numeric | 23 | 10 | √ | 0 | 其他活动二人工基本数量 |
| 5 | foaresource | 其他活动一人工*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 6 | ftmresource | 其他活动二机器*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 7 | fompformulaid | 其他活动一机器*计划活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 8 | fsumoomplanqty | 其他活动一机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动一机器计划活动总量 |
| 9 | foapformulaid | 其他活动一人工*计划活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 10 | foaactivityreport | 其他活动一人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 11 | fsumoopplanqty | 其他活动一人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动一人工计划活动总量 |
| 12 | fpamreportqty8 | 其他活动二人工汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动二人工汇报数量 |
| 13 | ftaresource | 其他活动二人工*资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 14 | funitfield8 | 其他活动二人工单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fpamreportqty4 | 其他活动二机器汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动二机器汇报数量 |
| 16 | ftmactivityreport | 其他活动二机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 17 | funitfield3 | 其他活动一机器单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fpalplanqty7 | 其他活动一人工基本数量 | numeric | 23 | 10 | √ | 0 | 其他活动一人工基本数量 |
| 19 | ftapformulaid | 其他活动二人工*计划活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 20 | fpalplanqty4 | 其他活动二机器基本数量 | numeric | 23 | 10 | √ | 0 | 其他活动二机器基本数量 |
| 21 | fomactivityreport | 其他活动一机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 22 | fpamreportqty3 | 其他活动一机器汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动一机器汇报数量 |
| 23 | ftaactivityreport | 其他活动二人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 24 | funitfield7 | 其他活动一人工单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fpalplanqty3 | 其他活动一机器基本数量 | numeric | 23 | 10 | √ | 0 | 其他活动一机器基本数量 |
| 26 | funitfield4 | 其他活动二机器单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fsumospplanqty | 其他活动二人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动二人工计划活动总量 |
| 28 | ftmpformulaid | 其他活动二机器*计划活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 29 | fispal4 | 其他活动二机器 | bpchar | 1 |  | √ | '0' | 其他活动二机器 |
| 30 | fiscomeup14 | 其他活动二机器默认 | bpchar | 1 |  | √ | '0' | 其他活动二机器默认 |
| 31 | fispal3 | 其他活动一机器 | bpchar | 1 |  | √ | '0' | 其他活动一机器 |
| 32 | fsumosmplanqty | 其他活动二机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动二机器计划活动总量 |
| 33 | fiscomeup13 | 其他活动一机器默认 | bpchar | 1 |  | √ | '0' | 其他活动一机器默认 |
| 34 | fispal8 | 其他活动二人工 | bpchar | 1 |  | √ | '0' | 其他活动二人工 |
| 35 | fiscomeup18 | 其他活动二人工默认 | bpchar | 1 |  | √ | '0' | 其他活动二人工默认 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 37 | fispal7 | 其他活动一人工 | bpchar | 1 |  | √ | '0' | 其他活动一人工 |
| 38 | fiscomeup17 | 其他活动一人工默认 | bpchar | 1 |  | √ | '0' | 其他活动一人工默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_plane_b_id |  | fid |
| 2 | pk_sfc_processplanentry_b |  | fentryid |

---

## 工序计划明细-分表 t_sfc_processplanentry_s

- **表名称：** 工序计划明细-分表
- **表名：** t_sfc_processplanentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fendprocessnumber | 拆分来源结束工序号 | int4 | 32 |  | √ | 0 | 拆分来源结束工序号 |
| 3 | fstartprocessnumber | 拆分来源起始工序号 | int4 | 32 |  | √ | 0 | 拆分来源起始工序号 |
| 4 | finsideplanqty | 生成内协工序计划数量 | numeric | 23 | 10 | √ | 0 | 生成内协工序计划数量 |
| 5 | fsrcprocesssequence | 拆分来源序列号 | int4 | 32 |  | √ | 0 | 拆分来源序列号 |
| 6 | fnormalsplitqty | 普通拆分数量 | numeric | 23 | 10 | √ | 0 | 普通拆分数量 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_procplan_entrys_num |  | fstartprocessnumber,fendprocessnumber |
| 2 | pk_sfc_processplanentry_s |  | fentryid |
| 3 | idx_sfc_procplan_entrys_id |  | fid |
| 4 | idx_sfc_procplan_entrys_seq |  | fsrcprocesssequence |

---

## 工序计划明细-多语言表 t_sfc_processplanentry_l

- **表名称：** 工序计划明细-多语言表
- **表名：** t_sfc_processplanentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprocessinstructions | 工序说明 | varchar | 512 |  | √ | ' ' | 工序说明 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_plane_l_id |  | fentryid |
| 2 | pk_t_sfc_processplanentry_l |  | fpkid |

---

## 工序计划-关联追踪表 t_sfc_processplan_tc

- **表名称：** 工序计划-关联追踪表
- **表名：** t_sfc_processplan_tc

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
| 1 | idx_sfc_processplan_tc_tid |  | ftid |
| 2 | idx_sfc_processplan_tc_tbill |  | ftbillid |
| 3 | pk_sfc_processplan_tc |  | fid |

---

## 工序计划-分表 t_sfc_processplan_s

- **表名称：** 工序计划-分表
- **表名：** t_sfc_processplan_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocesssequence | 拆分序列号 | int4 | 32 |  | √ | 0 | 拆分序列号 |
| 3 | fendprocessnumber | 拆分结束工序号 | int4 | 32 |  | √ | 0 | 拆分结束工序号 |
| 4 | fsrcprocessplanid | 来源工序计划 | int8 | 64 |  | √ | 0 | 工序计划 sfc_bd_processplan |
| 5 | fsplittype | 产生方式 | bpchar | 1 |  | √ | ' ' | 产生方式,枚举: A :首序到底拆分 B :中间工序到底拆分 C :指定工序段拆分 D :生成内协工序计划 |
| 6 | fstartprocessnumber | 拆分起始工序号 | int4 | 32 |  | √ | 0 | 拆分起始工序号 |
| 7 | fbillsn | 拆分流水号（直接下级流水） | int4 | 32 |  | √ | 0 | 拆分流水号（直接下级流水） |
| 8 | fcount | 拆分个数（直接下级个数） | int4 | 32 |  | √ | 0 | 拆分个数（直接下级个数） |
| 9 | frootprocessplanid | 主工序计划 | int8 | 64 |  | √ | 0 | 工序计划 sfc_bd_processplan |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_procplan_srcid |  | fsrcprocessplanid |
| 2 | pk_sfc_processplan_s |  | fid |
| 3 | idx_sfc_procplan_rootid |  | frootprocessplanid |
| 4 | idx_sfc_procplan_sspinfo |  | fsplittype,fprocesssequence,fstartprocessnumber,fendprocessnumber |

---

## 工序计划-多语言表 t_sfc_processplan_l

- **表名称：** 工序计划-多语言表
- **表名：** t_sfc_processplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_proplan_l_id |  | fid |
| 2 | pk_t_sfc_processplan_l |  | fpkid |

---

## 关联子实体-子表 t_sfc_processplanentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_processplanentry_lk

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
| 1 | idx_sfc_processplanentry_lk_fk |  | fentryid |
| 2 | pk_sfc_processplanentry_lk |  | fpkid |
