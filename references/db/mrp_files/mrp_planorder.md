# 计划订单-mrp_planorder

## 联副产品-子表 t_mrp_planordercopentry

- **表名称：** 联副产品-子表
- **表名：** t_mrp_planordercopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcopentrytype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: 10720 :联产品 10730 :副产品 |
| 3 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fbizcopyallqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 5 | fbizcopyqty | 单位数量 | numeric | 23 | 10 | √ | 0 | 单位数量 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcopentryauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fcopentryallqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 9 | fbizcopyunitid | 产品计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fcopentryversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 11 | fcopentryoperation | 产出工序 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 12 | fcopentrymaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fcopentryvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | fcopentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fcopentryqty | 基本单位单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位单位数量 |
| 16 | fcopentryunit | 产品基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fcopentryinvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 20 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_planordercopentry |  | fentryid |
| 2 | idx_mrp_planordercopentry_fid |  | fid |

---

## 计划订单-主表 t_mrp_planorder

- **表名称：** 计划订单-主表
- **表名：** t_mrp_planorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanprogram | 计划方案 | int8 | 64 |  | √ | 0 | [计划方案 mrp_planscheme](../msplan_files/mrp_planscheme.md) |
| 3 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 4 | frootdemandentryid | 根需求单据分录ID | int8 | 64 |  | √ | 0 | 根需求单据分录ID |
| 5 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 7 | frootdemandentryseq | 根需求单据行号 | int4 | 32 |  | √ | 0 | 根需求单据行号 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fyield | 成品率% | numeric | 23 | 10 | √ | 0.0000000000 | 成品率% |
| 10 | fdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 11 | fenddate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 12 | fdemandseq | 需求单据分录行号 | int4 | 32 |  | √ | 0 | 需求单据分录行号 |
| 13 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 15 | fismrpcal | 已计划运算 | bpchar | 1 |  | √ | '0' | 已计划运算 |
| 16 | fadviseorderqty | 建议订单数量 | numeric | 23 | 10 | √ | 0 | 建议订单数量 |
| 17 | fordertype | 订单类型 | varchar | 60 |  | √ | ' ' | 订单类型,枚举: 10030 :自制 10050 :委外 10040 :外购 10060 :内协 10070 :返工自制 10080 :返工委外 |
| 18 | fownertype | 货主类型 | varchar | 30 |  | √ | 'bos_org' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 19 | fmaterial | 物料主档 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 20 | fplantags | 计划标识 | int8 | 64 |  | √ | 0 | [计划标识 mpdm_plantag](../mpdm_files/mpdm_plantag.md) |
| 21 | fadvisedroptime | 建议投放时间 | timestamp | 0 |  |  | null | 建议投放时间 |
| 22 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 23 | fmateriallock | 订单物料锁定 | bpchar | 1 |  | √ | '0' | 订单物料锁定 |
| 24 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 25 | fqty | 基本单位本次投放数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位本次投放数量 |
| 26 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | fbizunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fbillstatus | 单据状态 | varchar | 60 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | forderdate | 计划准备日期 | timestamp | 0 |  |  | null | 计划准备日期 |
| 30 | fdroptime | 投放时间 | timestamp | 0 |  |  | null | 投放时间 |
| 31 | fdropbilltypeid | 投放单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 32 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 33 | fplanoperatenum2 | 计划运算号2 | int8 | 64 |  | √ | 0 | [运算日志 mrp_caculate_log](../msplan_files/mrp_caculate_log.md) |
| 34 | fthreestock | 三品库存 | numeric | 23 | 10 | √ | 0.0000000000 | 三品库存 |
| 35 | fkittingbaseqty | 齐套基本数量 | numeric | 23 | 10 | √ | 0 | 齐套基本数量 |
| 36 | fplanpersonid | 计划员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fordermoq | 最小订单量 | numeric | 23 | 10 | √ | 0.0000000000 | 最小订单量 |
| 38 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fcommentreason | 备注原因 | varchar | 30 |  | √ | ' ' | 备注原因,枚举: a :SOP变化 b :独立需求未及时录入 c :BOM未归档 d :EC变更或物料替代 e :故障品不参与排产 f :其他原因 |
| 40 | frootdemandbillid | 根需求单据ID | int8 | 64 |  | √ | 0 | 根需求单据ID |
| 41 | fdemandtype | fdemandtype | varchar | 50 |  | √ | ' ' |  |
| 42 | fbom | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 43 | fstartdate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 44 | fbizorderqty | 订单数量 | numeric | 23 | 10 | √ | 0 | 订单数量 |
| 45 | fdatasource | 数据来源 | varchar | 60 |  | √ | ' ' | 数据来源,枚举: A :手工新增 B :计算产生 C :拆分产生 D :合并产生 |
| 46 | fmateriallmft | 物料生产信息 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 47 | fadviseenddate | 建议完成日期 | timestamp | 0 |  |  | null | 建议完成日期 |
| 48 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | funit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 50 | fdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 51 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 52 | fishistory | 是否历史数据 | bpchar | 1 |  | √ | '0' | 是否历史数据 |
| 53 | fbizdropqty | 投放数量 | numeric | 23 | 10 | √ | 0 | 投放数量 |
| 54 | fdropqty | 基本单位投放数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位投放数量 |
| 55 | fproorpurorg | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 56 | frootdemandentity | 根需求单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 57 | fmaterialspread | 重新展算订单物料 | bpchar | 1 |  | √ | '0' | 重新展算订单物料 |
| 58 | fendproqty | 基本单位成品数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位成品数量 |
| 59 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 60 | finwardept | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 61 | fhistorydate | 历史日期 | timestamp | 0 |  |  | null | 历史日期 |
| 62 | fschedule | 投放失败原因 | varchar | 500 |  | √ | ' ' | 投放失败原因 |
| 63 | forderqty | 基本单位订单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位订单数量 |
| 64 | favailabledate | 可用日期 | timestamp | 0 |  |  | null | 可用日期 |
| 65 | fplanoperatenum | 计划运算号 | varchar | 100 |  | √ | ' ' | 计划运算号 |
| 66 | frootdemandbillno | 根需求单号 | varchar | 120 |  | √ | ' ' | 根需求单号 |
| 67 | fbasedemandqty | 基本单位净需求数量 | numeric | 23 | 10 | √ | 0 | 基本单位净需求数量 |
| 68 | fprodline | 产线 | int8 | 64 |  | √ | 0 | [产线日产能F7 mrp_prodline_f7](../mrp_files/mrp_prodline_f7.md) |
| 69 | fmaterialattr | 物料属性 | varchar | 60 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 |
| 70 | fmaterialplanid | 物料编码 | int8 | 64 |  | √ | 0 | [物料计划信息 mpdm_materialplan](../sbd_files/mpdm_materialplan.md) |
| 71 | fremark | fremark | varchar | 50 |  | √ | ' ' |  |
| 72 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 73 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 74 | fismpsonly | 只算MPS | bpchar | 1 |  | √ | '0' | 只算MPS |
| 75 | fecnversion | ECN版本 | int8 | 64 |  | √ | 0 | [ECN版本 pdm_ecnversion](../fmm_files/pdm_ecnversion.md) |
| 76 | fsurplusdropqty | 基本单位剩余待投放数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位剩余待投放数量 |
| 77 | fdemandbill | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 78 | fproddept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 79 | fplantag | fplantag | varchar | 60 |  | √ | ' ' |  |
| 80 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :正常 B :关闭 C :拆分关闭 D :合并关闭 E :投放关闭 |
| 81 | funfoldbomdate | 展开BOM时间 | timestamp | 0 |  |  | null | 展开BOM时间 |
| 82 | dropstatus | dropstatus | varchar | 30 |  | √ | ' ' |  |
| 83 | fdropstatus | 投放状态 | varchar | 30 |  | √ | ' ' | 投放状态,枚举: A :未投放 B :投放中 C :部分投放 D :已投放 E :投放失败 |
| 84 | finnersupplier | 内部供应商 | bpchar | 1 |  | √ | '0' | 内部供应商 |
| 85 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 86 | fadvisestartdate | 建议开始日期 | timestamp | 0 |  |  | null | 建议开始日期 |
| 87 | fbizendproqty | 成品数量 | numeric | 23 | 10 | √ | 0 | 成品数量 |
| 88 | fdemandbillentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_planorder_ma |  | fmaterial |
| 2 | idx_mrp_planorder_pl |  | fplanoperatenum |
| 3 | idx_mrp_planorder_fnum |  | fbillno |
| 4 | idx_mrp_planorder_tracknumber |  | ftracknumber |
| 5 | t_mrp_planorder_pkey |  | fid |
| 6 | idx_mrp_planorder_org |  | fproorpurorg |

