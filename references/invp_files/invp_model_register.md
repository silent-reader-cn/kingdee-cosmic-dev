# 资源注册模型-invp_model_register

## 数据源配置分录-子表 t_invp_sourceentry

- **表名称：** 数据源配置分录-子表
- **表名：** t_invp_sourceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilterdescds | 取数条件 | varchar | 2000 |  | √ | ' ' | 取数条件 |
| 3 | ffiltervalueds | 取数条件值 | varchar | 2000 |  | √ | ' ' | 取数条件值 |
| 4 | fbillfieldmapid | 实体字段映射编码 | int8 | 64 |  | √ | 0 | 通用映射配置 sbs_billfieldmapping |
| 5 | fsrcbilld | 源实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_sourceentry_fid |  | fid |
| 2 | pk_t_invp_sourceentry |  | fentryid |

---

## 资源注册模型-多语言表 t_invp_model_register_l

- **表名称：** 资源注册模型-多语言表
- **表名：** t_invp_model_register_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_modelrl_flocal |  | fid,flocaleid |
| 2 | pk_invp_model_register_l |  | fpkid |

---

## 资源注册模型-使用范围表 t_invp_model_register_u

- **表名称：** 资源注册模型-使用范围表
- **表名：** t_invp_model_register_u

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
| 1 | pk_t_invp_model_register_u |  | fdataid,fuseorgid |
| 2 | idx_t_invp_model_register_u_uo |  | fuseorgid |

---

## 目标实体详情分录-子表 t_invp_targetentry

- **表名称：** 目标实体详情分录-子表
- **表名：** t_invp_targetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsignname | fsignname | varchar | 80 |  | √ | ' ' |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fsignid | 字段标识 | varchar | 80 |  | √ | ' ' | 字段标识 |
| 6 | fdatatype | fdatatype | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_targetentry_fid |  | fid |
| 2 | pk_t_invp_targetentry |  | fentryid |

---

## 资源注册模型-主表 t_invp_model_register

- **表名称：** 资源注册模型-主表
- **表名：** t_invp_model_register

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型,枚举: 1 :供应 2 :需求 3 :水位因子 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | foutputresult | 输出结果映射 | int8 | 64 |  | √ | 0 | 通用映射配置 sbs_billfieldmapping |
| 6 | fapptype | 所属应用 | varchar | 50 |  | √ | ' ' | 业务应用列表 bos_devp_bizapplist |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbusinessentityid | 目标实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 12 | foutputmappingsupply | 输出转供应映射 | int8 | 64 |  | √ | 0 | 通用映射配置 sbs_billfieldmapping |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fapprovedate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 25 | foutputtypeid | 输出结果类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 28 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_model_register |  | fid |
| 2 | idx_t_invp_model_register_createorg |  | fcreateorgid |
| 3 | idx_t_invp_model_register_master |  | fmasterid |
| 4 | idx_invp_modelr_fnum |  | fnumber |
