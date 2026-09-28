# 质量追溯范围-pqt_retracemodel

## 质量追溯范围-多语言表 t_pqt_retracemodel_l

- **表名称：** 质量追溯范围-多语言表
- **表名：** t_pqt_retracemodel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pqt_retracemodel_fid |  | fid,flocaleid |
| 2 | pk_t_pqt_retracemodel_l |  | fpkid |

---

## 追溯清单分录-子表 t_pqt_retentry

- **表名称：** 追溯清单分录-子表
- **表名：** t_pqt_retentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmtono | 跟踪号 | varchar | 50 |  | √ | ' ' | 跟踪号 |
| 3 | flocation | 仓位 | varchar | 50 |  | √ | ' ' | 仓位 |
| 4 | fworkshop | 生产部门 | varchar | 50 |  | √ | ' ' | 生产部门 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frownum | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 7 | fsupplier | 供应商 | varchar | 50 |  | √ | ' ' | 供应商 |
| 8 | fexpiredate | 有效期至 | varchar | 50 |  | √ | ' ' | 有效期至 |
| 9 | fretracebill | 追溯单据 | int8 | 64 |  | √ | 0 | 追溯业务对象设置 pqt_entityobject |
| 10 | fdate | 日期 | varchar | 50 |  | √ | ' ' | 日期 |
| 11 | fprocessnumber | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 12 | fmftdate | 生产日期 | varchar | 50 |  | √ | ' ' | 生产日期 |
| 13 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 14 | forganization | 组织 | varchar | 50 |  | √ | ' ' | 组织 |
| 15 | fqty | 数量 | varchar | 50 |  | √ | ' ' | 数量 |
| 16 | fcustomer | 客户 | varchar | 50 |  | √ | ' ' | 客户 |
| 17 | fbillentry | 单据分录内码标识 | varchar | 50 |  | √ | ' ' | 单据分录内码标识 |
| 18 | fmversion | 物料版本 | varchar | 50 |  | √ | ' ' | 物料版本 |
| 19 | fwarehouse | 仓库 | varchar | 50 |  | √ | ' ' | 仓库 |
| 20 | fprocessname | 工序名称 | varchar | 50 |  | √ | ' ' | 工序名称 |
| 21 | fbomcode | BOM编码 | varchar | 50 |  | √ | ' ' | BOM编码 |
| 22 | fprocessdesc | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fauxpty | 辅助属性 | varchar | 50 |  | √ | ' ' | 辅助属性 |
| 25 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 26 | finvstatus | 库存状态 | varchar | 50 |  | √ | ' ' | 库存状态 |
| 27 | fisshow | 是否显示 | bpchar | 1 |  | √ | '0' | 是否显示 |
| 28 | fprocessseq | 工序序列 | varchar | 50 |  | √ | ' ' | 工序序列 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pqt_retentry |  | fentryid |
| 2 | idx_pqt_retentry_fseq |  | fseq |
| 3 | idx_pqt_retentry_fid |  | fid |

---

## 质量追溯范围-主表 t_pqt_retracemodel

- **表名称：** 质量追溯范围-主表
- **表名：** t_pqt_retracemodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fsystempreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 21 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pqt_retracemodel_fnumber |  | fnumber |
| 2 | pk_t_pqt_retracemodel |  | fid |
| 3 | idx_t_pqt_retracemodel_createorg |  | fcreateorgid |
| 4 | idx_t_pqt_retracemodel_master |  | fmasterid |

---

## 匹配分录-子表 t_pqt_mateentry

- **表名称：** 匹配分录-子表
- **表名：** t_pqt_mateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftargetentry | 目标单分录内码标识 | varchar | 50 |  | √ | ' ' | 目标单分录内码标识 |
| 2 | fmatchmode | 匹配方式 | varchar | 20 |  | √ | ' ' | 匹配方式,枚举: MATCH_DIRECT :直接匹配 MATCH_TARGET :通过目标单匹配 MATCH_TARGET_SOURCE :通过目标单&源单匹配 MATCH_SOURCE :通过源单匹配 MATCH_CUSTOM :自定义匹配 MATCH_LINK_FIELD :通过关联字段匹配 MATCH_OP_REPORT :通过工序汇报匹配 |
| 3 | flinkfield | 关联字段标识 | varchar | 50 |  | √ | ' ' | 关联字段标识 |
| 4 | fserial | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 5 | ftargetbill | 目标单据 | int8 | 64 |  | √ | 0 | 追溯业务对象设置 pqt_entityobject |
| 6 | fmaterialnum | 物料编码 | varchar | 50 |  | √ | ' ' | 物料编码 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | flot | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fsourcebill | 来源单据 | int8 | 64 |  | √ | 0 | 追溯业务对象设置 pqt_entityobject |
| 12 | fsourceentry | 源单分录内码标识 | varchar | 50 |  | √ | ' ' | 源单分录内码标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pqt_mateentry_fentryid |  | fentryid |
| 2 | pk_t_pqt_mateentry |  | fdetailid |
| 3 | idx_pqt_mateentry_fseq |  | fseq |

---

## 质量追溯范围-使用范围表 t_pqt_retracemodel_u

- **表名称：** 质量追溯范围-使用范围表
- **表名：** t_pqt_retracemodel_u

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
| 1 | pk_t_pqt_retracemodel_u |  | fdataid,fuseorgid |
| 2 | idx_t_pqt_retracemodel_u_uo |  | fuseorgid |