---

## 关联子实体-子表 t_mrp_planorder_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mrp_planorder_lk

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
| 1 | t_mrp_planorder_lk_pkey |  | fpkid |
| 2 | idx_mrp_planorder_lk_fk |  | fid |

---

## 计划订单-分表 t_mrp_planorder_a

- **表名称：** 计划订单-分表
- **表名：** t_mrp_planorder_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparentmaterial | 父项物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fkittingsign | 齐套状况 | varchar | 5 |  | √ | ' ' | 齐套状况,枚举: A :库存齐套 B :预计齐套 C :不齐套 D :暂收齐套 E :在途齐套 F :采购申请齐套 G :计划订单齐套 |
| 4 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 6 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 7 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_planorder_a |  | fid |

---

## 计划订单-多语言表 t_mrp_planorder_l

- **表名称：** 计划订单-多语言表
- **表名：** t_mrp_planorder_l

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
| 1 | pk_t_mrp_planorder_l |  | fpkid |
| 2 | idx_mrp_planorder_l |  | fid,flocaleid |

---

## 计划订单-反写记录表 t_mrp_planorder_wb

- **表名称：** 计划订单-反写记录表
- **表名：** t_mrp_planorder_wb

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
| 1 | idx_mrp_planorder_wb_fk |  | fid |
| 2 | t_mrp_planorder_wb_pkey |  | fentryid |

