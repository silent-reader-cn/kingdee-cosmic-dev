# 盘盈单-im_surplusbill

## 盘盈单-主表 t_im_surplusbill

- **表名称：** 盘盈单-主表
- **表名：** t_im_surplusbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcounttype | 盘点方式 | varchar | 5 |  | √ | ' ' | 盘点方式,枚举: A :定期盘点 |
| 3 | finvcountbillno | 盘点表编码 | varchar | 80 |  | √ | ' ' | 盘点表编码 |
| 4 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 5 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 6 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbizoperatorid | 业务员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 10 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fasyncstatus | 异步状态 | varchar | 50 |  | √ | ' ' | 异步状态,枚举: A :处理中 B :已完成 |
| 14 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | funitsrctype | 计量单位来源 | varchar | 50 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 21 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fbizoperatorgroupid | 业务组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 26 | fbillcretype | 单据生成类型 | varchar | 50 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 27 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 28 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 29 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 30 | fbizdeptid | 业务部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fsettlecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_surplusbill_forgbillno |  | fbillno,forgid |
| 2 | t_im_surplusbill_pkey |  | fid |

---

## 盘盈单-反写记录表 t_im_surplusbill_wb

- **表名称：** 盘盈单-反写记录表
- **表名：** t_im_surplusbill_wb

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
| 1 | t_im_surplusbill_wb_pkey |  | fentryid |
| 2 | idx_im_surplusbill_wb_fk |  | fid |

---

## 关联子实体-子表 t_im_surplusbill_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_surplusbill_entry_lk

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
| 1 | idx_im_surplusbill_entry_lk_fk |  | fentryid |
| 2 | t_im_surplusbill_entry_lk_pkey |  | fpkid |

---

## 物料明细-分表 t_im_surplusbillentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_surplusbillentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcurrencyid | 成本币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 4 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 5 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_surplusbillentry_c |  | fentryid |
| 2 | idx_im_surplusbillentry_c |  | fid |

---

## 物料明细-分表 t_im_surplusbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_surplusbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 3 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 4 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 50 |  | √ | ' ' | 来源系统单据分录ID |
| 5 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 6 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 7 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
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
| 1 | t_im_surplusbillentry_r_pkey |  | fentryid |
| 2 | idx_im_surplusbillentry_r_fid |  | fid |

---

## 物料明细-分表 t_im_surplusbillentry_x

- **表名称：** 物料明细-分表
- **表名：** t_im_surplusbillentry_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasegainqty | 盘盈数量（基本） | numeric | 23 | 10 | √ | 0.0000000000 | 盘盈数量（基本） |
| 3 | fqty3rdacc | fqty3rdacc | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fgainqty3rd | fgainqty3rd | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | fgainqty2nd | 盘盈数量（辅助） | numeric | 23 | 10 | √ | 0.0000000000 | 盘盈数量（辅助） |
| 6 | fqty2ndacc | 账存数量（辅助） | numeric | 23 | 10 | √ | 0.0000000000 | 账存数量（辅助） |
| 7 | fcheckbaseqty | 复盘数量（基本） | numeric | 23 | 10 | √ | 0 | 复盘数量（基本） |
| 8 | fgainqty | fgainqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fadjustbaseqty | 调整数量（基本） | numeric | 23 | 10 | √ | 0 | 调整数量（基本） |
| 10 | fadjustinvqty | 调整数量（库存） | numeric | 23 | 10 | √ | 0 | 调整数量（库存） |
| 11 | finvqtyacc | 账存数量（库存） | numeric | 23 | 10 | √ | 0.0000000000 | 账存数量（库存） |
| 12 | fadjustqty2nd | 调整数量（辅助） | numeric | 23 | 10 | √ | 0 | 调整数量（辅助） |
| 13 | fbaseqtyacc | 账存数量（基本） | numeric | 23 | 10 | √ | 0.0000000000 | 账存数量（基本） |
| 14 | fcheckinvqty | 复盘数量（库存） | numeric | 23 | 10 | √ | 0 | 复盘数量（库存） |
| 15 | finvgainqty | 盘盈数量（库存） | numeric | 23 | 10 | √ | 0.0000000000 | 盘盈数量（库存） |
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
| 1 | idx_im_surplusbillentry_x_id |  | fid |
| 2 | t_im_surplusbillentry_x_pkey |  | fentryid |

---

## 关联子实体-子表 t_im_surplusbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_surplusbill_lk

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
| 1 | idx_im_surplusbill_lk_fk |  | fid |
| 2 | t_im_surplusbill_lk_pkey |  | fpkid |

---

## 物料明细-子表 t_im_surplusbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_surplusbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty3rdacc | 账存数量（辅助2） | numeric | 23 | 10 | √ | 0 | 账存数量（辅助2） |
| 3 | fgainqty3rd | 盘盈数量（辅助2） | numeric | 23 | 10 | √ | 0 | 盘盈数量（辅助2） |
| 4 | fentryinvschemeid | fentryinvschemeid | int8 | 64 |  | √ | 0 |  |
| 5 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fserialqty | fserialqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fcheck3rdqty | 复盘数量（辅助2） | numeric | 23 | 10 | √ | 0 | 复盘数量（辅助2） |
| 10 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 11 | fentrydc | fentrydc | varchar | 5 |  | √ | ' ' |  |
| 12 | foutinvtypeid | foutinvtypeid | int8 | 64 |  | √ | 0 |  |
| 13 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fadjustqty3rd | 调整数量（辅助2） | numeric | 23 | 10 | √ | 0 | 调整数量（辅助2） |
| 15 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 16 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fqty | 盘点数量（库存） | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量（库存） |
| 20 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | fserialunitid | fserialunitid | int8 | 64 |  | √ | 0 |  |
| 22 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 23 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fkeepertype | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 25 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 26 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 27 | foutinvstatusid | foutinvstatusid | int8 | 64 |  | √ | 0 |  |
| 28 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 29 | finvunitid | finvunitid | int8 | 64 |  | √ | 0 |  |
| 30 | fqtyunit2nd | 盘点数量（辅助） | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量（辅助） |
| 31 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 33 | fqtyinvunit | fqtyinvunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 34 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 37 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 38 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 39 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 40 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 41 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 42 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 43 | fserialunitrate | fserialunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 45 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 46 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 47 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 48 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 49 | finvunitrate | finvunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 50 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 51 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 52 | funitcost | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 53 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 54 | fqtyunit3rd | 盘点数量（辅助2） | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量（辅助2） |
| 55 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 56 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 57 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 58 | fbaseqty | 盘点数量（基本） | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量（基本） |
| 59 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 60 | fcost | 成本 | numeric | 23 | 10 | √ | 0 | 成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_surplusbillentry |  | fid |
| 2 | t_im_surplusbillentry_pkey |  | fentryid |

---

## 盘盈单-多语言表 t_im_surplusbill_l

- **表名称：** 盘盈单-多语言表
- **表名：** t_im_surplusbill_l

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
| 1 | t_im_surplusbill_l_pkey |  | fpkid |
| 2 | idx_im_surplusbill_l_id |  | fid,flocaleid |

---

## 盘盈单-关联追踪表 t_im_surplusbill_tc

- **表名称：** 盘盈单-关联追踪表
- **表名：** t_im_surplusbill_tc

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
| 1 | idx_im_surplusbill_tc_tid |  | ftid |
| 2 | idx_im_surplusbill_tc_tbill |  | ftbillid |
| 3 | t_im_surplusbill_tc_pkey |  | fid |
