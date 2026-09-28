# 物料生产信息-bd_materialmftinfo

## 物料生产信息-使用范围表 t_bd_materialmftinfo_u

- **表名称：** 物料生产信息-使用范围表
- **表名：** t_bd_materialmftinfo_u

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
| 1 | t_bd_materialmftinfo_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_bd_materialmftinfo_u_uo |  | fuseorgid |

---

## 物料生产信息-多语言表 t_bd_materialmftinfo_l

- **表名称：** 物料生产信息-多语言表
- **表名：** t_bd_materialmftinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_mtfinfo_l |  | fid,flocaleid |
| 2 | t_bd_materialmftinfo_l_pkey |  | fpkid |

---

## 物料生产信息-使用范围位图表 t_bd_materialmftinfo_m

- **表名称：** 物料生产信息-使用范围位图表
- **表名：** t_bd_materialmftinfo_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutstorageunitid | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcostfactor | 成本系数 | numeric | 23 | 10 | √ | 0 | 成本系数 |
| 4 | frpthighlimit | 汇报上限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报上限允差（%） |
| 5 | finterprocesstype | 内协加工类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fissuemode | 领送料方式 | varchar | 10 |  | √ | ' ' | 领送料方式,枚举: 11010 :生产领料 11030 :看板 11050 :直送 11040 :不领料 |
| 8 | flocation | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | finwarehouse | 入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 11 | fisecn | 启用ECN | bpchar | 1 |  | √ | '0' | 启用ECN |
| 12 | fsupplyorgunitid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 15 | fissueleadtime | 领料提前期（分钟）（废弃） | int8 | 64 |  | √ | 0 | 领料提前期（分钟）（废弃） |
| 16 | fissinlowlimit | 领料下限允差（%） | numeric | 23 | 10 | √ | 0 | 领料下限允差（%） |
| 17 | fbomversionrule | fbomversionrule | int8 | 64 |  | √ | 0 |  |
| 18 | fisreportlimit | 汇报限额控制 | bpchar | 1 |  | √ | '0' | 汇报限额控制 |
| 19 | fisjointproduct | 可联副产品 | bpchar | 1 |  | √ | ' ' | 可联副产品 |
| 20 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 22 | fiskeypart | 关键件 | varchar | 10 |  | √ | ' ' | 关键件 |
| 23 | fpersonid | 调度员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fmanufacturemode | 制造方式 | varchar | 5 |  | √ | ' ' | 制造方式,枚举: A :离散制造 B :项目制造 C :重复制造 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fisstoragelimit | 入库限额控制 | bpchar | 1 |  | √ | '0' | 入库限额控制 |
| 27 | fsuspend | 停产 | bpchar | 1 |  | √ | ' ' | 停产 |
| 28 | fmaterialid | 物料(冗余显示用_不支持逻辑处理) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 29 | frcvinhighlimit | 入库上限允差（%） | numeric | 23 | 10 | √ | 0 | 入库上限允差（%） |
| 30 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 31 | finwarelocation | 入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 32 | fistransmincount | 考虑最小包装量 | bpchar | 1 |  | √ | '0' | 考虑最小包装量 |
| 33 | fisbompauxattmust | fisbompauxattmust | bpchar | 1 |  | √ | '0' |  |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | foverissuecontrl | 超发控制方式 | varchar | 5 |  | √ | 'B' | 超发控制方式,枚举: A :可超发 B :不可超发 C :最小包装量 |
| 36 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | ftransacttypeid | ftransacttypeid | int8 | 64 |  | √ | 0 |  |
| 38 | fissinhighlimit | 领料上限允差（%） | numeric | 23 | 10 | √ | 0 | 领料上限允差（%） |
| 39 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | foutputtype | foutputtype | varchar | 10 |  | √ | ' ' |  |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fisquotacontrol | 领料限额控制（废弃） | bpchar | 1 |  | √ | '0' | 领料限额控制（废弃） |
| 43 | foutwarelocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 44 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 45 | frcvinlowlimit | 入库下限允差（%） | numeric | 23 | 10 | √ | 0 | 入库下限允差（%） |
| 46 | fisbackflush | 倒冲 | bpchar | 1 |  | √ | '0' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 47 | finwarorg | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | fprovidetype | fprovidetype | varchar | 10 |  | √ | ' ' |  |
| 49 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 50 | fconsumefluctuate | 消耗波动(%) | numeric | 23 | 10 | √ | 0 | 消耗波动(%) |
| 51 | fisbulkmaterial | 散装物料 | bpchar | 1 |  | √ | ' ' | 散装物料 |
| 52 | fismainproduct | 可主产品 | bpchar | 1 |  | √ | ' ' | 可主产品 |
| 53 | frptlowlimit | 汇报下限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报下限允差（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_mtfm_modifyt_s |  | fsupplyorgunitid |
| 2 | t_bd_materialmftinfo_m_pkey |  | fid |

