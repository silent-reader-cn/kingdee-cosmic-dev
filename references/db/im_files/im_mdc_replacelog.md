# 生产领料申请替代记录-im_mdc_replacelog

## 子单据体-子表 t_im_mdc_replogentrycld

- **表名称：** 子单据体-子表
- **表名：** t_im_mdc_replogentrycld

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpriorityc | 替代优先级 | int8 | 64 |  | √ | 0 | 替代优先级 |
| 2 | fqtyc | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 3 | fbaseqtyc | 申请基本数量 | numeric | 23 | 10 | √ | 0 | 申请基本数量 |
| 4 | fismainreplacec | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 5 | fmaterielmasteridc | 替代物料(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbaseunitc | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fmaterialc | 替代物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | funitc | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mdc_replogentryc_fentryid |  | fentryid |
| 2 | pk_im_mdc_replogentrycld |  | fdetailid |

---

## 生产领料申请替代记录-主表 t_im_mdc_replacelog

- **表名称：** 生产领料申请替代记录-主表
- **表名：** t_im_mdc_replacelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | forderno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 10 | fsrcbillentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | freplacegroup | 替代组 | varchar | 50 |  | √ | ' ' | 替代组 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fproject | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_replacelog |  | fid |
| 2 | idx_mdc_replacelog_fsrcbillid |  | fsrcbillid |

---

## 单据体-子表 t_im_mdc_replogentry

- **表名称：** 单据体-子表
- **表名：** t_im_mdc_replogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 4 | fpriority | 替代优先级 | int8 | 64 |  | √ | 0 | 替代优先级 |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 10 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fbaseqty | 申请基本数量 | numeric | 23 | 10 | √ | 0 | 申请基本数量 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mdc_replogentry_fmasterid |  | fmaterielmasterid |
| 2 | idx_mdc_replogentry_fid |  | fid |
| 3 | pk_im_mdc_replogentry |  | fentryid |
