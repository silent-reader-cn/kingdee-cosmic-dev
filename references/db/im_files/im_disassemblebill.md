# 拆卸单-im_disassemblebill

## 拆卸单-关联追踪表 t_im_disassemblebill_tc

- **表名称：** 拆卸单-关联追踪表
- **表名：** t_im_disassemblebill_tc

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
| 1 | idx_im_disassemble_tc_ftbidtid |  | ftbillid,ftid |
| 2 | t_im_disassemblebill_tc_pkey |  | fid |
| 3 | idx_im_disassemblebill_tc_tbill |  | ftbillid |
| 4 | idx_im_disassemblebill_tc_tid |  | ftid |

---

## 拆卸前物料明细-子表 t_im_disassembleentry

- **表名称：** 拆卸前物料明细-子表
- **表名：** t_im_disassembleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 4 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 9 | finvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 10 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 11 | fownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 |
| 12 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 13 | fkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 16 | finvaccid | 即时库存ID | int8 | 64 |  | √ | 0 | 即时库存ID |
| 17 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 18 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 19 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | finvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 21 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 22 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 24 | fkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 |
| 25 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 26 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 27 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 28 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 29 | fownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 31 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 32 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 33 | fprocessingfee | 费用 | numeric | 23 | 10 | √ | 0 | 费用 |
| 34 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 35 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 36 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 37 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 38 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 39 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_disassembleentry_pkey |  | fentryid |
| 2 | idx_im_disassembleey_mmt |  | fmaterialmasterid |
| 3 | idx_im_disassembleey_wh |  | fwarehouseid |
| 4 | idx_im_disassembleentry_id |  | fid |
| 5 | idx_im_disassembleey_material |  | fmaterialid |
| 6 | idx_im_disassembleey_ow |  | fownerid |

---

## 关联子实体-子表 t_im_disassemblesubentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_disassemblesubentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_disassemblesubentry_lk_fk |  | fdetailid |
| 2 | t_im_disassemblesubentry_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_im_disassembleentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_disassembleentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_disassembleentry_lk_pkey |  | fpkid |
| 2 | idx_im_disassembleentry_lk_fk |  | fentryid |

---

## 拆卸单-主表 t_im_disassemblebill

- **表名称：** 拆卸单-主表
- **表名：** t_im_disassemblebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 9 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 10 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 11 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 14 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 19 | fcurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 |
| 23 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 24 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 25 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_disassembl_org |  | forgid |
| 2 | idx_im_disassembl_biztorgno |  | fbiztime,forgid,fbillno |
| 3 | idx_im_disassemble_forgbillno |  | fbillno,forgid |
| 4 | t_im_disassemblebill_pkey |  | fid |
| 5 | idx_im_disassembl_biztype |  | fbiztypeid |
| 6 | idx_im_disassembl_biztime |  | fbiztime |
| 7 | idx_im_dsbill_bktorgno |  | fbookdate,forgid,fbillno |

---

## 拆卸单-反写记录表 t_im_disassemblebill_wb

- **表名称：** 拆卸单-反写记录表
- **表名：** t_im_disassemblebill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_disassemblebill_wb_pkey |  | fentryid |
| 2 | idx_im_disassemblebill_wb_fk |  | fid |

---

## 拆卸后物料明细-子表 t_im_disassemblesubentry

- **表名称：** 拆卸后物料明细-子表
- **表名：** t_im_disassemblesubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 3 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fkeeper | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsubsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 9 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 10 | fsubsrcbillentity | 来源单据实体 | varchar | 100 |  | √ | ' ' | 来源单据实体 |
| 11 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 12 | finvtype | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 13 | fdisassmblerate | 拆卸成本比例% | numeric | 23 | 10 | √ | 0 | 拆卸成本比例% |
| 14 | fownertype | 入库货主类型 | varchar | 30 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_customer :客户 |
| 15 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 19 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 20 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 23 | fkeepertype | 入库保管者类型 | varchar | 30 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 |
| 24 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 25 | fsubsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 26 | fusagerate | fusagerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 27 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 28 | fowner | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 30 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 31 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 32 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 33 | fprocessingfee | 费用 | numeric | 23 | 10 | √ | 0.0000000000 | 费用 |
| 34 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 35 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 36 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 37 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 38 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 39 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 41 | finvstatus | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_disassemblesubey_mlid |  | fmaterialid |
| 2 | idx_im_disassemblesubey_entry |  | fentryid |
| 3 | idx_im_disassemblesubey_mmt |  | fmaterialmasterid |
| 4 | t_im_disassemblesubentry_pkey |  | fdetailid |
| 5 | idx_im_disassemblesubey_ow |  | fowner |
| 6 | idx_im_disassemblesubey_wh |  | fwarehouseid |

---

## 拆卸前物料明细-分表 t_im_disassembleentry_c

- **表名称：** 拆卸前物料明细-分表
- **表名：** t_im_disassembleentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcurrencyid | 成本币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 4 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 5 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_disassembleentry_c |  | fentryid |
| 2 | idx_im_disassembleentry_c |  | fid |

---

## 拆卸后物料明细-分表 t_im_disassemblesubentry_c

- **表名称：** 拆卸后物料明细-分表
- **表名：** t_im_disassemblesubentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 2 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_disassemblesubentry_c |  | fdetailid |
| 2 | idx_im_disassemblesubentry_c |  | fentryid |

---

## 关联子实体-子表 t_im_disassemblebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_disassemblebill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_disassemblebill_lk_fk |  | fid |
| 2 | t_im_disassemblebill_lk_pkey |  | fpkid |

---

## 拆卸单-多语言表 t_im_disassemblebill_l

- **表名称：** 拆卸单-多语言表
- **表名：** t_im_disassemblebill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_disassembl_l_flid |  | fid,flocaleid |
| 2 | idx_im_disassemble_l_locale |  | flocaleid |
| 3 | t_im_disassemblebill_l_pkey |  | fpkid |
