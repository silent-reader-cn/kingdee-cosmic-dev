# 物料库存信息-bd_materialinventoryinfo

## 物料库存信息-主表 t_bd_materialinvinfo

- **表名称：** 物料库存信息-主表
- **表名：** t_bd_materialinvinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fismaxinvalert | 启用最大库存预警 | bpchar | 1 |  | √ | '0' | 启用最大库存预警 |
| 3 | fgroupid | 库存分类 | int8 | 64 |  | √ | 0 | 库存分类 bd_materialinvinfogroup |
| 4 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fissaftyinvalert | 启用安全库存预警 | bpchar | 1 |  | √ | '0' | 启用安全库存预警 |
| 9 | fbarcode | 条码 | varchar | 255 |  | √ | ' ' | 条码 |
| 10 | fsaftyinvratio | 比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 比例(%) |
| 11 | fisuseunit3rd | fisuseunit3rd | bpchar | 1 |  | √ | '0' |  |
| 12 | fisautochangeabc | ABC分类自动修改 | bpchar | 1 |  | √ | '0' | ABC分类自动修改 |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 16 | fropointratio | 比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 比例(%) |
| 17 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | freorderpointqty | 再订货点（基本单位） | numeric | 23 | 10 | √ | 0.0000000000 | 再订货点（基本单位） |
| 19 | fmbdmasterid | 物料库存信息内码 | int8 | 64 |  | √ | 0 | 物料库存信息内码 |
| 20 | fwarehouseid | 默认仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 21 | fabctype | ABC分类 | varchar | 5 |  | √ | ' ' | ABC分类,枚举: A :A类 B :B类 C :C类 |
| 22 | fmininvratio | 比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 比例(%) |
| 23 | fismininvalert | 启用最小库存预警 | bpchar | 1 |  | √ | '0' | 启用最小库存预警 |
| 24 | fenable | 库存信息使用状态 | varchar | 5 |  | √ | ' ' | 库存信息使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | funitconvertdir | funitconvertdir | varchar | 5 |  | √ | '0' |  |
| 26 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 27 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fisoutputrequest | 序列号必录 | bpchar | 1 |  | √ | '0' | 序列号必录 |
| 30 | funit2ndid | funit2ndid | int8 | 64 |  | √ | 0 |  |
| 31 | fconsumption | 物料消耗量(天) | numeric | 23 | 10 | √ | 0.0000000000 | 物料消耗量(天) |
| 32 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | fminpackqty | 最小包装量 | numeric | 23 | 10 | √ | 0.0000000000 | 最小包装量 |
| 34 | finventoryunitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | fmaxinvratio | 比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 比例(%) |
| 36 | fserialruleid | 序列号规则 | int8 | 64 |  | √ | 0 | 供应链编码规则 bd_lotcoderule |
| 37 | fstatus | 库存信息数据状态 | varchar | 5 |  | √ | ' ' | 库存信息数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 38 | fisallowneginv | 允许负库存 | bpchar | 1 |  | √ | '0' | 允许负库存 |
| 39 | fmasterid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fisuseunit2nd | fisuseunit2nd | bpchar | 1 |  | √ | '0' |  |
| 42 | fenablelot | 启用批号管理 | bpchar | 1 |  | √ | '0' | 启用批号管理 |
| 43 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 44 | frobatchqty | 再订货批量 | numeric | 23 | 10 | √ | 0.0000000000 | 再订货批量 |
| 45 | fisreorderpointalert | 启用再订货点预警 | bpchar | 1 |  | √ | '0' | 启用再订货点预警 |
| 46 | fmanustrategyid | 制造策略 | int8 | 64 |  | √ | 0 | 制造策略 bd_manustrategy |
| 47 | fcreateorgid | 库存信息创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | fsngentimepoint | 序列号生成时点 | varchar | 50 |  | √ | ' ' | 序列号生成时点,枚举: 1 :必须预先生成 2 :仅入库时生成 3 :仅出库时生成 4 :出入库都可生成 |
| 51 | fctrlstrategy | 库存信息控制策略 | varchar | 5 |  | √ | ' ' | 库存信息控制策略,枚举: 2 :分配/局部共享 7 :私有 5 :全局共享 |
| 52 | fmininvqty | 最小库存（基本单位） | numeric | 23 | 10 | √ | 0.0000000000 | 最小库存（基本单位） |
| 53 | fenableserial | 启用序列号管理 | bpchar | 1 |  | √ | '0' | 启用序列号管理 |
| 54 | fisreserve | 允许预留 | bpchar | 1 |  | √ | '1' | 允许预留 |
| 55 | flocationid | 默认仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 56 | fsaftyinvqty | 安全库存（基本单位） | numeric | 23 | 10 | √ | 0.0000000000 | 安全库存（基本单位） |
| 57 | fisautonew | 自动新增 | bpchar | 1 |  | √ | '0' | 自动新增 |
| 58 | fmaxinvqty | 最大库存（基本单位） | numeric | 23 | 10 | √ | 0.0000000000 | 最大库存（基本单位） |
| 59 | freservationperiod | 预留期限 | int8 | 64 |  | √ | 0 | 预留期限 |
| 60 | funit3rdid | funit3rdid | int8 | 64 |  | √ | 0 |  |
| 61 | flotcoderuleid | 批号规则 | int8 | 64 |  | √ | 0 | 供应链编码规则 bd_lotcoderule |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_materinv_fmatid |  | fmasterid |
| 2 | idx_t_bd_materialinvinfo_createorg |  | fcreateorgid |
| 3 | t_bd_materialinvinfo_pkey |  | fid |
| 4 | idx_t_bd_materialinvinfobit |  | fbitindex |
| 5 | idx_bd_matinv_ctrlstrategy |  | fctrlstrategy |
| 6 | idx_t_bd_materialinvinfosrcid |  | fsourcedataid |
| 7 | idx_t_bd_materialinvinfo_master |  | fmasterid |

