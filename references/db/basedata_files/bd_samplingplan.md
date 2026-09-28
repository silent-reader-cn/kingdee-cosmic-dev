# 取样方案-bd_samplingplan

## 取样操作规程-子表 t_bd_samprocedureentry

- **表名称：** 取样操作规程-子表
- **表名：** t_bd_samprocedureentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fretentionperiod | 留存期限 | int4 | 32 |  | √ | 0 | 留存期限 |
| 3 | fmatchdimension | 匹配维度 | varchar | 1 |  | √ | ' ' | 匹配维度,枚举: A :物料 B :通用 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fsamplestorageloc | 留样位置 | varchar | 50 |  | √ | ' ' | 留样位置 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsamplingcontainer | 取样容器 | varchar | 50 |  | √ | ' ' | 取样容器 |
| 8 | fsamplenum | 取样份数 | int4 | 32 |  | √ | 0 | 取样份数 |
| 9 | storagecondition | storagecondition | varchar | 50 |  | √ | ' ' |  |
| 10 | fsamplestartdate | 留样开始计算日期 | varchar | 1 |  | √ | 'A' | 留样开始计算日期,枚举: A :生产日期 B :样品生成日期 |
| 11 | fsamplingratio | 取样比例 | int8 | 64 |  | √ | 0 | [抽样方案 qcbd_sampscheme](../qcbd_files/qcbd_sampscheme.md) |
| 12 | fsamplingmethod | 取样方法 | varchar | 50 |  | √ | ' ' | 取样方法 |
| 13 | fobscount | 预计观察次数 | int4 | 32 |  | √ | 0 | 预计观察次数 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fperiodunit | 留存期限单位 | varchar | 50 |  | √ | 'Y' | 留存期限单位,枚举: YEAR :年 MONTH :月 DAY :日 |
| 16 | fstoragecondition | 贮存条件 | varchar | 50 |  | √ | ' ' | 贮存条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_sampro_fid |  | fid |
| 2 | pk_t_bd_samprocedureentry |  | fentryid |
| 3 | idx_bd_sampro_fseq |  | fseq |
| 4 | idx_bd_samproent_fmatlid |  | fmaterialid |

---

## 取样方案-多语言表 t_bd_samplingplan_l

- **表名称：** 取样方案-多语言表
- **表名：** t_bd_samplingplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 150 |  | √ | ' ' | 方案名称 |
| 3 | fcomment | 备注 | varchar | 765 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_samplingplan_l |  | fpkid |
| 2 | idx_bd_sampplan_fid |  | fid,flocaleid |
| 3 | idx_bd_sampplan_fname |  | fname |

---

## 操作规程文件-附件表 t_bd_sampplan_operfile

- **表名称：** 操作规程文件-附件表
- **表名：** t_bd_sampplan_operfile

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
| 1 | pk_t_bd_sampplan_operfile |  | fpkid |
| 2 | idx_bd_sampfile_fentryid |  | fentryid |

---

## 取样方案-使用范围表 t_bd_samplingplan_u

- **表名称：** 取样方案-使用范围表
- **表名：** t_bd_samplingplan_u

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
| 1 | idx_t_bd_samplingplan_u_uo |  | fuseorgid |
| 2 | pk_t_bd_samplingplan_u |  | fdataid,fuseorgid |

---

## 观察项目-多选基础资料表 t_bd_sampplan_obsitems

- **表名称：** 观察项目-多选基础资料表
- **表名：** t_bd_sampplan_obsitems

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [检验项目 qcbd_inspectionitems](../qcbd_files/qcbd_inspectionitems.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_sampitem_fentryid |  | fentryid |
| 2 | pk_t_bd_sampplan_obsitems |  | fpkid |

---

## 取样方案-主表 t_bd_samplingplan

- **表名称：** 取样方案-主表
- **表名：** t_bd_samplingplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | [取样方案分类 bd_samplan_group](../basedata_files/bd_samplan_group.md) |
| 6 | fcomment | 备注 | varchar | 765 |  | √ | ' ' | 备注 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 20 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_samplingplan_master |  | fmasterid |
| 2 | pk_t_bd_samplingplan |  | fid |
| 3 | idx_bd_sampplan_fnumber |  | fnumber,forgid |
| 4 | idx_t_bd_samplingplan_createorg |  | fcreateorgid |
