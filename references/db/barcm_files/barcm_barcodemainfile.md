# 条码主档-barcm_barcodemainfile

## 条码主档-主表 t_barcm_bcmainfile

- **表名称：** 条码主档-主表
- **表名：** t_barcm_bcmainfile

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsalematerialid | 物料编号(销售) | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 3 | fsnnumbertext | 序列号文本 | varchar | 255 |  | √ | ' ' | 序列号文本 |
| 4 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | finventorymaterialid | 物料编号(库存) | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 7 | fdisabledate | 作废时间 | timestamp | 0 |  |  | null | 作废时间 |
| 8 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsncomment | 序列号备注 | varchar | 255 |  | √ | ' ' | 序列号备注 |
| 12 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :业务组织 |
| 13 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 14 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 15 | flotnumbertext | 批号文本 | varchar | 50 |  | √ | ' ' | 批号文本 |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 18 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 19 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | fsourcebizobjectid | 来源业务对象 | int8 | 64 |  | √ | 0 | 条码业务对象白名单 barcm_bizobjwhitelist |
| 21 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fdisablerid | 作废人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fkeepertype | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :库存组织 |
| 24 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 25 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 26 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 27 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 28 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 29 | fsrcorgid | 来源业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 31 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 33 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 36 | fisdisable | 已作废 | bpchar | 1 |  | √ | ' ' | 已作废 |
| 37 | flotnumber | 批号 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 38 | fmaterialid | 物料编号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 39 | fbarcoderuleid | 条码规则 | int8 | 64 |  | √ | 0 | 条码规则 barcm_barcoderule |
| 40 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 41 | fprdmaterialid | 物料编号(生产) | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 42 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 43 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 44 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 46 | faddprintcopies | 累计打印份数 | int4 | 32 |  | √ | 0 | 累计打印份数 |
| 47 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 48 | fcusmaterialid | 客户物料编码 | int8 | 64 |  | √ | 0 | 客户物料对应表明细信息 bd_customermaterialinfo |
| 49 | faddprinttimes | 累计打印次数 | int4 | 32 |  | √ | 0 | 累计打印次数 |
| 50 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 51 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 52 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 53 | fpurmaterialid | 物料编号(采购) | int8 | 64 |  | √ | 0 | 物料采购信息 bd_materialpurchaseinfo |
| 54 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 55 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 56 | fctrlstrategy | 控制策略 | bpchar | 3 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 57 | fbcprinttplid | 条码打印模板 | int8 | 64 |  | √ | 0 | 维护打印模板（新） bos_manageprinttpl |
| 58 | fenableserial | 启用序列号管理 | bpchar | 1 |  | √ | '0' | 启用序列号管理 |
| 59 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 60 | fentryinvorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 61 | fbarcodetypeid | 条码类型 | int8 | 64 |  | √ | 0 | 条码类型 barcm_barcodetype |
| 62 | fbarcodevalue | 条码 | varchar | 255 |  | √ | ' ' | 条码 |
| 63 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 64 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 65 | fsnnumber | 序列号（作废，源单可能反审核，导致序列号id不一致） | int8 | 64 |  | √ | 0 | 序列号主档 bd_snmainfile |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcmainfile |  | fid |
| 2 | idx_t_barcm_bcmainfile_createorg |  | fcreateorgid |
| 3 | idx_barcm_bcmainfile_bcvalue |  | fbarcodevalue |
| 4 | idx_t_barcm_bcmainfile_master |  | fmasterid |

---

## 条码主档-使用范围表 t_barcm_bcmainfile_u

- **表名称：** 条码主档-使用范围表
- **表名：** t_barcm_bcmainfile_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_barcm_bcmainfile_u |  | fdataid,fuseorgid |
| 2 | idx_t_barcm_bcmainfile_u_uo |  | fuseorgid |

---

## 条码主档-多语言表 t_barcm_bcmainfile_l

- **表名称：** 条码主档-多语言表
- **表名：** t_barcm_bcmainfile_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcmainfile_l |  | fpkid |
| 2 | idx_barcm_bcmainfile_fidflid |  | fid,flocaleid |

---

## 条码主档-分表 t_barcm_bcmainfile_a

- **表名称：** 条码主档-分表
- **表名：** t_barcm_bcmainfile_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgentime | 任务生成时间 | timestamp | 0 |  |  | null | 任务生成时间 |
| 3 | fpackagesizeid | 包装规格 | int8 | 64 |  | √ | 0 | 包装规格 barcm_packagesize |
| 4 | foutstockqty | 出库数量 | numeric | 23 | 10 | √ | 0 | 出库数量 |
| 5 | foutstockauxqty | 出库辅助数量 | numeric | 23 | 10 | √ | 0 | 出库辅助数量 |
| 6 | fpcsizeentryid | 包装规格行ID | int8 | 64 |  | √ | 0 | 包装规格行ID |
| 7 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fremainauxqty2 | 剩余辅助数量(2) | numeric | 23 | 10 | √ | 0 | 剩余辅助数量(2) |
| 9 | fnextlevelqty | 单层容量 | int4 | 32 |  | √ | 1 | 单层容量 |
| 10 | fpackagelistid | 装箱单ID | int8 | 64 |  | √ | 0 | 装箱单ID |
| 11 | fremainauxqty | 剩余辅助数量 | numeric | 23 | 10 | √ | 0 | 剩余辅助数量 |
| 12 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 13 | flevel | 层级 | int4 | 32 |  | √ | 1 | 层级 |
| 14 | foutstockbaseqty | 出库基本数量 | numeric | 23 | 10 | √ | 0 | 出库基本数量 |
| 15 | fremainbaseqty | 剩余基本数量 | numeric | 23 | 10 | √ | 0 | 剩余基本数量 |
| 16 | fgenseq | 生成顺序号 | int4 | 32 |  | √ | 0 | 生成顺序号 |
| 17 | fpackagelistno | 装箱单号 | varchar | 30 |  | √ | ' ' | 装箱单号 |
| 18 | ffacardid | 资产卡片ID | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 19 | fassetcode | 资产编码 | varchar | 255 |  | √ | '' | 资产编码 |
| 20 | fcontainertypeid | 包装容器类型 | int8 | 64 |  | √ | 0 | 包装容器类型 barcm_containertype_m |
| 21 | foutstockauxqty2 | 出库辅助数量(2) | numeric | 23 | 10 | √ | 0 | 出库辅助数量(2) |
| 22 | fremainqty | 剩余数量 | numeric | 23 | 10 | √ | 0 | 剩余数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_bcmainfilea_fid |  | fid |
| 2 | pk_barcm_bcmainfile_a |  | fid |
