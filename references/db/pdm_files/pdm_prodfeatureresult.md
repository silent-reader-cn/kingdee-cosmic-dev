# 产品配置清单-pdm_prodfeatureresult

## 产品配置清单-主表 t_pdm_prodfeatureresult

- **表名称：** 产品配置清单-主表
- **表名：** t_pdm_prodfeatureresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsoentryseq | 销售订单行号 | int4 | 32 |  | √ | 0 | 销售订单行号 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbomid | 源BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmaterialid | 配置产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | foldmaterialid | 源物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fsobillno | 销售订单编号 | varchar | 80 |  | √ | ' ' | 销售订单编号 |
| 10 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_prodfeaturerst_mid |  | fmaterialid |
| 2 | pk_t_pdm_prodfeatureresult |  | fid |

---

## 单据体-子表 t_pdm_prodfeaturerstentry

- **表名称：** 单据体-子表
- **表名：** t_pdm_prodfeaturerstentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | ffeatureid | 特征编码 | int8 | 64 |  | √ | 0 | [特征 bd_feature](../basedata_files/bd_feature.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | ffeaturevalid | 特征值 | int8 | 64 |  | √ | 0 | [特征值 bd_featurevalue](../basedata_files/bd_featurevalue.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_prodfeaturerstentry |  | fentryid |
| 2 | idx_pdm_prodfeaturerste_fid |  | fid |
