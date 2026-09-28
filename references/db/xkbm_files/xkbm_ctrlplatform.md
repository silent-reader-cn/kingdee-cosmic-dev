# 预算控制台-xkbm_ctrlplatform

## 预算控制台-多语言表 t_xkbm_ctrlplatform_l

- **表名称：** 预算控制台-多语言表
- **表名：** t_xkbm_ctrlplatform_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ctrlplatform_l |  | fpkid |
| 2 | idx_xkbm_ctrlplatform_l |  | fid,flocaleid |

---

## 预算控制规则单据体-子表 t_xkbm_orgctrlrule

- **表名称：** 预算控制规则单据体-子表
- **表名：** t_xkbm_orgctrlrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fctrlrule | 控制规则编码 | int8 | 64 |  | √ | 0 | [预算控制规则 xkbm_ctrlrule](../xkbm_files/xkbm_ctrlrule.md) |
| 3 | fctrllevel | 控制层级 | bpchar | 1 |  | √ | ' ' | 控制层级,枚举: 0 :本级 1 :包含直接下级 2 :包含所有下级 3 :包含直接下级_不含自己 4 :包含所有下级_不含自己 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fctrlbill | 控制单据 | varchar | 2000 |  | √ | ' ' | 控制单据 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_orgctrlrule |  | fentryid |
| 2 | idx_xkbm_orgctrlrule_rule |  | fctrlrule |
| 3 | idx_xkbm_orgctrlrule_fid |  | fid |

---

## 预算控制台-主表 t_xkbm_ctrlplatform

- **表名称：** 预算控制台-主表
- **表名：** t_xkbm_ctrlplatform

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织选择 xkbm_orgselect](../xkbm_files/xkbm_orgselect.md) |
| 3 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [预算模板分组 xkbm_reportgroup](../xkbm_files/xkbm_reportgroup.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fbgscheme | 预算方案编码 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 17 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ctrlplatform |  | fid |
| 2 | idx_xkbm_ctrlplatform_scheme |  | fbgscheme |
| 3 | idx_xkbm_ctrlplatform_org |  | forgunitid |
