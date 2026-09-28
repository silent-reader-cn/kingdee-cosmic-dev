# 工卡物料需求变更单-mpdm_cmatcmdchange

## 关联子实体-子表 t_mpdm_cmatcmdchange_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpdm_cmatcmdchange_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_cmatcmdchange_lk |  | fpkid |
| 2 | idx_mpdm_cmatcmdchange_lk_fk |  | fid |

---

## 工卡物料需求变更单-主表 t_mpdm_cmatcmdchange

- **表名称：** 工卡物料需求变更单-主表
- **表名：** t_mpdm_cmatcmdchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fworkcardid | 工卡编码 | int8 | 64 |  | √ | 0 | [工卡 mpdm_mrocardroute](../mpdm_files/mpdm_mrocardroute.md) |
| 4 | fbilldate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 5 | fchangetype | 版本变更类型 | varchar | 50 |  | √ | ' ' | 版本变更类型,枚举: A :修改版本 B :顺延版本 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fnewversion | 新版本号 | varchar | 50 |  | √ | ' ' | 新版本号 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 11 | fmaterialtypeid | 设备检修型号 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmodelmpdone | 型号L1 | varchar | 255 |  | √ | ' ' | 型号L1 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fchangereason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 17 | fproductmaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fcardmaterialid | 工卡物料需求 | int8 | 64 |  | √ | 0 | [工卡物料需求 mpdm_cardmatcommand](../mpdm_files/mpdm_cardmatcommand.md) |
| 20 | fneedmaterial | 需要物料 | bpchar | 1 |  | √ | '0' | 需要物料 |
| 21 | fnocheck | 忽略检查 | bpchar | 1 |  | √ | '0' | 忽略检查 |
| 22 | fisnewversion | 最新版本 | bpchar | 1 |  | √ | '0' | 最新版本 |
| 23 | fcabinconfigid | 构型 | int8 | 64 |  | √ | 0 | [客舱构型 mpdm_cabinconfig](../mpdm_files/mpdm_cabinconfig.md) |
| 24 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cmatcmcc_no |  | fbillno |
| 2 | idx_mpdm_cmatcmcc_cmid |  | fcardmaterialid |
| 3 | pk_mpdm_cmatcmdchange |  | fid |
| 4 | idx_mpdm_cmatcmcc_pmid |  | fproductmaterial |

---

## 单据体-多语言表 t_mpdm_cmatcmdchangeentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_mpdm_cmatcmdchangeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparamremark | 参数信息 | varchar | 255 |  | √ | ' ' | 参数信息 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cmatcmdchangeentry_l |  | fentryid,flocaleid |
| 2 | pk_mpdm_cmatcmdchangeentry_l |  | fpkid |

---

## 工卡物料需求变更单-关联追踪表 t_mpdm_cmatcmdchange_tc

- **表名称：** 工卡物料需求变更单-关联追踪表
- **表名：** t_mpdm_cmatcmdchange_tc

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
| 1 | idx_mpdm_cmatcmdchange_tc_tid |  | ftid |
| 2 | pk_mpdm_cmatcmdchange_tc |  | fid |
| 3 | idx_mpdm_cmatcmdchange_tc_tbill |  | ftbillid |

---

## 使用范围-多选基础资料表 t_mpdm_cmatcmdchangemtc

- **表名称：** 使用范围-多选基础资料表
- **表名：** t_mpdm_cmatcmdchangemtc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料检修信息 mpdm_materialmtcinfo](../mpdm_files/mpdm_materialmtcinfo.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cmatcmdchangemtc_fk |  | fentryid |
| 2 | pk_mpdm_cmatcmdchangemtc |  | fpkid |

---

## 工卡物料需求变更单-反写记录表 t_mpdm_cmatcmdchange_wb

- **表名称：** 工卡物料需求变更单-反写记录表
- **表名：** t_mpdm_cmatcmdchange_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cmatcmdchange_wb_fk |  | fid |
| 2 | pk_mpdm_cmatcmdchange_wb |  | fentryid |

---

## 单据体-子表 t_mpdm_cmatcmdchangeentry

- **表名称：** 单据体-子表
- **表名：** t_mpdm_cmatcmdchangeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrybaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | finvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 4 | fsupplyorg | 供货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fentryownertype | 供应方式 | varchar | 50 |  | √ | ' ' | 供应方式,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 6 | frowtype | 行类型 | varchar | 50 |  | √ | ' ' | 行类型,枚举: A :新增 B :变更前 C :变更后 D :失效 |
| 7 | flocation | 默认仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 10 | fisrequireqtyset | 按需定量 | bpchar | 1 |  | √ | '0' | 按需定量 |
| 11 | ffissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式,枚举: 11010 :生产领料 11040 :不领料 11060 :按需领料 |
| 12 | fentryprofessionaid | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 13 | fentryqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 14 | fentrymaterial | 物料编码(隐藏) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 16 | fisreplacement | 拆换件 | bpchar | 1 |  | √ | '0' | 拆换件 |
| 17 | fentryresptype | 预打单责任 | varchar | 50 |  | √ | ' ' | 预打单责任,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 18 | fmaterialattr | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 |
| 19 | fparamremark | 参数信息 | varchar | 255 |  | √ | ' ' | 参数信息 |
| 20 | fentryresp | 预打单责任方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fisbackflush | 倒冲 | varchar | 50 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 22 | foutwarehouse | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 23 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fentryiskey | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 25 | fisentryqtylimit | 限额控制 | bpchar | 1 |  | √ | '0' | 限额控制 |
| 26 | fwarehouse | 默认仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 27 | foutorg | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 29 | fmaterialmftid | 组件编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 30 | fisstockalloc | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 31 | fentrylimittop | 限额上限允差（%） | numeric | 23 | 10 | √ | 0 | 限额上限允差（%） |
| 32 | fcardoperationnoid | 工序号 | int8 | 64 |  | √ | 0 | [工卡工艺分录F7选择 mpdm_mrocardoperation_f7](../mpdm_files/mpdm_mrocardoperation_f7.md) |
| 33 | fcmdentryid | 工卡物料需求分录ID | int8 | 64 |  | √ | 0 | 工卡物料需求分录ID |
| 34 | fentrytype | 组件类型 | varchar | 50 |  | √ | ' ' | 组件类型,枚举: A :库存 |
| 35 | fentryunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | fentryowner | 供应方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 38 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 39 | fentrylimitlow | 限额下限允差（%） | numeric | 23 | 10 | √ | 0 | 限额下限允差（%） |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fentrysn | 序列号 | int8 | 64 |  | √ | 0 | 序列号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cmatcmdchangeentry_fk |  | fid |
| 2 | idx_mpdm_cmatcmcce_mid |  | fentrymaterial |
| 3 | pk_mpdm_cmatcmdchangeentry |  | fentryid |
