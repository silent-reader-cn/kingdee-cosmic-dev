# 预测方案-diif_scheme

## 预测方案-主表 t_diif_scheme

- **表名称：** 预测方案-主表
- **表名：** t_diif_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fnextforecastdate | 下次预测运算时间 | timestamp | 0 |  |  | null | 下次预测运算时间 |
| 5 | fcycleunit | 预测周期单位 | varchar | 50 |  | √ | ' ' | 预测周期单位,枚举: MONTH :月 WEEK :周 DAY :日 |
| 6 | fsourceid | 数据源 | int8 | 64 |  | √ | 0 | [预测数据源 diif_source](../diif_files/diif_source.md) |
| 7 | fcustomerstdid | 客户分类标准选择 | int8 | 64 |  | √ | 0 | [客户分类标准 bd_customergroupstandard](../basedata_files/bd_customergroupstandard.md) |
| 8 | fmaterialdim | 物料维度 | varchar | 50 |  | √ | ' ' | 物料维度,枚举: SKU :物料编码+辅助属性 MATERIAL :物料编码 MATERIALGROUP :物料分类 |
| 9 | frefhistorycyclecount | 显示历史周期数 | int4 | 32 |  | √ | 0 | 显示历史周期数 |
| 10 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' |  |
| 11 | fusepromodel | 是否启用智能销售预测模型 | bpchar | 1 |  | √ | '0' | 是否启用智能销售预测模型 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fidsschmeid | 数据智能服务方案id | varchar | 50 |  | √ | ' ' | 数据智能服务方案id |
| 14 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcustomdimbasetype | 自定义粒度预测对象类型 | varchar | 50 |  | √ | ' ' | 自定义粒度预测对象类型,枚举: bd_tpl :基础数据模板 |
| 16 | fsys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 17 | fcyclecount | 预测周期数 | int4 | 32 |  | √ | 0 | 预测周期数 |
| 18 | frollingexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 19 | fbillno | 方案编号 | varchar | 50 |  | √ | ' ' | 方案编号 |
| 20 | fapprovedate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | frollingdateset | 日期设置 | varchar | 50 |  | √ | ' ' | 日期设置 |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fincludecurrentcycle | 预测包含本期 | bpchar | 1 |  | √ | '0' | 预测包含本期 |
| 26 | flatestforecastcycle | 最新预测运算周期 | varchar | 50 |  | √ | ' ' | 最新预测运算周期 |
| 27 | fmaterialstdid | 物料分类标准选择 | int8 | 64 |  | √ | 0 | [物料分类标准 bd_materialgroupstandard](../basedata_files/bd_materialgroupstandard.md) |
| 28 | fcustomerenable | 开启客户维度 | bpchar | 1 |  | √ | '0' | 开启客户维度 |
| 29 | flatestforecastdate | 最新预测运算时间 | timestamp | 0 |  |  | null | 最新预测运算时间 |
| 30 | fcustomerdim | 客户粒度 | varchar | 50 |  | √ | ' ' | 客户粒度,枚举: CUSTOMERGROUP :客户分类 CUSTOMER :客户 |
| 31 | fforecastdim | 预测维度 | varchar | 100 |  | √ | ' ' | 预测维度 |
| 32 | ftype | 方案类型 | varchar | 50 |  | √ | ' ' | 方案类型,枚举: STD :标准预测 PRO :高级预测模型 |
| 33 | fscheduleid | 调度计划id | varchar | 100 |  | √ | ' ' | 调度计划id |
| 34 | fsalesfuncdim | 销售职能粒度 | varchar | 50 |  | √ | ' ' | 销售职能粒度,枚举: SALESORG :销售组织 SALESDEPT :销售部门 SALESGROUP :销售组 |
| 35 | fmodelstatus | 预测模型状态 | varchar | 50 |  | √ | ' ' | 预测模型状态,枚举: NOTACTIVE :未上线 TRAINING :训练中 ONLINE :已上线 OFFLINE :已下线 |
| 36 | fcustomenable | 开启自定义维度 | bpchar | 1 |  | √ | '0' | 开启自定义维度 |
| 37 | frollingforecast | 自动执行滚动预测 | bpchar | 1 |  | √ | '0' | 自动执行滚动预测 |
| 38 | fforecastbilltype | 生成预测单类型 | varchar | 50 |  | √ | ' ' | 生成预测单类型,枚举: |
| 39 | falgorithm | 预测算法 | varchar | 50 |  | √ | ' ' | 预测算法,枚举: TE :季节趋势指数平滑 MA :移动平均 |
| 40 | fresponsiblevisible | 预测单仅责任人可见 | bpchar | 1 |  | √ | '0' | 预测单仅责任人可见 |
| 41 | frollingpredtime | 执行时间 | int4 | 32 |  | √ | '-1' | 执行时间 |
| 42 | fcustomdimbasefield | 预测对象 | varchar | 50 |  | √ | ' ' | 预测对象,枚举: |
| 43 | fnoforcastwithouttrans | 无交易记录不预测 | bpchar | 1 |  | √ | '0' | 无交易记录不预测 |
| 44 | frollingcron | cron表达式 | varchar | 100 |  | √ | ' ' | cron表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_diif_scheme_billno |  | fbillno |
| 2 | pk_t_diif_scheme |  | fid |

---

## 预测方案-多语言表 t_diif_scheme_l

- **表名称：** 预测方案-多语言表
- **表名：** t_diif_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_diif_scheme_l |  | fpkid |
| 2 | idx_diif_scheme_l |  | fid,flocaleid |

---

## 预测范围明细-子表 t_diif_schemeresponsible

- **表名称：** 预测范围明细-子表
- **表名：** t_diif_schemeresponsible

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresponsibleid | 默认责任人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 4 | fcustomergroupid | 客户分类 | int8 | 64 |  | √ | 0 | [客户分类 bd_customergroup](../basedata_files/bd_customergroup.md) |
| 5 | fschemematerial | 物料明细 | varchar | 50 |  | √ | ' ' | 物料明细 |
| 6 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 10 | fcustombaseid | 自定义维度 | int8 | 64 |  | √ | 0 | 基础数据模板 bd_tpl |
| 11 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_diif_schemeresponsible |  | fentryid |
| 2 | idx_diif_schemeresponsible_fk |  | fid |

---

## 子单据体-子表 t_diif_schemematerial

- **表名称：** 子单据体-子表
- **表名：** t_diif_schemematerial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 2 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_diif_schemeorgmaterial_fk |  | fentryid |
| 2 | pk_t_diif_schemematerial |  | fdetailid |
