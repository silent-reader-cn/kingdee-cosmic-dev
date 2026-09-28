# 因子数据维护-invp_invleveldata

## 因子数据维护-主表 t_invp_invleveldata

- **表名称：** 因子数据维护-主表
- **表名：** t_invp_invleveldata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fmainplantype | 计划类型 | bpchar | 1 |  | √ | 'A' | 计划类型,枚举: A :再订货点 B :最大最小 C :平衡利库 D :固定期间 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 19 | fdimension | 库存水位维度 | int8 | 64 |  | √ | 0 | [库存水位维度 msplan_plan_dimension](../msplan_files/msplan_plan_dimension.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_invp_invleveldata_master |  | fmasterid |
| 2 | idx_invp_invleveldata_fnum |  | fnumber |
| 3 | pk_invp_invleveldata |  | fid |
| 4 | idx_t_invp_invleveldata_createorg |  | fcreateorgid |

---

## 因子数据维护-多语言表 t_invp_invleveldata_l

- **表名称：** 因子数据维护-多语言表
- **表名：** t_invp_invleveldata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_invleveldata_l |  | fid,flocaleid |
| 2 | pk_invp_invleveldata_l |  | fpkid |

---

## 因子数据维护-使用范围表 t_invp_invleveldata_u

- **表名称：** 因子数据维护-使用范围表
- **表名：** t_invp_invleveldata_u

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
| 1 | idx_t_invp_invleveldata_u_uo |  | fuseorgid |
| 2 | pk_t_invp_invleveldata_u |  | fdataid,fuseorgid |

---

## 水位因子数据-子表 t_invp_invleveldataentry

- **表名称：** 水位因子数据-子表
- **表名：** t_invp_invleveldataentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmaterialgroup | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 4 | forderauditdays | 订单审批时间（天） | int8 | 64 |  | √ | 0 | 订单审批时间（天） |
| 5 | fproductdays | 供应商生产/加工时间（天） | int8 | 64 |  | √ | 0 | 供应商生产/加工时间（天） |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentrymateriel | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fmaterialgroupstandard | 物料分类标准 | int8 | 64 |  | √ | 0 | [物料分类标准 bd_materialgroupstandard](../basedata_files/bd_materialgroupstandard.md) |
| 9 | fprepaydays | 申请预付款时间（天） | int8 | 64 |  | √ | 0 | 申请预付款时间（天） |
| 10 | fordercycledays | 订货周期（天） | int8 | 64 |  | √ | 0 | 订货周期（天） |
| 11 | fsafeinvdays | 安全库存天数 | int8 | 64 |  | √ | 0 | 安全库存天数 |
| 12 | ftransitdays | 供应商运输时间（天） | int8 | 64 |  | √ | 0 | 供应商运输时间（天） |
| 13 | fsuppliercomfirmdays | 供应商确认订单时间（天） | int8 | 64 |  | √ | 0 | 供应商确认订单时间（天） |
| 14 | fbufferdays | 缓冲时间（天） | int8 | 64 |  | √ | 0 | 缓冲时间（天） |
| 15 | finspectdays | 来料检验时间（天） | int8 | 64 |  | √ | 0 | 来料检验时间（天） |
| 16 | fplantype | 计划方式 | bpchar | 1 |  | √ | 'A' | 计划方式,枚举: A :再订货点 B :最大最小库存 C :平衡利库 D :固定期间 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fentrystock | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_invleveldataentry_fid |  | fid |
| 2 | pk_invp_invleveldataentry |  | fentryid |
