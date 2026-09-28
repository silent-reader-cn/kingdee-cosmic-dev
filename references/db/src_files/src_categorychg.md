# 品类变更-src_categorychg

## 品类变更-主表 t_src_categorychg

- **表名称：** 品类变更-主表
- **表名：** t_src_categorychg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | 寻源项目变更F7 src_bidchangef7 |
| 3 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 4 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 7 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 9 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_categorychg |  | fid |
| 2 | idx_src_categorychg_pid |  | fparentid |

---

## 标的分录-子表 t_src_categorychgentry

- **表名称：** 标的分录-子表
- **表名：** t_src_categorychgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialnane | 物料名称 | varchar | 100 |  | √ | ' ' | 物料名称 |
| 3 | fcategoryid1 | 变更后品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcategoryid | 原品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 7 | fpackagename | 标段 | varchar | 50 |  | √ | ' ' | 标段 |
| 8 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: 1 :采购清单 2 :供应商报价单 3 :线上议价单 4 :线下议价单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_categorychgentry_fid |  | fid |
| 2 | pk_src_categorychgentry |  | fentryid |
