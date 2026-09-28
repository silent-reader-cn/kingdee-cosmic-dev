# 项目即时成本差异临时表-pca_rt_costdif_tmp

## 项目即时成本差异临时表-主表 t_pca_rt_costdif_tmp

- **表名称：** 项目即时成本差异临时表-主表
- **表名：** t_pca_rt_costdif_tmp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodid | 期间id | int8 | 64 |  | √ | 0 | 期间id |
| 3 | fpcacostbillentryid | 项目成本单据单据体id | int8 | 64 |  | √ | 0 | 项目成本单据单据体id |
| 4 | fcostaccountid | 项目核算主体id | int8 | 64 |  | √ | 0 | 项目核算主体id |
| 5 | fpcacostbillid | 项目成本单据id | int8 | 64 |  | √ | 0 | 项目成本单据id |
| 6 | fbizsrcbillentryid | 业务来源单据体id | int8 | 64 |  | √ | 0 | 业务来源单据体id |
| 7 | fcostobjectid | 成本核算对象id | int8 | 64 |  | √ | 0 | 成本核算对象id |
| 8 | fbizsrcbillid | 业务来源单据id | int8 | 64 |  | √ | 0 | 业务来源单据id |
| 9 | fmodifytime | 计算时间 | timestamp | 0 |  |  | null | 计算时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_rt_costdif_tmp |  | fid |

---

## 子要素核算明细-子表 t_pca_rt_costdif_tmpentry

- **表名称：** 子要素核算明细-子表
- **表名：** t_pca_rt_costdif_tmpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconvsubelementid | 成本子要素id | int8 | 64 |  | √ | 0 | 成本子要素id |
| 3 | fentryrtamount | 既时投入差异 | numeric | 23 | 10 | √ | 0 | 既时投入差异 |
| 4 | fentryexrtamount | 既时投入差异（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 既时投入差异（不计入项目成本） |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryrtoutamount | 即时转出 | numeric | 23 | 10 | √ | 0 | 即时转出 |
| 7 | fentryexrtoutamount | 即时转出（不计入项目成本） | numeric | 23 | 10 | √ | 0 | 即时转出（不计入项目成本） |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_rt_costdif_tmpentry_fk |  | fid |
| 2 | pk_pca_rt_costdif_tmpentry |  | fentryid |