---

## 物料生产信息-主表 t_bd_materialmftinfo

- **表名称：** 物料生产信息-主表
- **表名：** t_bd_materialmftinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstaworhours | 单位标准工时 | numeric | 23 | 10 | √ | 0 | 单位标准工时 |
| 3 | fprocessrouteid | 工艺路线 | int8 | 64 |  | √ | 0 | [工艺路线 mpdm_sfcprocessroute](../sbd_files/mpdm_sfcprocessroute.md) |
| 4 | fgroupid | 生产分类 | int8 | 64 |  | √ | 0 | [生产分类 bd_materialmftinfogroup](../sbd_files/bd_materialmftinfogroup.md) |
| 5 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | finspectionleadtime | 检验提前期（天） | int4 | 32 |  | √ | 0 | 检验提前期（天） |
| 7 | fdepartmentorgid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fscraprate | 变动损耗率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率(%) |
| 9 | ffixbatchqty | ffixbatchqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fforwardtime | fforwardtime | int8 | 64 |  | √ | 0 |  |
| 12 | fplandepartmentid | fplandepartmentid | int8 | 64 |  | √ | 0 |  |
| 13 | fbatchcycle | fbatchcycle | int8 | 64 |  | √ | 0 |  |
| 14 | fyield | fyield | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fbackwardtime | fbackwardtime | int8 | 64 |  | √ | 0 |  |
| 16 | fthrowmode | fthrowmode | varchar | 10 |  | √ | ' ' |  |
| 17 | fstamacworhours | 标准机器实作工时 | numeric | 23 | 10 | √ | 0 | 标准机器实作工时 |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | fxkallocationtype | 生产信息分配类型 | varchar | 30 |  | √ | ' ' | 生产信息分配类型,枚举: 1 :个性化 2 :共享型 |
| 20 | fbatchincqty | fbatchincqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 21 | ffixedleadtime | 固定提前期（天） | int8 | 64 |  | √ | 0 | 固定提前期（天） |
| 22 | fname | fname | varchar | 60 |  | √ | ' ' |  |
| 23 | fchangeleadtime | 变动提前期（天） | int8 | 64 |  | √ | 0 | 变动提前期（天） |
| 24 | ftestleadtime | ftestleadtime | int8 | 64 |  | √ | 0 |  |
| 25 | fbackwarddaysoffset | fbackwarddaysoffset | int8 | 64 |  | √ | 0 |  |
| 26 | fchangebatch | 变动批量 | int4 | 32 |  | √ | 0 | 变动批量 |
| 27 | fmbdmasterid | 物料生产信息内码 | int8 | 64 |  | √ | 0 | 物料生产信息内码 |
| 28 | fstalabworkhours | 标准人工实作工时 | numeric | 23 | 10 | √ | 0 | 标准人工实作工时 |
| 29 | fpartdays | fpartdays | int8 | 64 |  | √ | 0 |  |
| 30 | fpreprocessingtime | 前处理时间（天） | int4 | 32 |  | √ | 0 | 前处理时间（天） |
| 31 | fcommoninfoid | 物料组织公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 32 | fplanpersonid | fplanpersonid | int8 | 64 |  | √ | 0 |  |
| 33 | fparttype | fparttype | varchar | 10 |  | √ | ' ' |  |
| 34 | ftimeunit | 时间单位 | varchar | 30 |  | √ | ' ' | 时间单位,枚举: hour :小时 minute :分钟 second :秒 |
| 35 | fenable | 生产信息使用状态 | varchar | 10 |  | √ | ' ' | 生产信息使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fnumber | 编码 | varchar | 80 |  |  | ' ' | 编码 |
| 37 | fscraprateexpr | fscraprateexpr | varchar | 10 |  | √ | ' ' |  |
| 38 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 39 | fchangebatchqty | fchangebatchqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 40 | fisolatedrule | fisolatedrule | varchar | 10 |  | √ | ' ' |  |
| 41 | fprodtypeid | 生产类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 42 | fmultiple | fmultiple | int8 | 64 |  | √ | 0 |  |
| 43 | fsubunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 44 | fisconfigurable | fisconfigurable | bpchar | 1 |  | √ | '0' |  |
| 45 | fstatus | 生产信息数据状态 | varchar | 10 |  | √ | ' ' | 生产信息数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 46 | fmasterid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 47 | foffsetmode | foffsetmode | varchar | 10 |  | √ | ' ' |  |
| 48 | fbondcontrol | 保税控制 | bpchar | 1 |  | √ | '0' | 保税控制,枚举: 0 :非保税 1 :保税 2 :不控制 |
| 49 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 50 | fstamacprehours | 标准机器准备工时 | numeric | 23 | 10 | √ | 0 | 标准机器准备工时 |
| 51 | fminbatchqty | fminbatchqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 52 | fmaterialattr | fmaterialattr | varchar | 10 |  | √ | ' ' |  |
| 53 | fcreateorgid | 生产信息创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | fmftunitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 55 | fleadtimetype | fleadtimetype | varchar | 10 |  | √ | ' ' |  |
| 56 | fstalabworprehours | 标准人工准备工时 | numeric | 23 | 10 | √ | 0 | 标准人工准备工时 |
| 57 | fpostprocessingtime | 后处理时间（天） | int4 | 32 |  | √ | 0 | 后处理时间（天） |
| 58 | fctrlstrategy | 生产信息控制策略 | varchar | 10 |  | √ | ' ' | 生产信息控制策略,枚举: 2 :分配/局部共享 7 :私有 5 :全局共享 |
| 59 | fmaxbatchqty | fmaxbatchqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 60 | fbatchpolicy | fbatchpolicy | varchar | 10 |  | √ | ' ' |  |
| 61 | fisautonew | 自动新增 | bpchar | 1 |  | √ | '0' | 自动新增 |
| 62 | fforwarddayoffset | fforwarddayoffset | int8 | 64 |  | √ | 0 |  |
| 63 | fplantype | fplantype | varchar | 10 |  | √ | ' ' |  |
| 64 | fmtfstrategyid | fmtfstrategyid | int8 | 64 |  | √ | 0 |  |
| 65 | fismergesign | fismergesign | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_materialmftinfo_pkey |  | fid |
| 2 | idx_t_bd_materialmftinfo_createorg |  | fcreateorgid |
| 3 | idx_t_bd_materialmftinfo_master |  | fmasterid |
| 4 | idx_bd_mtfinfo_master |  | fmasterid |
| 5 | idx_t_bd_materialmftinfobit |  | fbitindex |
| 6 | idx_t_bd_materialmftinfosrcid |  | fsourcedataid |

---

## 物料控制组分录-子表 t_bd_mftcontrolentry

- **表名称：** 物料控制组分录-子表
- **表名：** t_bd_mftcontrolentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizgroup | 业务分组 | int8 | 64 |  | √ | 0 | [物料控制组控件 bd_prodgroupcontrol](../basedata_files/bd_prodgroupcontrol.md) |
| 3 | fremarks | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmaterialcontrolid | 编码 | int8 | 64 |  | √ | 0 | [物料控制组 bd_materialcontrolgroup](../basedata_files/bd_materialcontrolgroup.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_mftcontrolg_fid |  | fid |
| 2 | t_bd_mftcontrolentry_pkey |  | fentryid |
