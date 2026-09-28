# 执行方案-qcbd_invimpschem

## 分单规则分录-子表 t_qcbd_invpscmentry

- **表名称：** 分单规则分录-子表
- **表名：** t_qcbd_invpscmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsplitreason | 请检分单依据 | varchar | 50 |  | √ | ' ' | 请检分单依据,枚举: |
| 3 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_invpscmentry |  | fentryid |
| 2 | idx_qcbd_invpry_fid |  | fid |
| 3 | idx_qcbd_invpry_fseq |  | fseq |

---

## 执行方案-主表 t_qcbd_invpscm

- **表名称：** 执行方案-主表
- **表名：** t_qcbd_invpscm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | 执行方案分类 qcbd_invimpschemgrp |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | filterstring | 通用过滤控件文本 | varchar | 255 |  | √ | ' ' | 通用过滤控件文本 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | filterstring_tag | 通用过滤控件文本_详情 | text | 0 |  |  | null | 通用过滤控件文本_详情 |
| 13 | fxkallocationtype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: 1 :个性化 2 :共享型 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | finspectfreezeinv | 启用库存冻结 | bpchar | 1 |  | √ | '0' | 启用库存冻结 |
| 16 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fapplyorgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | finspectleadtime | 检验提前期（天） | int4 | 32 |  | √ | 0 | 检验提前期（天） |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fsetdate | 指定日期 | timestamp | 0 |  |  | null | 指定日期 |
| 22 | ffirstinspectdate | 首次检验日期 | varchar | 5 |  | √ | ' ' | 首次检验日期,枚举: A :生产日期 B :到期日期 C :指定日期 |
| 23 | finspectcyscle | 检验周期 | varchar | 5 |  | √ | ' ' | 检验周期,枚举: A :月 B :天 |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fautoexec | 自动执行 | bpchar | 1 |  | √ | '0' | 自动执行 |
| 26 | flongmon | 月 | int4 | 32 |  | √ | 0 | 月 |
| 27 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 28 | fquaorgid | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fdatasource | 数据源 | varchar | 5 |  | √ | ' ' | 数据源,枚举: A :即时库存 B :物料主数据 |
| 31 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 32 | flongday | 天 | int4 | 32 |  | √ | 0 | 天 |
| 33 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | finspectnumstyle | 检验数量取值 | varchar | 5 |  | √ | ' ' | 检验数量取值,枚举: A :数量 B :可用量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_qcbd_invpscm_createorg |  | fcreateorgid |
| 2 | idx_qcbd_invpcm_fcreatetime |  | fcreatetime |
| 3 | pk_qcbd_invpscm |  | fid |
| 4 | uidx_qcbd_invpscm_billno |  | fnumber |
| 5 | idx_t_qcbd_invpscm_master |  | fmasterid |

---

## 执行方案-多语言表 t_qcbd_invpscm_l

- **表名称：** 执行方案-多语言表
- **表名：** t_qcbd_invpscm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_invpcml_fid |  | fid,flocaleid |
| 2 | idx_qcbd_invpcml_fname |  | fname |
| 3 | pk_qcbd_invpscm_l |  | fpkid |

---

## 执行方案-使用范围位图表 t_qcbd_invpscm_m

- **表名称：** 执行方案-使用范围位图表
- **表名：** t_qcbd_invpscm_m

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
| 1 | pk_t_qcbd_invpscm_m |  | forgid |

---

## 执行方案-使用范围表 t_qcbd_invpscm_u

- **表名称：** 执行方案-使用范围表
- **表名：** t_qcbd_invpscm_u

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
| 1 | pk_t_qcbd_invpscm_u |  | fdataid,fuseorgid |
| 2 | idx_t_qcbd_invpscm_u_uo |  | fuseorgid |

---

## 物料-多选基础资料表 t_qcbd_inscmmater

- **表名称：** 物料-多选基础资料表
- **表名：** t_qcbd_inscmmater

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_inscer_fid |  | fid,fbasedataid |
| 2 | pk_qcbd_inscmmater |  | fpkid |

---

## 执行日志分录-子表 t_qcbd_invpscmlog

- **表名称：** 执行日志分录-子表
- **表名：** t_qcbd_invpscmlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fexecres | 执行结果 | varchar | 5 |  | √ | ' ' | 执行结果,枚举: A :成功 B :失败 |
| 4 | fexecstep | 执行步骤 | varchar | 5 |  | √ | ' ' | 执行步骤,枚举: A :数据获取 B :生成执行明细 C :生成库存请检单 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fexectime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 7 | fexeclog | 执行日志 | varchar | 255 |  | √ | ' ' | 执行日志 |
| 8 | fexeclog_tag | 执行日志_详情 | text | 0 |  |  | null | 执行日志_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_invpscmlog |  | fentryid |
| 2 | idx_qcbd_invpog_fid |  | fid |
| 3 | idx_qcbd_invpog_fseq |  | fseq |

---

## 物料分类-多选基础资料表 t_qcbd_inscmmatgrp

- **表名称：** 物料分类-多选基础资料表
- **表名：** t_qcbd_inscmmatgrp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_inscmmatgrp |  | fpkid |
| 2 | idx_qcbd_inscrp_fid |  | fid,fbasedataid |
