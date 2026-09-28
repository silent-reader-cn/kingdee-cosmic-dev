# 完整性检查方案-plm_plmmm_integrity_pro

## 完整性检查方案-多语言表 t_plmmm_integrity_project_l

- **表名称：** 完整性检查方案-多语言表
- **表名：** t_plmmm_integrity_project_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmmm_integrity_project_l |  | fpkid |
| 2 | idx_plmmm_integrity_project_l |  | fid,flocaleid |

---

## 流程状态-多选基础资料表 t_plmmm_integrity_life

- **表名称：** 流程状态-多选基础资料表
- **表名：** t_plmmm_integrity_life

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [流程状态 plm_lc_status](../plmsm_files/plm_lc_status.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmmm_integrity_life |  | fid |
| 2 | pk_t_plmmm_integrity_life |  | fpkid |

---

## 完整性检查方案-主表 t_plmmm_integrity_project

- **表名称：** 完整性检查方案-主表
- **表名：** t_plmmm_integrity_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fchecktype | 检查方式 | varchar | 30 |  | √ | ' ' | 检查方式,枚举: total :全部通过 onlyone :至少一个通过 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fproprule_tag | 物料属性规则_详情 | text | 0 |  |  | null | 物料属性规则_详情 |
| 12 | fenable | 启用状态 | varchar | 50 |  | √ | ' ' | 启用状态,枚举: 0 :禁用 1 :启用 |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | fproprule | 物料属性规则 | varchar | 255 |  | √ | ' ' | 物料属性规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmmm_integrity_project |  | fnumber |
| 2 | pk_t_plmmm_integrity_project |  | fid |

---

## 流程启动时校验模板-多选基础资料表 t_plmmm_integrity_flow

- **表名称：** 流程启动时校验模板-多选基础资料表
- **表名：** t_plmmm_integrity_flow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [流程设计 wf_model](../wf_files/wf_model.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmmm_integrity_flow |  | fid |
| 2 | pk_t_plmmm_integrity_flow |  | fpkid |

---

## 分类-多选基础资料表 t_plmmm_integrity_classif

- **表名称：** 分类-多选基础资料表
- **表名：** t_plmmm_integrity_classif

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmmm_integrity_classif |  | fpkid |
| 2 | idx_plmmm_integrity_classif |  | fid |

---

## 单据体-子表 t_plmmm_integrity_entry

- **表名称：** 单据体-子表
- **表名：** t_plmmm_integrity_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilterdetail | 过滤条件详情 | varchar | 255 |  | √ | ' ' | 过滤条件详情 |
| 3 | fbizobjectid | 业务模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 4 | fobjectrule | 字段规则 | varchar | 2000 |  | √ | ' ' | 字段规则 |
| 5 | ffilterdetail_tag | 过滤条件详情_详情 | text | 0 |  |  | null | 过滤条件详情_详情 |
| 6 | flanguage | 规则描述语言 | varchar | 20 |  | √ | ' ' | 规则描述语言 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmmm_integrity_entry |  | fentryid |
| 2 | idx_plmmm_integrity_entry |  | fid |
