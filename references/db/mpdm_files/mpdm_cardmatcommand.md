# 工卡物料需求-mpdm_cardmatcommand

## 使用范围-多选基础资料表 t_mpdm_cmaterialcmdmtc

- **表名称：** 使用范围-多选基础资料表
- **表名：** t_mpdm_cmaterialcmdmtc

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
| 1 | pk_mpdm_cmaterialcmdmtc |  | fpkid |
| 2 | idx_mpdm_cmaterialcmdmtc_fk |  | fentryid |

---

## 物料信息-多语言表 t_mpdm_cmaterialcmdentry_l

- **表名称：** 物料信息-多语言表
- **表名：** t_mpdm_cmaterialcmdentry_l

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
| 1 | pk_mpdm_cmaterialcmdentry_l |  | fpkid |
| 2 | idx_mpdm_cmaterialcmdentry_l_0 |  | fentryid,flocaleid |

---

## 物料信息-子表 t_mpdm_cmaterialcmdentry

- **表名称：** 物料信息-子表
- **表名：** t_mpdm_cmaterialcmdentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrybaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | finvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 4 | fsupplyorg | 供货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fentryownertype | 供应方式 | varchar | 50 |  | √ | ' ' | 供应方式,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 6 | flocation | 默认仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 9 | fisrequireqtyset | 按需定量 | bpchar | 1 |  | √ | '0' | 按需定量 |
| 10 | ffissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式,枚举: 11010 :生产领料 11040 :不领料 11060 :按需领料 |
| 11 | fentryprofessionaid | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 12 | fentryqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 13 | fentrymaterial | 物料编码(隐藏) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fisreplacement | 拆换件 | bpchar | 1 |  | √ | '0' | 拆换件 |
| 15 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 16 | fentryresptype | 预打单责任 | varchar | 50 |  | √ | ' ' | 预打单责任,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 17 | fmaterialattr | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 |
| 18 | fparamremark | 参数信息 | varchar | 255 |  | √ | ' ' | 参数信息 |
| 19 | fentryresp | 预打单责任方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fisbackflush | 倒冲 | varchar | 50 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 21 | foutwarehouse | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 22 | fentryiskey | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 23 | fisentryqtylimit | 限额控制 | bpchar | 1 |  | √ | '0' | 限额控制 |
| 24 | fwarehouse | 默认仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 25 | foutorg | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fisstockalloc | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 27 | fmaterialmftid | 组件编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 28 | fcabinconfigsen | 构型敏感 | bpchar | 1 |  | √ | '0' | 构型敏感 |
| 29 | fentrylimittop | 限额上限允差（%） | numeric | 23 | 10 | √ | 0 | 限额上限允差（%） |
| 30 | fcardoperationnoid | 工序号 | int8 | 64 |  | √ | 0 | [工卡工艺分录F7选择 mpdm_mrocardoperation_f7](../mpdm_files/mpdm_mrocardoperation_f7.md) |
| 31 | fentrytype | 组件类型 | varchar | 50 |  | √ | ' ' | 组件类型,枚举: A :库存 |
| 32 | fmaterielmtc | fmaterielmtc | int8 | 64 |  | √ | 0 |  |
| 33 | fentryunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 34 | fentryowner | 供应方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 36 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 37 | fentrylimitlow | 限额下限允差（%） | numeric | 23 | 10 | √ | 0 | 限额下限允差（%） |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | fentrysn | 序列号 | int8 | 64 |  | √ | 0 | 序列号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cmaterialcmdentry_mid |  | fentrymaterial |
| 2 | pk_mpdm_cmaterialcmdentry |  | fentryid |
| 3 | idx_cmaterialcmdentry_mft |  | fmaterialmftid |
| 4 | idx_mpdm_cmaterialcmdentry_fk |  | fid |

---

## 工卡物料需求-使用范围表 t_mpdm_cmaterialcmd_u

- **表名称：** 工卡物料需求-使用范围表
- **表名：** t_mpdm_cmaterialcmd_u

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
| 1 | idx_t_mpdm_cmaterialcmd_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_cmaterialcmd_u |  | fdataid,fuseorgid |

---

## 工卡物料需求-使用范围位图表 t_mpdm_cmaterialcmd_m

- **表名称：** 工卡物料需求-使用范围位图表
- **表名：** t_mpdm_cmaterialcmd_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_cmaterialcmd_m |  | forgid |

---

## 工卡物料需求-多语言表 t_mpdm_cmaterialcmd_l

- **表名称：** 工卡物料需求-多语言表
- **表名：** t_mpdm_cmaterialcmd_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cmaterialcmd_l_0 |  | fid,flocaleid |
| 2 | pk_mpdm_cmaterialcmd_l |  | fpkid |

---

## 工卡物料需求-主表 t_mpdm_cmaterialcmd

- **表名称：** 工卡物料需求-主表
- **表名：** t_mpdm_cmaterialcmd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fworkcardid | 工卡编码 | int8 | 64 |  | √ | 0 | [工卡 mpdm_mrocardroute](../mpdm_files/mpdm_mrocardroute.md) |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fbomversionid | BOM版本号 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 17 | ffromchange | 变更生成 | bpchar | 1 |  | √ | '0' | 变更生成 |
| 18 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 21 | fmaterialtypeid | 检修设备型号 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 22 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fmodelmpdone | 型号L1 | varchar | 255 |  | √ | ' ' | 型号L1 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fproductmaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 27 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 28 | fneedmaterial | 需要物料 | bpchar | 1 |  | √ | '0' | 需要物料 |
| 29 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 30 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fnocheck | 忽略检查 | bpchar | 1 |  | √ | '0' | 忽略检查 |
| 32 | fisnewversion | 最新版本 | bpchar | 1 |  | √ | '1' | 最新版本 |
| 33 | fcabinconfigid | 构型 | int8 | 64 |  | √ | 0 | [客舱构型 mpdm_cabinconfig](../mpdm_files/mpdm_cabinconfig.md) |
| 34 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 36 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 37 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cmaterialcmd_master |  | fmasterid |
| 2 | idx_t_mpdm_cmaterialcmd_createorg |  | fcreateorgid |
| 3 | pk_mpdm_cmaterialcmd |  | fid |
| 4 | idx_t_mpdm_cmaterialcmd_master |  | fmasterid |
| 5 | idx_cmaterialcmd_createorg |  | fcreateorgid |
| 6 | idx_cmaterialcmd_wcid |  | fworkcardid |

---

## 数据来源依据-附件表 t_mpdm_matcommentrydoc

- **表名称：** 数据来源依据-附件表
- **表名：** t_mpdm_matcommentrydoc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_matcommentrydoc_fentryid |  | fentryid |
| 2 | pk_mpdm_matcommentrydoc |  | fpkid |
