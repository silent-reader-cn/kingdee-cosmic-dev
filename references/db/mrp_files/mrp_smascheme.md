# 缺料分析方案-mrp_smascheme

## 缺料分析方案-多语言表 t_mrp_smascheme_l

- **表名称：** 缺料分析方案-多语言表
- **表名：** t_mrp_smascheme_l

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
| 1 | idx_mrp_smascheme_l |  | fid,flocaleid |
| 2 | pk_mrp_smascheme_l |  | fpkid |

---

## 库存单据体-子表 t_mrp_smaschstoentry

- **表名称：** 库存单据体-子表
- **表名：** t_mrp_smaschstoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fwarehouseid | 仓库编码 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_smaschstoentry |  | fentryid |
| 2 | idx_mrp_smaschstoentry |  | fid,fseq |

---

## 缺料分析方案-主表 t_mrp_smascheme

- **表名称：** 缺料分析方案-主表
- **表名：** t_mrp_smascheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcrossprjsupply | 考虑跨项目供应 | bpchar | 1 |  | √ | '0' | 考虑跨项目供应 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbusinesstype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: lackanalye :缺料分析 tracemtrl :追料分析 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fprioritytype | 优先顺序 | varchar | 50 |  | √ | ' ' | 优先顺序,枚举: demandpriority :需求优先级 planbegintime :计划开工日期 planendtime :计划完工日期 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fisincludetransstk | 强制考虑调拨仓库 | bpchar | 1 |  | √ | '0' | 强制考虑调拨仓库 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | fmatchowner | 匹配供应考虑货主和货主类型 | bpchar | 1 |  | √ | '0' | 匹配供应考虑货主和货主类型 |
| 15 | fcreateorgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fsubstituted | 物料替代 | varchar | 50 |  | √ | ' ' | 物料替代,枚举: 1 :考虑替代 0 :忽略替代 |
| 19 | fexceptcheck | 收料忽略质检结果 | bpchar | 1 |  | √ | '0' | 收料忽略质检结果 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fmftdeptorgid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | freserved | 考虑预留 | varchar | 50 |  | √ | ' ' | 考虑预留,枚举: 0 :忽略弱预留 1 :考虑弱预留 |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fisincludeppbomstk | 强制考虑领料仓库 | bpchar | 1 |  | √ | '0' | 强制考虑领料仓库 |
| 26 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 27 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_smascheme |  | fid |
| 2 | idx_mrp_smascheme |  | fmasterid,fcreateorgid |
| 3 | idx_t_mrp_smascheme_createorg |  | fcreateorgid |
| 4 | idx_t_mrp_smascheme_master |  | fmasterid |

---

## 供应参数单据体-子表 t_mrp_smaschsupentry

- **表名称：** 供应参数单据体-子表
- **表名：** t_mrp_smaschsupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 3 | fsupplyres | 供应资源 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fisexcept | 排除 | bpchar | 1 |  | √ | '0' | 排除 |
| 5 | fexpireddate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsupplypriority | 供应优先级 | int4 | 32 |  | √ | 0 | 供应优先级 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_smaschsupentry |  | fentryid |
| 2 | idx_mrp_smaschsupentry |  | fid,fseq |

---

## 缺料分析方案-使用范围表 t_mrp_smascheme_u

- **表名称：** 缺料分析方案-使用范围表
- **表名：** t_mrp_smascheme_u

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
| 1 | idx_t_mrp_smascheme_u_uo |  | fuseorgid |
| 2 | pk_t_mrp_smascheme_u |  | fdataid,fuseorgid |
