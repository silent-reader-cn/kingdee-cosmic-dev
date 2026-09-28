# 供应商资质-pds_conformaptitude

## 供应商资质-主表 t_pds_conformaptitude

- **表名称：** 供应商资质-主表
- **表名：** t_pds_conformaptitude

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
| 1 | pk_pds_conformaptitude |  | fid |
| 2 | idx_pds_conformaptitude_pid |  | fparentid |

---

## 供应商资质分录-子表 t_pds_conformaptentry

- **表名称：** 供应商资质分录-子表
- **表名：** t_pds_conformaptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 资质名称 | varchar | 255 |  | √ | ' ' | 资质名称 |
| 3 | fdateto | 有效日期至 | timestamp | 0 |  |  | null | 有效日期至 |
| 4 | fprojectid | 寻源项目ID | int8 | 64 |  | √ | 0 | 寻源项目ID |
| 5 | fparentid | 父单据ID | int8 | 64 |  | √ | 0 | 父单据ID |
| 6 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fsysresultid | 检查结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 9 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | [检查项 pbd_check_item](../pbd_files/pbd_check_item.md) |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 12 | faptitudetypeid | 资质类型 | int8 | 64 |  | √ | 0 | [资质类型维护 bd_qualification_type](../basedata_files/bd_qualification_type.md) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_conformaptitudeentry |  | fentryid |
| 2 | idx_pds_conformaptentry_fid |  | fid |
| 3 | idx_pds_conformaptentry_pro |  | fprojectid |
| 4 | idx_pds_conformaptentry_pid |  | fparentid |
