# 调拨申请单-im_transapply

## 调拨申请单-多语言表 t_im_transapply_l

- **表名称：** 调拨申请单-多语言表
- **表名：** t_im_transapply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_transapply_l_pkey |  | fpkid |
| 2 | idx_im_transapply_l_id |  | fid,flocaleid |

---

## 调拨申请单-反写记录表 t_im_transapply_wb

- **表名称：** 调拨申请单-反写记录表
- **表名：** t_im_transapply_wb

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
| 1 | idx_im_transapply_wb_fk |  | fid |
| 2 | t_im_transapply_wb_pkey |  | fentryid |

---

## 物料明细-分表 t_im_transapplyentry_y

- **表名称：** 物料明细-分表
- **表名：** t_im_transapplyentry_y

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 物流单据 | bpchar | 1 |  | √ | '0' | 物流单据 |
| 5 | ftransratedown | 数量短缺比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 数量短缺比率(%) |
| 6 | frowbillstatus | 行关闭状态 | bpchar | 1 |  | √ | 'A' | 行关闭状态,枚举: A :正常 D :已关闭 |
| 7 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 8 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 9 | fremtrsinbaseqty | 未调入基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未调入基本数量 |
| 10 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 13 | ftransrateup | 数量超出比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 数量超出比率(%) |
| 14 | fremtrsinqty | 未调入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未调入数量 |
| 15 | finlocation | 调入仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 16 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_transapplyentry_y_pkey |  | fentryid |
| 2 | idx_im_tse_y_feid |  | fid |

---

## 调拨申请单-关联追踪表 t_im_transapply_tc

- **表名称：** 调拨申请单-关联追踪表
- **表名：** t_im_transapply_tc

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
| 1 | idx_im_transapply_tc_ftbidtid |  | ftbillid,ftid |
| 2 | idx_im_transapply_tc_tid |  | ftid |
| 3 | t_im_transapply_tc_pkey |  | fid |
| 4 | idx_im_transapply_tc_tbill |  | ftbillid |

---

## 物料明细-子表 t_im_transapplyentry

- **表名称：** 物料明细-子表
- **表名：** t_im_transapplyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finprojectid | 调入项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 3 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | finvstatusid | 调出库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 7 | freltransbaseqty | 关联调拨基本数量 | numeric | 23 | 10 | √ | 0 | 关联调拨基本数量 |
| 8 | fauditqty | 核准数量 | numeric | 23 | 10 | √ | 0.0000000000 | 核准数量 |
| 9 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fownertype | 出库货主类型 | varchar | 36 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 11 | finkeepertype | 入库保管者类型 | varchar | 36 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 12 | fkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | finownerid | 调入货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fininvstatus | 调入库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 16 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 17 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 18 | fprojectid | 调出项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 19 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fkeepertype | 出库保管者类型 | varchar | 36 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 21 | fwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 22 | fininvtype | 调入库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 23 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 24 | fownerid | 调出货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 26 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 27 | foutorgid | 调出组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 31 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 32 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 33 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 34 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 36 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 37 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 38 | finwarehouseid | 调入仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 39 | freltransqty | 关联调拨数量 | numeric | 23 | 10 | √ | 0 | 关联调拨数量 |
| 40 | finkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | finmpmtaskno | 调入项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 42 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 43 | ftransoutqty | 已调出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已调出数量 |
| 44 | ftransoutbaseqty | 已调出基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已调出基本数量 |
| 45 | fremaintransoutqty | 未调出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未调出数量 |
| 46 | finvtypeid | 调出库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 47 | ftransinbaseqty | 已调入基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已调入基本数量 |
| 48 | fremaintransoutbaseqty | 未调出基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未调出基本数量 |
| 49 | frowterminatestatus | 行终止状态 | bpchar | 1 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 50 | flocationid | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 51 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 52 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 53 | ftransinqty | 已调入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已调入数量 |
| 54 | finorgid | 调入组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 55 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 56 | fmpmtaskno | 调出项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 57 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 58 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 59 | finownertype | 入库货主类型 | varchar | 36 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 60 | fisfreegift | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_transapplyentry_pkey |  | fentryid |
| 2 | idx_im_transapply_e_mmt |  | fmaterialmasterid |
| 3 | idx_im_transapplyentry |  | fid |
| 4 | idx_im_transapply_e_wh |  | fwarehouseid |

---

## 关联子实体-子表 t_im_transapply_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_transapply_lk

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
| 1 | t_im_transapply_lk_pkey |  | fpkid |
| 2 | idx_im_transapply_lk_fk |  | fid |

---

## 关联子实体-子表 t_im_transapplyentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_transapplyentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftransoutbaseqty | 已调出基本数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 已调出基本数量_确认携带值 |
| 2 | fremaintransoutbaseqty_old | 未调出基本数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 未调出基本数量_原始携带值 |
| 3 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 4 | ftransinbaseqty_old | 已调入基本数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 已调入基本数量_原始携带值 |
| 5 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 6 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 7 | ftransinbaseqty | 已调入基本数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 已调入基本数量_确认携带值 |
| 8 | fremaintransoutbaseqty | 未调出基本数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 未调出基本数量_确认携带值 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | ftransoutbaseqty_old | 已调出基本数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 已调出基本数量_原始携带值 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 12 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_transapplyentry_lk_pkey |  | fpkid |
| 2 | idx_im_transapplyentry_lk_fk |  | fentryid |

---

## 调拨申请单-主表 t_im_transapply

- **表名称：** 调拨申请单-主表
- **表名：** t_im_transapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 4 | fhandcloseflag | 手工关闭 | bpchar | 1 |  | √ | ' ' | 手工关闭 |
| 5 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fapplyuserid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 10 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fsettlecurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 17 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 22 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 23 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 24 | ftranstype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transapply_forgbillno |  | fbillno,forgid |
| 2 | t_im_transapply_pkey |  | fid |
| 3 | idx_im_transapply_org |  | forgid |
| 4 | idx_im_transapply_biztorgno |  | fbiztime,forgid,fbillno |
