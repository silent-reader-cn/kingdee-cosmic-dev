# 出库申请单-im_outapplybill

## 出库申请单-主表 t_im_outapplybill

- **表名称：** 出库申请单-主表
- **表名：** t_im_outapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 4 | fhandcloseflag | 手工关闭 | bpchar | 1 |  | √ | ' ' | 手工关闭 |
| 5 | fbiztime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fapplyuserid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fbizorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fownertype | fownertype | varchar | 30 |  | √ | ' ' |  |
| 11 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 12 | fapplytype | 申请类型 | varchar | 30 |  | √ | ' ' | 申请类型,枚举: CKSQLX01_SYS :货损出库 CKSQLX02_SYS :耗材出库 CKSQLX03_SYS :报废出库 CKSQLX04_SYS :福利领用 CKSQLX05_SYS :办公用品领用 CKSQLX06_SYS :劳保用品领用 |
| 13 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fdeptid | 领用部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 20 | fsettlecurrency | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fbillcretype | 单据生成类型 | varchar | 10 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 25 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 26 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 27 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 30 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_outapplybill_forgbillno |  | fbillno,forgid |
| 2 | idx_outapplybill_biztorgno |  | fbiztime,forgid,fbillno |
| 3 | pk_im_outapplybill |  | fid |
| 4 | idx_im_outapplybill_org |  | forgid |

---

## 关联子实体-子表 t_im_outapplybill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_outapplybill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_outapplybill_lk_fk |  | fid |
| 2 | pk_im_outapplybill_lk |  | fpkid |

---

## 关联子实体-子表 t_im_outapplybillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_outapplybillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_outapplybillentry_lk |  | fpkid |
| 2 | idx_im_outapplybillentry_lk_fk |  | fentryid |

---

## 出库申请单-反写记录表 t_im_outapplybill_wb

- **表名称：** 出库申请单-反写记录表
- **表名：** t_im_outapplybill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_outapplybill_wb |  | fentryid |
| 2 | idx_im_outapplybill_wb_fk |  | fid |

---

## 出库申请单-多语言表 t_im_outapplybill_l

- **表名称：** 出库申请单-多语言表
- **表名：** t_im_outapplybill_l

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
| 1 | pk_im_outapplybill_l |  | fpkid |
| 2 | idx_im_outapplybill_l_0 |  | fid,flocaleid |

---

## 物料明细-子表 t_im_outapplybillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_outapplybillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 3 | flogisticsbill | 物流单据 | bpchar | 1 |  | √ | ' ' | 物流单据 |
| 4 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | funoutbaseqty | 未出库基本数量 | numeric | 23 | 10 | √ | 0 | 未出库基本数量 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fauditqty | 审批数量 | numeric | 23 | 10 | √ | 0 | 审批数量 |
| 9 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 10 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | freloutqty | 关联出库数量 | numeric | 23 | 10 | √ | 0 | 关联出库数量 |
| 12 | fqty | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 13 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 14 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 15 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 16 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 18 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 19 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 20 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 21 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 50 |  | √ | ' ' | 来源系统单据分录ID |
| 22 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 23 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 26 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 27 | frowclosestatus | 行关闭状态 | varchar | 50 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 28 | foutqty | 累计出库数量 | numeric | 23 | 10 | √ | 0 | 累计出库数量 |
| 29 | freceiveprojectid | 领用项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 30 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 31 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 32 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 33 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 34 | funoutqty | 未出库数量 | numeric | 23 | 10 | √ | 0 | 未出库数量 |
| 35 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 36 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 37 | foutbaseqty | 累计出库基本数量 | numeric | 23 | 10 | √ | 0 | 累计出库基本数量 |
| 38 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 39 | fowner | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | frowterminatestatus | 行终止状态 | varchar | 50 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 41 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 42 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 43 | freloutbaseqty | 关联出库基本数量 | numeric | 23 | 10 | √ | 0 | 关联出库基本数量 |
| 44 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 45 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 46 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 47 | fbaseqty | 基本申请数量 | numeric | 23 | 10 | √ | 0 | 基本申请数量 |
| 48 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 49 | fsrcsysbillid | 来源系统单据ID | varchar | 50 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_outapplybillentry |  | fentryid |
| 2 | idx_im_outapplybillentry_fk |  | fid |

---

## 出库申请单-关联追踪表 t_im_outapplybill_tc

- **表名称：** 出库申请单-关联追踪表
- **表名：** t_im_outapplybill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
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
| 1 | idx_im_outapplybill_tc_tid |  | ftid |
| 2 | pk_im_outapplybill_tc |  | fid |
| 3 | idx_im_outapplybill_tc_tbill |  | ftbillid |
