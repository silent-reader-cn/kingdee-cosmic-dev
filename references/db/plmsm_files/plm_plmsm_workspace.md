# 个人工作区-plm_plmsm_workspace

## 个人工作区-分表 t_plm_pdm_basic_mb

- **表名称：** 个人工作区-分表
- **表名：** t_plm_pdm_basic_mb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flcstageid | 生命周期阶段 | int8 | 64 |  | √ | 0 | 生命周期阶段 plm_lc_stage |
| 3 | flcstatusid | 生命周期状态 | int8 | 64 |  | √ | 0 | 生命周期状态 plm_lc_status |
| 4 | flatestversion | flatestversion | varchar | 10 |  | √ | ' ' |  |
| 5 | fsyncid_result | ID同步结果 | varchar | 255 |  | √ | ' ' | ID同步结果 |
| 6 | fbomversion | fbomversion | varchar | 50 |  | √ | ' ' |  |
| 7 | fcheckoutstatus | 检出状态 | varchar | 50 |  | √ | ' ' | 检出状态,枚举: N :未检出 Y :已检出 |
| 8 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 9 | fattachmenturl | 附件地址 | varchar | 500 |  | √ | ' ' | 附件地址 |
| 10 | fhead | fhead | int8 | 64 |  | √ | 0 |  |
| 11 | fsyncid | fsyncid | int8 | 64 |  | √ | 0 |  |
| 12 | fclassattrid | fclassattrid | int8 | 64 |  | √ | 0 |  |
| 13 | fchangetype | fchangetype | bpchar | 1 |  | √ | 'A' |  |
| 14 | fdescriptionld | fdescriptionld | varchar | 255 |  | √ | ' ' |  |
| 15 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 16 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'A' | 变更状态,枚举: A : B :变更中 |
| 17 | fparentfolderid | 所属文件夹 | int8 | 64 |  | √ | 0 | 系统文件夹 plm_pdm_folder_hub |
| 18 | fpicflowstatus | 数据状态图标 | varchar | 255 |  | √ | ' ' | 数据状态图标 |
| 19 | fcheckouttorid | 检出人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | flatestversiondetails | flatestversiondetails | varchar | 50 |  | √ | ' ' |  |
| 21 | fsynctime | fsynctime | timestamp | 0 |  |  | null |  |
| 22 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 23 | fclassifyid | fclassifyid | int8 | 64 |  | √ | 0 |  |
| 24 | fownerld | 所有者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fisvirtualdoc | 是否虚文档 | bpchar | 1 |  | √ | '0' | 是否虚文档 |
| 26 | fchangemode | fchangemode | bpchar | 1 |  | √ | 'A' |  |
| 27 | fenablestatus | fenablestatus | bpchar | 1 |  | √ | 'A' |  |
| 28 | fapplyorgid | fapplyorgid | int8 | 64 |  | √ | 0 |  |
| 29 | fchangereason | fchangereason | bpchar | 1 |  | √ | 'A' |  |
| 30 | fviewid | fviewid | int8 | 64 |  | √ | 0 |  |
| 31 | fbaseunits | fbaseunits | int8 | 64 |  | √ | 0 |  |
| 32 | fsubnewbomversion | fsubnewbomversion | int8 | 64 |  | √ | 0 |  |
| 33 | fexecapplystatus | fexecapplystatus | bpchar | 1 |  | √ | 'A' |  |
| 34 | fmfgbomid | fmfgbomid | int8 | 64 |  | √ | 0 |  |
| 35 | fflowstatus | 流程状态 | varchar | 50 |  | √ | ' ' | 流程状态,枚举: A :未开始 B :流程中 C :流程结束 |
| 36 | flatestbranch | flatestbranch | int8 | 64 |  | √ | 0 |  |
| 37 | fcheckoutattrstatus | fcheckoutattrstatus | bpchar | 1 |  | √ | 'N' |  |
| 38 | fmaterial_attr | fmaterial_attr | varchar | 50 |  | √ | ' ' |  |
| 39 | finvetory_type | finvetory_type | int8 | 64 |  | √ | 0 |  |
| 40 | ferpmaterialid | ferpmaterialid | int8 | 64 |  | √ | 0 |  |
| 41 | flistcontrol | 列表控制 | int8 | 64 |  | √ | 0 | 列表控制 |
| 42 | fpicinstance | 对象图标 | varchar | 255 |  | √ | ' ' | 对象图标 |
| 43 | fchangesource | fchangesource | bpchar | 1 |  | √ | 'A' |  |
| 44 | fisfirstversion | fisfirstversion | int4 | 32 |  | √ | 0 |  |
| 45 | fistemplate | 是否模板 | bpchar | 1 |  | √ | '0' | 是否模板 |
| 46 | fmainid | fmainid | int8 | 64 |  | √ | 0 |  |
| 47 | fheadrevision | fheadrevision | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pdm_basic_mb_cls |  | fclassifyid |
| 2 | pk_plm_pdm_basic_mb |  | fid |
| 3 | idx_plm_pdm_basic_b_des |  | fdescriptionld |

---

## 个人工作区-主表 t_plm_pdm_basic

- **表名称：** 个人工作区-主表
- **表名：** t_plm_pdm_basic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodelid | 业务模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 4 | frdmversion | 系统版本 | varchar | 10 |  | √ | ' ' | 系统版本 |
| 5 | fseq | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdatastagebit | 数据阶段位 | int8 | 64 |  | √ | 1 | 数据阶段位 |
| 8 | fhasmaterial | fhasmaterial | bpchar | 1 |  | √ | '-' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fspecification | fspecification | varchar | 50 |  | √ | ' ' |  |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbizorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdisplayname | 显示名称 | varchar | 1024 |  | √ | ' ' | 显示名称 |
| 22 | fsummary_tag | 显示名称_作废_详情 | text | 0 |  |  | null | 显示名称_作废_详情 |
| 23 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 24 | fctrlstrategy | 研发信息控制策略 | varchar | 50 |  | √ | ' ' | 研发信息控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 27 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 28 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |
| 29 | fsummary | 显示名称_作废 | varchar | 255 |  | √ | ' ' | 显示名称_作废 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_pdm_basic_createorg |  | fcreateorgid |
| 2 | pk_plm_pdm_basic |  | fid |
| 3 | idx_t_plm_pdm_basic_master |  | fmasterid |
| 4 | idx_plm_pdm_basic_name |  | fname |
| 5 | idx_plm_pdm_basic_modelid |  | fmodelid |
| 6 | idx_plm_pdm_basic_number |  | fnumber |

---

## 个人工作区-使用范围表 t_plm_pdm_basic_u

- **表名称：** 个人工作区-使用范围表
- **表名：** t_plm_pdm_basic_u

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
| 1 | idx_t_plm_pdm_basic_u_uo |  | fuseorgid |
| 2 | pk_t_plm_pdm_basic_u |  | fdataid,fuseorgid |

---

## 个人工作区-多语言表 t_plm_pdm_basic_l

- **表名称：** 个人工作区-多语言表
- **表名：** t_plm_pdm_basic_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fspecification | fspecification | varchar | 50 |  | √ | ' ' |  |
| 4 | fdisplayname | 显示名称 | varchar | 2000 |  | √ | ' ' | 显示名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 8 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pdm_basic_l |  | fpkid |
| 2 | idx_plm_pdm_basic_l_0 |  | fid,flocaleid |
