# 采购员-物料可采控制-msbd_puropermaterctrl

## 采购员-物料可采控制-多语言表 t_msbd_puropermaterctrl_l

- **表名称：** 采购员-物料可采控制-多语言表
- **表名：** t_msbd_puropermaterctrl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msbd_puropmatctrl_l_fid |  | fid |
| 2 | pk_msbd_puropermaterctrl_l |  | fpkid |

---

## 单据体-子表 t_msbd_puropmatctrlentry

- **表名称：** 单据体-子表
- **表名：** t_msbd_puropmatctrlentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeptid | 采购部门编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | foperatorid | 采购员编码 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | foperatorgroupid | 采购组编码 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 6 | fmaterialgroupid | 物料分类编码 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_puropmatcone_fdeptid |  | fdeptid,fid |
| 2 | idx_msbd_puropmatcone_foperid |  | foperatorid,fid |
| 3 | idx_msbd_puropmatcone_fopgrpid |  | foperatorgroupid,fid |
| 4 | pk_msbd_puropmatctrlentry |  | fentryid |
| 5 | idx_msbd_puropmatctrlentry_fid |  | fid |
| 6 | idx_msbd_puropmatcone_fmatid |  | fmaterialid,fid |

---

## 采购员-物料可采控制-主表 t_msbd_puropermaterctrl

- **表名称：** 采购员-物料可采控制-主表
- **表名：** t_msbd_puropermaterctrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcontroltype | 控制类型 | varchar | 10 |  | √ | ' ' | 控制类型,枚举: ALLOW :允采 LIMIT :限采 |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 8 | fcontroldimension | 控制维度 | varchar | 20 |  | √ | ' ' | 控制维度,枚举: OPER_MATER :采购员-物料 OPER_MATERGRP :采购员-物料分类 OPERGRP_MATER :采购组-物料 OPERGRP_MATERGRP :采购组-物料分类 DEPT_MATER :采购部门-物料 DEPT_MATERGRP :采购部门-物料分类 |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msbd_puropermaterctrl |  | fid |
| 2 | idx_msbd_puropmatctrl_forgid |  | forgid |
