# MTO在途调整建议-mrp_mtoinwayconvert

## MTO在途调整建议-主表 t_mrp_mtoinwayconv

- **表名称：** MTO在途调整建议-主表
- **表名：** t_mrp_mtoinwayconv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fcaculatelogid | 运算编号 | int8 | 64 |  | √ | 0 | [运算日志 mrp_caculate_log](../msplan_files/mrp_caculate_log.md) |
| 9 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_mtoinwayconv_billno |  | fbillno |
| 2 | pk_mrp_mtoinwayconv |  | fid |

---

## MTO在途调整建议-多语言表 t_mrp_mtoinwayconv_l

- **表名称：** MTO在途调整建议-多语言表
- **表名：** t_mrp_mtoinwayconv_l

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
| 1 | idx_mrp_mtoinwayconv_l_lid |  | fid,flocaleid |
| 2 | pk_mrp_mtoinwayconv_l |  | fpkid |

---

## 在途明细单据体-子表 t_mrp_mtoinwayconventry

- **表名称：** 在途明细单据体-子表
- **表名：** t_mrp_mtoinwayconventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplybillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 4 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 5 | fsupplydate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 8 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fdemandbillno | 需求单据编码 | varchar | 80 |  | √ | ' ' | 需求单据编码 |
| 10 | fbasesplitqty | 基本单位拆分数量 | numeric | 23 | 10 | √ | 0 | 基本单位拆分数量 |
| 11 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 12 | fdemandbillentryseq | 需求单据分录行号 | int4 | 32 |  | √ | 0 | 需求单据分录行号 |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fdemandorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fqty | 供应数量 | numeric | 23 | 10 | √ | 0 | 供应数量 |
| 16 | funitid | 业务单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fsupplybillid | 供应单据ID | varchar | 50 |  | √ | ' ' | 供应单据ID |
| 18 | fsplitqty | 拆分数量 | numeric | 23 | 10 | √ | 0 | 拆分数量 |
| 19 | fissuelocationid | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 20 | fsupplybillentity | 供应类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | fsupplybillentryseq | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 22 | fissuewarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 23 | fsupplybillentryid | 供应单据分录ID | varchar | 50 |  | √ | ' ' | 供应单据分录ID |
| 24 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 25 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 26 | freqtracknumberid | 需求跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 27 | fsupplyorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fdemandbillentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 31 | fdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_mtoinwayconventry |  | fentryid |
| 2 | idx_mrp_mtoinwayconventry_fid |  | fid |