---

## 物料库存信息-使用范围表 t_bd_materialinvinfo_u

- **表名称：** 物料库存信息-使用范围表
- **表名：** t_bd_materialinvinfo_u

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
| 1 | t_bd_materialinvinfo_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_bd_materialinvinfo_u_uo |  | fuseorgid |

---

## 物料库存信息-分表 t_bd_materialinvinfo_x

- **表名称：** 物料库存信息-分表
- **表名：** t_bd_materialinvinfo_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstartdatecaltype | 生产日计算方式 | bpchar | 1 |  | √ | '' | 生产日计算方式,枚举: 1 :到期日-保质期 2 :到期日-保质期+1 |
| 3 | foutboundrules | 出库规则(废弃) | bpchar | 1 |  | √ | ' ' | 出库规则(废弃),枚举: A :按批号先进先出 B :按批号后进先出 C :按批号顺序 D :按近效期 |
| 4 | fshelflifeunit | 保质期单位 | varchar | 10 |  | √ | ' ' | 保质期单位,枚举: day :日 month :月 year :年 |
| 5 | fdateofoverdueforout | 出库失效提前期 | int8 | 64 |  | √ | 0 | 出库失效提前期 |
| 6 | fenablewarnlead | 启用预警 | bpchar | 1 |  | √ | '0' | 启用预警 |
| 7 | fenablebarcode | 启用条码管理 | bpchar | 1 |  | √ | '0' | 启用条码管理 |
| 8 | fshelflife | 保质期 | int8 | 64 |  | √ | 0 | 保质期 |
| 9 | fwarnleadtime | 预警提前期 | int8 | 64 |  | √ | 0 | 预警提前期 |
| 10 | fenableshelflifemgr | 保质期管理 | bpchar | 1 |  | √ | '0' | 保质期管理 |
| 11 | foutboundrule | 出库规则 | int8 | 64 |  | √ | '1837734917334093824' | 出库规则配置 bd_matchout_rule |
| 12 | fcalculationforenddate | 到期日计算方式 | bpchar | 1 |  | √ | ' ' | 到期日计算方式,枚举: 0 :生产日期+保质期 1 :生产日期+保质期-1 2 :生产日期+保质期上个月的最后一天 |
| 13 | fdateofoverdueforin | 入库失效提前期 | int8 | 64 |  | √ | 0 | 入库失效提前期 |
| 14 | fcaldirection | 计算方向 | bpchar | 1 |  | √ | '' | 计算方向,枚举: 1 :按生产日计算到期日 2 :按到期日计算生产日 3 :相互计算 4 :互不计算 |
| 15 | fleadtimeunit | 提前期单位 | varchar | 10 |  | √ | ' ' | 提前期单位,枚举: day :日 month :月 year :年 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_materialinvinfo_x_pkey |  | fid |
| 2 | idx_bd_materinv_fshelflife_x |  | fshelflife |

---

## 物料库存信息-使用范围位图表 t_bd_materialinvinfo_m

- **表名称：** 物料库存信息-使用范围位图表
- **表名：** t_bd_materialinvinfo_m

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
| 1 | pk_t_bd_materialinvinfo_m |  | forgid |

---

## 物料库存信息-多语言表 t_bd_materialinvinfo_l

- **表名称：** 物料库存信息-多语言表
- **表名：** t_bd_materialinvinfo_l

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
| 1 | t_bd_materialinvinfo_l_pkey |  | fpkid |
| 2 | idx_materialinv_l_fid |  | fid,flocaleid |
