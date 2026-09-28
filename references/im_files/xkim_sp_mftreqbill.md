# 简单领料申请单-xkim_sp_mftreqbill

## 简单领料申请单-关联追踪表 t_im_mreqbill_tc

- **表名称：** 简单领料申请单-关联追踪表
- **表名：** t_im_mreqbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_mreqbill_tc_pkey |  | fid |
| 2 | idx_im_mreqbill_tc_tbill |  | ftbillid |
| 3 | idx_im_mreq_tc_ftbidtid |  | ftbillid,ftid |
| 4 | idx_im_mreqbill_tc_tid |  | ftid |

---

## 物料明细-子表 t_xkim_sp_mreqbillentry

- **表名称：** 物料明细-子表
- **表名：** t_xkim_sp_mreqbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 3 | foutqty | 已出库数量 | numeric | 23 | 10 | √ | 0 | 已出库数量 |
| 4 | flogisticsbill | 物流单据 | bpchar | 1 |  | √ | '0' | 物流单据 |
| 5 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 7 | fshortageratio | 数量短缺比率(%) | numeric | 23 | 10 | √ | 0 | 数量短缺比率(%) |
| 8 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0 |  |
| 11 | fseq | 分录行号 | numeric | 23 | 10 | √ | 0 | 分录行号 |
| 12 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0 |  |
| 13 | fexcessratio | 数量超出比率(%) | numeric | 23 | 10 | √ | 0 | 数量超出比率(%) |
| 14 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 15 | fauditqty | 核准数量 | numeric | 23 | 10 | √ | 0 | 核准数量 |
| 16 | frowstatus | 行状态 | varchar | 100 |  | √ | ' ' | 行状态,枚举: A :暂存 B :已提交 C :已审核 D :已关闭 |
| 17 | funitrate | funitrate | numeric | 23 | 10 | √ | 0 |  |
| 18 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | fmftunitqty | 子项单位数量 | numeric | 23 | 10 | √ | 0 | 子项单位数量 |
| 22 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 23 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 24 | fmftunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 27 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 28 | fremainoutqty | 未出库数量 | numeric | 23 | 10 | √ | 0 | 未出库数量 |
| 29 | foutbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0 | 已出库基本数量 |
| 30 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 31 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 32 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 33 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 34 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 35 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 36 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 37 | fremainoutbaseqty | 未出库基本数量 | numeric | 23 | 10 | √ | 0 | 未出库基本数量 |
| 38 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 39 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 40 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 41 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 42 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 45 | funcontrolledqty | 不控制数量 | bpchar | 1 |  | √ | '1' | 不控制数量 |
| 46 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 47 | fisfreegift | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 48 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkim_sp_mr_e_id_s |  | fid,fseq |
| 2 | idx_xkim_sp_mr_e_mmt |  | fmaterialmasterid |
| 3 | pk_t_xkim_sp_mreqbillentry |  | fentryid |
| 4 | idx_xkim_sp_mr_e_wh |  | fwarehouseid |
| 5 | idx_xkim_sp_mr_e_mid |  | fmaterialid |

---

## 简单领料申请单-反写记录表 t_im_mreqbill_wb

- **表名称：** 简单领料申请单-反写记录表
- **表名：** t_im_mreqbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_mreqbill_wb_pkey |  | fentryid |
| 2 | idx_im_mreqbill_wb_fk |  | fid |

---

## 关联子实体-子表 t_im_mreqbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_mreqbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
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
| 1 | t_im_mreqbillentry_lk_pkey |  | fpkid |
| 2 | idx_im_mreqbillentry_lk_fk |  | fentryid |

---

## 简单领料申请单-主表 t_xkim_sp_mreqbill

- **表名称：** 简单领料申请单-主表
- **表名：** t_xkim_sp_mreqbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fischargeagainstbill | fischargeagainstbill | bpchar | 1 |  | √ | '0' |  |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  |  | null | 物料生产信息 bd_materialmftinfo |
| 4 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsupplyowner | 供应货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fmftqty | 生产数量 | numeric | 23 | 10 |  | 0 | 生产数量 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fmatversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 10 | fbomid | BOM编码 | int8 | 64 |  |  | null | BOM维护 pdm_mftbom |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fapplyuserid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbizorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 15 | fcostcenterorg | 成本中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fsupplyownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_customer :客户 bd_supplier :供应商 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | funitsrctype | 计量单位来源 | varchar | 50 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fmftunitid | 生产单位 | int8 | 64 |  |  | null | 计量单位 bd_measureunits |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已关闭 |
| 23 | fsettlecurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 28 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 29 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 30 | fisalreadychargeagainst | fisalreadychargeagainst | bpchar | 1 |  | √ | '0' |  |
| 31 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkim_sp_mrbl_idtn |  | forgid,fbiztime,fbillno |
| 2 | idx_xkim_sp_mr_billno |  | fbillno |
| 3 | pk_t_xkim_sp_mreqbill |  | fid |
| 4 | idx_xkim_sp_mr_borgno |  | fbiztime,forgid,fbillno |

---

## 关联子实体-子表 t_im_mreqbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_mreqbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_mreqbill_lk_pkey |  | fpkid |
| 2 | idx_im_mreqbill_lk_fk |  | fid |

---

## 简单领料申请单-多语言表 t_xkim_sp_mreqbill_l

- **表名称：** 简单领料申请单-多语言表
- **表名：** t_xkim_sp_mreqbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkim_sp_mrb_l_flid |  | fid,flocaleid |
| 2 | pk_t_xkim_sp_mreqbill_l |  | fpkid |
