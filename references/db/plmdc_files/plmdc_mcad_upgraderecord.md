# CAD模型升级记录-plmdc_mcad_upgraderecord

## 匹配分类-子表 t_plmdc_mcadup_entry

- **表名称：** 匹配分类-子表
- **表名：** t_plmdc_mcadup_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatchclassify | 匹配分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 3 | ftype | 匹配类型 | varchar | 5 |  | √ | ' ' | 匹配类型 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | foriginalclassifyid | 原分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_cad_up_entry |  | foriginalclassifyid |
| 2 | pk_t_plmdc_mcadup_entry |  | fentryid |

---

## CAD模型升级记录-主表 t_plmdc_mcadupgraderecord

- **表名称：** CAD模型升级记录-主表
- **表名：** t_plmdc_mcadupgraderecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmatchmodeltypeid | 匹配模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 3 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | foriginalmodeltypeid | 原模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 6 | fmatchttype | 匹配类型 | varchar | 50 |  | √ | ' ' | 匹配类型,枚举: A :MCAD B :ECAD |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_cad_uprecord |  | foriginalmodeltypeid |
| 2 | pk_t_plmdc_mcadupgraderecord |  | fid |
