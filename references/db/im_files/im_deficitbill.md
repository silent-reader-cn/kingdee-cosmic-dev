# 盘亏单-im_deficitbill

## 盘亏单-反写记录表 t_im_deficitbill_wb

- **表名称：** 盘亏单-反写记录表
- **表名：** t_im_deficitbill_wb

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
| 1 | t_im_deficitbill_wb_pkey |  | fentryid |
| 2 | idx_im_deficitbill_wb_fk |  | fid |

---

## 盘亏单-关联追踪表 t_im_deficitbill_tc

- **表名称：** 盘亏单-关联追踪表
- **表名：** t_im_deficitbill_tc

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
| 1 | idx_im_deficitbill_tc_tbill |  | ftbillid |
| 2 | idx_im_deficitbill_tc_tid |  | ftid |
| 3 | t_im_deficitbill_tc_pkey |  | fid |

---

## 盘亏单-多语言表 t_im_deficitbill_l

- **表名称：** 盘亏单-多语言表
- **表名：** t_im_deficitbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_deficitbill_l |  | fid,flocaleid |
| 2 | t_im_deficitbill_l_pkey |  | fpkid |

---

## 盘亏单-主表 t_im_deficitbill

- **表名称：** 盘亏单-主表
- **表名：** t_im_deficitbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcounttype | 盘点方式 | varchar | 5 |  | √ | ' ' | 盘点方式,枚举: A :定期盘点 |
| 3 | finvcountbillno | 盘点表编码 | varchar | 80 |  | √ | ' ' | 盘点表编码 |
| 4 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 5 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 6 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbizoperatorid | 业务员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 10 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fasyncstatus | 异步状态 | varchar | 50 |  | √ | ' ' | 异步状态,枚举: A :处理中 B :已完成 |
| 14 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 15 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | funitsrctype | 计量单位来源 | varchar | 50 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 22 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 26 | fbizoperatorgroupid | 业务组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 27 | fbillcretype | 单据生成类型 | varchar | 50 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 28 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 29 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 30 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 31 | fbizdeptid | 业务部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fsettlecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_deficitbill_pkey |  | fid |
| 2 | idx_im_deficitbill_forgbillno |  | fbillno,forgid |

---

## 物料明细-分表 t_im_deficitbillentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_deficitbillentry_c

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
| 1 | pk_im_deficitbillentry_c |  | fentryid |
| 2 | idx_im_deficitbillentry_c |  | fid |

---

## 物料明细-分表 t_im_deficitbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_deficitbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 3 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 4 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 50 |  | √ | ' ' | 来源系统单据分录ID |
| 5 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 6 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 7 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 8 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | fsrcsysbillid | 来源系统单据ID | varchar | 50 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_deficitbillentry_r_pkey |  | fentryid |
| 2 | idx_im_deficitbillentry_r |  | fid |

---

## 物料明细-分表 t_im_deficitbillentry_x

- **表名称：** 物料明细-分表
- **表名：** t_im_deficitbillentry_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flossqty | flossqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fqty3rdacc | fqty3rdacc | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fqty2ndacc | 账存数量（辅助） | numeric | 23 | 10 | √ | 0.0000000000 | 账存数量（辅助） |
| 5 | fcheckbaseqty | 复盘数量（基本） | numeric | 23 | 10 | √ | 0 | 复盘数量（基本） |
| 6 | fbaselossqty | 盘亏数量（基本） | numeric | 23 | 10 | √ | 0.0000000000 | 盘亏数量（基本） |
| 7 | finvlossqty | 盘亏数量（库存） | numeric | 23 | 10 | √ | 0.0000000000 | 盘亏数量（库存） |
| 8 | fadjustbaseqty | 调整数量（基本） | numeric | 23 | 10 | √ | 0 | 调整数量（基本） |
| 9 | fadjustinvqty | 调整数量（库存） | numeric | 23 | 10 | √ | 0 | 调整数量（库存） |
| 10 | flossqty3rd | flossqty3rd | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | flossqty2nd | 盘亏数量（辅助） | numeric | 23 | 10 | √ | 0.0000000000 | 盘亏数量（辅助） |
| 12 | finvqtyacc | 账存数量（库存） | numeric | 23 | 10 | √ | 0.0000000000 | 账存数量（库存） |
| 13 | fadjustqty2nd | 调整数量（辅助） | numeric | 23 | 10 | √ | 0 | 调整数量（辅助） |
| 14 | fbaseqtyacc | 账存数量（基本） | numeric | 23 | 10 | √ | 0.0000000000 | 账存数量（基本） |
| 15 | fcheckinvqty | 复盘数量（库存） | numeric | 23 | 10 | √ | 0 | 复盘数量（库存） |
| 16 | fqtyacc | fqtyacc | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fcheck2ndqty | 复盘数量（辅助） | numeric | 23 | 10 | √ | 0 | 复盘数量（辅助） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_deficitbillentry_x_pkey |  | fentryid |
| 2 | idx_im_deficitbillentry_x |  | fid |

