# MTO库存调整-mrp_mtoinvconvert

## MTO库存调整-主表 t_mrp_mtoinvconvert

- **表名称：** MTO库存调整-主表
- **表名：** t_mrp_mtoinvconvert

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fcaculatelogid | 运算编号 | int8 | 64 |  | √ | 0 | 运算日志 mrp_caculate_log |
| 9 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_mtoinvconvert |  | fid |
| 2 | idx_mrp_mtoinvconvert_logid |  | fcaculatelogid |

---

## MTO转换单据体-子表 t_mrp_mtoconvertentry

- **表名称：** MTO转换单据体-子表
- **表名：** t_mrp_mtoconvertentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnoupdateinvfields | fnoupdateinvfields | varchar | 100 |  | √ | ' ' |  |
| 3 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsrcbillentryseq | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 6 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 7 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 8 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 9 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 10 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fxtbillid | 形态转换单内码 | int8 | 64 |  | √ | 0 | 形态转换单内码 |
| 13 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 14 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 15 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 16 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 18 | fkeepertype | 保管者类型 | varchar | 30 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 19 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 20 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 21 | finvid | 即时库存内码 | int8 | 64 |  | √ | 0 | 即时库存内码 |
| 22 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 24 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 25 | fxtbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 26 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 30 | flotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 31 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 32 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 33 | fxtbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 34 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 35 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 36 | fsrcbillentity | 来源单据实体 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 37 | fxtseq | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 38 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 39 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 40 | fgroupno | 同组标识 | varchar | 36 |  | √ | ' ' | 同组标识 |
| 41 | fxtbillentryid | 形态转换单分录内码 | int8 | 64 |  | √ | 0 | 形态转换单分录内码 |
| 42 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 43 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 44 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 45 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 46 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 47 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 48 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 49 | fconverttype | 转换类型 | bpchar | 1 |  | √ | 'A' | 转换类型,枚举: A :转换前 B :转换后 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_mtoconvertentry |  | fentryid |
| 2 | idx_mrp_mtoconvertentry_fid |  | fid |

---

## 库存明细单据体-子表 t_mrp_mtoinvconvertentry

- **表名称：** 库存明细单据体-子表
- **表名：** t_mrp_mtoinvconvertentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 4 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 5 | fbaseinvqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 8 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 9 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 10 | fdemandbillno | 需求单据编码 | varchar | 80 |  | √ | ' ' | 需求单据编码 |
| 11 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 12 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 13 | fdemandbillentryseq | 需求单据分录行号 | int4 | 32 |  | √ | 0 | 需求单据分录行号 |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 16 | finvqty | 库存量 | numeric | 23 | 10 | √ | 0 | 库存量 |
| 17 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 19 | fissuelocationid | 发料仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 20 | finvid | 即时库存内码 | int8 | 64 |  | √ | 0 | 即时库存内码 |
| 21 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 23 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 24 | fissuewarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 25 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 26 | freqtracknumberid | 需求跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fdemandbillentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 30 | fdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_mtoinvconvertentry |  | fentryid |
| 2 | idx_mrp_mtoinvconvertentry_fid |  | fid |

---

## MTO库存调整-多语言表 t_mrp_mtoinvconvert_l

- **表名称：** MTO库存调整-多语言表
- **表名：** t_mrp_mtoinvconvert_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_mtoinvconvert_l_lid |  | fid,flocaleid |
| 2 | pk_mrp_mtoinvconvert_l |  | fpkid |
