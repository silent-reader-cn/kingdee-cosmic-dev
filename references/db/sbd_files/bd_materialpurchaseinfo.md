# 物料采购信息-bd_materialpurchaseinfo

## 物料采购信息-多语言表 t_bd_materialpurinfo_l

- **表名称：** 物料采购信息-多语言表
- **表名：** t_bd_materialpurinfo_l

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
| 1 | idx_bd_materialpurinfo_l_fid |  | fid,flocaleid |
| 2 | t_bd_materialpurinfo_l_pkey |  | fpkid |

---

## 物料采购信息-主表 t_bd_materialpurinfo

- **表名称：** 物料采购信息-主表
- **表名：** t_bd_materialpurinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 采购分类 | int8 | 64 |  | √ | 0 | [采购分类 bd_materialpurinfogroup](../sbd_files/bd_materialpurinfogroup.md) |
| 3 | fisneedrequest | 需要请购 | bpchar | 1 |  | √ | '0' | 需要请购 |
| 4 | fiscontrolqty | 控制收货数量 | bpchar | 1 |  | √ | '0' | 控制收货数量 |
| 5 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | finspectionleadtime | 检验提前期（天） | int4 | 32 |  | √ | 0 | 检验提前期（天） |
| 7 | freceiverateup | 收货超收比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 收货超收比率(%) |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fpurchaseunitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | freceiveratedown | 收货欠收比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 收货欠收比率(%) |
| 14 | fstatus | 采购信息数据状态 | varchar | 5 |  | √ | ' ' | 采购信息数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fsupplier | 默认供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 16 | fmasterid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbondcontrol | 保税控制 | bpchar | 1 |  | √ | '0' | 保税控制,枚举: 0 :非保税 1 :保税 2 :不控制 |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 21 | fisreturn | 允许退货(封存) | bpchar | 1 |  | √ | '0' | 允许退货(封存) |
| 22 | ffixedleadtime | 固定提前期（天） | int4 | 32 |  | √ | 0 | 固定提前期（天） |
| 23 | fcreateorgid | 采购信息创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 26 | fchangeleadtime | 变动提前期（天） | int4 | 32 |  | √ | 0 | 变动提前期（天） |
| 27 | fpurchasepriceunitid | 采购计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fiscontrolday | 控制时间 | bpchar | 1 |  | √ | '0' | 控制时间 |
| 29 | foperator | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | fisquotacontrol | 配额控制 | bpchar | 1 |  | √ | '0' | 配额控制 |
| 32 | fchangebatch | 变动批量 | int4 | 32 |  | √ | 0 | 变动批量 |
| 33 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fmbdmasterid | 物料采购信息内码 | int8 | 64 |  | √ | 0 | 物料采购信息内码 |
| 35 | fpostprocessingtime | 后处理时间（天） | int4 | 32 |  | √ | 0 | 后处理时间（天） |
| 36 | freceivedayup | 收货提前天数 | int8 | 64 |  | √ | 0 | 收货提前天数 |
| 37 | fpreprocessingtime | 前处理时间（天） | int4 | 32 |  | √ | 0 | 前处理时间（天） |
| 38 | fcommoninfoid | 物料组织公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 39 | fctrlstrategy | 采购信息控制策略 | varchar | 5 |  | √ | ' ' | 采购信息控制策略,枚举: 2 :分配/局部共享 7 :私有 5 :全局共享 |
| 40 | fisautonew | 自动新增 | bpchar | 1 |  | √ | '0' | 自动新增 |
| 41 | fenable | 采购信息使用状态 | varchar | 5 |  | √ | ' ' | 采购信息使用状态,枚举: 0 :禁用 1 :可用 |
| 42 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 43 | freceivedaydown | 收货延迟天数 | int8 | 64 |  | √ | 0 | 收货延迟天数 |
| 44 | fisapprovedsupplier | 货源控制 | bpchar | 1 |  | √ | '0' | 货源控制 |
| 45 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_materialpurinfobit |  | fbitindex |
| 2 | idx_bd_matpur_ctrlstrategy |  | fctrlstrategy |
| 3 | idx_t_bd_materialpurinfosrcid |  | fsourcedataid |
| 4 | idx_t_bd_materialpurinfo_createorg |  | fcreateorgid |
| 5 | t_bd_materialpurinfo_pkey |  | fid |
| 6 | idx_bd_materialpurinfo_master |  | fmasterid |
| 7 | idx_t_bd_materialpurinfo_master |  | fmasterid |

---

## 物料采购信息-使用范围表 t_bd_materialpurinfo_u

- **表名称：** 物料采购信息-使用范围表
- **表名：** t_bd_materialpurinfo_u

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
| 1 | t_bd_materialpurinfo_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_bd_materialpurinfo_u_uo |  | fuseorgid |

---

## 物料采购信息-使用范围位图表 t_bd_materialpurinfo_m

- **表名称：** 物料采购信息-使用范围位图表
- **表名：** t_bd_materialpurinfo_m

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
| 1 | pk_t_bd_materialpurinfo_m |  | forgid |
