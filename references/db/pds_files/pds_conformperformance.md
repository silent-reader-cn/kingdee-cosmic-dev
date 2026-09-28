# 供应商绩效-pds_conformperformance

## 供应商绩效-主表 t_pds_conformperform

- **表名称：** 供应商绩效-主表
- **表名：** t_pds_conformperform

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
| 1 | pk_pds_conformperform |  | fid |
| 2 | idx_pds_conformperform_pid |  | fparentid |

---

## 供应商绩效分录-子表 t_pds_conformperfentry

- **表名称：** 供应商绩效分录-子表
- **表名：** t_pds_conformperfentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 寻源项目ID | int8 | 64 |  | √ | 0 | 寻源项目ID |
| 3 | fparentid | 父单据ID | int8 | 64 |  | √ | 0 | 父单据ID |
| 4 | fsubject | 改善主题 | varchar | 255 |  | √ | ' ' | 改善主题 |
| 5 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 6 | fconfirmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待处理 B :打回 C :改善中 D :改善提交 E :改善通过 F :改善驳回 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fsysresultid | 检查结果 | int8 | 64 |  | √ | 0 | [评估等级 bd_evagrade](../basedata_files/bd_evagrade.md) |
| 10 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | [检查项 pbd_check_item](../pbd_files/pbd_check_item.md) |
| 11 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 12 | fimprovetypeid | 改善类型 | int8 | 64 |  | √ | 0 | [供应商辅助资料 srm_extdata](../pbd_files/srm_extdata.md) |
| 13 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fbillno | 改善单号 | varchar | 80 |  | √ | ' ' | 改善单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_conformperfentry_pro |  | fprojectid |
| 2 | idx_pds_conformperfentry_pid |  | fparentid |
| 3 | idx_pds_conformperfentry_fid |  | fid |
| 4 | pk_pds_conformperfentry |  | fentryid |
