# 供应商IP-pds_conformsupip

## 供应商IP-主表 t_pds_conformsupip

- **表名称：** 供应商IP-主表
- **表名：** t_pds_conformsupip

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 3 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 4 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_conformsupip |  | fid |
| 2 | idx_pds_conformsupip_pid |  | fparentid |

---

## 供应商IP分录-子表 t_pds_conformsupipentry

- **表名称：** 供应商IP分录-子表
- **表名：** t_pds_conformsupipentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 寻源项目ID | varchar | 50 |  | √ | ' ' | 寻源项目ID |
| 3 | fparentid | 父单据ID | int8 | 64 |  | √ | 0 | 父单据ID |
| 4 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbilldate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | fsysresultid | 检查结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 8 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | [检查项 pbd_check_item](../pbd_files/pbd_check_item.md) |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 10 | ftype | 操作类型 | bpchar | 1 |  | √ | ' ' | 操作类型,枚举: 1 :报名IP 2 :投标IP 3 :报价IP |
| 11 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 12 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_conformsupipentry_pid |  | fparentid |
| 2 | idx_pds_conformsupipentry_pro |  | fprojectid |
| 3 | pk_pds_conformsupipentry |  | fentryid |
| 4 | idx_pds_conformsupipentry_fid |  | fid |