---

## 关联子实体-子表 t_im_deficitbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_deficitbillentry_lk

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
| 1 | t_im_deficitbillentry_lk_pkey |  | fpkid |
| 2 | idx_im_deficitbillentry_lk_fk |  | fentryid |

---

## 物料明细-子表 t_im_deficitbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_deficitbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty3rdacc | 账存数量（辅助2） | numeric | 23 | 10 | √ | 0 | 账存数量（辅助2） |
| 3 | fentryinvschemeid | fentryinvschemeid | int8 | 64 |  | √ | 0 |  |
| 4 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fserialqty | fserialqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fcheck3rdqty | 复盘数量（辅助2） | numeric | 23 | 10 | √ | 0 | 复盘数量（辅助2） |
| 9 | foutownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | finvstatusid | finvstatusid | int8 | 64 |  | √ | 0 |  |
| 11 | fentrydc | fentrydc | varchar | 5 |  | √ | ' ' |  |
| 12 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 13 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fadjustqty3rd | 调整数量（辅助2） | numeric | 23 | 10 | √ | 0 | 调整数量（辅助2） |
| 15 | fownertype | fownertype | varchar | 36 |  | √ | ' ' |  |
| 16 | fkeeperid | fkeeperid | int8 | 64 |  | √ | 0 |  |
| 17 | foutkeeper | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 20 | fqty | 盘点数量（库存） | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量（库存） |
| 21 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 22 | fserialunitid | fserialunitid | int8 | 64 |  | √ | 0 |  |
| 23 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 24 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fkeepertype | fkeepertype | varchar | 36 |  | √ | ' ' |  |
| 26 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 27 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 28 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 29 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 30 | flossqty3rd | 盘亏数量（辅助2） | numeric | 23 | 10 | √ | 0 | 盘亏数量（辅助2） |
| 31 | finvunitid | finvunitid | int8 | 64 |  | √ | 0 |  |
| 32 | fqtyunit2nd | 盘点数量（辅助） | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量（辅助） |
| 33 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 34 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 35 | fqtyinvunit | fqtyinvunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 36 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 39 | fmaterialname | 物料名称(历史) | varchar | 100 |  | √ | ' ' | 物料名称(历史) |
| 40 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 41 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 42 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 43 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | fserialunitrate | fserialunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 45 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 46 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 47 | foutkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 48 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 49 | foutownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 50 | finvtypeid | finvtypeid | int8 | 64 |  | √ | 0 |  |
| 51 | finvunitrate | finvunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 52 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 53 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 54 | funitcost | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 55 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 56 | fqtyunit3rd | 盘点数量(辅助2) | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量(辅助2) |
| 57 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 58 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 59 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 60 | fbaseqty | 盘点数量（基本） | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量（基本） |
| 61 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 62 | fcost | 成本 | numeric | 23 | 10 | √ | 0 | 成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_deficitbillentry |  | fid |
| 2 | t_im_deficitbillentry_pkey |  | fentryid |

---

## 关联子实体-子表 t_im_deficitbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_deficitbill_lk

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
| 1 | t_im_deficitbill_lk_pkey |  | fpkid |
| 2 | idx_im_deficitbill_lk_fk |  | fid |
