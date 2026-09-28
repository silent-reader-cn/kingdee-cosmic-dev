# 发料计划方案定义-pom_planprogram

## 需求参数单据体-子表 t_pom_planproentry

- **表名称：** 需求参数单据体-子表
- **表名：** t_pom_planproentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresourceregister | 数据源配置 | int8 | 64 |  | √ | 0 | [数据源配置 mrp_resource_dataconfig](../msplan_files/mrp_resource_dataconfig.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdemandsrc | 需求来源 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fisscmrpoperat | 参与MRP运算 | bpchar | 1 |  | √ | '0' | 参与MRP运算 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pom_planproentry |  | fentryid |
| 2 | idx_pom_planproentry |  | fid,fseq |

---

## 需求优先级映射-子表 t_pom_planpentry

- **表名称：** 需求优先级映射-子表
- **表名：** t_pom_planpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffruncondition_tag | 生效条件_详情 | text | 0 |  |  | null | 生效条件_详情 |
| 3 | felementtype | 要素类型 | varchar | 30 |  | √ | ' ' | 要素类型,枚举: 0 :数值 1 :日期 2 :实体 |
| 4 | fdemandentity | 业务实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fdemandlogo | 字段标识 | varchar | 100 |  | √ | ' ' | 字段标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdemandname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 8 | ftypename | 名称 | int8 | 64 |  | √ | 0 | [优先级类型定义 mrp_priority_type](../msplan_files/mrp_priority_type.md) |
| 9 | fpentryfrunconditiondesc | 生效条件 | varchar | 255 |  | √ | ' ' | 生效条件 |
| 10 | ffruncondition | 生效条件 | varchar | 255 |  | √ | ' ' | 生效条件 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | felementname | 要素名称 | varchar | 100 |  | √ | ' ' | 要素名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pom_planpentry |  | fentryid |
| 2 | idx_pom_planpentry |  | fid,fseq |

---

## 发料计划方案定义-使用范围表 t_pom_planprogram_u

- **表名称：** 发料计划方案定义-使用范围表
- **表名：** t_pom_planprogram_u

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
| 1 | pk_t_pom_planprogram_u |  | fdataid,fuseorgid |
| 2 | idx_t_pom_planprogram_u_uo |  | fuseorgid |

---

## 发料计划方案定义-多语言表 t_pom_planprogram_l

- **表名称：** 发料计划方案定义-多语言表
- **表名：** t_pom_planprogram_l

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
| 1 | idx_pom_planprogram_l |  | fid,flocaleid |
| 2 | pk_t_pom_planprogram_l |  | fpkid |

---

## 发料计划方案定义-使用范围位图表 t_pom_planprogram_m

- **表名称：** 发料计划方案定义-使用范围位图表
- **表名：** t_pom_planprogram_m

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
| 1 | pk_t_pom_planprogram_m |  | forgid |

---

## 供应参数单据体-子表 t_pom_planproscentry

- **表名称：** 供应参数单据体-子表
- **表名：** t_pom_planproscentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresourceregisters | 数据源配置 | int8 | 64 |  | √ | 0 | [数据源配置 mrp_resource_dataconfig](../msplan_files/mrp_resource_dataconfig.md) |
| 3 | fsupplyres | 供应资源 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsupplypriority | 供应优先级 | int4 | 32 |  | √ | 0 | 供应优先级 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fisscmrpoperat | 参与MRP运算 | bpchar | 1 |  | √ | '0' | 参与MRP运算 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pom_planproscentry |  | fentryid |
| 2 | idx_pom_planproscentry |  | fid,fseq |

---

## 发料计划方案定义-主表 t_pom_planprogram

- **表名称：** 发料计划方案定义-主表
- **表名：** t_pom_planprogram

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdemandmodel | 需求模型 | int8 | 64 |  | √ | 0 | [资源注册模型 mrp_resourceregister_cf](../msplan_files/mrp_resourceregister_cf.md) |
| 4 | fwaterlevel | 考虑水位 | bpchar | 1 |  | √ | '0' | 考虑水位 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | foutofdate | 需求：拖期期间 | varchar | 30 |  | √ | ' ' | 需求：拖期期间,枚举: 1 :所有拖期期间 2 :指定拖期期间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcomputemode | 优先级计算模式 | varchar | 30 |  | √ | ' ' | 优先级计算模式,枚举: A :继承父项 B :重新计算 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fscoutofdate | 供应：拖期期间 | varchar | 30 |  | √ | ' ' | 供应：拖期期间,枚举: 1 :所有拖期期间 2 :指定拖期期间 |
| 13 | fmrpsetup | MRP参数设置 | int8 | 64 |  | √ | 0 | [MRP参数设置 mrp_paramset](../mrp_files/mrp_paramset.md) |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fday | 需求拖期期间 | int4 | 32 |  | √ | 0 | 需求拖期期间 |
| 17 | fcreateorgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fcalalloc | 调拨 | bpchar | 1 |  | √ | '0' | 调拨 |
| 21 | fminpack | 考虑最小包装量 | bpchar | 1 |  | √ | '0' | 考虑最小包装量 |
| 22 | fsupplymodel | 供应模型 | int8 | 64 |  | √ | 0 | [资源注册模型 mrp_resourceregister_cf](../msplan_files/mrp_resourceregister_cf.md) |
| 23 | fappmode | 优先级应用模式 | varchar | 30 |  | √ | ' ' | 优先级应用模式,枚举: A :需求日期 B :动态计算 |
| 24 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fplanoutlook | 计划展望期 | int4 | 32 |  | √ | 0 | 计划展望期 |
| 26 | fcalissue | 配送 | bpchar | 1 |  | √ | '0' | 配送 |
| 27 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: A :MRP B :SCM |
| 28 | frelativetransfer | 关联字段映射 | int8 | 64 |  | √ | 0 | [实体字段映射 mrp_billfieldtransfer](../msplan_files/mrp_billfieldtransfer.md) |
| 29 | fscday | 供应拖期期间 | int4 | 32 |  | √ | 0 | 供应拖期期间 |
| 30 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 33 | fstockreserve | 考虑预留 | bpchar | 1 |  | √ | '0' | 考虑预留 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pom_planprogram |  | fid |
| 2 | idx_t_pom_planprogram_createorg |  | fcreateorgid |
| 3 | idx_t_pom_planprogram_master |  | fmasterid |
| 4 | idx_pom_planprogram |  | fnumber,fcreateorgid |

---

## 组织参数单据体-子表 t_pom_planproorgentry

- **表名称：** 组织参数单据体-子表
- **表名：** t_pom_planproorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvstrategy | 库存供应策略 | int8 | 64 |  | √ | 0 | [库存供应策略 mrp_stocksupply_policy](../msplan_files/mrp_stocksupply_policy.md) |
| 3 | fsupplynet | 供应网络 | int8 | 64 |  | √ | 0 | [供应网络定义 mrp_definitionsupply](../msplan_files/mrp_definitionsupply.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdemandorg | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_planproorgentry |  | fid,fseq |
| 2 | pk_t_pom_planproorgentry |  | fentryid |