---

## 单据体-子表 t_mrp_planorderentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_planorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequiredate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 3 | fentryreplacematerial | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 4 | frequireqty | 基本单位需求数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位需求数量 |
| 5 | fwastagerateformula | 损耗计算公式 | varchar | 30 |  | √ | ' ' | 损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 6 | fstandqty | 基本单位标准用量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位标准用量 |
| 7 | fissuemode | 领送料方式 | varchar | 30 |  | √ | '11010' | 领送料方式,枚举: 11010 :生产领料 11040 :不领料 |
| 8 | fiscannegative | 退料 | bpchar | 1 |  | √ | '0' | 退料 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率% |
| 11 | fbizrequireqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 12 | fbizqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0 | 用量：分母 |
| 13 | foperatemrp | MRP运算 | bpchar | 1 |  | √ | '1' | MRP运算 |
| 14 | freplacegroup | 替代组号 | int4 | 32 |  | √ | 0 | 替代组号 |
| 15 | fbomid | BOM表头ID | int8 | 64 |  | √ | 0 | BOM表头ID |
| 16 | fentryreplaceplan | 替代方案 | int8 | 64 |  | √ | 0 | [物料替代方案 mpdm_replaceplan](../basedata_files/mpdm_replaceplan.md) |
| 17 | fbizlossqty | 损耗数量 | numeric | 23 | 10 | √ | 0 | 损耗数量 |
| 18 | fownertype | 货主类型 | varchar | 30 |  | √ | 'bos_org' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 19 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 20 | fisjumplevel | 跳层 | bpchar | 1 |  | √ | '0' | 跳层 |
| 21 | fbizdroprequireqty | 已投放需求数量 | numeric | 23 | 10 | √ | 0 | 已投放需求数量 |
| 22 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 23 | fentryauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 24 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 25 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fbizunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fqtydenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位用量：分母 |
| 28 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fentrydroprequireqty | 基本单位已投放需求数量 | numeric | 23 | 10 | √ | 0 | 基本单位已投放需求数量 |
| 30 | fchildbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 31 | fversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 32 | fissueorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 34 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fentryrepqty | 替代数量 | numeric | 23 | 10 | √ | 0 | 替代数量 |
| 36 | foutorgid | 调出组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fentryreplacestra | 替代策略 | varchar | 30 |  | √ | ' ' | 替代策略,枚举: 1001 :整批替代 1002 :混用替代 1003 :整批+混用 1004 :手工替代 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | flossqty | 基本单位损耗数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位损耗数量 |
| 41 | fbizstandqty | 标准用量 | numeric | 23 | 10 | √ | 0 | 标准用量 |
| 42 | fprocesssequence | 工序序列 | int4 | 32 |  | √ | 0 | 工序序列 |
| 43 | fentryisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 44 | fsupplytype | 供应类型 | varchar | 60 |  | √ | ' ' | 供应类型,枚举: 10040 :外购 10030 :自制 10050 :委外 |
| 45 | fiskey | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 46 | fmaterialid | 子项编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 47 | fentryconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 48 | fentryreplacepriority | 替代优先级 | int4 | 32 |  | √ | 0 | 替代优先级 |
| 49 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 50 | fmode | 行标识 | varchar | 60 |  | √ | ' ' | 行标识,枚举: A :手工新增 B :BOM展开新增 |
| 51 | fleadtime | 提前期偏置时间(天) | int4 | 32 |  | √ | 0 | 提前期偏置时间(天) |
| 52 | foutlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 53 | fqtytype | 用量类型 | varchar | 60 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 54 | fqtynumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位用量：分子 |
| 55 | fbizqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0 | 用量：分子 |
| 56 | fentryreplacemethod | 替代方式 | varchar | 30 |  | √ | ' ' | 替代方式,枚举: A :替代 B :取代 C :按比例 |
| 57 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 58 | ftype | 子项类型 | varchar | 30 |  | √ | ' ' | 子项类型,枚举: A :库存 B :物料组 C :文本 D :设备 E :工具 |
| 59 | flocationid | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 60 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 61 | fisstockalloc | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 62 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 63 | fentryrepmaterials | 替代物料 | varchar | 512 |  | √ | ' ' | 替代物料 |
| 64 | fisbackflushnew | 倒冲 | varchar | 30 |  | √ | 'A' | 倒冲,枚举: A :不倒冲 B :始终倒冲 |
| 65 | fentrymaterialplanid | 物料计划信息 | int8 | 64 |  | √ | 0 | [物料计划信息 mpdm_materialplan](../sbd_files/mpdm_materialplan.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_planorderentry |  | fid,fseq |
| 2 | t_mrp_planorderentry_pkey |  | fentryid |

---

## 单据体-分表 t_mrp_planorderentry_c

- **表名称：** 单据体-分表
- **表名：** t_mrp_planorderentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnetrequireratio | 净需求比例(%) | numeric | 23 | 10 | √ | 0 | 净需求比例(%) |
| 3 | ftagnum_tag | 位号_详情 | text | 0 |  |  | null | 位号_详情 |
| 4 | ftagnum | 位号 | varchar | 255 |  | √ | ' ' | 位号 |
| 5 | fsmulatoccup | fsmulatoccup | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fcmplstdmdnum | fcmplstdmdnum | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fentrylicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 10 | fcmplsetplan | fcmplsetplan | int8 | 64 |  | √ | 0 |  |
| 11 | fentrybonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fbomexpandpath | bom展开路径 | varchar | 500 |  | √ | ' ' | bom展开路径 |
| 14 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_planorderentry_c |  | fid |
| 2 | pk_mrp_planorderentry_c |  | fentryid |

---

## 联副产品-多语言表 t_mrp_planordercopentry_l

- **表名称：** 联副产品-多语言表
- **表名：** t_mrp_planordercopentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcopentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_planordercopentry_l |  | fpkid |
| 2 | idx_mrp_planordercopentry_l_el |  | fentryid,flocaleid |

---

## 计划订单-关联追踪表 t_mrp_planorder_tc

- **表名称：** 计划订单-关联追踪表
- **表名：** t_mrp_planorder_tc

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
| 1 | idx_mrp_planorder_tc_tbill |  | ftbillid |
| 2 | t_mrp_planorder_tc_pkey |  | fid |
| 3 | idx_mrp_planorder_tc_tid |  | ftid |
