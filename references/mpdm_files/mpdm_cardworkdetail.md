# 工卡工作清单-mpdm_cardworkdetail

## 工序信息-子表 t_mpdm_cworkdetailentry

- **表名称：** 工序信息-子表
- **表名：** t_mpdm_cworkdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductionworkshopid | 生产车间 | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 3 | ffirstcheck | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 4 | fworkhours | 工时 | numeric | 23 | 10 | √ | 0 | 工时 |
| 5 | fprocessno | 工序号 | varchar | 100 |  | √ | ' ' | 工序号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | foperationqty | 工序数量 | numeric | 23 | 10 | √ | 0 | 工序数量 |
| 8 | fmachiningtype | 加工类型 | varchar | 50 |  | √ | ' ' | 加工类型,枚举: 1001 :厂内加工 1002 :委外加工 1003 :内协加工 1004 :不限制 |
| 9 | fchecktype | 检验方式 | varchar | 50 |  | √ | ' ' | 检验方式,枚举: 1011 :免检 1012 :车间检验 1013 :质量检验 |
| 10 | ffloorratio | 汇报下限允差(%) | numeric | 23 | 10 | √ | 0 | 汇报下限允差(%) |
| 11 | fbasebatchqty | 基本批量 | numeric | 23 | 10 | √ | 0 | 基本批量 |
| 12 | foperationid | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 13 | fprocessgroup | 工序组 | int8 | 64 |  | √ | 0 | 工序组(废弃) mpdm_progroup |
| 14 | foperationunitid | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 16 | fworkstation | 工位 | int8 | 64 |  | √ | 0 | 工位 mpdm_workstation |
| 17 | fheadqty | 表头数量 | numeric | 23 | 10 | √ | 0 | 表头数量 |
| 18 | foprctrlstrategy | 工序控制策略 | int8 | 64 |  | √ | 0 | 工序控制策略(废弃) mpdm_proctrlstrategy |
| 19 | foperationdesc | 工序说明 | varchar | 255 |  | √ | ' ' | 工序说明 |
| 20 | fbottleprocedure | 瓶颈工序 | bpchar | 1 |  | √ | '0' | 瓶颈工序 |
| 21 | fprofessiona | 专业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 22 | fproductionorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fupperratio | 汇报上限允差(%) | numeric | 23 | 10 | √ | 0 | 汇报上限允差(%) |
| 24 | fheadunitid | 表头单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fismilestoneprocess | 里程碑工序 | bpchar | 1 |  | √ | '0' | 里程碑工序 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fcollaborative | 协作工序 | bpchar | 1 |  | √ | '0' | 协作工序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_cworkdetailentry |  | fentryid |
| 2 | idx_mpdm_cworkdentry_fid |  | fid,fentryid |
| 3 | idx_mpdm_cworkdentry_fprono |  | fprocessno |

---

## 工卡工作清单-使用范围位图表 t_mpdm_cworkdetail_m

- **表名称：** 工卡工作清单-使用范围位图表
- **表名：** t_mpdm_cworkdetail_m

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
| 1 | pk_t_mpdm_cworkdetail_m |  | forgid |

---

## 工卡工作清单-多语言表 t_mpdm_cworkdetail_l

- **表名称：** 工卡工作清单-多语言表
- **表名：** t_mpdm_cworkdetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cworkdetail_l_fid |  | fid,flocaleid |
| 2 | pk_t_mpdm_cworkdetail_l |  | fpkid |

---

## 工卡工作清单-使用范围表 t_mpdm_cworkdetail_u

- **表名称：** 工卡工作清单-使用范围表
- **表名：** t_mpdm_cworkdetail_u

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
| 1 | pk_t_mpdm_cworkdetail_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_cworkdetail_u_uo |  | fuseorgid |

---

## 工卡工作清单-主表 t_mpdm_cworkdetail

- **表名称：** 工卡工作清单-主表
- **表名：** t_mpdm_cworkdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcardnoid | 工卡编码 | int8 | 64 |  | √ | 0 | 工卡维护 mpdm_workcards |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmajordesc | 重要工作描述 | varchar | 255 |  | √ | ' ' | 重要工作描述 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcancelerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmajorflag | 重要工作标记 | bpchar | 1 |  | √ | '0' | 重要工作标记 |
| 11 | fproductenvironment | 生产环境 | varchar | 255 |  | √ | ' ' | 生产环境 |
| 12 | fcanceltime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fsumhours | 工时（汇总） | numeric | 23 | 10 | √ | 0 | 工时（汇总） |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fworkunit | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 26 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | ffirstexe | 首次执行（待定） | bpchar | 1 |  | √ | '0' | 首次执行（待定） |
| 28 | fmaterialunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 31 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_cworkdetail_master |  | fmasterid |
| 2 | idx_t_mpdm_cworkdetail_createorg |  | fcreateorgid |
| 3 | pk_t_mpdm_cworkdetail |  | fid |
| 4 | idx_mpdm_cworkd_fcardnoid |  | fcardnoid |
