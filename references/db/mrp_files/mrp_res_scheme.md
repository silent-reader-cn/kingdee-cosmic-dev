# 资源计划方案-mrp_res_scheme

## 资源计划方案-使用范围表 t_mrp_res_scheme_u

- **表名称：** 资源计划方案-使用范围表
- **表名：** t_mrp_res_scheme_u

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
| 1 | idx_t_mrp_res_scheme_u_uo |  | fuseorgid |
| 2 | pk_t_mrp_res_scheme_u |  | fdataid,fuseorgid |

---

## 资源计划方案-使用范围位图表 t_mrp_res_scheme_m

- **表名称：** 资源计划方案-使用范围位图表
- **表名：** t_mrp_res_scheme_m

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
| 1 | pk_t_mrp_res_scheme_m |  | forgid |

---

## 资源计划方案-多语言表 t_mrp_res_scheme_l

- **表名称：** 资源计划方案-多语言表
- **表名：** t_mrp_res_scheme_l

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
| 1 | pk_mrp_res_scheme_l |  | fpkid |
| 2 | idx_mrp_res_scheme_l_id |  | fid,flocaleid |

---

## 资源清单参数单据体-子表 t_mrp_res_schlist

- **表名称：** 资源清单参数单据体-子表
- **表名：** t_mrp_res_schlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flistinrun | 参与运算 | bpchar | 1 |  | √ | '0' | 参与运算 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | flistfieldtran | 实体字段映射 | int8 | 64 |  | √ | 0 | 实体字段映射 mrp_billfieldtransfer |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | flistresource | 数据源配置 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconfig |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_res_schlist_id |  | fid |
| 2 | pk_mrp_res_schlist |  | fentryid |

---

## 需求参数单据体-子表 t_mrp_res_schreq

- **表名称：** 需求参数单据体-子表
- **表名：** t_mrp_res_schreq

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freqinrun | 参与运算 | bpchar | 1 |  | √ | '0' | 参与运算 |
| 3 | freqfieldtran | 实体字段映射 | int8 | 64 |  | √ | 0 | 实体字段映射 mrp_billfieldtransfer |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | freqresource | 数据源配置 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconfig |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_res_schreq_id |  | fid |
| 2 | pk_mrp_res_schreq |  | fentryid |

---

## 资源计划方案-主表 t_mrp_res_scheme

- **表名称：** 资源计划方案-主表
- **表名：** t_mrp_res_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchkgroupplan | 资源计划：拖期期间 | varchar | 5 |  | √ | ' ' | 资源计划：拖期期间,枚举: 1 :所有拖期期间 2 :指定拖期期间 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | flistday | 资源清单拖期期间 | int8 | 64 |  | √ | 0 | 资源清单拖期期间 |
| 5 | fsupplyday | 供应拖期期间 | int8 | 64 |  | √ | 0 | 供应拖期期间 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | freqmodel | 需求模型 | int8 | 64 |  | √ | 0 | 资源注册模型 mrp_resourceregister_cf |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | fisadjust | 考虑调整 | bpchar | 1 |  | √ | '0' | 考虑调整 |
| 15 | fisreplace | 考虑替代 | bpchar | 1 |  | √ | '0' | 考虑替代 |
| 16 | fcreateorgid | 计划组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fplanmodel | 资源计划模型 | int8 | 64 |  | √ | 0 | 资源注册模型 mrp_resourceregister_cf |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fchkgroupreq | 需求：拖期期间 | varchar | 5 |  | √ | ' ' | 需求：拖期期间,枚举: 1 :所有拖期期间 2 :指定拖期期间 |
| 22 | fplanday | 资源计划拖期期间 | int8 | 64 |  | √ | 0 | 资源计划拖期期间 |
| 23 | freqday | 需求拖期期间 | int8 | 64 |  | √ | 0 | 需求拖期期间 |
| 24 | fsupplymodel | 供应模型 | int8 | 64 |  | √ | 0 | 资源注册模型 mrp_resourceregister_cf |
| 25 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | fplanoutlook | 计划展望期 | int8 | 64 |  | √ | 0 | 计划展望期 |
| 27 | flistmodel | 资源清单模型 | int8 | 64 |  | √ | 0 | 资源注册模型 mrp_resourceregister_cf |
| 28 | fchkgrouplist | 资源清单：拖期期间 | varchar | 5 |  | √ | ' ' | 资源清单：拖期期间,枚举: 1 :所有拖期期间 2 :指定拖期期间 |
| 29 | fchkgroupsupply | 供应：拖期期间 | varchar | 5 |  | √ | ' ' | 供应：拖期期间,枚举: 1 :所有拖期期间 2 :指定拖期期间 |
| 30 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fchkgroupplantype | 计划类型按钮组 | varchar | 5 |  | √ | ' ' | 计划类型按钮组,枚举: 1 :资源计划 2 :资源评估 |
| 32 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 33 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mrp_res_scheme_master |  | fmasterid |
| 2 | idx_t_mrp_res_scheme_createorg |  | fcreateorgid |
| 3 | pk_mrp_res_scheme |  | fid |
| 4 | idx_mrp_res_scheme_no |  | fnumber |

---

## 组织参数单据体-子表 t_mrp_res_schorg

- **表名称：** 组织参数单据体-子表
- **表名：** t_mrp_res_schorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrysupplyorg | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_res_schorg_id |  | fid |
| 2 | pk_mrp_res_schorg |  | fentryid |

---

## 供应参数单据体-子表 t_mrp_res_schsupply

- **表名称：** 供应参数单据体-子表
- **表名：** t_mrp_res_schsupply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplyfieldtran | 实体字段映射 | int8 | 64 |  | √ | 0 | 实体字段映射 mrp_billfieldtransfer |
| 3 | fsupplyresource | 数据源配置 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconfig |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsupplyinrun | 参与运算 | bpchar | 1 |  | √ | '0' | 参与运算 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_res_schsupply |  | fentryid |
| 2 | idx_mrp_res_schsupply_id |  | fid |

---

## 资源计划参数单据体-子表 t_mrp_res_schplan

- **表名称：** 资源计划参数单据体-子表
- **表名：** t_mrp_res_schplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanresource | 数据源配置 | int8 | 64 |  | √ | 0 | 数据源配置 msplan_resource_dataconf |
| 3 | fplanfieldtran | 实体字段映射 | int8 | 64 |  | √ | 0 | 实体字段映射 mrp_billfieldtransfer |
| 4 | fplaninrun | 参与运算 | bpchar | 1 |  | √ | '0' | 参与运算 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_res_schplan_id |  | fid |
| 2 | pk_mrp_res_schplan |  | fentryid |
